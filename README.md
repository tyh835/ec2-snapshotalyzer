# SnapPy

## About

Snappy is a CLI that uses `boto3` to manage AWS EC2 instance snapshots.

## Installation

Run `pipenv install` in the file directory.

If you don't yet have `pipenv`, install at [https://pipenv.readthedocs.io/en/latest/](https://pipenv.readthedocs.io/en/latest/)

## Configuring

Use the standard configuration on the AWS CLI. e.g.

`aws configure`

and add your Access and Secret keys.

The profile should have full-access to AWS EC2 (more restrictive permissions pending).

## Running

`pipenv run python main.py <command> <resource> <options>`

`command` can be list, start, stop, or create.

`resource` can be instances, volumes, or snapshots as appropriate.

## Options

`--tag` is optional, and filters AWS resources by the tag provided (Key:Value).

`--id` specifies the AWS id of the AWS resource.

`--region` specifies the AWS region of the resources.

`--profile` specifies the AWS profile to use as credentials.

*--all* is an option for listing snapshots. Lists all snapshots rather than just most recent ones.
