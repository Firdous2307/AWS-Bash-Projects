import boto3
import json

# Initializing DynamoDB resource and table
dynamodb_table_name = "TODOApp"  
dynamodb = boto3.resource("dynamodb")

def lambda_handler(event, context):
    # Extracting relevant information from the event
    http_method = event["httpMethod"]
    item_id = event["queryStringParameters"]["user-id"] 
    
    if http_method == "GET":
        response = table.get_item(Key={"user-id": item_id}) 
        if "Item" in response:
            return build_response(200, response["Item"])
        else:
            return build_response(404, {"Message": "Item not found"})
    elif http_method == "POST":
        # Creating a new item in the table with the provided data
        table.put_item(Item={**{"user-id": item_id}, **request_body})
        return {"statusCode": 200, "body": json.dumps({"Message": "Item created"})}

    elif http_method == "PATCH":
        # Updating a specific attribute of an item       
        request_body = json.loads(event["body"])
        response = table.update_item(
            Key={"user-id": item_id}, 
            UpdateExpression=f"set {request_body['updateKey']} = :value",
            ExpressionAttributeValues={":value": update_value},
            ReturnValues="UPDATED"
        )
        
        return {"statusCode": 200, "body": json.dumps({"Message": "Item updated", "UpdatedAttributes": response})}
    elif http_method == "DELETE":
        # Deleting an item from the table
        response = table.delete_item(Key={"user-id": item_id}) 
        return {"statusCode": 200, "body": json.dumps({"Message": "Item deleted", "DeletedItem": response})}
    else:
        # Handle invalid operations
        return {"statusCode": 400, "body": json.dumps({"Message": "Invalid operation"})}

