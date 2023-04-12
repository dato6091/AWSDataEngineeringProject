import requests
import json

URL = "https://6bgdlcjkxa.execute-api.eu-west-1.amazonaws.com/Test/ingestionpl"

# Declare the InvoiceNo variable 
InvoiceNo = '536365'
req_params = {'InvoiceNo': InvoiceNo}


response = requests.get(URL, params=req_params)

json_data = response.json()

body = json.loads(json_data['body'])

# Create a new dictionary to hold the structured data
structured_data = {}

# Iterate over the items in the body
for k, v in body.items():
    # Extract the nested dictionary from the value string
    nested_dict = json.loads(v['S'])
    # Add the nested dictionary to the structured data dictionary
    structured_data[k] = nested_dict

# Add the structured InvoiceNo to the structured data dictionary
structured_data['InvoiceNo'] = body['InvoiceNo']['S']

print("Stock codes in InvoiceNo:", InvoiceNo)
for k, v in structured_data.items():
    if k != 'InvoiceNo':
        print(k, v)
