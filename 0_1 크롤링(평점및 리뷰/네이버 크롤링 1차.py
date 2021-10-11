import os
import sys
import csv
import json
import time
import requests


class CRAWL:
    def _init_(self):
        self.seoul_dict={}
        self.tmp_list=[]
        self.data=[]
        self.write=[]


    # 주소 파일 이릭기
    
    def get_seoul_code(self):
        dong_list=[]
        with open("juso.txt","rt", encoding='UTF8') as f:
            for line in f:
                if line == '\n':
                    self.seoul_dict[key]= dong_list
                    dong_list=[]
                    continue


                tem=line.split(",")
                gu=tem[0]
                dong=tem[1].replace("\n","")
                dong_list.append(dong)
                key=gu

        def get_json_value(self,key,i):

            try:
                if key in self.data["time"][i]:
                    value=self.data["items"][i][key]
                    self.write.append("none")
                else:
                    self.write.append("none")

            except:
                self.stop=1



        def crawling(self):


            print('[*] start Crawling!')
            f=open("test.csv","w",encoding='utf-8-sig', newline='')
            f.close()

            # 반복 시작

            for gu,dong_list in self.seoul_dict.items():
                print('-'+gu)

                for dong in dong_list:
                    print('-'+dong)

                    gu_dong=gu+ '+' + dong + "+" + u'맛집'
                    display=100

                    self.stop=0

                    #쿼리 보내기

                    for start in range(1,6):
                        url='https://strore.naver.com/sogum/api/businesses?start='+str(start)\
                        +'&display='+str(display)\
                        +'&query='+gu_dong\
                        +'&sortingOrder=reviewCount'\

                        time.sleep(5)

                        data= requests.get(url)
                        if data.status_code==500:
                            break
                        self.data= json.loads(data.text)

                        #파씽

                        for i in range(display):

                            self.wirte.append(gu)
                            self.wirte.append(dong)

                            self.get_json_value('name',i)
                            self.get_json_value('category', i)
                            self.get_json_value('microReview', i)
                            self.get_json_value('commOnAddr', i)
                            self.get_json_value('addr', i)

                            if self.stop==1:
                                    break
                            with open('test.cvc','a',newline='') as f:
                                writer= csv.writer(f)
                                writer.writerow(self.write)

                            self.write=[]

                print('------------------------------------------------------------------')            

if __name__ == "_main_":


    cr=CRAWL()
    cr.get_seoul_code()
    cr.Crawling()