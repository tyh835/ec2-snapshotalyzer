def print_instances(instances):
    for i in instances:
        tags = { t['Key']: t['Value'] for t in i.tags or [] }
        print(', '.join([
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            'Project: {0}'.format(tags.get('Project', '<no project>'))
        ]))

    return


def print_volumes(instances):
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


def print_snapshots(instances):
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

    return