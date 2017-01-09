from flask_blog import app # From the __init__.py file

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'