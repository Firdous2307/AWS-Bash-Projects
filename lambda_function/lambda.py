import boto3
import json

dynamodb_table_name = "TODOApp"
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(dynamodb_table_name)

def lambda_handler(event, context):
    http_method = event.get("httpMethod")
    resource_path = event.get("resource")  

    if http_method == "GET" and resource_path == "/item":
        item_id = event.get("queryStringParameters", {}).get("user-id", None)
        if item_id is not None:
            response = get_item(item_id)
        else:
            response = get_all_items()
    elif http_method == "POST" and resource_path == "/item":
        request_body = json.loads(event.get("body", "{}"))
        response = create_item(request_body)
    elif http_method == "PATCH" and resource_path == "/item":
        request_body = json.loads(event.get("body", "{}"))
        response = update_item(request_body)
    elif http_method == "DELETE" and resource_path == "/item":
        item_id = event.get("queryStringParameters", {}).get("user-id", None)
        if item_id is not None:
            response = delete_item(item_id)
        else:
            response = build_response(400, {"Message": "Invalid DELETE request"})
    else:
        response = build_response(400, {"Message": "Invalid operation"})
    
    return response

def get_all_items():
    try:
        response = table.scan()
        items = response.get("Items", [])
        return build_response(200, {"items": items})
    except Exception as e:
        return build_response(500, {"Message": "Internal Server Error"})

def get_item(item_id):
    try:
        response = table.get_item(Key={"user-id": item_id})
        if "Item" in response:
            return build_response(200, response["Item"])
        else:
            return build_response(404, {"Message": "Item not found"})
    except Exception as e:
        return build_response(500, {"Message": "Internal Server Error"})

def create_item(item_data):
    try:
        table.put_item(Item=item_data)
        return build_response(201, {"Message": "Item created successfully"})
    except Exception as e:
        return build_response(500, {"Message": "Internal Server Error"})

def update_item(item_data):
    item_id = item_data.get("user-id")
    update_key = item_data.get("updateKey")
    update_value = item_data.get("updateValue")
    
    if item_id and update_key and update_value:
        try:
            response = table.update_item(
                Key={"user-id": item_id},
                UpdateExpression=f"set {update_key} = :value",
                ExpressionAttributeValues={":value": update_value},
                ReturnValues="UPDATED"
            )
            return build_response(200, {"Message": "Item updated", "UpdatedAttributes": response})
        except Exception as e:
            return build_response(500, {"Message": "Internal Server Error"})
    else:
        return build_response(400, {"Message": "Invalid PATCH request"})

def delete_item(item_id):
    try:
        response = table.delete_item(Key={"user-id": item_id})
        return build_response(200, {"Message": "Item deleted", "DeletedItem": response})
    except Exception as e:
        return build_response(500, {"Message": "Internal Server Error"})

def build_response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }
