# Standard in packages that you create. Used to to create installable packages.

from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Darrell Hale',
    author_email='look585carbon@gmail.com',
    description='A utility for backing up PostgreSQL databases.',
    long_description=long_desscription,
    long_description_content_type='text/markdown',
    url='https://github.com/darrelldhale/pgbackup',
    packages=find_packages('src')

)



