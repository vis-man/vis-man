# Technical Notes

## Useful commands
Check you have at least Python 3 (should have 3.8.x):

    python --version
    
To install required packages from requirements.txt

    pip install -r requirements.txt

Install Django:

    pip install Django

Check Django version (should have 3.2.6):

    python -m django --version

## Running a Django app

This branch has everything needed to see a basic Django site.

With Django installed, run via terminal:

    python manage.py runserver

Then, enter this in your browser:

    http://localhost:8000/survey/

This is your localhost where Django's light development server runs. And you should see some text that says:

    This is the survey index.

## Directory Notes

Note that, the way Django works, there can be multiple 'apps' within a 'project'. So:

*vms/* is the directory for the entire project.

*survey/* is the directory for the survey app specifically.

## DB migrations
To perform DB migration
python manage.py makemigrations
python manage.py migrate

