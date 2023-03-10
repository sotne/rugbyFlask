from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField
from wtforms.validators import EqualTo, InputRequired


class SignUpForm(FlaskForm):
    email=EmailField('Email', validators=[InputRequired()])
    username=StringField('Username', validators=[InputRequired()])
    password=PasswordField('Password', validators=[InputRequired()])
    confirm_pass=PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit=SubmitField()
    

class LoginForm(FlaskForm):
    email=EmailField('Email', validators=[InputRequired()])
    password=PasswordField('Password', validators=[InputRequired()])
    submit=SubmitField()

class UpdatesForm(FlaskForm):
    body = TextAreaField('body', validators=[InputRequired()])
    submit = SubmitField()