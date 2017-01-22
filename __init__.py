from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from flask.ext.markdown import Markdown

app = Flask(__name__)

# dtatbase
app.config.from_object('settings')
db = SQLAlchemy(app)

# Migrate
migrate = Migrate(app,db)

# Markdown
markdown = Markdown(app)

from blog import views
from author import views
