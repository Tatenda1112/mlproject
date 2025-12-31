from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path, 'r') as file_obj:
        # Read lines and remove newline characters
        requirements = [req.replace("\n", "") for req in file_obj.readlines()]

        # Remove the '-e .' if it exists in the requirements.txt
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    # Filter out empty strings or comments
    return [req for req in requirements if req.strip() and not req.startswith('#')]

setup(
    name='MLPROJECTS',
    version='0.1.0',
    author='Tatenda Mukonoweshuro',
    author_email='tatendatatenda1112@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)