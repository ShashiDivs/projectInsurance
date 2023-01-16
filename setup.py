from setuptools import find_packages, setup
from typing import List

requirement_file_name = 'requirements.txt'
REMOVE_PACKAGE = '-e .'

def get_requirements()->List[str]:
    with open(requirement_file_name) as requirement_file:
        requirement_list = requirement_file.readlines()
    
    requirement_list = [requirement_name.replace('\n','') for requirement_name in requirement_list]

    if REMOVE_PACKAGE in requirement_list:
        requirement_list.remove(REMOVE_PACKAGE)
    return requirement_list



setup(name='Insurance',
    version='0.0.3',
    description='Insurance Industry level Project',
    author='Shashi',
    author_mail='shashipolity@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements()
)