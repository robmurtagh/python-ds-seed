# Python Data Science Seed Project

Minimal scaffolding for Python machine learning projects. It supports interactive, line-by-line execution with Jupyter kernel.

Contains some extra notes on setting up in MS Visual Studio Code (VSCode)



## General usage

* Install a virtual environment:
```
virtualenv --no-site-packages venv
```
* Activate virtual environment:
```
source venv/bin/activate
```
* Install dependencies from repo:
```
pip install -r requirements.txt
```



## Note on VSCode

* Get add-in (requires subsequent VSCode restart):
```
Cntl + Shift + P -> Install Extensions -> Python
```
* Select virtualenv interpretter:
```
Cntl + Shift + P
Select Workspace Interpretter
python2.7 venv/bin/python2.7
```
* Run Python code to set up default launch.json e.g.:
```
script_python.py
fn + F5
```
* Run Jupyter code e.g.:
```
script_jupyter.py
'Run Cell'
```
* (Optional) User defined snippet for generating Juptyer cells 
```
Code -> Preferences -> User Snippet -> Python
```
```
    "Jupyter Cell": {
        "prefix": "cell",
        "body": [
            "#%%"
        ],
        "description": "Begins a Jupter Cell which can be run independently"
    }
```