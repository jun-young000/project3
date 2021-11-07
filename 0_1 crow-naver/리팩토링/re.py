
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
import os
import csv
#from babel.numbers import format_currency
#from day5 import play5

df= open('save.csv', 'r', encoding='cp949')
rdr = csv.reader(df)
for line in rdr:
  print(line)
df.close()

# df['naver_map_url'] = []

chromedriver = './chromedriver'
driver = webdriver.Chrome(chromedriver)


for i, keyword in enumerate(df['사업장명add'].tolist()):  # 정정코드
  print("이번에 찾을 키워드 :", i, f"/ {df.shape[0]} 행", keyword)

  try:
    naver_map_search_url = f"https://map.naver.com/v5/search/{keyword}/place"  # 검색 url 만들기
    driver.get(naver_map_search_url)  # 검색 url 접속, 즉 검색하기

    time.sleep(2)  # 중요함
    cu = driver.current_url  # 검색이 성공된 플레이스에 대한 개별 페이지

    res_code = re.findall(r"place/(\d+)", cu)
    final_url = 'https://pcmap.place.naver.com/restaurant/' + res_code[0] + '/review/visitor#'

    print(final_url)
    df['naver_map_url'][i] = final_url

  except IndexError:
    df['naver_map_url'][i] = ''
    print('none')
# 1단계- 총3192까지 나오면됨






















    for i in range(0, 2142):  # 4회차
      # for i in range(1200,1793): # 3회차
      # for i in range(600,1200): # 2회차
      # for i in range(0,600): # 1회차
      print('======================================================')
      print(str(i) + '번째 식당')

      # 식당 리뷰 개별 url 접속
      driver.get(df['naver_map_url'][i])
      thisurl = df['naver_map_url'][i]
      time.sleep(2)
      # 더보기 버튼 다 누르기
      # 더보기 버튼 누르기까지 10개
      # 더보기 버튼 누르면 10개 추가됨
      while True:
        try:
          time.sleep(1)  # 1초로 바꾸고
          driver.find_element_by_tag_name('body').send_keys(Keys.END)
          time.sleep(3.5)  # 4초로 바꾸고
          driver.find_element_by_xpath('//*[@id="app-root"]/div/div/div[2]/div[5]/div[4]/div[4]/div[2]/a').click()
          # driver.find_element_by_xpath('//*[@id="app-root"]/div/div/div[2]/div[5]/div[4]/div[5]/div[2]/a').click()
          # driver.find_element_by_xpath('//*[@id="app-root"]/div/div/div[2]/div[5]/div[4]/div[4]/div[2]/a').click()리뷰안되면이걸로
          time.sleep(3.5)  # 4초로 바꾸고
          driver.find_element_by_tag_name('body').send_keys(Keys.END)
          time.sleep(1)  # 1초로 바꾸고

        except NoSuchElementException:
          print('-더보기 버튼 모두 클릭 완료-')
          break

      # 파싱
      html = driver.page_source
      soup = BeautifulSoup(html, 'lxml')
      time.sleep(1)

      # 식당 구분
      restaurant_name = df['사업장명'][i]
      print('식당 이름 : ' + restaurant_name)

      user_review_id[restaurant_name] = {}
      review_json[restaurant_name] = {}
      image_json[restaurant_name] = {}

      try:
        restaurant_classificaton = soup.find_all('span', attrs={'class': '_3ocDE'})[0].text
      except:
        restaurant_classificaton = 'none'
      print('식당 구분 : ' + restaurant_classificaton)
      print('----------------------------------------------')

      try:
        one_review = soup.find_all('div', attrs={'class': '_1Z_GL'})
        review_num = len(one_review)  # 특정 식당의 리뷰 총 개수
        print('리뷰 총 개수 : ' + str(review_num))

        # 리뷰 개수
        for i in range(len(one_review)):

          # user url
          user_url = one_review[i].find('div', attrs={'class': '_23Rml'}).find('a').get('href')
          print('user_url = ' + user_url)

          # user url로부터 user code 뽑아내기
          user_code = re.findall(r"my/(\w+)", user_url)[0]
          print('user_code = ' + user_code)

          # review 1개에 대한 id 만들기
          res_code = re.findall(r"restaurant/(\d+)", thisurl)[0]
          review_id = str(res_code) + "_" + user_code
          print('review_id = ' + review_id)

          # rating, 별점
          rating = one_review[i].find('span', attrs={'class': '_2tObC'}).text
          print('rating = ' + rating)

          # 주의!!! 사진 리뷰 유무에 따라 날짜 파싱코드 다름
          # ('span', attrs = {'class':'_3WqoL'})
          # 사진 없는 경우 : 총 6개 중 4번째
          # 사진 있는 경우 : 총 5개 중 3번째

          # date
          # 사진 리뷰 없음
          if len(one_review[i].find_all('span', attrs={'class': '_3WqoL'})) == 5:
            date = one_review[i].find_all('span', attrs={'class': '_3WqoL'})[2].text
          elif len(one_review[i].find_all('span', attrs={'class': '_3WqoL'})) == 6:
            date = one_review[i].find_all('span', attrs={'class': '_3WqoL'})[3].text
          else:
            date = ""
          print('date = ' + date)

          # review 내용
          try:
            review_content = one_review[i].find('span', attrs={'class': 'WoYOw'}).text
          except:  # 리뷰가 없다면
            review_content = ""
          print('리뷰 내용 : ' + review_content)

          # image 내용
          sliced_soup = one_review[i].find('div', attrs={'class': '_1aFEL _2GO1Q'})

          if (sliced_soup != None):
            sliced_soup = sliced_soup.find('div', attrs={'class': 'dRZ2X'})

            try:
              img_url = 'https://search.pstatic.net/common/?autoRotate=true&quality=95&type=l&size=800x800&src=' + \
                        re.findall(r'src=(.*jpeg)', str(sliced_soup))[0]
            except:
              if (len(re.findall(r'src=(.*jpg)', str(sliced_soup))) != 0):
                img_url = 'https://search.pstatic.net/common/?autoRotate=true&quality=95&type=l&size=800x800&src=' + \
                          re.findall(r'src=(.*jpg)', str(sliced_soup))[0]
              elif (len(re.findall(r'src=(.*png)', str(sliced_soup))) != 0):
                img_url = 'https://search.pstatic.net/common/?autoRotate=true&quality=95&type=l&size=800x800&src=' + \
                          re.findall(r'src=(.*png)', str(sliced_soup))[0]
              else:
                img_url = ""
          else:
            img_url = ""

          print('이미지 url : ' + img_url)
          print('----------------------------------------------')
          print('\n')

          # 리뷰정보
          # user_review_id
          user_review_id[restaurant_name][user_code] = review_id

          # review_json
          review_json[restaurant_name][review_id] = review_content

          # image_json
          image_json[restaurant_name][review_id] = img_url

          # rating_df_list
          naver_review = user_code, restaurant_name, rating, date
          rating_list.append(naver_review)




      except NoSuchElementException:
        none_review = "네이버 리뷰 없음"
        print(none_review)
        review_num = 0
        # 리뷰정보 = restaurant_name, restaurant_classification, review_num, none_review

        # rating_df_list
        naver_review = user_code, restaurant_name, none_review, none_reivew
        rating_list.append(naver_review)

      print('\n')

