import json

from color_logger import ColorLog

log = ColorLog()
log.info('Loading lambda function')


def lambda_handler(event, context):
    # Parse out query string params
    rawPath = event['rawPath']
    firstName = event['queryStringParameters']['firstName']
    lastName = event['queryStringParameters']['lastName']
    email = event['queryStringParameters']['email']

    # Process data
    path = event['rawPath'].lower()

    if path(event) == 'get':
        pass
        # TODO: Get item from db

    elif path(event) == 'create':
        pass
        # TODO: Create item in db


    # TODO: Create http response object
    responseObject = {
        "statusCode": http_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response_body)
    }

    # 4. Return
    return responseObject
