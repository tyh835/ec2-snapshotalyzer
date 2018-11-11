import boto3

session = boto3.Session(profile_name='snappy')
ec2 = session.resource('ec2')

def list_instances():
    for instance in ec2.instances.all():
        print(instance)

if __name__ == '__main__':
    list_instances()
