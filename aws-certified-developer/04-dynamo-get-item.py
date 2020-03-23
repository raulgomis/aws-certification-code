
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('rgomis-test2')

response = table.get_item(
    ConsistentRead=False,
    Key={
        'pk': 2,
        'sk': 2
    }
)
 
if hasattr(response, 'Item'):
    print(item)
else: 
    print("Element not found")

