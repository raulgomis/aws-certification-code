
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('rgomis-test2')

response = table.scan(
    FilterExpression=Attr('age').eq(32)
)
items = response['Items']
print(items)