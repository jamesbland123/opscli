import boto3
from .abstractprovider import AbstractProvider

class Account(AbstractProvider):
    def get(self):
        client = boto3.client('sts')
        account_id = client.get_caller_identity().get('Account')
        return account_id

    def help(self):
        pass