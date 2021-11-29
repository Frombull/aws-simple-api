import json

print('Loading function')


def lambda_handler(event, context):
    # 1. Parse out query string params
    rawPath = event['rawPath']
    firstName = event['queryStringParameters']['firstName']
    lastName = event['queryStringParameters']['lastName']
    email = event['queryStringParameters']['email']

    # 2. Construct the body of the response object
    Response = {
        "rawPath": rawPath,
        "firstName": firstName,
        "lastName": lastName,
        "email": email
    }

    # 3. Create http response object
    responseObject = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(Response)
    }

    # 4. Return
    return responseObject
