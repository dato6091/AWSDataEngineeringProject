import pandas as pd
import requests

URL = "https://6bgdlcjkxa.execute-api.eu-west-1.amazonaws.com/Test/ingestionpl"

# Read the testfile
# Need to specify that InvoiceNo is a string, since the sample only has integers
data = pd.read_csv("Testdata.csv", sep=',', dtype={"InvoiceNo": str})


# Write a single row from the testfile into the api
# export = data.loc[2].to_json()
# response = requests.post(URL, data = export)
# print(response)

# Write all the rows from the testfile into the api as put request
for i in data.index:
    # convert the row to json
    export = data.loc[i].to_json()
    print(export)
    
    # send it to the api
    response = requests.post(URL, data=export)

    # print the return code
    print(response)