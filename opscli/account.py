import boto3

def get_account():
    client = boto3.client('sts')
    account_id = client.get_caller_identity().get('Account')
    return account_id