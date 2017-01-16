import os, sys

# Something about setting the path for the app ?? - LOOKUP
#
# The expression returns the full path name of the executing
# script in a multiplatform-safe way. No need to hardwire any directions,
# that's why it is so useful.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Not sure what this is either

# The Flask-Script extension provides support for writing external scripts
# in Flask. This includes running a development server, a customised Python
# shell, scripts to set up your database, cronjobs, and other command-line
# tasks that belong outside the web application itself.
# Flask-Script works in a similar way to Flask itself. You define and add
# commands that can be called from the command line to a Manager instance:

from flask.ext.script import Manager, Server
from flask.ext.migrate import MigrateCommand
from flask_blog import app



manager = Manager(app)
manager.add_command('db', MigrateCommand)

# This sets the variables in order to connect the server
# Manager allows runserver to be called directly from the command line
manager.add_command('runserver', Server(
    use_debugger = True, # Remove at production
    use_reloader = True, # rreloads manager.py after any change
    host = os.getenv('IP', '0.0.0.0'), # the host for the browser page specific to c9
    port = int(os.getenv('PORT', 5000)) # The port to use
    )
)

if __name__ == ('__main__'):
    manager.run()

