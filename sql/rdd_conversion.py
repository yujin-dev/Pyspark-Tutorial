from pyspark.sql import SparkSession
import re

comma_delimiter = re.compile(""",(?=(?:[^"]*"[^"]*")*[^"]*$)""")

def map_response_rdd(line:str):
    splits = comma_delimiter.split(line)
    double1 = None if not splits[6] else float(splits[6])
    double2 = None if not splits[14] else float(splits[14])
    return splits[2], double1, splits[9], double2

def get_col_names(line:str):
    splits = comma_delimiter.split(line)
    return [splits[2], splits[6], splits[9], splits[14]]

if __name__ == "__main__":

    session = SparkSession.builder.appName("StackOverFlowSurvey").master("local[*]").getOrCreate()
    sc = session.SparkContext

    lines = sc.textFile("data/2016-stack-overflow-survey-responses.csv")

    response_rdd = lines.filter(lambda line: not comma_delimiter.split(line)[2] == "country").map(map_response_rdd)
    col_names = lines.filter(lambda line: comma_delimiter.split(line)[2] == "country").map(get_col_names)

    response_df = response_rdd.toDF(col_names.collect()[0])
    response_df.printSchema()
    response_df.show(20)

    for res in response_df.rdd.take(10):
        print(res)
    