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
    ec2 = set_client(**kwargs)

    if id:
        print_volumes([ec2.Instance(id)])
        return

    instances = filter_instances(ec2, tag)

    print_volumes(instances)

    return


# list snapshots
@ls.command('snapshots')
@click.option('--tag', default=None, help='Show the most recent snapshot of EC2 instances with the corresponding tag (<Key>:<Value>)')
@click.option('--id', default=None, help='Show the most recent snapshot of EC2 instance with the specified id')
@click.option('--all', 'list_all', default=False, is_flag=True, help='Show all snapshots for each EC2 instance, not just the most recent')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def list_snapshots(tag, id, list_all, **kwargs):
    """List EBS snapshots [options]"""
    ec2 = set_client(**kwargs)

    if id:
        list_all = True
        print_snapshots([ec2.Instance(id)], list_all)
        return

    instances = filter_instances(ec2, tag)

    print_snapshots(instances, list_all)

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
@click.option('--id', default=None, help='Start EC2 instance with the specified id')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def start_instances(tag, id, **kwargs):
    """Start (all) EC2 instances [options]"""
    ec2 = set_client(**kwargs)

    if id:
        start_instance(ec2, id=id)
        return

    instances = filter_instances(ec2, tag)

    for instance in instances:
        start_instance(ec2, instance=instance)

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
@click.option('--id', default=None, help='Stop EC2 instance with the specified id')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def stop_instances(tag, id, **kwargs):
    """Stop (all) EC2 instances [options]"""
    ec2 = set_client(**kwargs)

    if id:
        stop_instance(ec2, id=id)
        return

    instances = filter_instances(ec2, tag)

    for instance in instances:
        stop_instance(ec2, instance=instance)

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
