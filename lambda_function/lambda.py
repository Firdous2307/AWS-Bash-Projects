import boto3
import json

dynamodb_table_name = "TODOApp"
dynamodb = boto3.resource("dynamodb")


def lambda_handler(event, context):
    http_method = event.get("httpMethod")
    query_parameters = event.get("queryStringParameters", {})
    item_id = query_parameters.get("user-id", None)
    
    if http_method == "GET" and item_id is not None:
        response = table.get_item(Key={"user-id": item_id})
        if "Item" in response:
            return build_response(200, response["Item"])
        else:
            return build_response(404, {"Message": "Item not found"})
    elif http_method == "POST":
        request_body = json.loads(event.get("body", "{}"))
        table.put_item(Item={**{"user-id": item_id}, **request_body})
        return build_response(200, {"Message": "Item created"})
    elif http_method == "PATCH":
        request_body = json.loads(event.get("body", "{}"))
        update_key = request_body.get("updateKey")
        update_value = request_body.get("updateValue")
        
        if item_id is not None and update_key is not None and update_value is not None:
            response = table.update_item(
                Key={"user-id": item_id},
                UpdateExpression=f"set {update_key} = :value",
                ExpressionAttributeValues={":value": update_value},
                ReturnValues="UPDATED"
            )
            return build_response(200, {"Message": "Item updated", "UpdatedAttributes": response})
        else:
            return build_response(400, {"Message": "Invalid PATCH request"})
    elif http_method == "DELETE" and item_id is not None:
        response = table.delete_item(Key={"user-id": item_id})
        return build_response(200, {"Message": "Item deleted", "DeletedItem": response})
    else:
        return build_response(400, {"Message": "Invalid operation"})

def build_response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }
