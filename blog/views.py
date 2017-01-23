from flask_blog import app
from flask import render_template, redirect, flash, url_for, session, abort
from blog.form import SetupForm, PostForm
from flask_blog import db
from author.models import Author
from blog.models import Blog, Category, Post
from author.decorators import login_required, author_required
from slugify import slugify
import bcrypt


@app.route('/')
@app.route('/index')
def index():
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))
    return "Welcome"
    
@app.route('/admin')
@author_required
def admin():
    if session.get('is_author'):
        return render_template('blog/admin.html')
    else:
        abort(403)
    
@app.route('/setup', methods=('GET', 'POST'))
def setup():
    error=""
    form = SetupForm()
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        author = Author(
            form.fullname.data,
            form.email.data,
            form.username.data,
            hashed_password,
            True
            )
            
        db.session.add(author)
        db.session.flush()
        
        if author.id:
            blog = Blog(
                form.name.data,
                author.id
                )
            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = 'Error creating user'
        if author.id and blog.id:
            db.session.commit()
            flash('Blog created')
            return redirect(url_for('admin'))
        else:
            db.session.rollback()
            error = 'Error creating blog'
    
    return render_template('blog/setup.html', form=form, error=error)
    
@app.route('/post', methods=('GET', 'POST'))
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        if form.new_category.data:
            new_category = Category(form.new_category.data)
            db.session.add(new_category)
            db.session.flush()
            category = new_category
        elif form.category.data:
                category_id = form.category.get_pk(form.category.data)
                category = Category.query.filter_by(id=category_id).first()
        else:
            category = None
        blog = Blog.query.first()
        author = Author.query.filter_by(username=session['username']).first()
        title = form.title.data
        body = form.body.data
        slug = slugify(title)
        post = Post(blog, author, title, body, category, slug)
        
        db.session.add(post)
        db.session.commit()
        
        return redirect(url_for('article', slug=slug))
            
            
    return render_template('blog/post.html', form=form)
   

@app.route('/article/<slug>')
@author_required
def article(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    return render_template('blog/article.html', post=post)

    
