# ec2-snapshotalyzer

Manage AWS EC2 instance snapshots.

## About

This project uses `boto3` to manage AWS EC2 instance snapshots.

## Configuring

Use the configuration file created by the AWS CLI. e.g.

`aws configure --profile snappy`

This profile should have full-access to AWS EC2 (more restrictive permissions pending).

## Running

`pipenv run python scripts/snappy.py <command> <resource> <options>`

*command* can be list, start, stop, or create.
*resource* can be instance(s), volume(s), or snapshot(s) when appropriate.

### Options

*--project* is optional, and represents the "Project" tag on the EC2 instances.
*--id* specifies the AWS id of the AWS resource.
*--region* specifies the AWS region of the resources.
*--profile* specifies the AWS profile to use as credentials.