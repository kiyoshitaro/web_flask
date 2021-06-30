from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired
import numpy as np


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

    factor_arr = [(m, m) for m in range(1, 5)]

    # area_factor = SelectField('Vị trí địa lý',choices = factor_arr,default=2)
    # point_factor = SelectField('Điểm thi',choices = factor_arr,default=2)
    # fee_factor = SelectField('Học phí',choices = factor_arr, default=2)
    # major_factor = SelectField('Chuyên ngành',choices = factor_arr,default=2)

    cities = []
    i = 0
    for i in list(json.load(open("data/city.json")).values()):
        cities.extend(i)
    cities = [(i, i) for i in sorted(cities)]

    subjects = [(list(i.items())[0][0],
                 list(i.items())[0][0] + " : " + list(i.items())[0][1])
                for i in json.load(open("data/subject.json"))]

    subject1 = SelectField('Tổ hợp thi 1', choices=subjects)
    point1 = StringField('Điểm thi', validators=[DataRequired()])
    subject2 = SelectField('Tổ hợp thi 2', choices=subjects)
    point2 = StringField('Điểm thi', validators=[DataRequired()])
    city = SelectField('Thành phố sinh sống', choices=cities)
    fee = StringField('Số tiền có thể chi trả 1 kì (triệu đồng)',
                      validators=[DataRequired()])
    favor = StringField('Sở thích, nguyện vọng của sinh viên',
                        validators=[DataRequired()])

    print(subject1, point1)

    submit = SubmitField('Submit')


class FactorForm(FlaskForm):
    arr = [(i, i) for i in range(1, 5)]
    area_factor = SelectField("Vị trí địa lý", choices=arr, default=1)
    point_factor = SelectField("Điểm thi", choices=arr, default=1)
    fee_factor = SelectField("Học phí", choices=arr, default=1)
    major_factor = SelectField("Chuyên ngành", choices=arr, default=1)


class PolypForm(FlaskForm):
    models = [(0, "UNet"), (1, "PraNet"), (2, "SCWSRCCANet (our)")]
    # model = SelectField("Mô hình",choices = models,default=2)
    submit = SubmitField('Submit')
