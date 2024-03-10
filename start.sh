#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Apply migrations to create database tables
python manage.py migrate

# Run Django development server
python manage.py runserver 0.0.0.0:8080
