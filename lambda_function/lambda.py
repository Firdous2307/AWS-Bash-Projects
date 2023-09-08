import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoList')  

def lambda_handler(event, context):
    try:
        # Extract 'task_id', 'task', and 'priority' from the event
        task_id = event['task_id']
        task = event['task']
        priority = event['priority']

        # Create new item in DynamoDB table
        response = table.put_item(
            Item={
                'task_id': task_id,
                'task': task,
                'priority': priority
            }
        )

        # Return a success response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'Task successfully added'})
        }
    except KeyError as e:
        # Handle missing key in the event
        error_message = f"KeyError: {str(e)}"
        return {
            'statusCode': 400,  # Bad Request
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': error_message})
        }
