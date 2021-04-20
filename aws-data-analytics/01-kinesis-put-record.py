#!/usr/bin/env python3
import requests
import boto3
import uuid
import time
import random
import json

client = boto3.client('kinesis', region_name='us-east-1')
partition_key = str(uuid.uuid4())

number_of_results = 500
r = requests.get('https://randomuser.me/api/?exc=login&results=' + str(number_of_results))
data = r.json()["results"]

while True:
        records = []
        for user in data:
                records.append({
                        'Data': json.dumps(user),
                        'PartitionKey': partition_key,
                })
        print("Send records: " + str(len(records)))
        response = client.put_records(
                Records = records,
                StreamName='my-data-stream')
        print("Reponse: " + str(response))
        time.sleep(random.uniform(0, 1))