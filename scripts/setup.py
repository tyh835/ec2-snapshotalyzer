import boto3

session = boto3.Session()
ec2 = session.resource('ec2')

def set_defaults(region=None, profile=None, **kwargs):
    if profile:
        global session
        session = boto3.Session(profile_name=profile)

    if region:
        global ec2
        ec2 = session.resource('ec2', region_name=region)

    return
