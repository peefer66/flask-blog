from flask_blog import app
from flask import render_template, redirect, url_for, session, request
from author.form import RegisterForm, LoginForm
from author.models import Author
from author.decorators import login_required
import bcrypt

@app.route('/login', methods=("GET", "POST"))
def login():
    form = LoginForm()
    error=None
    # if the caling request is GET and next is present
    # create a cookie with the calling url
    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)
        
    if form.validate_on_submit():
        author = Author.query.filter_by(
            username = form.username.data
            ).first()
        
        if author: # ie found records
            if bcrypt.hashpw(form.password.data, author.password) == author.password:
            # Create session
                session['username'] = form.username.data
                session['is_author'] = author.is_author
                if 'next' in session:
                    next = session.get('next')
                    session.pop('next')
                    return redirect(next)
                else:
                    # redirect to def index
                    return redirect(url_for('index'))
            else:
                error = "Incorrect username and password"
        else:
            error = "Incorrect username and password"
    return render_template('author/login.html', form=form, error=error)

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template('author/register.html', form=form)
    
@app.route('/success')
def success():
    return "Author Registered"
    

@app.route('/logout')
def logout():
    session.pop('username')
    session.pop('is_author')
    return redirect(url_for('login'))