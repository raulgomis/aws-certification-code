
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('rgomis-test2')

for x in range(1, 200):
    response = table.delete_item(
        Key={
            'pk': x,
            'sk': 2
        }
    )
