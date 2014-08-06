Tutorial on Python, Django and AJAX
===================================

It is Django based project with contains sample applications on different aspects of using AJAX in Python and Django environment.

I have a little bit changed structure of default Django project. Main change is renaming main project folder to **app**. It contains:

* **settings.py** - main settings file
* **urls.py** - main URL configuration file
* **wsgi.py** - WSGI application module

Source code for each part of tutorial is in separated application folders (eg. sample1, sample2, etc.).

# Using

To properly work with this example you need to be installed following libraries:

* Python 2.7
* Django 1.6

Used libraries:

* jQuery 1.11.1
* Bootstrap 2.1.1 (Sample 2)
* jQuery twitter bootstrap wizard plugin 1.0 (Sample 2)

To run samples just execute following commands on your favorite console:

  python manage.py syncdb
  python manage.py runserver

First command will create database if it is not exists or migrate data if it is exists. Second command will run local server on address http://localhost:8000/.

# Samples

Here is list of samples:

* **Sample 1** - Very simple example of using AJAX in Python and Django ([read article](http://kenanbek.me/post/very-simple-example-on-using-ajax-in-python-and-django/))
* **Sample 2** - Form Wizard with AJAX data processing
* **Sample 3** - Coming Soon :)
