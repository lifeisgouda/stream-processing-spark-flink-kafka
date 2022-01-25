'''
Uber data에서 trip 수를 세는 코드
'''

# import packages
from distutils.command.config import config
from pyspark import SparkConf, SparkContext
import pandas as pd 

# Spart setting
conf = SparkConf().setMaster("local").setAppName("uber-data-trips")
sc = SparkContext(conf=conf)    # Spark 객체 초기화에 사용

# Data file
directory = "/Users/jane/dev/stream-processing-spark-flink-kafka/spark/data"
filename = "fhvhv_tripdata_2020-03.csv"

# Data parsing
lines = sc.textFile(f"file:///{directory}/{filename}")
header = lines.first()
filtered_lines = lines.filter(lambda row:row != header)

# 필요한 부분만 골라서 카운트
# countByValue로 같은 날짜 등장하는 부분을 센다.
dates = filtered_lines.map(lambda x: x.split(",")[2].split(" ")[0])
result = dates.countByValue()

# CSV로 결과값 저장 
pd.Series(result, name="trips").to_csv("trips_date.csv")
