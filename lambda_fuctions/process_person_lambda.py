import json
import logging as log


log.basicConfig(level=log.INFO,
                format='[%(levelname)s] (%(asctime)s) - %(message)s',
                datefmt='%H:%M:%S')

log.info('Loading function')


def lambda_handler(event, context):
    # Parse out query string params
    rawPath = event['rawPath']
    firstName = event['queryStringParameters']['firstName']
    lastName = event['queryStringParameters']['lastName']
    email = event['queryStringParameters']['email']

    # Process data
    if eventPath(event) == 'get':
        Response = {
            "rawPath": rawPath,
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "message": "GET METHOD"
        }
    elif eventPath(event) == 'create':
        Response = {
            "rawPath": rawPath,
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "message": "USER CREATED"
        }

    # Create http response object
    responseObject = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(Response)
    }

    # 4. Return
    return responseObject


def eventPath(event):
    if event['rawPath'].lower() == '/getperson':
        return 'get'
    elif event['rawPath'].lower() == '/createperson':
        return 'create'
    else:
        return None
