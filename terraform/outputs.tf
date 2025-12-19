output "s3_bucket" {
  value = aws_s3_bucket.airflow_bucket.bucket
}

output "glue_job_name" {
  value = aws_glue_job.etl_job.name
}
