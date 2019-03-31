
import boto3
import logging

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='rgomis-test')

# Process messages by printing out body and optional author name
while(True):
    for message in queue.receive_messages(
            AttributeNames=[
                'SentTimestamp'
            ],
            MaxNumberOfMessages=1,
            MessageAttributeNames=[
                'All'
            ],
            WaitTimeSeconds=20
            ):
        # Get the custom author message attribute if it was set
        author_text = ''
        if message.message_attributes is not None:
            author_name = message.message_attributes.get('Author').get('StringValue')
            if author_name:
                author_text = ' ({0})'.format(author_name)

        # Print out the body and author (if set)
        print('Hello, {0}!{1}'.format(message.body, author_text))

        # Let the queue know that the message is processed
        message.delete()


