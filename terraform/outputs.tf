output "alb_dns_name" {
  description = "Public URL of the Application Load Balancer"
  value       = aws_lb.eventor_alb.dns_name
}

output "rds_endpoint" {
  description = "Endpoint address of the RDS MySQL database"
  value       = aws_db_instance.eventor_db.endpoint
}