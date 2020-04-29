from app import app, model
from flask import render_template, flash, redirect, request, jsonify
from app.forms import LoginForm, SentimentForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Thai'}
    return render_template('index.html', title='Home', user=user)

@app.route('/post')
def post():
    user = {'username': 'Hung'}
    posts = [
        {
            'author': {'username': 'Nguyen'},
            'body': 'Flask de hoc qua phai khong?'
        },
        {
            'author': {'username': 'Long'},
            'body': 'Lap trinh Web that thu vi!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Yeu cau dang nhap tu user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/post')

    return render_template('login.html', title='Sign In', form=form)

@app.route('/sentiment', methods=['GET','POST'])
def predict():
    form = SentimentForm()
    print(form,"qqqqqqqqqq")
    model_clf = model['pipeline_clf']
    if form.validate_on_submit():
        data = [form.sentence.data]
    
    # data = request.get_json(force=True)
        prediction = model_clf.predict(data)
        output_text = "Text:" + str(data[0]) 
        
        output = "Class: " + str(prediction)
        print(output,"wwwwwwwww")
        flash(output)
    # return jsonify(output_text, output)
    return render_template('sentiment.html', title='Sentiment', form=form)
