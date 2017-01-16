from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.migrate import Migrate

app = Flask(__name__)

# dtatbase
app.config.from_object('settings')
db = SQLAlchemy(app)

# Migrate
migrate = Migrate(app,db)

from blog import views
from author import views
