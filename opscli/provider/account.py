""" Account class """
import boto3
from .abstractprovider import AbstractProvider
import argparse
import sys

class Account(AbstractProvider):
    """
    Account class which provides methods to retrieve information
    about cloud accounts.

    Attributes:
        None
    """
    def get(self):
        """
        Retrieves cloud account information
        
        Args: 
            None

        Returns: 
            <dict> account information
        """
        parser = argparse.ArgumentParser(description='Returns account details')
        parser.add_argument('account')
        args = parser.parse_args(sys.argv[2:3])

        client = boto3.client('sts')
        account_id = client.get_caller_identity().get('Account')
        results = {"account_id" : account_id}
        return results

