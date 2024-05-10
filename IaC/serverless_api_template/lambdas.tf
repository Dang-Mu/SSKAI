module "lambda" {

  source                       = "./lambda"
  prefix                       = var.prefix
  container_registry           = var.container_registry
  container_repository         = var.container_repository
  container_image_tag          = var.container_image_tag
  ram_mib                      = var.lambda_ram_size
  timeout_s                    = var.lambda_timeout
  eks_cluster_name             = var.eks_cluster_name
  attach_ssm_readonly_policy   = var.attach_ssm_readonly_policy
  attach_ec2_policy            = var.attach_ec2_policy
  attach_cloudwatch_policy     = var.attach_cloudwatch_policy
  attach_lambda_policy         = var.attach_lambda_policy
  attach_s3_policy             = var.attach_s3_policy
  attach_vpc_policy            = var.attach_vpc_policy
  attach_eks_policy            = var.attach_eks_policy
  state_bucket_name            = var.state_bucket_name
  db_api_url                   = var.db_api_url
  karpenter_node_iam_node_name = var.karpenter_node_iam_node_name
}
