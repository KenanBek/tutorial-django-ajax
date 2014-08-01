Tutorial on Python, Django and AJAX
===================================

# Welcome

Hi,

This code project is Django based project with contains sample application on different aspects of using AJAX in Python and Django environment.

I have a little bit changed structure of default Django project. Main change is renaming main folder to **configuraiton**. It contains:

* **settings.py** - main settings file
* **urls.py** - main URL configuraiton file
* **wsgi.py** - WSGI application module

Source code for each part of tutorial is in sample application folders (eg. sample1, sample2, etc.).

# Using

To properly work with this example you need to be installed follwoing libraries:

* Python 2.7
* Django 1.6

To run samples just run following commands on your favorite console:

  python manage.py syncdb
  python manage.py runserver

First command will create databe if it is not exists or migrate data if it is exists. Second ccommand will run local server on address http://localhost:8000/.
