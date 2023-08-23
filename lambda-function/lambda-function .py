# Deploy Lambda function
aws lambda create-function \
    --function-name To-do-App Project \
    --runtime python 3.11 \
    --handler lambda_function.lambda_handler \
    --role arn:aws:iam:"$AWS_ACCOUNT_ID":role/my-lambda-role \
    --code S3Bucket=my-lambda-bucket-01,S3Key=your-lambda-zip-file