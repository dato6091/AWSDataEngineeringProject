import base64
import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    client = boto3.client("dynamodb")

    print("Received event: " + json.dumps(event, indent=2))

    for record in event['Records']:
        # Decode Kinesis data (base64 encoded)
        t_record = base64.b64decode(record['kinesis']['data'])

        # Decode the bytes into a string
        str_record = str(t_record, 'utf-8')

        # Transform the json string into a dictionary
        dict_record = json.loads(str_record)

        # Create Overview row
        ############################################

        customer_key = dict()
        customer_key.update({'CustomerID': {"N": str(dict_record['CustomerID'])}})

        ex_customer = dict()
        ex_customer.update({str(dict_record['InvoiceNo']): {'Value': {"S":str(dict_record['Description'])}}})

        response = client.update_item(TableName='Customer', Key=customer_key, AttributeUpdates=ex_customer)
        
        print("Customer Key: ", customer_key)


        # Create Inventory row
        #############################################

        inventory_key = dict()
        inventory_key.update({'InvoiceNo': {"S": str(dict_record['InvoiceNo'])}})
        print("Inventory key: ", inventory_key)

        # Create the export dictionary 
        ex_dynamoRecord = dict()

        # Remove InvoiceNo and StockCode from the record, because want these fields to be 
        # the name of the row and the name of column respectively and they don't need to appear in the description
        stock_dict = dict(dict_record)
        stock_dict.pop("InvoiceNo", None)
        stock_dict.pop("StockCode", None)

        # Turn the dict into a json
        stock_json = json.dumps(stock_dict)

        # Create a record (column) for the InvoiceNo
        # Add the stock json to the column with teh name of the stock number
        ex_dynamoRecord.update({str(dict_record["StockCode"]): {"Value": {"S": stock_json}, "Action": "PUT"}})

        # print(ex_dynamoRecord)
        response = client.update_item(TableName='Invoice', Key=inventory_key, AttributeUpdates = ex_dynamoRecord)

        return "Successfully processed {} records.".format(len(event['Records']))




