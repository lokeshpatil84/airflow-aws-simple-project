resource "aws_glue_job" "etl_job" {
  name     = "airflow-demo-glue-job"
  role_arn = aws_iam_role.glue_role.arn

  command {
    script_location = "s3://${aws_s3_bucket.airflow_bucket.bucket}/glue/glue_etl_script.py"
    python_version  = "3"
  }

  glue_version = "4.0"
  number_of_workers = 2
  worker_type       = "G.1X"
}
