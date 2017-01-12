from flask_wtf import Form
from wtforms import validators, StringField
from author.form import RegisterForm


# Initially was SetupForm(Form) but can replace Form with RegisterForm because 
# this in itself inherits Form. So you can use field from RegisterForm
class SetupForm(RegisterForm):
    name = StringField('Blog name', [
        validators.required(),
        validators.length(max=80)
        ])
    fullname = RegisterForm.fullname
    
