""" Account class """
import boto3
from .abstractprovider import AbstractProvider

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
        client = boto3.client('sts')
        account_id = client.get_caller_identity().get('Account')
        return account_id

