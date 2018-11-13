import boto3
import botocore


def set_client(region=None, profile=None, **kwargs):
    session = boto3.Session()
    ec2 = session.resource('ec2')

    if profile:
        session = boto3.Session(profile_name=profile)

    if region:
        ec2 = session.resource('ec2', region_name=region)

    return ec2


def filter_instances(tag, ec2):
    instances = []
    if tag:
        tag = tag.split(':')

    if tag:
        try:
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
        print('Failed to start {0}. '.format(instance.id) + str(err))
    except:
        print('Failed to start {0}. Please ensure that the id is correct and you are using the correct region'.format(instance.id))

    return


def stop_instance(ec2, id=None, instance=None):
    instance = instance or ec2.Instance(id)
    try:
        print('Stopping {0}...'.format(instance.id))
        instance.stop()
    except botocore.exceptions.ClientError as err:
        print('Failed to stop {0}. '.format(instance.id) + str(err))
    except:
        print('Failed to stop {0}... Please ensure that the id is correct and you are using the correct region'.format(instance.id))

    return


def create_snapshot(ec2, id=None, instance=None):
    instance = instance or ec2.Instance(id)
    try:
        print('Stopping {0}...'.format(instance.id))
        instance.stop()
        instance.wait_until_stopped()
        for volume in instance.volumes.all():
            print('Creating snapshot {0}...'.format(volume.id))
            volume.create_snapshot(Description='Created by Snappy')
        print('Restarting {0}...'.format(instance.id))
        instance.start()
        instance.wait_until_running()
        print('Success')
    except:
        print('Failed to create snapshot of {0}... Please ensure that the id is correct and you are using the correct region'.format(instance.id))

    return