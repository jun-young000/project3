## 네이버음식점 데이터 최종 전처리



```
# datanode가 안 올라옴

cd hadoop
rm -rf datanode_dir

cd
stop-all.sh
hdfs datanode -format

start-all.sh
pyspark
```



```python
rest = spark.read.option("header", "true").csv("/user/engineer/data/data/naver_final_rating.csv", encoding="utf-8")


# 지역구별로 새로운 데이터프레임에 저장
gujwa = spark.sql("SELECT * FROM resto WHERE SUBSTR(address, 13, 3) = '구좌읍'")
seongsan = spark.sql("SELECT * FROM resto WHERE SUBSTR(address, 14, 3) = '성산읍'")
jocheon = spark.sql("SELECT * FROM resto WHERE SUBSTR(address, 13, 3) = '조천읍'")
pyoseon = spark.sql("SELECT * FROM resto WHERE SUBSTR(address, 14, 3) = '표선면'")
aewol = spark.sql("SELECT * FROM resto WHERE SUBSTR(address, 13, 3) = '애월읍'")
hanrim = spark.sql("SELECT * FROM resto WHERE SUBSTR(address, 13, 3) = '한림읍'")
anduck = spark.sql("SELECT * FROM resto WHERE SUBSTR(address, 14, 3) = '안덕면'")
hankyung = spark.sql("SELECT * FROM resto WHERE SUBSTR(address, 13, 3) = '한경면'")
daejeong = spark.sql("SELECT * FROM resto WHERE SUBSTR(address, 14, 3) = '대정읍'")

jeju = 
spark.sql("SELECT * FROM resto WHERE address LIKE '%제주시%' AND address NOT IN ('%구좌읍%', '%성산읍%', '%조천읍%', '%표선면%', '%애월읍%', '%한림읍%', '%안덕면%', '%한경면%', '%대정읍%')")

seoguipo = spark.sql("SELECT * FROM resto WHERE address LIKE '%서귀포시%' AND address NOT IN ('%구좌읍%', '%성산읍%', '%조천읍%', '%표선면%', '%애월읍%', '%한림읍%', '%안덕면%', '%한경면%', '%대정읍%')")



# 주소 키워드 컬럼 추가하기

from pyspark.sql.functions lit

gujwa.withColumn("category", lit('구좌읍'))
seongsan.withColumn("category", lit('성산읍'))
jocheon.withColumn("category", lit('조천읍'))
pyoseon.withColumn("category", lit('표선면'))
aewol.withColumn("category", lit('애월읍'))
hanrim.withColumn("category", lit('한림읍'))
anduck.withColumn("category", lit('안덕면'))
hankyung.withColumn("category", lit('한경면'))
daejeong.withColumn("category", lit('대정읍'))
jeju.withColumn("category", lit('제주시'))
seoguipo.withColumn("category", lit('서귀포시'))


# csv로 저장

gujwa.write.format("csv").option("header", "true").mode("overwrite").save("/user/enginner/data/data/gujwa")
seongsan.write.format("csv").option("header", "true").mode("overwrite").save("/user/enginner/data/data/seongsan")
jocheon.write.format("csv").option("header", "true").mode("overwrite").save("/user/enginner/data/data/jocheon")
pyoseon.write.format("csv").option("header", "true").mode("overwrite").save("/user/enginner/data/data/pyoseon")
aewol.write.format("csv").option("header", "true").mode("overwrite").save("/user/enginner/data/data/aewol")
hanrim.write.format("csv").option("header", "true").mode("overwrite").save("/user/enginner/data/data/hanrim")
anduck.write.format("csv").option("header", "true").mode("overwrite").save("/user/enginner/data/data/anduck")
hankyung.write.format("csv").option("header", "true").mode("overwrite").save("/user/enginner/data/data/hankyung")
daejeong.write.format("csv").option("header", "true").mode("overwrite").save("/user/enginner/data/data/daejeong")
jeju.write.format("csv").option("header", "true").mode("overwrite").save("/user/enginner/data/data/jeju")
seoguipo.write.format("csv").option("header", "true").mode("overwrite").save("/user/enginner/data/data/seoguipo")


```

