from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        requirements = [req for req in requirements if req != '-e .']
    return requirements


setup(
    name='NetflixDataScienceProject',
    version='0.0.1',
    author='Durga Charan',
    author_email='mallickdurgacharan188@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)