from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(filepath:str)->List[str]:
    
    ''' This function will return the list of requirements '''
    
    requirements=[]
    with open(filepath) as fileObj:
        requirements=fileObj.readlines()
        requirements=[req.replace('\n',' ') for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject', 
    version='1.0',
    author='Arindam Ghosh',
    author_email='arindamsmith@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)