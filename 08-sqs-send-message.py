
import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='rgomis-test')

# Create a new message
for x in range(1,100):
    response = queue.send_message(MessageBody="message #%s" % x)
    # The response is NOT a resource, but gives you a message ID and MD5
    print(response.get('MessageId'))
    print(response.get('MD5OfMessageBody'))


