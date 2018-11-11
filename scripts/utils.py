import boto3


def set_client(region=None, profile=None, **kwargs):
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


def print_instances(instances):
    for i in instances:
        tags = { t['Key']: t['Value'] for t in i.tags or [] }
        print(', '.join([
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            tags.get('Project', '<no project>')
        ]))

    return


def print_volumes(instances):
    for i in instances:
        tags = { t['Key']: t['Value'] for t in i.tags or [] }
        for v in i.volumes.all():
            print(', '.join([
            v.id,
            i.id,
            v.state,
            str(v.size) + 'GiB',
            v.encrypted and 'Encrpyted' or 'Not Encrypted',
            tags.get('Project', '<no project>')
        ]))

    return