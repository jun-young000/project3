import requests
import urllib.parse as urlparse
from geopy import distance
import  folium

class Route:
    def __init__(self, headers={"X-NCP-APIGW-API-KEY-ID": "4rC5urm6tLQwzAMgWM5K",
                                "X-NCP-APIGW-API-KEY": "STzqPRYvuC"}):
        self.headers = headers

    # 출발지 -> 위경도 변환
    def addr_to_xy(self):
        # 주소값 입력
        self.d1_name = input("출발지 1을 입력하세요. : ")
        # URL 설정
        self.d1_url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={}".format(self.d1_name)
        # 리퀘스트
        self.response1 = requests.get(self.d1_url, headers=self.headers)
        # JSON 파싱하여 위경도 추출
        self.d1_x = self.response1.json()["addresses"][0]["x"]
        self.d1_y = self.response1.json()["addresses"][0]["y"]
        return self.d1_x, self.d1_y

    # row.data 파일이름을 total2가 아니라 jeju로 정의하고 시작함
    map_jeju = folium.Map(location=[33.2141, 126.3148], zoom_start=16)

    for i in jeju.index:
        # 행 우선 접근 방식으로 값 추출하기
        name = jeju.loc[i, 'name']
        upjong = jeju.loc[i, "upjong"]
        address = jeju.loc[i, "address_x"]
        category = jeju.loc[i, "category"]
        biz = jeju.loc[i, "평점_평균"]
        img = df_seoul.loc[i, "img"]  # 이미지 받아온느거
        html = '''
        이름 : {}<br>
        업종 : {}<br>
        주소 : {}<br>
        카테고리 : {}<br>
        평점_평균 : {}<br>
        *****당장 만나야 하는 우리의 위치***** : {}<br>
        lat : {}<br>
        lng : {}<br>

        <img src="{}" alt="이미지" width="400" />
        '''.format(name, upjong, address, category, biz, lat, lng, img)

        iframe = folium.IFrame(html, width=500, height=300)
        popup = folium.Popup(iframe, max_width=500)
        marker = folium.Marker([lat, lng], popup=popup)
        marker.add_to(map_jeju)

    map_seoul