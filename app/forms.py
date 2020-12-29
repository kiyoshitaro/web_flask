from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')


class SentimentForm(FlaskForm):
    sentence = StringField('Sentence', validators=[DataRequired()])
    submit = SubmitField('Check')

class WordForm(FlaskForm):
    word = StringField('Word', validators=[DataRequired()])
    submit = SubmitField('Check')

class ActressForm(FlaskForm):
    actress = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Check')

class CodeForm(FlaskForm):
    actress_id = StringField('Id', validators=[DataRequired()])
    submit = SubmitField('Check')

class StudentForm(FlaskForm):
    import json
    # areas = [(i,area) for i, area in enumerate(json.load(open("data/city.json")).keys())]
    cities = []
    for i in list(json.load(open("data/city.json")).values()):
        cities.extend((i))
    cities = [(i,i) for i in sorted(cities)]  

    subjects = [(list(i.items())[0][0], list(i.items())[0][0] + " : " + list(i.items())[0][1]) for i in json.load(open("data/subject.json"))]

    subject1 = SelectField('Tổ hợp thi 1', choices=subjects)
    point1 = StringField('Điểm thi', validators=[DataRequired()])
    subject2 = SelectField('Tổ hợp thi 2', choices=subjects)
    point2 = StringField('Điểm thi')
    # area = SelectField('Khu vực sinh sống', choices=areas)
    city = SelectField('Thành phố sinh sống', choices=cities)
    fee = StringField('Số tiền có thể chi trả 1 kì (triệu đồng)', validators=[DataRequired()])
    submit = SubmitField('Submit')
