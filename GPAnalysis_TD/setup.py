from setuptools import setup, find_packages
import os
from typing import List

def read_requirements(file_path: str) -> List[str]:
    with open(file_path, 'r') as f:
        return [line.strip() for line in f 
                if line.strip() 
                and not line.startswith('#')
                and not line.startswith('-e')]

# Read requirements
requirements = read_requirements('req.txt')

setup(
    name='GPAnalysis_TD',
    version='0.1.0',
    author='Tavish',
    author_email='tavish0554@gmail.com',
    description='A package for Gaussian Process Analysis with Temporal Dynamics',
    packages=find_packages(),
    install_requires=requirements,
)