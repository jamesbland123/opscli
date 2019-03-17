""" Azs class """
import boto3
from .abstractprovider import AbstractProvider
import argparse
import sys

class Azs(AbstractProvider):
    """
    Azs class which provides methods to retrieve information
    about azs within a region.

    Attributes:
        None
    """
    def get(self):
        """
        Retrieves azs for a region
        
        Args: 
            --region

        Returns: 
            <dict> azs information
        """

        parser = argparse.ArgumentParser(description='Returns account details')
        parser.add_argument('--region', help='region', default='us-west-2')
        args = parser.parse_args(sys.argv[3:])

        client = boto3.client('ec2', region_name=args.region)
        response = client.describe_availability_zones(Filters=[{'Name': 'region-name', 'Values': [args.region]}])
        print(args.region)

        azslist = list()
        for key in response["AvailabilityZones"]:
            azslist.append(key["ZoneName"])
        return { "AZS" : azslist }

