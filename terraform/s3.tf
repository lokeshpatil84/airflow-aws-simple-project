resource "aws_s3_bucket" "airflow_bucket" {
  bucket = "airflow-demo-etl-bucket-123"
}

resource "aws_s3_object" "glue_script" {
  bucket = aws_s3_bucket.airflow_bucket.bucket
  key    = "glue/glue_etl_script.py"
  source = "../glue/glue_etl_script.py"
}
