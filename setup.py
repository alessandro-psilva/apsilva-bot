import os
from setuptools import setup



def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def geckodriver():
    pass

setup(
    name='apsilva-bot',
    version='1.0.0',
    description='Bot para Instagram',
    author='Alessandro Silva',
    author_email='alessandro-psilva@outlook.com',
    packages=[
        'apsilva_bot',
    ],
    long_description=read('README.md'),  
    install_requires=[
        'selenium~=3.141.0',
    ],
)

geckodriver()