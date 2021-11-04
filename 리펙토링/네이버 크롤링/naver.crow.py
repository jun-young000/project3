import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import re
from bs4 import BeautifulSoup
import random
import multiprocessing
from tqdm import tqdm


df = pd.read_csv('./제주특별자치도음식점목록(통합).csv', sep=',', encoding='CP949')


df['naver_map_url'] = '' # 미리 url을 담을 column을 만들어줌
chromedriver = './chromedriver'
driver = webdriver.Chrome(chromedriver)
# driver = webdriver.Chrome(executable_path=r'C:\\Users\\ui\\Desktop\chromedriver.exe') # 웹드라이버가 설치된 경로를 지정해주시면 됩니다.

df = df[~df['상세영업상태명'].str.contains("폐업", na=False, case=False)]
