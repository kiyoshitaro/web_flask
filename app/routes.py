from app import app, model
from flask import render_template, flash, redirect, request, jsonify
from app.forms import LoginForm, SentimentForm, ActressForm, CodeForm
import requests


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



@app.route('/code', methods=['GET','POST'])

def search():

    url = 'https://jav-rest-api-htpvmrzjet.now.sh/api/actress?name='
    url_code = "https://jav-rest-api-htpvmrzjet.now.sh/api/videos/"
    form = ActressForm()
    formVideo = CodeForm()
    actresses = []
    videos = []

    if form.validate_on_submit():
        name = form.actress.data
        actressURL = url + name
        actressRequest = requests.get(actressURL).json()
        actresses = actressRequest["result"]
        # counts = len(actressRequest['result'])

        # print("{:<3} | {:<7} | {:17} | {}\t".format("#", "ID", "Actress Name", "Japanese Name"))
        # print("=======================================================")

        # for i in range(counts):
        #     actress_id = actressRequest['result'][i]['id']
        #     actress_name = actressRequest['result'][i]['name']
        #     actress_japName = actressRequest['result'][i]['japanName']
        #     print("{:>3} | {:<7} | {:17} | {}\t".format(i+1, actress_id, actress_name, actress_japName))
        # print('Found {} babes named "{}"'.format(counts, name))
        # print()
    
        
    if formVideo.validate_on_submit():
        actress_id = formVideo.actress_id.data
        vidURL = url_code + actress_id
        videoRequest = requests.get(vidURL).json()
        videos = videoRequest["result"]
        video_counts = len(videos)

        for i in range(video_counts):
            siteUrl = videos[i]['siteUrl']
            video_code = siteUrl[(siteUrl.find("cid=") + 4):(len(siteUrl) - 1)].replace('00', '-', 1).upper()
            videos[i]["code"] = video_code
            videos[i]["imageUrl"] = "https" + videos[i]["imageUrl"][6:]



    # return jsonify(output_text, output)
    return render_template('code.html', title='Actress', form=form,formVideo = formVideo,actresses = actresses, videos = videos)
