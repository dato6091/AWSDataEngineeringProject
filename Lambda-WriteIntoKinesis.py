import json
import boto3

def lambda_handler(event, context):
    #Print the event to see it in CloudWatch
    print("My Event:")
    print(event)
    
    # Get the method from the request
    method = event['context']['http-method']
    
    if method == 'POST':
        
        # Get the body of the request and convert it into json object
        p_record = event['body-json']
        recordstring = json.dumps(p_record)
        
        # Start the kinesis client 
        client = boto3.client('kinesis')
        response = client.put_record(
            StreamName='APIDataStream', # Name of the Kinesis Data Stream
            Data=recordstring,
            PartitionKey='string' #REQUIRED but since we have only one shard, the value doesn´t matter
            )
        
        return {
            'statusCode': 200,
            'body': json.dumps(p_record)
            }
    
    elif method == 'GET':
        # Start the DynamoDB client to query the tables
        dynamo_client = boto3.client('dynamodb')
        
        # Get the customerID & the invoice number 
        # depending on what was passed, I will query the Customer table or the Invoice table
        im_customerID = event['params']['querystring']['CustomerID']
        im_InvoiceNo = event['params']['querystring']['InvoiceNo']

        if im_customerID:
            print(im_customerID)
            
            # Obtain the record, if exists, from the DynamoDB table
            response = dynamo_client.get_item(TableName = 'Customer', Key = {'CustomerID': {'N': im_customerID}})
            print(response['Item'])
        
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'])
            }

        elif im_InvoiceNo:
            print(im_InvoiceNo)
            
            # Obtain the record, if exists, from the DynamoDB table
            response = dynamo_client.get_item(TableName = 'Invoice', Key = {'InvoiceNo': {'S': im_InvoiceNo}})
            print(response['Item'])
        
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'])
            }
        
    
    
    else:
        return{
            'statusCode': 501,
            'body': json.dumps("Server Error")
        }
