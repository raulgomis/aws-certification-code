
import boto3
import time

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('rgomis-test2')

for x in range(1, 200):
    table.put_item(
    Item={
            'pk': x,
            'sk': 2,
            'username': 'rgomis',
            'first_name': 'Raul',
            'last_name': 'Gomis',
            'age': 32,
            'account_type': 'standard_user',
        }
    )