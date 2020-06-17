import json
import pymysql
import traceback


def hello(event, context):

    body = {
        "message": "Hello World!!"
    }

    print("hello")
    return responseSuccess(body)

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration

def responseSuccess(body):
    return {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": { 
            "Access-Control-Allow-Origin": "*"    #this code slove the cross access control issu CORS policy: 
        }        
    }

def getNameById(event, context):
    print("in getNameById")
    body = json.loads(event["body"])
    id = body["id"]
    print("querybyId:{}.".format(id))
    conn = getDBConnection()
    body = {
        "message": "Lambda End!!"
    }
    return responseSuccess(body)

    # queryById(id)

def getDBConnection():
    try:
        conn = pymysql.connect("localhost", user="root",
                               passwd="Zhong86915237#", db="world", connect_timeout=10)
        return conn
    except Exception as e:
        print("An exception occurred while trying connecting db:", e)
        traceback.print_exc()
