from setuptools import setup

setup(
    name='snappy',
    version='0.2.0',
    author='Tony Han',
    author_email='itony9401@live.com',
    description='Snappy is a CLI that uses `boto3` to manage AWS EC2 instance snapshots.',
    long_description='''
        Usage: snappy [OPTIONS] COMMAND [ARGS]...

        Snappy manages EC2 instances and EBS snapshots

        Append [options] to the end of the command

        Options:
          --help     Show this message and exit.
          --version  Show the version and exit.

        Commands:
          create  Commands for creating snapshots
          list    Commands for listing instances, volumes, and snapshots
          start   Commands for starting instances
          stop    Commands for stopping instances
    ''',
    keywords='aws ec2 ebs snapshot management cli',
    license='GPLv3+',
    packages=['snappy'],
    url='https://github.com/tyh835/snappy',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        snappy=snappy.snappy:cli
    ''',
    platforms=['any']
)