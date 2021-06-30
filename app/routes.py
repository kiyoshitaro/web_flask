from app import app, model
from flask import render_template, flash, redirect, request, jsonify
from app.forms import LoginForm, SentimentForm, WordForm, ActressForm, CodeForm, StudentForm, FactorForm, PolypForm
import requests

dicts = open("dict.txt", "r").read().split("\n")


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Thai'}
    return render_template('index.html', title='Home', user=user)


import json
datas = json.load(open("data/clean_university.json"))
areas = dict([
    (area, i)
    for i, area in enumerate(json.load(open("data/city.json")).keys())
])
st_data = (2, "A02", 18, "A01", 22, 6, "khoa học kĩ thuật")
st_data = (4, 'D07', 19.5, 'D01', 16, 4.5, "dược")
st_data = (7, 'A01', 19.5, 'N00', 22, 10, "âm nhạc")
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def make_matrix(datas, st_data):
    input_array = []
    for college in datas:

        var_area = (float(areas[college["area"]]) - float(st_data[0]))**2

        var_point = 0
        var_point1 = 100
        var_point2 = 100
        c = 0
        if (st_data[1] in college["point"]):
            c = c + 1
            if st_data[2] > float(college["point"][st_data[1]]):
                var_point1 = st_data[2] - float(college["point"][st_data[1]])
            else:
                var_point1 = (float(college["point"][st_data[1]]) -
                              st_data[2]) * 6
        if (st_data[3] in college["point"]):
            c = c + 1
            if st_data[4] > float(college["point"][st_data[3]]):
                var_point2 = st_data[4] - float(college["point"][st_data[3]])
            else:
                var_point2 = (float(college["point"][st_data[3]]) -
                              st_data[4]) * 6

        if c == 0:
            var_point = 100
        else:
            var_point = min(var_point1, var_point2)

        if float(college["fee"]) < st_data[5]:
            var_fee = st_data[5] - float(college["fee"])
        else:
            var_fee = (float(college["fee"]) - st_data[5]) * 2



        var_major = sorted([similar(st_data[6].lower(),i.lower())**2 for i in college["major_name"]])[-1] * 18 \
        + sorted([similar(st_data[6].lower(),i.lower())**2 for i in college["major_name"]])[-2] * 10

        input_array.append([var_area, var_fee, var_point, var_major])
    return input_array


from topsis import topsis
t = [i for i in datas if i["point"] != {}]
input_array = make_matrix(t, st_data)
topsis(input_array, [3, 1, 3, 3], [-1, -1, -1, 1])


@app.route('/college_recommend', methods=['GET', 'POST'])
def college_recommend():
    import numpy as np
    form = StudentForm()
    area_city = json.load(open("data/city.json"))
    res = []
    scores = []
    inps = []
    points = []
    majors = []
    all_std = []
    factors = [1, 1, 1, 1]
    factorForm = FactorForm()

    if form.validate_on_submit():
        area_id = ""
        for k, v in area_city.items():
            if (form.city.data in v):
                area_id = areas[k]

        # factors = [int(form.area_factor.data),int(form.fee_factor.data),int(form.point_factor.data),int(form.major_factor.data)]
        st_data = (area_id, form.subject1.data, float(form.point1.data),
                   form.subject2.data, float(form.point2.data),
                   float(form.fee.data), form.favor.data)

        input_array = make_matrix(t, st_data)
        print(st_data, "ssssss")
        # print(type(form.area_factor.data),form.area_factor.data,"tttt")
        ids, ids_bot, _ = topsis(input_array, factors, [-1, -1, -1, 1])
        # ids = np.append(ids,ids_bot)

        inps = [[round(t, 2) for t in input_array[i]] for i in ids]

        all_std = [(j[0], [round(t, 2) for t in j[1]], j[2])
                   for j in sorted(zip([k["name"] for k in t], input_array, _),
                                   key=lambda x: x[2])[::-1]]
        print(all_std, _)
        scores = [_[i] for i in ids]

        for id in ids:
            p = []
            if form.subject1.data in t[id]["point"]:
                p = [[
                    form.subject1.data,
                    round(t[id]["point"][form.subject1.data], 2)
                ]]
            if form.subject2.data in t[id]["point"]:
                p.append([
                    form.subject2.data,
                    round(t[id]["point"][form.subject2.data], 2)
                ])
            points.append(p)
        majors = [
            sorted(t[i]["major_name"],
                   key=lambda x: similar(st_data[6], x))[-5:][::-1]
            for i in ids
        ]
        for id in ids:
            res.append(t[id])
        print(points, majors)
        print(len(ids), "tttttt")
        # res = t[id]

    return render_template('college_recommend.html',
                           title='College Recomender',
                           form=form,
                           ress=zip(res, scores, inps, points, majors),
                           all_std=all_std)


import imghdr
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory, url_for
import glob
from skimage.io import imread
import cv2
import numpy as np
import torch
import torch.nn.functional as F


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


def save_img(path, img, lib="cv2", overwrite=True):
    if not overwrite and os.path.exists(path):
        pass
    else:
        print(path)
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        elif lib == "cv2":
            cv2.imwrite(path, img)


