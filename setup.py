from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = 'e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[requirement.replace("\n"," ") for requirement in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        return requirements

setup(
    name="WaferFaultPrediction",
    version="0.0.1",
    author="Williams Efosa",
    author_email="efosa_email@yahoo.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)