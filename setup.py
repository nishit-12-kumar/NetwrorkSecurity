'''
The setup.py file is an essential part of packaging and
distributing Python projects. It is used by setuptools
(or distutils in older Python versions) to define the configuration
of your project, such as its metadata, dependencies, and more...
'''

from setuptools import find_packages , setup
from typing import List


HYPEN_E_DOT = '-e .'

def get_requirements()->List[str]:

    '''
        this function will return the List of requirements
    '''

    requirements = []
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

print(get_requirements())


setup(
    name='Network Security',
    version='0.0.1',
    author='Nishit Kumar',
    author_email='nishitkumaroll12@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements()
)


