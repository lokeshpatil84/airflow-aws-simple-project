resource "aws_athena_database" "demo_db" {
  name   = "demo_db"
  bucket = aws_s3_bucket.airflow_bucket.bucket
}
