import json
import boto3

# Initializing the DynamoDB client
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    # Get HTTP method from the API Gateway event
    http_method = event['httpMethod']
    
  