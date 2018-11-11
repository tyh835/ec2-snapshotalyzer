# ec2-snapshotalyzer

Manage AWS EC2 instance snapshots.

## About

This project uses `boto3` to manage AWS EC2 instance snapshots.

## Configuring

Use the configuration file created by the AWS CLI. e.g.

`aws configure --profile snappy`

This profile should have access to list EC2 instances, start and stop EC2 instances, and filter EC2 instances by tag.

## Running

`pipenv run python scripts/snappy.py <command> <--project=PROJECT>`

*command* can be list, start, or stop.
*project* is optional, and represents the "Project" tag on EC2 instances.
