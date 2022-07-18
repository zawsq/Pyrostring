from setuptools import find_packages, setup

from Pyrostring.__version__ import __Pyrostring__ 

with open("requirements.txt") as requirements_txt:
    requirements = requirements_txt.read().splitlines()


setup(
      name='Pyrostring',
      version=__Pyrostring__,
      description='Pyrogram Fast Session String Generator',
      author='GojouSats',
      url='https://github.com/GojouSats/Pyrostring',
      packages=find_packages(),
      install_requires=requirements
     )    
    
