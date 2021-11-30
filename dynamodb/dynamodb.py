import boto3
from botocore.config import Config

from logger import ColorLog


log = ColorLog()

my_config = Config(
    region_name='sa-east-1',
    signature_version='v4',
    retries={
        'max_attempts': 3,
        'mode': 'standard'
    }
)

TABLE_NAME = 'persons-table'
dynamodb_client = boto3.client('dynamodb', config=my_config)

item = {
    'firstName': {'S': 'Marco'},
    'lastName': {'S': 'Di Toro'},
    'email': {'S': 'marco@somemail.com'}
}


def main():
    response = dynamodb_client.put_item(TableName=TABLE_NAME,
                                        Item=item)
    http_response = response["ResponseMetadata"]["HTTPStatusCode"]

    if http_response == 200:
        log.info('Item added successfuly!')
    else:
        log.error(f'{http_response} Error adding item to DB ')



if __name__ == '__main__':
    main()
