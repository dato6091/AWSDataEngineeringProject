from __future__ import print_function

import base64
import json
import boto3
from datetime import datetime

s3_client = boto3.client("s3")

# Converting datetime object to string
dateTimeObj = datetime.now()

# Format the string
timestampStr = dateTimeObj.strftime("%d-%b-%Y-%H%M%S")

# This is the list for the records
kinesisRecords = []

def lambda_handler(event, context):
    print("Received event: " + str(json.dumps(event, indent=2)))
    print("Records:")
    print(event['Records'])

    print()
    
    for record in event['Records']:
        # Kinesis data is base 64 encoded, so I will decode it here
        payload = base64.b64decode(record['kinesis']['data'])
        # Still needs to be decoded from bytes to string
        payload = payload.decode("utf-8")
        # Append each record to the list
        kinesisRecords.append(payload)
        # For logging purposes
        print("Decoded payload:" + payload)

    # make a string out of the list. Backslash n for new line in the s3 file
    ex_string = "\n".join(kinesisRecords)

    # generate the name for the file with the timestamp
    mykey = 'output-' + timestampStr + '.txt'

    # put the file into the s3 bucket
    response = s3_client.put_object(Body=ex_string, Bucket='awsde-project', Key=mykey)

    return "Successfully processed {} records.".format(len(event['Records']))
