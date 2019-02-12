
#1/11/19 __init.py__: initializes and tells python that the current
directory is a python directory
setup.py: where you can tell the computer to download libraries
via pip or something
requirements.txt:gets dependencies for our program

from setuptools import setup
setup(name = 'hello', version='1.0.0', url='',author='tjzhang',packages=['']

The command 'pip freeze > requirements.txt' writes the dependencies
for the current version of pip to the file requirements.txt To install
the module requirements, use 'pip install -r requirements.txt .'.

#1/21/19
Dictionaries: S 3.5.7.4
Add SSH key to Github: S 4.5

#1/23/19:
Read REST section in book by Thursday 9.1 ssh-add
Going through the specified REST tutorial on next Thursday.
A cloud data center utilizes containers and virtualization.

#2/5/19
.yaml files contain endpoint, REST method, and python code
Starting a local server in nist/examples/flask-connexion-swagger
Installed requirements in testENV pyenv

#2/7/19
Learned more about .yaml files and how they specify how to use
URLs to tell the server what to do.
