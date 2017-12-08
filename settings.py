import os


SECRET_KEY = "Super_secret_key"
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vagrant:vagrant@0.0.0.0/restaurant'  # NOQA
SQLALCHEMY_TRACK_MODIFICATIONS = True
UPLOADED_IMAGES_DEST = '/vagrant/restaurant/static/images'
UPLOADED_IMAGES_URL = '/static/images/'
