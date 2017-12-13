import os


SECRET_KEY = "Super_secret_key"
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:////vagrant/food-zone/restaurant.db'  # NOQA
SQLALCHEMY_TRACK_MODIFICATIONS = True
UPLOADED_IMAGES_DEST = '/vagrant/restaurant/static/images'
UPLOADED_IMAGES_URL = '/static/images/'
