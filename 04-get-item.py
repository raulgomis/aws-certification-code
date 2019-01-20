
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('rgomis-test2')

response = table.get_item(
    ConsistentRead=False,
    Key={
        'pk': 1,
        'sk': 2
    }
)
item = response['Item']
print(item)