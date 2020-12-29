from app import app, model
from flask import render_template, flash, redirect, request, jsonify
from app.forms import LoginForm, SentimentForm, WordForm, ActressForm, CodeForm, StudentForm
import requests

dicts = open("dict.txt","r").read().split("\n")

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Thai'}
    return render_template('index.html', title='Home', user=user)




import json
datas = json.load(open("data/clean_university_.json"))
areas = dict([(area,i) for i, area in enumerate(json.load(open("data/city.json")).keys())])
st_data = (2, "A02", 18, "A01" , 22, 6)
st_data = (4, 'D07', 19.5, 'D01', 16, 4.5)

def make_matrix(datas, st_data):
    input_array = []
    for college in datas:
        var_area = (float(areas[college["area"]]) - float(st_data[0]))**2
        if float(college["fee"]) < st_data[5]:
            var_fee = st_data[5] - float(college["fee"])
        else:
            var_fee = (float(college["fee"]) - st_data[5])**2
        var_point = 0
        c = 0
        if(st_data[1] in college["point"]):
            c = c+1
            if st_data[2] > float(college["point"][st_data[1]]):
                var_point += st_data[2] - float(college["point"][st_data[1]])
            else:
                var_point += (float(college["point"][st_data[1]]) - st_data[2])**3
        if(st_data[3] in college["point"]):
            c = c+1
            if st_data[4] > float(college["point"][st_data[3]]):
                var_point += st_data[4] - float(college["point"][st_data[3]])
            else:
                var_point += (float(college["point"][st_data[3]]) - st_data[4])**3

        if c == 0:
            var_point = 100
        else:
            var_point /= c

        input_array.append([var_area,var_fee,var_point])
    return input_array

from topsis import topsis
input_array = make_matrix(t,st_data)
topsis(input_array,[0.33,0.33,0.33],[-1, -1, -1])


@app.route('/college_recommend')
def college_recommend():
    form = StudentForm()
    print(form.subject1,"ssssss")
    return render_template('college_recommend.html', title='College Recomender', form=form)


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


@app.route('/match_word', methods=['GET','POST'])

def match():

    form = WordForm()
    words = form.word.data
    if words:
        words = words.split(" ")
    res = []
    if words and len(words) == 2:
        print(words[1],"sssss")
        for i in dicts:
            if i.split(" ")[0] == words[1]:
                res.append(i)

    # data = request.get_json(force=True)
    # return jsonify(output_text, output)
    return render_template('match_word.html', title='Match word', form=form, res = res)

# lst = open("Viet74K.txt").read().split("\n")
# new_lst = [i.lower() for i in lst if len(i.split(" ")) == 2 and "-" not in i]
# with open("dict.txt") as f:
#     f.write("\n".join(new_lst))



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

