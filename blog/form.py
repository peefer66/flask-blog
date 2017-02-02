from flask_wtf import Form
from wtforms import validators, StringField, TextAreaField
from author.form import RegisterForm
from blog.models import Category
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_wtf.file import FileField, FileAllowed


# Initially was SetupForm(Form) but can replace Form with RegisterForm because 
# this in itself inherits Form. So you can use field from RegisterForm
class SetupForm(RegisterForm):
    name = StringField('Blog name', [
        validators.required(),
        validators.length(max=80)
        ])
    fullname = RegisterForm.fullname

def categories():
    return Category.query
    
class PostForm(Form):
    image = FileField('Image', validators=[FileAllowed([
        'jpg', 'png'],'Images only!')])
        
    title = StringField('Title',[
            validators.required(),
            validators.Length(max=80)
            ])
    body = TextAreaField('Content', validators=[validators.required()])
    category = QuerySelectField('Category', query_factory=categories, allow_blank=True)
    new_category = StringField('New Category')
    