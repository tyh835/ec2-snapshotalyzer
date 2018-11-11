def print_instances(instances):
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


def print_volumes(instances):
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