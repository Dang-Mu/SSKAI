import subprocess
import os
from nodepool_generator import *

eks_cluster_name = os.environ.get('EKS_CLUSTER_NAME')

kubectl = '/var/task/kubectl'
kubeconfig = '/tmp/kubeconfig'

# get eks cluster kubernetes configuration by aws cli
result_get_kubeconfig = subprocess.run([
    "aws", "eks", "update-kubeconfig",
    "--name", eks_cluster_name,
    "--region", "ap-northeast-2",
    "--kubeconfig", kubeconfig
])

def apply_nodepool_yaml(eks_cluster_name, nodepool_name, nodeclass_name, family_list):
    nodepool_filename = generate_yaml(eks_cluster_name, nodepool_name, nodeclass_name, family_list)
    result_create_nodepool = subprocess.run([
        kubectl, "apply", "-f", nodepool_filename, "--kubeconfig", kubeconfig
    ])
    if result_create_nodepool != 0: print("create nodepool returncode != 0")

    return result_create_nodepool

def handler(event, context):
    ssm = boto3.client('ssm', region_name='ap-northeast-2')
    param_lambda_url = ssm.get_parameter(Name="recocommend_family_lambda_function_url", WithDecryption=False)
    recommend_lambda_url = param_lambda_url['Parameter']['Value']

    region = 'ap-northeast-2'

    family_dict = get_instance_family(recommend_lambda_url, region)

    for nodepool_name, family_list in family_dict.items():
        nodeclass_name = 'ec2-gpu'
        result = apply_nodepool_yaml(eks_cluster_name, nodepool_name, nodeclass_name, family_list)

    streamlit_cpu_nodepool_name = 'streamlit-cpu-nodepool'
    streamlit_cpu_nodepool_family_list = [
        't3.nano', 't3.micro', 't3.small', 't3.medium', 't3.large', 't3.xlarge',
        'm5.large', 'm5.xlarge'
    ]
    streamlit_nodeclass_name = 'ec2-cpu'

    result = apply_nodepool_yaml(eks_cluster_name, streamlit_cpu_nodepool_name, streamlit_nodeclass_name, streamlit_cpu_nodepool_family_list)

    return {
        'statusCode': 200,
        'body': "complete update nodepool"
    }
