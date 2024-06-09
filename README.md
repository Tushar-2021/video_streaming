# Video Streaming Application

This project is a video streaming application built with Django and Django REST Framework. It allows users to manage and stream videos using the OpenCV library.

## Features

- User account management (registration, login)
- Video management (create, retrieve, update, delete videos)
- Video streaming with OpenCV and multithreading
- Search functionality for videos
- RESTful API for interacting with the application

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/videostreaming.git
   cd videostreaming
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
