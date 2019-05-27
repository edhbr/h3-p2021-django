# h3-p2021-django

A Django discovery project

**[Live project here](https://h3-p2021-django.herokuapp.com)**

## Prerequisites

- Python 3.x.x

- PIP

- Virtualenv : `$ pip install virtualenv`

- Stylus executable available from a `stylus` command : `$ npm install -g stylus`

## Install

1. Clone the repository

   `$ git clone git@github.com:edhbr/h3-p2021-django.git`

2. Get inside

   `$ cd h3-p2021-django`

3. Install it with virtual env

   `$ virtualenv . -p python`

4. Get inside virtualenv

   4.1 Windows

   `$ "Scripts/activate.bat"`

   4.2 Linux & Mac

   `$ source bin/activate`

5. Install dependencies

`$ pip install -r requirements.txt`

6. Rename settings.sample.ini

`$ mv settings.sample.ini settings.ini`

7. Fill it with your value

`$ vim settings.ini`

8. Install sample database

`$ mv db.sample.sqlite3 db.sqlite3`

9. Collect static files

`$ python manage.py collectstatic --no-input`

10. Run Django

`$ python manage.py runserver`

11. Enjoy

## Features

It's a basic blog featuring :

- A home page

  - Featured article
  - Title
  - Punchline
  - Posts list

- Single post page
  - Title
  - Lead
  - Published date
  - Featured image (hosted on Cloudinary)
  - Markdown body
