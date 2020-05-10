from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')


class SentimentForm(FlaskForm):
    sentence = StringField('Sentence', validators=[DataRequired()])
    submit = SubmitField('Check')

class ActressForm(FlaskForm):
    actress = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Check')

class CodeForm(FlaskForm):
    actress_id = StringField('Id', validators=[DataRequired()])
    submit = SubmitField('Check')