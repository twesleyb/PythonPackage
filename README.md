# PythonPackage

An example python package.

The EVcouplings package was used as an example.

## The Python Environment

Always try to work in a python virtual environment. I find that `conda` works
well for me. 
* Create a new environment
* Install pip
* Install requirments.txt with pip, `pip install -r requirments.txt`

## Installation
```
# you need the build package
pip install build

python -m build
```

Simple `pip install .` also works.

## Usage
from pythonpackage.utils.fun import *
my_fun()


## Documentation
We need yet another utility for generating documentation, `Sphinx`

```bash
# install sphinx
sudo apt-get install python3-sphinx
```

* `sphinx-quickstart` - maybe this should be the first step when creating a package...
* it gets complicated from here... need knowledge of `rst` and then additional
    rules about how to document python functions...

