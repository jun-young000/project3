import pandas as pd
from selenium import webdriver

import time

df = pd.read_csv('sb_restaurant.csv', sep=',', encoding='CP949')

df = df[['업소명', '소재지도로명', '업태명', '주된음식', '행정동명', '소재지전화번호']]
df.columns = ['name', 'address', 'cate1', 'cate2', 'dong', 'phone']
df = df.drop_duplicates(['name'], keep='first')

df['cate_mix'] = df['cate1'] + df['cate2']

print(df)

driver = webdriver.Chrome('chromedriver.exe')
df['kakao_keyword'] = df['dong'] + " " + df['name']

for i, keyword in enumerate(df['kakao_keyword'].tolist()):
    print(keyword, end=" ")
    try:
        kakao_map_search_url = f"https://map.kakao.com/?q={keyword}"
        driver.get(kakao_map_search_url)
        time.sleep(1)

        rate = driver.find_element_by_css_selector("#info\.search\.place\.list > li.PlaceItem.clickArea.PlaceItem-ACTIVE > div.rating.clickArea > span.score > em").text
        rateNum = driver.find_element_by_css_selector("#info\.search\.place\.list > li.PlaceItem.clickArea.PlaceItem-ACTIVE > div.rating.clickArea > span.score > a").text

        print("리뷰 " + rateNum + ", 평점 " + rate)

    except Exception as e1:
        print("정보 없음")
        pass