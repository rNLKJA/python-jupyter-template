# setup.py
from setuptools import setup, find_packages

setup(
    name='python-jupyter-template',
    version='0.1.0',
    url='https://github.com/your-username/python-jupyter-template',
    author='Your Name',
    author_email='your-email@example.com',
    description=('A comprehensive Python and Jupyter notebook template for modern data science projects.'),
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[line.strip() for line in open("requirements.txt", "r")],
)
