from setuptools import setup

setup(
    name='snappy',
    version='0.1',
    author='Tony Han',
    author_email='itony9401@live.com',
    description='Snappy is a CLI that uses `boto3` to manage AWS EC2 instance snapshots.',
    license='GPLv3+',
    packages=['snappy', 'snappy.client', 'snappy.utils'],
    url='https://github.com/tyh835/snappy',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        snappy=snappy.__main__:cli
    '''
)