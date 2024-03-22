from recommender_inference_family import get_instance_family_for_inference
import json


# requestBody : {'region' : string}
def lambda_handler(event, context):
    try:
        json_body = json.loads(event['body'])
    except Exception as e:
        response = {
            'statusCode': 500,
            'errorMessage': e
        }
        return response
    
    region_name = json_body['region']
    try:
        family = get_instance_family_for_inference(region_name)
    except Exception as e:
        response = {
            'statusCode': 500,
            'errorMessage': "Family for Inference API 오류 발생"
        }
        return response

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'family': family,
        })
    }
    return response