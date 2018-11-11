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


def filter_instances(project):
    instances = []

    if project:
        filters = [{'Name':'tag:Project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    return instances

