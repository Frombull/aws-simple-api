import json

import boto3
from botocore.config import Config
from botocore.exceptions import ClientError

from logger import ColorLog


my_config = Config(
    region_name='sa-east-1',
    signature_version='v4',
    retries={
        'max_attempts': 3,
        'mode': 'standard'
    }
)
TABLE = 'persons-table'
dynamodb = boto3.client('dynamodb', config=my_config)

log = ColorLog()


def savePerson(*, first_name: str, last_name: str, email: str) -> dict:
    response = dynamodb.put_item(TableName=TABLE,
                                 Item={
                                     'firstName': {'S': first_name},
                                     'lastName': {'S': last_name},
                                     'email': {'S': email}
                                 })

    http_code = response["ResponseMetadata"]["HTTPStatusCode"]
    if http_code == 200:
        log.info('Item added successfuly!')
    else:
        log.error(f'{http_code}, Error adding item to DB ')

    return response


def getPerson(*, first_name: str, last_name: str):
    response = dynamodb.get_item(TableName=TABLE,
                                 Key={
                                    'firstName': {'S': first_name},
                                    'lastName': {'S': last_name},
                                 })

    http_code = response['ResponseMetadata']['HTTPStatusCode']
    if http_code == 200:
        log.info('Item retrieved successfuly!')
    else:
        log.error(f'{http_code}, Error retrieving item from DB ')

    return response


if __name__ == '__main__':
    #savePerson(first_name='TestFirstName', last_name='TestLastName', email='test@somemail.com')
    #getPerson(first_name='Bestfirstname', last_name='Evenbetterlastname')
    pass

