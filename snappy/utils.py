def print_instances(instances):
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

            if s.state == 'completed' and not list_all: break

    return