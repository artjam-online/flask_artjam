"""
forms.py
~~~~~~~~
"""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo, AnyOf
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
    name = StringField("Name Of Student")


class LoginForm(FlaskForm):
    username = StringField('username',
        validators=[InputRequired(message='A username is required'),
        Length(min=8, max=25, message='Username must be between 8 to 25 characters')])
    password = PasswordField('password',
        validators=[InputRequired(message='A password is required'),
                    Length(min=8, message='Password must be 8 or more characters')])
    remember = BooleanField('remember me')
    recaptcha = RecaptchaField()
    submit = SubmitField('submit')


class RegisterForm(FlaskForm):
    email = StringField('email',
        validators=[InputRequired(), Email(message='Invalid email'),
                    Length(max=50)])
    username = StringField('username',
                           validators=[InputRequired(message='A username is required'),
                                       Length(min=8, max=25, message='Username must be between 8 to 25 characters')])
    password = PasswordField('password',
                             validators=[InputRequired(message='A password is required'),
                                         Length(min=8, message='Password must be 8 or more characters')])
    submit = SubmitField('submit')
