import boto3


def set_client(region=None, profile=None, **kwargs):
    session = boto3.Session()
    ec2 = session.resource('ec2')

    if profile:
        session = boto3.Session(profile_name=profile)

    if region:
        ec2 = session.resource('ec2', region_name=region)

    return ec2


def filter_instances(project, ec2):
    instances = []

    if project:
        filters = [{'Name':'tag:Project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    return instances


def start_instance(ec2, id=None, instance=None):
    try:
        instance = instance or ec2.Instance(id)
        print('Starting {0}...'.format(instance.id))
        instance.start()
    except:
        print('Failed to start {0}... Please ensure that the id is correct and you are using the correct region'.format(instance.id))

    return


def stop_instance(ec2, id=None, instance=None):
    try:
        instance = instance or ec2.Instance(id)
        print('Stopping {0}...'.format(instance.id))
        instance.stop()
    except:
        print('Failed to stop {0}... Please ensure that the id is correct and you are using the correct region'.format(instance.id))

    return