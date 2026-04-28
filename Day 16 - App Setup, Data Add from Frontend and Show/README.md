## Context

- [Project Setup](#project-setup)
- [Setup Everything Inside App](#setup-everything-inside-app)
  - [App Setup](#app-setup)
  - [Templates and URL Setup](#templates-and-url-setup)
- [Data Add From Frontend And Show](#data-add-from-frontend-and-show)

## Project Setup

- Virtual Environment
  - `python -m venv .venv`
  - `.venv\scripts\activate`
    
- Django Install
  - `pip install django`
    
- Project Create (Start)
  - `django-admin startproject my_project`
  - `cd my_project`
  - `dir`
    - my_project folder
    - manage.py file

- Database Initialize
  - `python manage.py makemigrations`
  - `python manage.py migrate`
    
- Superuser Create
  - `python manage.py createsuperuser`
  - username
  - email
  - password
  - confirmation

- Server Run
  - `python manage.py runserver`

## App Setup

- App Create (Start)
  - enter into the project
    - `cd my_project`
  - create app
    - `python manage.py startapp my_app`
  - dir
    - `crud_p1_project/crud_app`
    
- App Register (Add)
  - Register App inside project/settings.py/INSTALLED_APPS
    - `crud_p1_project/settings.py/INSTALLED_APPS/crud_app`

- Model Create
  - create Model inside models.py
    - `crud_app/models.py/StudentModel`
    - [models.py](school_app/models.py)
    
- Model Register
  - register Model inside admin.py
    - `crud_app/admin.py/StudentModel`
    - [admin.py](school_app/admin.py)

## Templates Setup

## URL Setup


