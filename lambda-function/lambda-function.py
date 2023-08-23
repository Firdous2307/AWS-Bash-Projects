import json
import boto3

# Initializing the DynamoDB client
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    try:
        http_method = event['httpMethod']
        table_name = "$TABLE_NAME"
        
        if http_method == 'GET':
            response = dynamodb.scan(TableName="$TABLE_NAME")
            items = response.get('Items', [])
            
            return {
                "statusCode": 200,
                "body": json.dumps(items)
            }
        elif http_method == 'POST':
            request_body = json.loads(event['body'])
            