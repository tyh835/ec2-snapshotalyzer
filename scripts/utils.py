import boto3


def set_defaults(region=None, profile=None, **kwargs):
    session = boto3.Session()
    ec2 = session.resource('ec2')

    if profile:
        session = boto3.Session(profile_name=profile)

    if region:
        ec2 = session.resource('ec2', region_name=region)

    return ec2


def filter_instances(project, ec2=None):
    instances = []

    if project:
        filters = [{'Name':'tag:Project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    return instances
