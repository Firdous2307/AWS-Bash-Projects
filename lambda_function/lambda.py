import json
import boto3


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoApp')  

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        # Create new item in DynamoDB table
        response = table.put_item(
            Item={
                'task': event['task'],
                'deadline': event['deadline'],
                'priority': event['priority'],
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
    elif event['httpMethod'] == 'GET':
        # Retrieve all items from DynamoDB table
        response = table.scan()
        
        items = response.get('Items', [])
        
        # Return response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(items)
        }
    elif event['httpMethod'] == 'PATCH':
        # Update an item in the DynamoDB table based on task name
        task_name = event['queryStringParameters']['task'] if 'queryStringParameters' in event else None

        if task_name:
            response = table.update_item(
                Key={
                    'task': task_name
                },
                UpdateExpression='SET deadline = :d, priority = :p',
                ExpressionAttributeValues={
                    ':d': event['deadline'],
                    ':p': event['priority']
                }
            )

            # Return response
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'message': 'Task successfully updated'})
            }
        else:
            # Invalid or missing task parameter
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'message': 'Invalid or missing task parameter'})
            }
    elif event['httpMethod'] == 'DELETE':
        # Delete an item from the DynamoDB table based on task name
        task_name = event['queryStringParameters']['task'] if 'queryStringParameters' in event else None

        if task_name:
            response = table.delete_item(
                Key={
                    'task': task_name
                }
            )

            # Return response
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'message': 'Task successfully deleted'})
            }
        else:
            # Invalid or missing task parameter
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'message': 'Invalid or missing task parameter'})
            }
    else:
        # Handle other HTTP methods or return an error if needed
        return {
            'statusCode': 405,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'Method not allowed'})
        }
