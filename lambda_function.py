import json
import logging
import os

import boto3


def lambda_handler(event, context):
    try:
        client = boto3.client('sns')
        for record in event['Records']:
            print("record : {}".format(json.dumps(record)))
            subject = get_subject(record)
            response = client.publish(
                TopicArn=os.environ['topic_arn'],
                Message=json.dumps(record),
                Subject=subject
            )
            response_log = get_response_log(record, response)
            print(response_log)
            print('........................................................')


    except Exception as e:
        logging.error(e)


def get_response_log(record, response):
    return "response : {}".format(response) + " for request (keys) {}".format(
        record["dynamodb"]["Keys"])


def get_subject(record):
    subject = record["eventName"].lower() + " " + json.dumps(record["dynamodb"]["Keys"])
    return subject
