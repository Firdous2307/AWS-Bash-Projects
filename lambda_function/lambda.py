import json
import boto3


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoList')  

def lambda_handler(event, context):
        print(event)
        # Create new item in DynamoDB table
        response = table.put_item(
            Item={
                'task': event['task'],
                'deadline': event['deadline'],
                'priority': event['priority']
            }
        )
        
        # Return response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'Task successfully added'})
        }
        