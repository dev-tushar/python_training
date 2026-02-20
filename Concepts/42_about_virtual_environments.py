"""
Virtual Environments
"""

"""
Virtual Environments: If we are working on multiple projects then instead of using same
python-installation-folder for all projects, we can create separate copy of python-installation-folder
for each project and use. This separate copy of python-installation-folder is called virtual environments
"""

"""
How to create virtual environments?

2 ways:

1st-way: Using command-line/command-prompt. We can run below command to create virtual environments
    python -m venv myvenv1
    python -m venv myvenv2
    python -m venv myvenv3

2nd-way: Few IDEs will also provide option to create virtual environments
   Example: pycharm, vs-code 

"""

r"""
Example: Using command-line/command-prompt.
C:\Users\mahad>cd\
C:\>cd B1_python_training
C:\B1_python_training>python -m venv myvenv1
C:\B1_python_training>python -m venv myvenv2
C:\B1_python_training>
"""

r"""
Example: Using pycharm
File->Settings->project:python_training-> python-interpreter-> add interpreter -> Generate New
"""