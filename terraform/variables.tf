variable "aws_region" {
  description = "AWS region for deployment"
  type        = string
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "EC2 instance size"
  type        = string
  default     = "t2.micro"
}

variable "db_username" {
  description = "Master username for RDS MySQL"
  type        = string
  default     = "admin"
}

variable "db_password" {
  description = "Master password for RDS MySQL"
  type        = string
  sensitive   = true
}

variable "db_name" {
  description = "Database schema name"
  type        = string
  default     = "the_eventor_db"
}