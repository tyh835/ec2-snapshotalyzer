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
@click.option('--project', default=None, help='Show only instances for the project (tag Project:<Name>)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def list_instances(project, **kwargs):
    """List EC2 instances [options]"""
    ec2 = set_client(**kwargs)
    instances = filter_instances(project, ec2)

    print_instances(instances)

    return


# list volumes
@ls.command('volumes')
@click.option('--project', default=None, help='Show only volumes attached to instances of the project (tag Project:<Name>)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def list_volumes(project, **kwargs):
    """List EBS volumes [options]"""
    ec2 = set_client(**kwargs)
    instances = filter_instances(project, ec2)

    print_volumes(instances)

    return


# list snapshots
@ls.command('snapshots')
@click.option('--project', default=None, help='Show only volumes attached to instances of the project (tag Project:<Name>)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def list_snapshots(project, **kwargs):
    """List EBS volumes [options]"""
    ec2 = set_client(**kwargs)
    instances = filter_instances(project, ec2)

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
@click.option('--project', default=None, help='Start only instances of the project (tag Project:<Name>)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def start_instances(project, **kwargs):
    """Start EC2 instances [options]"""
    ec2 = set_client(**kwargs)
    instances = filter_instances(project, ec2)

    for instance in instances:
        start_instance(ec2, instance=instance)

    return


# start instance --id
@start.command('instance')
@click.option('--id', default=None, help='Start the instance with specified --id (required)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def start_instance_by_id(id, **kwargs):
    """Start a specific EC2 instance by id [options]"""
    if not id:
        print('Error: --id is a required parameter')
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
@click.option('--project', default=None, help='Stop only instances of the project (tag Project:<Name>)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def stop_instances(project, **kwargs):
    """Stop EC2 instances [options]"""
    ec2 = set_client(**kwargs)
    instances = filter_instances(project, ec2)

    for instance in instances:
        stop_instance(ec2, instance=instance)

    return


# stop instance --id
@stop.command('instance')
@click.option('--id', default=None, help='Stop the instance with specified --id (required)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def stop_instance_by_id(id, **kwargs):
    """Start a specific EC2 instance by id [options]"""
    if not id:
        print('Error: --id is a required parameter')
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


# create snapshots
@create.command('snapshots')
@click.option('--project', default=None, help='Create snapshots for only instances of the project (tag Project:<Name>)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def create_snapshots(project, **kwargs):
    """Create snapshots of EC2 instances [options]"""
    ec2 = set_client(**kwargs)
    instances = filter_instances(project, ec2)

    for instance in instances:
        for volume in instance.volumes.all():
            create_snapshot(ec2, volume=volume)

    return


# create snapshot --id
@create.command('snapshot')
@click.option('--id', default=None, help='Create snapshot of the instance with specified --id (required)')
@click.option('--region', default=None, help='Specify the AWS region of the resources.')
@click.option('--profile', default=None, help='Specify the AWS profile to use as credentials.')
def create_snapshot_by_id(id, **kwargs):
    """Create snapshot of an EC2 instance by id [options]"""
    if not id:
        print('Error: --id is a required parameter')
        return

    ec2 = set_client(**kwargs)

    create_snapshot(ec2, id=id)

    return


if __name__ == '__main__':
    cli()
