""" Regions class """
import boto3
from .abstractprovider import AbstractProvider
import argparse
import sys

class Regions(AbstractProvider):
    """
    Regions class which provides methods to retrieve information
    about available regions.

    Attributes:
        None
    """
    def get(self):
        """
        Retrieves cloud regions
        
        Args: 
            None

        Returns: 
            <dict> region information
        """
        client = boto3.client('ec2')
        response = client.describe_regions()

        regionlist = list()
        for key in response["Regions"]:
            regionlist.append(key["RegionName"])
        return { "Regions" : regionlist }

