def print_instances(instances):
    """List EC2 instances"""

    for i in instances:
        tags = []

        if i.tags:
            tags = ['{0}:{1}'.format(t['Key'], t['Value']) for t in i.tags ] or []

        print(', '.join([
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
        ] + tags))

    return


def print_volumes(instances):
    """Lists EBS volumes"""

    for i in instances:
        for v in i.volumes.all():
            print(', '.join([
                v.id,
                i.id,
                v.state,
                str(v.size) + 'GiB',
                v.encrypted and 'Encrpyted' or 'Not Encrypted',
            ]))

    return


def print_snapshots(instances, list_all):
    """Lists volume snapshots (most recent or all)"""

    for i in instances:
        for v in i.volumes.all():
            for s in v.snapshots.all():
                print(', '.join([
                    s.id,
                    v.id,
                    i.id,
                    s.state,
                    s.progress,
                    s.start_time.strftime('%c'),
                ]))

                if s.state == 'completed' and not list_all:
                    break

    return


def has_pending_snapshots(volume):
    """Determines whether a volume has pending snapshots"""

    snapshots = list(volume.snapshots.all())
    return snapshots and snapshots[0].state == 'pending'