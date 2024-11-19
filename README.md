
# Data Ingestion and Processing Pipeline

This repository contains a comprehensive implementation of a data ingestion and processing pipeline using AWS services. The pipeline supports data ingestion, storage, transformation, and querying, showcasing the use of AWS Lambda, Kinesis, S3, DynamoDB, and API Gateway.

## Overview

The project consists of several components:

1. **Data Ingestion Pipeline**: 
   - Simulates real-time data streaming via a Python client.
   - Sends data to AWS API Gateway, which triggers a Lambda function to write into a Kinesis Data Stream.

2. **Stream to Raw Storage Pipeline**:
   - Writes data from Kinesis to an S3 bucket for raw data storage.

3. **Stream to DynamoDB Pipeline**:
   - Processes and reformats data from Kinesis and writes it to DynamoDB tables.

4. **API Pipeline to Query Data**:
   - Allows querying of stored data from DynamoDB using an API Gateway endpoint.

## Architecture

The pipeline consists of the following steps:

1. **Data Ingestion**:
   - A Python client reads data from a CSV file and streams it as JSON objects to the API Gateway.
   - The API Gateway triggers a Lambda function to write the data into Kinesis.

2. **Data Storage**:
   - A Lambda function reads data from Kinesis and writes it to:
     - **S3**: For raw data storage.
     - **DynamoDB**: For structured data storage.

3. **Data Querying**:
   - A Lambda function retrieves data from DynamoDB based on specified query parameters (e.g., InvoiceNo, CustomerID).
   - The API Gateway exposes an endpoint for querying the data.

## Prerequisites

- AWS account with access to:
  - Lambda
  - API Gateway
  - Kinesis
  - S3
  - DynamoDB
  - IAM
- Python 3.x with the following libraries:
  - `pandas`
  - `requests`
  - `boto3`

## Project Components

### 1. **Python Client**
   - Reads a CSV file using `pandas`.
   - Sends data as JSON objects to the API Gateway.
   - File: `PythonClient.py`

### 2. **Lambda Functions**
   - **Write to Kinesis**: Reads data from API Gateway and writes to Kinesis (`Lambda-WriteIntoKinesis.py`).
   - **Write to S3**: Reads data from Kinesis and writes to S3 (`Lambda-WriteIntoS3.py`).
   - **Write to DynamoDB**: Reads data from Kinesis, processes it, and writes to DynamoDB (`Lambda-WriteIntoDynamoDB.py`).
   - **Query DynamoDB**: Queries data from DynamoDB and returns results (`ReadDatafromDynamoDB.py`).

### 3. **AWS Resources**
   - **API Gateway**: Exposes endpoints for data ingestion and querying.
   - **Kinesis**: Serves as the intermediary for data streaming.
   - **S3**: Stores raw data for further processing.
   - **DynamoDB**: Stores structured data for querying.

### 4. **Testing**
   - Use Postman or the Python client to test API endpoints and ensure data integrity.

## How to Run

1. Clone this repository and navigate to the project directory.
2. Set up AWS resources as described in the document.
3. Configure IAM roles and permissions for Lambda functions.
4. Deploy Lambda functions and API Gateway.
5. Run the Python client to ingest data.
6. Use Postman or Python scripts to query data from DynamoDB.

## Files

- `PythonClient.py`: Simulates data ingestion.
- `Lambda-WriteIntoKinesis.py`: Writes data to Kinesis.
- `Lambda-WriteIntoS3.py`: Writes data to S3.
- `Lambda-WriteIntoDynamoDB.py`: Writes data to DynamoDB.
- `ReadDatafromDynamoDB.py`: Queries data from DynamoDB.

## Future Enhancements

- Implement automated testing for pipeline components.
- Add monitoring and alerting using AWS CloudWatch.
- Optimize DynamoDB capacity settings for scaling.
- Implement data transformation for downstream analytics.

## Author

Documented and implemented by [Your Name].

## License

This project is licensed under the MIT License. See the LICENSE file for details.
