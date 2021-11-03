import pandas as pd
import numpy as np
from IPython.core.interactiveshell import InteractiveShell
import pymysql
from . import models
InteractiveShell.ast_node_interactivity = "all"
from haversine import haversine
import json

def conn(jeju):
    host_name = 'localhost'
    host_port = 3306
    username = 'root'
    password = '0000'
    database_name = jeju
    db = pymysql.connect(
        host=host_name,     # MySQL Server Address
        port=host_port,          # MySQL Server Port
        user=username,      # MySQL username
        passwd=password,    # password for MySQL username
        db=database_name,   # Database name
        charset='utf8'
    )
    return db

LL = models.Restaurant.objects.all()  # 위경도 데이터
LL1 = LL.values()
LL_sam = pd.DataFrame(LL1)
LL_sam = LL_sam.reindex()

def get_latlog(request) :
    lat = request.GET['lat']
    long = request.GET['long']
    state = [lat, long]
    return state

def make_OMscore(LL_sam, state, quantile=0.6):
    # 리뷰가중평점
    m = LL_sam['rating_count'].quantile(quantile)
    C = LL_sam['rating_average'].mean()
    LL_sam['weighted_rating'] = LL_sam.apply(
        (lambda x: (x['rating_count'] / (x['rating_count'] + m) * x['rating_average']) + (m / (m + x['rating_count']) * C)), axis=1)

    # 내 위치 입력하면 모든 식당과의 거리 산출 - 약 5초
    # state = state
    LL_sam['distance'] = [haversine(state, list((LL_sam[['Latitude', 'Longtitude']].iloc[i]))) for i in
                          range(len(LL_sam))]

    # 로그함수를 이용해 거리 점수 산출 - 최대점수 5점으로 조정
    LL_sam['distance_log'] = np.log(-LL_sam['distance'] + LL_sam['distance'].max() + 1)
    LL_sam['distance_log'] = LL_sam['distance_log'] / LL_sam['distance_log'].max() * 5

    # 어디가맨 지수
    LL_sam['OMscore'] = LL_sam['distance_log'] * 0.2 + LL_sam['weighted_rating'] * 0.8

    # 어디가맨 지수 상위 10개 식당
    top10 = LL_sam[['name', 'address', 'OMscore', 'Latitude', 'Longtitude']].sort_values('OMscore', ascending=False)[:10]

    # 딕셔너리 생성
    dic = {}
    dic['name'] = list(top10['name'])
    dic['address'] = list(top10['address'].values)
    dic['OMscore'] = list(top10['OMscore'].values)
    dic['Latitude'] = list(top10['Latitude'].values)
    dic['Longtitude'] = list(top10['Longtitude'].values)

    # 어디가맨 지수 상위 10개 식당 추출
    return dic

def make_db(state):
    db = conn('jeju')
    sql = 'select * from restaurant'
    LL_sam = pd.read_sql(sql,db)
    file_path = "./OMscore.json"
    with open(file_path,'w', encoding="UTF-8") as outfile:
        json.dump(make_OMscore(LL_sam,state), outfile, ensure_ascii=False)
    return make_OMscore(LL_sam,state)

state=[33.4,125.54]


make_db(state)
