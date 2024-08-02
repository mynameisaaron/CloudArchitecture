# NOTE TWO THINGS:
# 1) CONFIRM THAT YOUR TABLE VARIABLE IN THE LAMBDA_HANDLER REFERENCES THE NAME OF YOUR PETSHOP DATABASE
# 2) THIS LAMBDA FUNTION WILL BE TRIGGERED BY THE API GATEWAY'S GET METHOD (IN THE NEXT STEP)
import boto3
import json
from boto3.dynamodb.conditions import Attr

def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table('PetShopAPI')
    
    # Extract query parameters
    query_params = event.get('queryStringParameters', {})
    
    # Build the filter expression
    filter_expression = None
    valid_params = ['id', 'name', 'owner', 'breed', 'gender', 'birthday']
    
    for param, value in query_params.items():
        if param in valid_params:
            condition = Attr(param).eq(value)
            filter_expression = condition if filter_expression is None else filter_expression & condition
    
    # Execute the scan with filter
    if filter_expression:
        response = table.scan(
            FilterExpression=filter_expression
        )
    else:
        response = table.scan()
    
    # Format the response
    items = response['Items']
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': f"{len(items)} records found",
            'data': items
        })
    }
