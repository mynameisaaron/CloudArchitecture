# NOTE TWO THINGS:
# 1) CONFIRM THAT YOUR TABLE VARIABLE IN THE LAMBDA_HANDLER REFERENCES THE NAME OF YOUR PETSHOP DATABASE
# 2) THIS LAMBDA FUNTION WILL BE TRIGGERED BY THE API GATEWAY'S PATCH METHOD (IN THE NEXT STEP)
import boto3
import json

def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table('PetShopAPI')
    
    # Extract the pet ID from the query string parameters
    pet_id = event.get('queryStringParameters', {}).get('id')
    
    if pet_id is None:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing pet ID'})
        }
    
    # Extract the request body
    body = json.loads(event['body'])
    
    # Build the update expression
    update_expression = "set "
    expression_attribute_values = {}
    expression_attribute_names = {}
    
    for key, value in body.items():
        update_expression += f"#{key} = :{key}, "
        expression_attribute_values[f":{key}"] = value
        expression_attribute_names[f"#{key}"] = key
    
    update_expression = update_expression.rstrip(', ')
    
    # Update the pet record in DynamoDB
    response = table.update_item(
        Key={'id': pet_id},
        UpdateExpression=update_expression,
        ExpressionAttributeNames=expression_attribute_names,
        ExpressionAttributeValues=expression_attribute_values,
        ReturnValues="UPDATED_NEW"
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f"Record {pet_id} updated successfully"})
    }
