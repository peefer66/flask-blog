import os

SECRET_KEY = "youwillneverguess"
DEBUG = True

# database set-up
DB_USERNAME = 'peefer66'
DB_PASSWORD = ''
BLOG_DATABASE_NAME = 'blog'
DB_HOST = os.getenv('IP', '0.0.0.0')

DB_URI = "mysql+pymysql://{}:{}{}{}".format(DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI


