from ast import Pass
import email
from email import message
from email.policy import default
from random import choices
from unicodedata import name

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField, DateField, SelectField,TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, URL, Optional


class ContactForm(FlaskForm):
    #a contact form
    name = StringField(
        'Name',
        [DataRequired()],
        render_kw={'placeholder':'your name'}
    )
    email = StringField(
        'Email',
        [
            Email(message=('Not a valid email address.')),
            DataRequired(),
            
        ],render_kw={"placeholder": "your email"}
    )
        #TextField
    body = TextAreaField(
        'Message',
        [
            DataRequired(),
            Length(min=1,
            message=('Your message is too short.'))
        ], render_kw={"placeholder": 'i.e. "Wow your website is SO amazing!"', 'class': 'textField'}
    )
    #recaptcha = RecaptchaField()
    submit = SubmitField('Send')

class SignupForm(FlaskForm):
    first = StringField(
        'First',
        validators=[DataRequired()],
        render_kw={"placeholder": "first name"}
    )
    last = StringField(
        'Last',
        validators=[DataRequired()],
        render_kw={"placeholder": "last name"}
    )
    username = StringField(
        'Username',
        validators=[DataRequired()],
        render_kw={"placeholder": 'choose wisely'}
    )
    email = StringField(
        'Email',
        [ 
            Email(message='Not a valid email address.'),
            DataRequired()
        ],render_kw={"placeholder": "email"}
    )
    password = PasswordField(
        'Password',
        [ 
            DataRequired(message="Please enter a password.")
        ],render_kw={"placeholder": "password"}
    )
    confirmPassword = PasswordField(
        'Confirm Password',
        [ 
            EqualTo('password', message='Passwords must match')
        ],render_kw={"placeholder": "don't mess this up"}
    )
    dateOfBirth = DateField(
        'Date of Birth',
        [
            DataRequired()
        ],
        format='%Y-%m-%d',
        render_kw={"placeholder": "yyyy-mm-dd"}
    )
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    #user login form
    email = StringField(
        'Email',
        validators=[ 
            DataRequired(),
            Email(message='Enter a valid email.')
        ],render_kw={'placeholder': 'email'}
    )
    password = PasswordField(
        'Password',
        validators = [
            DataRequired()
        ],render_kw={'placeholder': 'password'}
    )
    submit = SubmitField('Log In')

class UpdateProfileForm(FlaskForm):
    picture = FileField(
        'Profile Picture',
        validators=[FileAllowed(['jpg','png','jpeg','heic'])]
    )
    first = StringField(
        'First',
        validators=[DataRequired()],
        render_kw={"placeholder": "first name"}
    )
    last = StringField(
        'Last',
        validators=[DataRequired()],
        render_kw={"placeholder": "last name"}
    )
    username = StringField(
        'Username',
        validators=[DataRequired()],
        render_kw={"placeholder": 'choose wisely'}
    )
    email = StringField(
        'Email',
        validators=[ 
            Email(message='Not a valid email address.'),
            DataRequired()
        ],render_kw={"placeholder": "email"}
    )
    bio = TextAreaField(
        'Bio',
        [
            Length(max=180,
            message=('Your bio can not exceed 180 characters.'))
        ], render_kw={"placeholder": 'your bio', 'class': 'textField'}
    )

    submit = SubmitField('Update')

class AddAssetForm(FlaskForm):
    submit = SubmitField()

class ShowAssetForm(FlaskForm):
    checked = BooleanField(
    'label',
    #default = "checked"
    )
