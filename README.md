# Django Calculator Project

This is a simple **Django-based calculator web application**. It demonstrates basic CRUD functionality, templates, static files handling, and deployment-ready settings.
live <https://django-app-m6nw.onrender.com/>
---

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
- [Folder Structure](#folder-structure)
- [Running the Project](#running-the-project)
- [Static Files](#static-files)
- [License](#license)

---

## Features

- Simple calculator interface for basic arithmetic operations.
- Django templates for frontend rendering.
- Static files management using Django’s staticfiles app.
- Ready for development and production deployment.

---

## Technologies

- Python 3.8+
- Django 4.2
- SQLite (default database)
- HTML/CSS for frontend

---

## Setup Instructions

1. **Clone the repository**:

```bash
git clone <(https://github.com/ankulmaurya88/Django-cal)>
cd Django-cal
Create a virtual environment and activate it:
```
``` bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
Install dependencies:

``` bash
pip install -r requirements.txt
Create required static folders:
```
``` bash
mkdir -p static
mkdir -p staticfiles
```
Run migrations:

``` bash
python3 manage.py migrate
Collect static files:
```
```bash
python3 manage.py collectstatic --noinput
```
Run the development server:

```bash

python3 manage.py runserver
```
---
``` bash 
Django-cal/
├─ cal/                   # Main Django project folder
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ asgi.py
├─ calulator/             # Django app folder
│  ├─ models.py
│  ├─ views.py
│  ├─ urls.py
│  └─ templates/
├─ static/                # App static files
├─ staticfiles/           # Collected static files
├─ templates/             # Project-wide templates
├─ db.sqlite3             # Database file
├─ manage.py
└─ requirements.txt
```

Static Files
STATIC_URL = '/static/'

STATIC_ROOT = <project-root>/staticfiles

STATICFILES_DIRS = [<project-root>/static]

Run python manage.py collectstatic to copy all static files to STATIC_ROOT for production.

License
This project is licensed under the MIT License.



---

