## Context

- [Project Setup](#project-setup)
- [Setup Everything Inside App](#setup-everything-inside-app)
  - [App Setup](#app-setup)
  - [Templates and URL Setup](#templates-and-url-setup)
- [Data Add From Frontend And Show](#data-add-from-frontend-and-show)

---

## Project Setup

- Virtual Environment
  - `python -m venv .venv`
  - `.venv\scripts\activate`
- Django Install
  - `pip install django`
- Project Start
  - django-admin startproject `school_project`
  - vs code open `code .`

---

## App Setup

- App Setup
  - App Start
    - `school_project/school_app`
    - `python manage.py startapp school_app`
  - App Add
    - `school_project/settings.py/INSTALLED_APPS/school_app`
- Model Setup
  - Model Create `school_app/models.py/StudentModel`
    - [models.py](school_app/models.py)
  - Model Register `school_app/admin.py/StudentModel`
    - [admin.py](school_app/admin.py)
- Templates Setup
- URL Setup

---

- Database Setup
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- Superuser Create
  - python manage.py createsuperuser
    - username
    - email
    - password
    - confirmation

---
