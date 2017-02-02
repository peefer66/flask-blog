from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from flask.ext.markdown import Markdown
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)

# dtatbase
app.config.from_object('settings')
db = SQLAlchemy(app)

# Migrate
migrate = Migrate(app,db)

# Markdown
markdown = Markdown(app)

#images
uploaded_images = UploadSet('images', IMAGES)
configure_uploads(app, uploaded_images)

from blog import views
from author import views
