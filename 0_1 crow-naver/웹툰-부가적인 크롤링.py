
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pandas as pd

URL = "https://comic.naver.com/webtoon/weekday"

html = requests.get(URL).text

soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all('a',{"class" : "title"})
id_list = [] ; title_list = [] ; author_list = [] ; day_list = []; genre_list = []; story_list =[]; platform_list = []
num = 0

driver = webdriver.Chrome()
driver.get(URL)

for i in range(len(title)):
    sleep(0.5)

    page = driver.find_elements_by_class_name('title')
    page[i].click()

    sleep(0.5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    day = soup.find_all('ul', {'class':"category_tab"})
    day = day[0].find('li',{'class':'on'}).text[0:1]

    t = title[i].text
    if (t in title_list):
        day_list[title_list.index(t)] += ', ' +day
        driver.back()
        continue

        id_list.append(i) ; num += 1
        title_list.append(t)
        day_list.append(day)
        platform_list.append('네이버 웹툰')

        author = soup.find_all('h2')
        author = author[1].find('span',{'class':'wrt_nm'}).text[8:]

        author_list.append(author)

        genre = soup.find('span',{'class':'genre'}).text
        genre_list.append(genre)

        story = soup.find_all('p')
        story = str(story[3])
        story = story.replace('<p>','').replace('</p>','').replace('<br/>','\n')
        story_list.append(story)

        driver.back()

        cols = []
        total_data = pd.DataFrame(columns = cols)
        total_data['id'] = id_list
        total_data['title'] = title_list
        total_data['author'] = author_list
        total_data['day'] = day_list
        total_data['genre'] = genre_list
        total_data['story'] = story_list
        total_data['platform'] = platform_list
        total_data.tocsv('네이버웹툰.csv', encoding = 'utf-8-sig')