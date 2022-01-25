# Stream Processing Study
## 학습 계기
회사에서 Interest map(사용자의 정보를 기반으로 유저의 관심사를 모델링)이라는 프로젝트를 진행하면서 유저의 IDFA가 factor가 되는 단계까지 되었다. Airflow에서 SQL Dag로 Athena나 Redshift에서 처리하는데 한계가 발생하였고, 해결 방법으로 Stream processing을 선택하였다. Apache Flink는 Data engineer분들이 도입 중에 있어서 Spark부터 순차적으로 학습하게 되었다.

## 학습기간 
약 2주 (2022년 1월 24일 ~ 2022년 2월 6일 하루 3시간씩 할애)

## 학습 노트
- Spark: [노트 링크](https://fourierdev.notion.site/Stream-Processing-Apache-Spark-1c477a3235fa4003af3617b583d7d19c)
- Flink (TBD): [노트 링크](https://fourierdev.notion.site/Stream-Processing-Apache-Flink-3a408fb9ee224870b4fd4b55a87ad6cf)
- Kafka (TBD): [노트 링크](https://fourierdev.notion.site/Stream-Processing-Apache-Kafka-TBD-d92ecbf7f60e4d2b9d7dd10487fa4a8e)


## 학습 방법 및 자료
책, 공식문서, 강의를 발췌독 하여 정리하였다. 
### 자료 링크
- [Spark Document](https://spark.apache.org/docs/latest/)
- [Spark Documen - PySpark](https://spark.apache.org/docs/latest/api/python/getting_started/index.html)
- [스파크를 다루는 기술 Spark in Action](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791160504798)
- [실시간 빅데이터 처리를 위한 Spark & Flink](https://fastcampus.co.kr/data_online_flink)
- [스파크 완벽 가이드](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791162241288)
- [9가지 사례로 익히는 고급 스파크 분석](https://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791162240526)