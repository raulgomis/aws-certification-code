#!/usr/bin/env python3
from __future__ import print_function

import os
import boto3

region = os.environ.get('AWS_DEFAULT_REGION', 'ap-southeast-2')

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name=region)

table_name = "rgomis-test2"

params = {
    'TableName' : table_name,
    'KeySchema': [       
        { 'AttributeName': "pk", 'KeyType': "HASH"},    # Partition key
        { 'AttributeName': "sk", 'KeyType': "RANGE" }   # Sort key
    ],
    'AttributeDefinitions': [       
        { 'AttributeName': "pk", 'AttributeType': "N" },
        { 'AttributeName': "sk", 'AttributeType': "N" }
    ],
    'ProvisionedThroughput': {       
        'ReadCapacityUnits': 10, 
        'WriteCapacityUnits': 10
    }
}

# Create the table
table = dynamodb.create_table(**params)

# Wait for the table to exist before exiting
print('Waiting for', table_name, '...')
table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

# Print out some data about the table.
print(table.item_count)
