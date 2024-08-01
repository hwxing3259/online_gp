from setuptools import setup
import os
import sys


setup(
    name='online_gp',
    version='1.0.0',
    description=('Repo for Streaming GPs'),
    long_description='see github',
    author='',
    author_email='',
    url='',
    license='MPL-2.0',
    packages=['online_gp'],
    install_requires=['setuptools>=41.0.0',
'matplotlib>=3.0.3',
'seaborn',
'scipy>=1.2.1',
'torch>=1.6.0',
'numpy>=1.16.2',
'gpytorch>=0.3.1',
'botorch',
'scikit_learn>=0.20.3',
'pandas>=1.0',
's3fs>=0.4',
'tabulate',
'hydra-core>=1.0',
'xlrd'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 0',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.7'],
)
