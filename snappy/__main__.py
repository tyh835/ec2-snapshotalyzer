import click
from utils import print_instances, print_volumes, print_snapshots
from client import (
    set_client,
    filter_instances,
    start_instance,
    stop_instance,
    create_snapshot
)

@click.group()
def cli():
    """
    Snappy manages EC2 instances and EBS snapshots

    Append [options] to the end of the command
    """
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
@click.option('--tag', default=None, help='Show EC2 instances with the corresponding tag (<Key>:<Value>)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def list_instances(tag, **kwargs):
    """List EC2 instances [options]"""
    ec2 = set_client(**kwargs)
    instances = filter_instances(ec2, tag)

    print_instances(instances)

    return


# list volumes
@ls.command('volumes')
@click.option('--tag', default=None, help='Show volumes of EC2 instances with the corresponding tag (<Key>:<Value>)')
@click.option('--id', default=None, help='Show volumes of EC2 instance with the specified id')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def list_volumes(tag, id, **kwargs):
    """List EBS volumes [options]"""
    instances = []
    ec2 = set_client(**kwargs)

    if id:
        instances = [ec2.Instance(id)]
    else:
        instances = filter_instances(ec2, tag)

    print_volumes(instances)

    return


# list snapshots
@ls.command('snapshots')
@click.option('--tag', default=None, help='Show snapshots of EC2 instances with the corresponding tag (<Key>:<Value>)')
@click.option('--id', default=None, help='Show snapshots of EC2 instance with the specified id')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def list_snapshots(tag, id=None, **kwargs):
    """List EBS snapshots [options]"""
    instances = []
    ec2 = set_client(**kwargs)

    if id:
        instances = [ec2.Instance(id)]
    else:
        instances = filter_instances(ec2, tag)

    print_snapshots(instances)

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
@click.option('--tag', default=None, help='Start EC2 instances with the corresponding tag (<Key>:<Value>)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def start_instances(tag, **kwargs):
    """Start (all) EC2 instances [options]"""
    ec2 = set_client(**kwargs)
    instances = filter_instances(ec2, tag)

    for instance in instances:
        start_instance(ec2, instance=instance)

    return


# start instance --id
@start.command('instance')
@click.option('--id', default=None, help='Start EC2 instance with the specified id')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def start_instance_by_id(id, **kwargs):
    """Start a specific EC2 instance by id [options]"""
    if not id:
        print('Error: --id is a required option')
        return

    ec2 = set_client(**kwargs)

    start_instance(ec2, id=id)

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
@click.option('--tag', default=None, help='Stop EC2 instances with the corresponding tag (<Key>:<Value>)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def stop_instances(tag, **kwargs):
    """Stop (all) EC2 instances [options]"""
    ec2 = set_client(**kwargs)
    instances = filter_instances(ec2, tag)

    for instance in instances:
        stop_instance(ec2, instance=instance)

    return


# stop instance --id
@stop.command('instance')
@click.option('--id', default=None, help='Stop EC2 instance with the specified id')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def stop_instance_by_id(id, **kwargs):
    """Start a specific EC2 instance by id [options]"""
    if not id:
        print('Error: --id is a required option')
        return

    ec2 = set_client(**kwargs)

    stop_instance(ec2, id=id)

    return


"""
***
*** Snappy stop commands
***
"""

@cli.group('create')
def create():
    """Commands for creating snapshots"""
    pass


# create snapshots [--id]
@create.command('snapshots')
@click.option('--tag', default=None, help='Create snapshots of EC2 instances with the corresponding tag (<Key>:<Value>)')
@click.option('--id', default=None, help='Create snapshots of EC2 instance with specified id')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def create_snapshots(tag, id, **kwargs):
    """Create snapshots of (all) EC2 instances [options]"""
    ec2 = set_client(**kwargs)

    if id:
        create_snapshot(ec2, id=id)
        return

    instances = filter_instances(ec2, tag)

    for instance in instances:
        create_snapshot(ec2, instance=instance)

    return


if __name__ == '__main__':
    cli()
