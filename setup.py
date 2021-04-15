#!/usr/bin/env python3

from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))
#here = path.abspath(path.dirname('setup.py'))

# read long description 
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

# read dependencies 
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    depends = f.read()

# for packaging files must be in a package (with init) and listed in package_data
# package-externals can be included with data_files,
# and there is a bug in pattern matching http://bugs.python.org/issue19286
# install unclear for data_files

setup(
    # package info
    name='PythonPackage',
    version='0.0.0',
    description='description',
    long_description=readme,
    long_description_content_type='text/markdown',

    # project homepage
    url='https://github.com/twesleyb/PythonPackage',

    # author info
    author='Tyler Bradshaw',
    author_email='twesleyb10@gmail.com',

    # choose your license
    license='MIT',

    # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Bio-Informatics',

        # The license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],

    # What PythonPackage relates to:
    keywords='python package example',

    # Specify  packages via find_packages() and exclude the tests and
    # documentation:
    packages=find_packages(),

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    include_package_data=True,
    package_data={
        'pythonpackage.data.raw': ['*.*'], # yaml is a good format!
    },

    # Runtime dependencies. (will be installed by pip when EVcouplings is installed)
    #setup_requires=['setuptools>=18.2', 'numpy'],

    # FIXME: should read from requirements.txt!
    install_requires=['setuptools>=18.2', 'numpy', 'pandas']
    
)
