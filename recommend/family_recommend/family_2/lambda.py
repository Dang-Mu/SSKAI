from family_2 import get_family_2_for_inference
import json

def handler(event, context):
    try:
        body = json.loads(event["body"])
    except Exception as e:
        response = {
            'statusCode': 500,
            'errorMessage': e
        }
        return response
    
    region_name = body.get('region')
    try:
        family = get_family_2_for_inference(region_name)
    except Exception as e:
        raise e

    response = {
        'statusCode': 200,
        'body': json.dumps({
            'family': family,
        })
    }
    return response

# for test
if __name__ == "__main__":
    family = get_family_2_for_inference("ap-northeast-2")
    print(family)