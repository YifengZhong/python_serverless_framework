import json


def hello(event, context):
    if event['httpMethod'] == 'OPTIONS':
        return {
            "statusCode": 204,
            "headers": {
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key',
            'Access-Control-Allow-Methods': 'POST, GET, PUT, DELETE',
            'Access-Control-Allow-Origin': '*',
            },
            "body": None,            
        }
    body = {
        "message": "Hello World!!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": { 
            "Access-Control-Allow-Origin": "*" 
        }        
    }
    print("hello")
    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
