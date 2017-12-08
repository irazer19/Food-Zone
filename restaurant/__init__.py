from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads, IMAGES


app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# images
uploaded_images = UploadSet('images', IMAGES)
configure_uploads(app, uploaded_images)

from restaurants import views  # NOQA
from menu_item import views  # NOQA
