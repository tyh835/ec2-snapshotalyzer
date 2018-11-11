import click
from utils import filter_instances
from setup import (
    session,
    ec2,
    set_defaults
)


@click.group()
def cli():
    """Snappy manages EC2 instances and EBS snapshots"""
    pass


"""
***
*** Snappy list commands
***
"""

@cli.group('list')
def ls():
    """Commands for listing instances, volumes, and snapshots"""
    pass


# list instances
@ls.command('instances')
@click.option('--project', default=None, help='Show only instances for the project (tag Project:<Name>)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def list_instances(project, **kwargs):
    """List EC2 instances [options]"""
    set_defaults(**kwargs)
    instances = filter_instances(project)

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


# list volumes
@ls.command('volumes')
@click.option('--project', default=None, help='Show only volumes attached to instances of the project (tag Project:<Name>)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def list_volumes(project, **kwargs):
    """List EBS volumes [options]"""
    set_defaults(**kwargs)
    instances = filter_instances(project)

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


"""
***
*** Snappy start commands
***
"""

@cli.group('start')
def start():
    """Commands for starting instances"""
    pass


# start instances
@start.command('instances')
@click.option('--project', default=None, help='Start only instances for the project (tag Project:<Name>)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def start_instances(project, **kwargs):
    """Start EC2 instances in the default region, [options]"""
    set_defaults(**kwargs)
    instances = filter_instances(project)

    for i in instances:
        print('Starting {0}...'.format(i.id))
        i.start()

    return


# start instance --id
@start.command('instance')
@click.option('--id', default=None, help='Start only the instance with specified --id (required)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def start_instance(id, **kwargs):
    """Start EC2 instance in the default region, [options] --id (required)"""
    set_defaults(**kwargs)

    if not id:
        print('--id is a required parameter')
        return

    try:
        instance = ec2.Instance(id)
        print('Starting {0}...'.format(instance.id))
        instance.start()
    except:
        print('Failed to start {0}... Please ensure that the id is correct and you are using the correct region'.format(instance.id))

    return


"""
***
*** Snappy stop commands
***
"""

@cli.group('stop')
def stop():
    """Commands for stopping instances"""
    pass


# stop instances
@stop.command('instances')
@click.option('--project', default=None, help='Stop only instances for the project (tag Project:<Name>)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def stop_instances(project, **kwargs):
    """Stop EC2 instances in the default region, [options]"""
    set_defaults(**kwargs)
    instances = filter_instances(project)

    for i in instances:
        print('Stopping {0}...'.format(i.id))
        i.stop()

    return


# stop instance --id
@stop.command('instance')
@click.option('--id', default=None, help='Stop only the instance with specified --id (required)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def stop_instance(id, **kwargs):
    """Start EC2 instance in the default region, [options] --id (required)"""
    set_defaults(**kwargs)

    if not id:
        print('--id is a required parameter')
        return

    try:
        instance = ec2.Instance(id)
        print('Stopping {0}...'.format(instance.id))
        instance.stop()
    except:
        print('Failed to stop {0}... Please ensure that the id is correct and you are using the correct region'.format(instance.id))

    return


if __name__ == '__main__':
    cli()
