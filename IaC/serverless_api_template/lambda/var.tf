variable "prefix" {}
variable "container_registry" {}
variable "container_repository" {}
variable "container_image_tag" {}
variable "ram_mib" {}
variable "timeout_s" {}
variable "eks_cluster_name" {}
variable "attach_ssm_readonly_policy" {}
variable "attach_cloudwatch_policy" {}
variable "attach_ec2_policy" {}
variable "attach_lambda_policy" {}
variable "attach_s3_policy" {}
variable "attach_vpc_policy" {}
variable "attach_eks_policy" {}
variable "attach_iam_policy" {}
variable "attach_pricing_policy" {}
variable "db_api_url" {}
variable "state_bucket_name" {}
variable "karpenter_node_role_parameter_name" {}
variable "region_name" {}
variable "model_s3_url" {}
variable "upload_s3_url" {}
