from setuptools import setup, find_packages

setup(
    name='mypackage',
    description='Example python package',
    version='0.1',
    packages=find_packages(exclude=['mytests*']),
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    author='David Usoro',
    author_email='usorodave1@gmail.com'
)