'''
Restaurant의 평균 리뷰 개수 구하기
'''

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("category-review-average")
sc = SparkContext(conf=conf)

directory = "/Users/jane/dev/stream-processing-spark-flink-kafka/spark/data"
filename = "restaurant_reviews.csv"

lines = sc.textFile(f"file:///{directory}/{filename}")

header = lines.first()

filtered_lines = lines.filter(lambda row: row != header)

def parse(row):
    #'0,짜장면,중식,125'
    fields = row.split(",")
    category = fields[2]
    reviews = int(fields[3])
    return (category, reviews)

categoryReviews = filtered_lines.map(parse)

categoryReviewsCount = categoryReviews.mapValues(lambda x: (x, 1))

reduced = categoryReviewsCount.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))

averages = reduced.mapValues(lambda x: x[0] / x[1])

averages.collect()