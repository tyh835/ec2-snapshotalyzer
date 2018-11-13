# ec2-snapshotalyzer

Manage AWS EC2 instance snapshots.

## About

Snappy is a CLI that uses `boto3` to manage AWS EC2 instance snapshots.

## Configuring

Use the configuration file created by the AWS CLI. e.g.

`aws configure --profile snappy`

This profile should have full-access to AWS EC2 (more restrictive permissions pending).

## Running

`pipenv run python snappy <command> <resource> <options>`

*command* can be list, start, stop, or create.

*resource* can be instances, volumes, or snapshots as appropriate.

### Options

*--tag* is optional, and filters AWS resources by the tag provided (Key:Value).

*--id* specifies the AWS id of the AWS resource.

*--region* specifies the AWS region of the resources.

*--profile* specifies the AWS profile to use as credentials.

*--all* is an option for listing snapshots. Lists all snapshots rather than just most recent ones.