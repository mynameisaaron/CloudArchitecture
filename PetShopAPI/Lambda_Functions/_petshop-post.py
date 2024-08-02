# NOTE TWO THINGS:
# 1) CONFIRM THAT YOUR TABLE VARIABLE IN THE LAMBDA_HANDLER REFERENCES THE NAME OF YOUR PETSHOP DATABASE
# 2) THIS LAMBDA FUNTION WILL BE TRIGGERED BY THE API GATEWAY'S POST METHOD (IN THE NEXT STEP)
import boto3
import json
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table('PetShopAPI')
    
    try:
        # Extract the request body
        body = json.loads(event['body'])
        
        # Add the item to DynamoDB
        response = table.put_item(
            Item={
                'id': body['id'],
                'name': body['name'],
                'breed': body['breed'],
                'gender': body['gender'],
                'owner': body['owner'],
                'birthday': body['birthday']
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f"Record {body['id']} added successfully"})
        }
    
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': f"Missing required field: {str(e)}"})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f"Database error: {str(e)}"})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f"An unexpected error occurred: {str(e)}"})
        }
