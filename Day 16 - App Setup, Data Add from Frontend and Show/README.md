## Context

- [Project Setup](#project-setup)
- [Setup Everything Inside App](#setup-everything-inside-app)
  - [App Setup](#app-setup)
  - [Templates and URL Setup](#templates-and-url-setup)
- [Data Add From Frontend And Show](#data-add-from-frontend-and-show)

--

## Project Setup

- Virtual Environment
  - `python -m venv .venv`
  - `.venv\scripts\activate`
- Django Install
  - `pip install django`
- Project Create
  - django-admin startproject `school_project`
- Initialize database
- Create Superuser

## App Setup
- App Setup
  - Create App `school_project/school_app`
  - Add App `school_project/settings.py/INSTALLED_APPS/school_app`
  - Create Model `school_app/models.py/StudentModel`
    - [models.py](school_app/models.py)
  - Register Model `school_app/admin.py/StudentModel`
    - [admin.py](school_app/admin.py)
- Templates and URL Setup
