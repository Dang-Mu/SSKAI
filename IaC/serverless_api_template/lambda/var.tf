variable "prefix" {}
variable "container_registry" {}
variable "container_repository" {}
variable "container_image_tag" {}
variable "ram_mib" {}
variable "eks_cluster_name" {}
variable "attach_cloudwatch_policy" {}
variable "attach_ec2_policy" {}
variable "attach_lambda_policy" {}
variable "attach_s3_policy" {}
variable "attach_vpc_policy" {}
variable "attach_eks_policy" {}
variable "recommend_bucket_name" {}
variable "inference_url" {
    type = string
    default = "https://wpcwvjlvkl.execute-api.ap-northeast-2.amazonaws.com/sskai-api-dev/inferences"
}