import app.network.models as models
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit(
#         '.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/polyp_segment')
# def home():
#     return render_template('polyp_segmentation.html')

# @app.route('/polyp_segment', methods=['POST'])
# def upload_image():
#     if 'file' not in request.files:
#         flash('No file part')
#         return redirect(request.url)
#     file = request.files['file']
#     if file.filename == '':
#         flash('No image selected for uploading')
#         return redirect(request.url)
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         flash('Image successfully uploaded and displayed below')
#         return render_template('polyp_segmentation.html', filename=filename)
#     else:
#         flash('Allowed image types are - png, jpg, jpeg, gif')
#         return redirect(request.url)
# @app.route('/polyp_segment/display/<filename>')
# def display_image(filename):
#     return redirect(url_for('static', filename='uploads/' + filename), code=301)


@app.route('/polyp_segment')
def polyp_segment():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('polyp_segmentation.html', files=files)


@app.route('/polyp_segment', methods=['POST'])
def upload_files():
    for f in glob.glob("static/uploads/*.png"):
        os.remove(f)
    for f in glob.glob("static/outputs/*.png"):
        os.remove(f)

    uploaded_file = request.files['file']
    print(uploaded_file)
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            return "Invalid image", 400
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        return redirect('/polyp_segment/segment')
    return '', 204


@app.route('/polyp_segment/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


@app.route('/polyp_segment/segment', methods=['POST', 'GET'])
def segment():

    form = PolypForm()
    img_size = (352, 352)
    img_paths = glob.glob("static/uploads/*.png")
    print("111")

    if form.validate_on_submit():
        # if True:
        print(img_paths)

        arch_path = [
            # ("UNet", "weights/unet_99.pth"),
            # ("PraNet", "weights/pranet-19.pth"),
            ("SCWSRCCANet", "weights/scws_rcca_178.pth"),
        ]

        for (arch, model_path) in arch_path:
            model = models.__dict__[arch]()
            model.cpu()
            device = torch.device("cpu")
            model.load_state_dict(
                torch.load(model_path,
                           map_location=device)["model_state_dict"])
            for img_path in img_paths:
                image_ = imread(img_path)
                image = cv2.resize(image_, img_size)
                image = image.astype("float32") / 255
                image = image.transpose((2, 0, 1))
                image = image[:, :, :, np.newaxis]
                image = np.asarray(image.transpose((3, 0, 1, 2)))
                filename = os.path.basename(img_path)
                name = os.path.splitext(filename)[0]
                ext = os.path.splitext(filename)[1]
                image = torch.tensor(image).float()

                if arch == "UNet":
                    res2 = model(image)
                else:
                    res5, res4, res3, res2 = model(image)

                res = res2
                res = F.upsample(res,
                                 size=image_.shape[:2],
                                 mode="bilinear",
                                 align_corners=False)
                res = res.sigmoid().data.cpu().numpy().squeeze()
                res = (res - res.min()) / (res.max() - res.min() + 1e-8)
                print(filename, res)
                save_img(
                    os.path.join(
                        app.config['OUTPUT_PATH'],
                        "PR_" + str(arch),
                        filename,
                    ),
                    res.round() * 255,
                    "cv2",
                )

                vis_x = 200
                mask_img = np.asarray(image_) + vis_x * np.array(
                    (res.round(), np.zeros_like(
                        res.round()), np.zeros_like(res.round()))).transpose(
                            (1, 2, 0))

                mask_img = mask_img[:, :, ::-1]
                save_img(
                    os.path.join(
                        app.config['OUTPUT_PATH'],
                        "PR_MASK_" + str(arch),
                        filename,
                    ),
                    mask_img.round(),
                    "cv2",
                )
    pr = ["upload/output/PR_SCWSRCCANet/"  + os.path.basename(file) for file in img_paths]
    pr_mask = ["upload/output/PR_MASK_SCWSRCCANet/"  + os.path.basename(file) for file in img_paths]

    return render_template(
        'choosemodel.html',
        title='Choose model polyp segmentation',
        form=form,
        imgs=zip(img_paths, pr, pr_mask),
    )


@app.route('/post')
def post():
    user = {'username': 'Hung'}
    posts = [{
        'author': {
            'username': 'Nguyen'
        },
        'body': 'Flask de hoc qua phai khong?'
    }, {
        'author': {
            'username': 'Long'
        },
        'body': 'Lap trinh Web that thu vi!'
    }]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Yeu cau dang nhap tu user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/post')

    return render_template('login.html', title='Sign In', form=form)


@app.route('/sentiment', methods=['GET', 'POST'])
def predict():
    form = SentimentForm()
    print(form, "qqqqqqqqqq")
    model_clf = model['pipeline_clf']
    if form.validate_on_submit():
        data = [form.sentence.data]

        # data = request.get_json(force=True)
        prediction = model_clf.predict(data)
        output_text = "Text:" + str(data[0])

        output = "Class: " + str(prediction)
        print(output, "wwwwwwwww")
        flash(output)
    # return jsonify(output_text, output)
    return render_template('sentiment.html', title='Sentiment', form=form)


@app.route('/match_word', methods=['GET', 'POST'])
def match():

    form = WordForm()
    words = form.word.data
    if words:
        words = words.split(" ")
    res = []
    if words and len(words) == 2:
        print(words[1], "sssss")
        for i in dicts:
            if i.split(" ")[0] == words[1]:
                res.append(i)

    # data = request.get_json(force=True)
    # return jsonify(output_text, output)
    return render_template('match_word.html',
                           title='Match word',
                           form=form,
                           res=res)


# lst = open("Viet74K.txt").read().split("\n")
# new_lst = [i.lower() for i in lst if len(i.split(" ")) == 2 and "-" not in i]
# with open("dict.txt") as f:
#     f.write("\n".join(new_lst))


@app.route('/code', methods=['GET', 'POST'])
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
            video_code = siteUrl[(siteUrl.find("cid=") +
                                  4):(len(siteUrl) - 1)].replace('00', '-',
                                                                 1).upper()
            videos[i]["code"] = video_code
            videos[i]["imageUrl"] = "https" + videos[i]["imageUrl"][6:]

    # return jsonify(output_text, output)
    return render_template('code.html',
                           title='Actress',
                           form=form,
                           formVideo=formVideo,
                           actresses=actresses,
                           videos=videos)
