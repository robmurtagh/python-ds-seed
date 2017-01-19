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
* (Optional) I generally then need to upgrade the version of pip available in the virtualenv:
```
pip install --upgrade pip
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
* (Optional) User defined snippets for helping with Jupyter/IPython: 
```
Code -> Preferences -> User Snippet -> Python
```
```
    "IPython - New Jupyter cell": {
        "prefix": "cell",
        "body": [
            "#%%"
        ],
        "description": "Begins a Jupter Cell which can be run independently"
    },

    "Pylint - Turn off linting": {
        "prefix": "pylint-off",
        "body": [
            "#pylint: skip-file"
        ],
        "description": "When written at the top of a file, turns off all pylint alerting"
    },

    "IPython - Import display function": {
        "prefix": "ipython-display",
        "body": [
            "from IPython.display import display"
        ],
        "description": "Imports the 'display' function from IPython"
    },

    "IPython - Enable auto-reload": {
        "prefix": "ipython-reload",
        "body": [
            "#pylint: skip-file",
            "c = get_config()",
            "c.InteractiveShellApp.extensions = ['autoreload']",
            "c.InteractiveShellApp.exec_lines = ['%autoreload 2']",
            "c.InteractiveShellApp.exec_lines.append('print(\"Warning: disable autoreload in ipython_config.py to improve performance.\")')"
        ],
        "description": "Add this to a file 'ipython_config.py' in order to enable dynamic reloading"
    }
```
* Execute line-by-line, or many lines:
```
Cntl + Alt + Enter
```
