import boto3
import botocore
from utils import has_pending_snapshots

def set_client(region=None, profile=None, **kwargs):
    session = boto3.Session()
    ec2 = session.resource('ec2')

    if profile:
        session = boto3.Session(profile_name=profile)

    if region:
        ec2 = session.resource('ec2', region_name=region)

    return ec2


def filter_instances(ec2, tag):
    instances = []

    if tag:
        try:
            tag = tag.split(':')
            filters = [{'Name':'tag:{0}'.format(tag[0]), 'Values':[tag[1]]}]
            instances = ec2.instances.filter(Filters=filters)
        except:
            print('Error: please provide a valid tag (Key:Value)')
            return instances
    else:
        instances = ec2.instances.all()

    return instances


def start_instance(ec2, id=None, instance=None):
    instance = instance or ec2.Instance(id)

    try:
        print('Starting {0}...'.format(instance.id))
        instance.start()
    except botocore.exceptions.ClientError as err:
        print(' Failed to start {0}. '.format(instance.id) + str(err))

    return


def stop_instance(ec2, id=None, instance=None):
    instance = instance or ec2.Instance(id)

    try:
        print('Stopping {0}...'.format(instance.id))
        instance.stop()
    except botocore.exceptions.ClientError as err:
        print(' Failed to stop {0}. '.format(instance.id) + str(err))

    return


def create_snapshot(ec2, id=None, instance=None):
    instance = instance or ec2.Instance(id)

    try:
        instance.stop()
        print('Stopping {0}...'.format(instance.id))
        instance.wait_until_stopped()

        for volume in instance.volumes.all():
            if has_pending_snapshots(volume):
                print(' Skipping {0}, snapshot already in progress'.format(volume.id))
                continue

            print(' Creating snapshot of {0}...'.format(volume.id))
            volume.create_snapshot(Description='Created by Snappy')

        instance.start()
        print('Restarting {0}...'.format(instance.id))
        instance.wait_until_running()
        print('Success')

    except botocore.exceptions.ClientError as err:
        print(' Failed to create snapshot of {0}. '.format(instance.id) + str(err))

    return