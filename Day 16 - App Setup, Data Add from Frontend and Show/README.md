## Context

- [Project Setup](#project-setup)
- [Setup Everything Inside App](#setup-everything-inside-app)
  - [App Setup](#app-setup)
  - [Templates and URL Setup](#templates-and-url-setup)
- [Data Add From Frontend And Show](#data-add-from-frontend-and-show)

## Project Setup

- VENV Create
  - `python -m venv .venv`
  - `.venv\scripts\activate`
    
- Django Install
  - `pip install django`
    
- Project Create (Start)
  - `django-admin startproject school_project . (including space dot)`

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

- App
  - Create App (Start)
    - `python manage.py startapp school_app`
    
  - Register App (Add)
    - register app inside project/settings.py/INSTALLED_APPS
      - `my_project/settings.py/INSTALLED_APPS/my_app`

- Model
  - Create Model
    - create Model inside school_app/models.py
      - example: `TeacherModel`
      - `school_app/models.py/TeacherModel`
      - [models.py](school_app/models.py)
    
  - register model
    - register Model inside school_app/admin.py
      - `school_app/admin.py/TeacherModel`
      - [admin.py](school_app/admin.py)

## templates
- folder create named `templates` folder
  - file create inside `templates` folder
    - `home.html`file
    - `teacher.html`file
  - folder create inside `templates` folder
    - `master`folder
      - file create inside `master` folder
        - `base.html`file
        - `nav.html`file

## URL Setup


