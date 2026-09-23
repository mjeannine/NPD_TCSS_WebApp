# NPD Traffic Count – Web App

This is the web version of the [NPD Traffic Count App](https://github.com/mjeannine/NPD-Traffic-Count-MobileApp). It manages surveyors, roads, counting spots and survey phases, and stores the vehicle counts collected through the mobile app.

## Features

- Surveyor registration and login (email-based accounts)
- Token authentication for the mobile app
- Roads, counting spots and survey phases
- 12 vehicle categories, from motorcycles to trailer trucks
- Admin dashboard to manage all data

## Built with

Python, Django, Django REST Framework, PostgreSQL

## Run it

    git clone https://github.com/mjeannine/NPD_TCSS_WebApp.git
    cd NPD_TCSS_WebApp
    pip install django djangorestframework psycopg2-binary pillow
    python manage.py migrate
    python manage.py runserver

Requires a PostgreSQL database named `NPD_Traffic_Count` (see `NPD_TCSS/settings.py`).
