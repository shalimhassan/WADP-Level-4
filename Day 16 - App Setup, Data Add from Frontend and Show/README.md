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
  - `cls`
    
- Project Create (Start)
  - `django-admin startproject crud_p1_project`
  - `code .`

## App Setup

- App Create (Start)
  - enter into project
    - `cd crud_p1_project`
  - create app
    - `python manage.py startapp crud_app`
  - dir
    - `crud_p1_project/crud_app`
    
- App Register (Add)
  - Register App inside project/settings.py/INSTALLED_APPS
    - `crud_p1_project/settings.py/INSTALLED_APPS/crud_app`
      
## Model Setup

- Model Create
  - create Model inside models.py
    - `crud_app/models.py/StudentModel`
    - [models.py](school_app/models.py)
    
- Model Register
  - register model inside admin.py
    - `crud_app/admin.py/StudentModel`
    - [admin.py](school_app/admin.py)
      
## Templates Setup

## URL Setup

- Database Setup
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- Superuser Create
  - python manage.py createsuperuser
    - username
    - email
    - password
    - confirmation
