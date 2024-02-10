# ai_app_framework
Django app utilizing OpenAI API

### Getting Started
1. Create a directory on Desktop called "Projects".
2. Go into "Projects" directory and create another directory called "ai_app".
3. Go into "ai_app" directory via terminal (Unix & Linux) or powershell (Windows).
4. In the terminal, type:
   ```
   python -V
   pip -V
   ```
   Check which version of Python and Pip is installed. 3.10 or later is recommended for Python and whatever is the latest for Pip. Make sure both Python and Pip is calling Python3 and Pip3, respectively.
6. After confirming that the versions are latest versions of Python and Pip, type:
   ```
   python -m venv venv
   ```
   This command will be create a directory called "venv".
   NOTE: The second "venv" can be anything you set. It doesn't have to be "venv".

7. Then type:
   Unix & Linux
   ```
   source venv/bin/activate
   ```
   or
   Windows
   ```
   venv/Scripts/activate
   ```
9. You will see the "(venv)" at the beginning of the command line prompt. This means that you are now in the virtual environment.
10. Then type:
    ```
    which pip
    which python
    ```
    the output should show a directory of both pip and python inside the venv directory. If not, try:
    ```
    which pip3
    which python3
    ```
    If these commands show that pip and python are in the "venv" directory, you have to edit the "activate" file to include aliases as below.
    ```
    deactivate
    nano venv/bin/activate
    ```
    Once "activate" file is opened, scroll to the bottom of the script and add:
    ```
    alias pip=pip3
    alias python=python3
    ```
    ctrl+x then y to save and exit the text editor.
11. The activate the virtual environment again by typing:
    ```
    source venv/bin/activate
    ```
12. Make sure that your virtual environment is clean by typing:
    ```
    pip freeze
    ```
    It should just return a blank output.
13. Now, install Django and create project:
    ```
    pip install Django
    django-admin startproject NAME_OF_CHOICE
    ```
14. Next, go into the project directory NAME_OF_CHOICE and create an app:
    ```
    cd NAME_OF_CHOICE
    python manage.py startapp NAME_OF_CHOICE_2
    ```
15. Now, install openai library:
    ```
    pip install opoenai
    ```
16. Now you are ready to start making your ai webapp!
