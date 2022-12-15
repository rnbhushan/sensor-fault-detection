1.Creation of virtual environment : initally default version will be assigned to virtual environment
    >> pip list
    >> pip
    >> python3 -m pip install --upgrade pip
    >>python --version
    >>python3 -m pip uninstall virtualenv
    >>python3 -m pip install virtualenv
2.Creating virtual environment by assigning unique name
    >> python3 -m virtualenv env (or)
    >> python -m venv env
3.activation of virtualenv
    >> .\env\Scripts\activate
4.building app upon the virtualenv i have made
    >> installing all the packages and dependencies
    pandas
    numoy
    matplotlib
    sklearn

    >>to run requirements.txt file
        >> pip install -r .\requirements.txt or 
        python -m pip install matplotlib
        doubt  :  how to install requirements.txt


Git hub Setup :
just putl all my files will be uploaded to github

Create .gitignore file if not created in project folder and add list of files to be ignored which are related to local system
    ipynb_checkpoints
    env