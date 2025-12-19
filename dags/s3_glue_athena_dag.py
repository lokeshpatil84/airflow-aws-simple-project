from airflow import DAG
from airflow.providers.amazon.aws.operators.s3 import S3CreateObjectOperator
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.providers.amazon.aws.operators.athena import AthenaOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1)
}

with DAG(
    dag_id='aws_simple_airflow_project',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    upload_to_s3 = S3CreateObjectOperator(
        task_id='upload_csv_to_s3',
        s3_bucket='my-airflow-demo-bucket',
        s3_key='raw/sample_data.csv',
        data='id,name,amount\n1,A,100\n2,B,200',
        replace=True
    )

    run_glue_job = GlueJobOperator(
        task_id='run_glue_etl',
        job_name='airflow-demo-glue-job',
        script_location='s3://my-airflow-demo-bucket/glue/glue_etl_script.py',
        iam_role_name='AWSGlueServiceRole-Airflow'
    )

    run_athena_query = AthenaOperator(
        task_id='run_athena_query',
        query='SELECT * FROM demo_db.sales;',
        database='demo_db',
        output_location='s3://my-airflow-demo-bucket/athena-output/'
    )

    upload_to_s3 >> run_glue_job >> run_athena_query
