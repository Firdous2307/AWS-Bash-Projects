import json
import boto3
import logging

# Logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# Initializing the DynamoDB client
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    try:
        http_method = event['httpMethod']
        table_name = "ToDOApp"
        
        if http_method == 'GET':
            response = dynamodb.scan(TableName='ToDOApp')
            items = response.get('Items', [])
            
            return {
                "statusCode": 200,
                "body": json.dumps(items)
            }
        elif http_method == 'POST':
            request_body = json.loads(event['body'])
            
            if 'task' not in request_body:
                return {
                    "statusCode": 400,
                    "body": "Missing 'task' field in request"
                }
            
            new_item = {
                'id': {'S': str(hash(request_body['task']))},
                'task': {'S': request_body['task']}
            }
            
            dynamodb.put_item(TableName='ToDOApp', Item=new_item)
            
            return {
                "statusCode": 201,
                "body": "Item added successfully"
            }
        else:
            return {
                "statusCode": 405,
                "body": "Method not allowed"
            }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"An error occurred: {str(e)}"
        }
