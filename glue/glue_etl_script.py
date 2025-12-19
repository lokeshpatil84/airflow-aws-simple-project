import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)

datasource = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://my-airflow-demo-bucket/raw/"]},
    format="csv",
    format_options={"withHeader": True}
)

glueContext.write_dynamic_frame.from_options(
    frame=datasource,
    connection_type="s3",
    connection_options={"path": "s3://my-airflow-demo-bucket/processed/"},
    format="parquet"
)
