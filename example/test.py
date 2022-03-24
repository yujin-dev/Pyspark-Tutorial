from pyspark.sql import SparkSession

class ConnPsql:

    def __init__(self):
        self.engine = SparkSession.builder.appName("App").getOrCreate()

    def get_psql_table(self, table_name):
        postgre_table = self.engine.read.format("jdbc")\
                        .option("url", "jdbc:postgresql://postgres:qraft@10.0.0.12:5432/xf_target")\
                        .option("dbtable", "cssecurity")\
                        .load()
                        # .option("password", "qraft")\
                        # .option("user", "postgres")\
        return postgre_table

    def get_query(self, table_name, query, view_name="postgreTable"):
        p_table = self.get_psql_table(table_name=table_name)
        p_table.createOrReplaceTempView(view_name)
        return self.engine.sql(query)


if __name__ == "__main__":

    conn = ConnectPsql()