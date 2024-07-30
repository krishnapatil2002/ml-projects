# setup.py is responsible in creating the machine learning application as a package or we can say ist is the overview of the application
# -e .  is used to trigger the step up file which is used in requirements.txt
from setuptools import find_packages,setup

from typing import List


HYPEN = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requiremnts 
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # reading one line at a time 
        requirements = [req.replace("/n"," ") for req in requirements]

        if HYPEN in requirements:
            requirements.remove(HYPEN)
setup(  
name = 'mlproject',
version='1.1.1',
author='krishna patil',
packages=find_packages(),
author_email='patilkrishna4849@gmail.com',
install_requires=get_requirements('requirement.txt')
)