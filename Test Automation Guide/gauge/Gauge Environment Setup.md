1. Install pyenv
2. sudo apt-get install python-is-python3
3. sudo apt-get install python3-pip

## Issues when running gauge
1. in python env set to use python3

##### No module named 'pkg_resources' in Python

> `python3 -m pip install --upgrade setuptools`

##### /home/devqe/.pyenv/versions/3.10.4/bin/python3: No module named pip

> `python3 -m ensurepip --upgrade`


https://stackoverflow.com/questions/72441758/typeerror-descriptors-cannot-not-be-created-directly

```
pip install protobuf==3.20.*
```