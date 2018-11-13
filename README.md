# Snappy

Version: 0.2.3

## About

Snappy is a CLI that uses `boto3` to manage AWS EC2 instance snapshots.

## Configuring for Development

Run `pipenv install` in the file directory.

If you don't yet have `pipenv`, install at [https://pipenv.readthedocs.io/en/latest/](https://pipenv.readthedocs.io/en/latest/)

Use the standard configuration on the AWS CLI. e.g.

`aws configure`

and add your Access and Secret keys.

The profile you use with SnapPy should have the following IAM permissions:

- `ec2:DescribeTags`
- `ec2:DescribeInstances`
- `ec2:DescribeInstanceAttribute`
- `ec2:DescribeInstanceStatus`
- `ec2:DescribeVolumes`
- `ec2:DescribeVolumeAttribute`
- `ec2:DescribeVolumeStatus`
- `ec2:DescribeSnapshots`
- `ec2:DescribeSnapshotAttribute`
- `ec2:DescribeClassicLinkInstances`
- `ec2:StartInstances`
- `ec2:StopInstances`
- `ec2:RebootInstances`
- `ec2:CreateSnapshot`

Or use the following IAM Policy JSON configuration:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SnapPyPolicy",
            "Effect": "Allow",
            "Action": [
                "ec2:RebootInstances",
                "ec2:DescribeInstances",
                "ec2:DescribeTags",
                "ec2:DescribeSnapshotAttribute",
                "ec2:DescribeInstanceAttribute",
                "ec2:DescribeClassicLinkInstances",
                "ec2:DescribeSnapshots",
                "ec2:StopInstances",
                "ec2:DescribeVolumeAttribute",
                "ec2:DescribeVolumeStatus",
                "ec2:StartInstances",
                "ec2:DescribeVolumes",
                "ec2:CreateSnapshot",
                "ec2:DescribeInstanceStatus"
            ],
            "Resource": "*"
        }
    ]
}
```

## Running

`pipenv run python main.py <command> <resource> <options>`

`command` can be list, start, stop, reboot, or create.

`resource` can be instances, volumes, or snapshots as appropriate.

## Options

`--tag` is optional, and filters AWS resources by the tag provided (Key:Value).

`--id` specifies the AWS id of the AWS resource.

`--force` to run the command on all resources on the region when no tag or id is specified.

`--region` specifies the AWS region of the resources.

`--profile` specifies the AWS profile to use as credentials.

`--all` is an option for listing snapshots. Lists all snapshots rather than just most recent ones.

## Installation

You can build from source by cloning the this git repository:

`git clone https://github.com/tyh835/snappy.git`

and build by running `cd snappy && pipenv install` and `pipenv run python setup.py bdist_wheel`.

Then, install the binary using `pip3 install dist/<wheel-file-name-here>.whl`

Or, you can install the binary directly at:

`pip3 install https://s3-us-west-2.amazonaws.com/tyh835-bin/snappy-0.2.3-py3-none-any.whl`

Then, run `snappy --help` and you are set!