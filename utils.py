
# EXTRACT INFO FROM HTML 

def extract_info_from_html():
    from bs4 import BeautifulStoneSoup
    import re
    html = open("data/url.html").read()
    soup = BeautifulStoneSoup(html)
    inputTag = soup.findAll("a")
    inputTag = str(inputTag).split(",")
    m = [re.search(" +href=\"(.*?)\"", i) for i in inputTag]
    urls = [i.group(1) for i in m]

    code = [i[9:-9].replace("<","") for i in str(soup.findAll('strong')).split(",")]
    city  = [i.split('<span class="uni-code">')[0].replace("\t","").replace("</span>","").replace("\n","") for i in html.split('<i class="fa fa-map-marker" aria-hidden="true"></i>')[1:]]
    abbr  = [i.split('</div>')[0].replace("\t","").replace("</span>","").replace("\n","") for i in html.split('<div class="name-group">')[1::2]]

    # ADD CODE TO UNI_INFO
    map_abbr_code = [{"abbr":m,"code":n}for m,n in zip(abbr,code) if m != ""]
    import json
    uni = json.load(open("data/university.json"))

    len(uni)
    new_uni = []
    abbrs = []
    for i in uni:
        if(i["abbr"] in abbrs):
            continue
        else:
            for j in map_abbr_code:
                if(j["abbr"] == i["abbr"]):
                    i["code"] = j["code"]
                    break
            new_uni.append(i)
            abbrs.append(i["abbr"])

    with open('data/university_add_code.json', 'w') as outfile:
        json.dump(new_uni, outfile,ensure_ascii=False, indent=4)



# REFORMAT DATA + COMBINE POINT, MAJOR, SUBJECT + AREA

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def reformat(data):
    code = data["university_meta"]["university_code"]
    major_name = set([j["major_name"] for j in data["diemchuan_datas"]])
    # point_all = [float(j["point"]) for j in data["diemchuan_datas"] if is_number(j["point"])]
    point_all = []
    for u in data["diemchuan_datas"]:
        if(is_number(u["point"]) and float(u["point"]) < 40):
            if("Ngôn ngữ" in u["major_name"] or "Thang điểm 40" in u["note"]):     
                point_all.append(float(u["point"])*3/4)
            else:
                point_all.append(float(u["point"]))

    subject_group_all = [j["subject_group"].replace(" ","").split(";") for j in data["diemchuan_datas"]]
    subject_group = set()
    for t in subject_group_all:
        if t != "":
            subject_group.update(t)
    subject_group = [t for t in subject_group if ("A" in t or "B" in t or"C" in t or "D" in t) and len(t)==3]




    point_all = []
    for l in subject_group:
        point_all.append((l,[]))
    point_all = dict(point_all)
    for u in data["diemchuan_datas"]:
        if(is_number(u["point"]) and float(u["point"]) < 40 and u["subject_group"] in subject_group):
            if("Ngôn ngữ" in u["major_name"] or "Thang điểm 40" in u["note"]):  
                point_all[u["subject_group"]].append(float(u["point"])*3/4)
            else:
                point_all[u["subject_group"]].append(float(u["point"]))


    point = []            
    for l in subject_group:
        if(len(point_all[l]) >0):
            point.append((l,sum(point_all[l])/len(point_all[l])))
    point = dict(point)


    return {"code": code,
    "major_name" : list(major_name),
    "subject_group" : subject_group,
    "point" : point,
    "point_all" : point_all,
    # "city" : city
    }

def add_uni_detail_info():
    import json
    f = open("data/university_diemchuan")
    s = f.read()
    s = s.split("\n")
    s = [json.loads(i) for i in s]
    city_area = json.load(open("data/city.json"))
    new_datas = []
    datas = [reformat(i) for i in s if i["diemchuan_datas"] != []  and len([float(j["point"]) for j in i["diemchuan_datas"] if is_number(j["point"])]) != 0]
    new_uni = json.load(open("university_add_code.json"))

    # ADD AREA
    for i in new_uni:
        for j in datas:
            if(i["code"] == j["code"]):
                i["major_name"] = j["major_name"]
                i["subject_group"] = j["subject_group"]
                i["point"] = j["point"]
                i["city"] = " ".join(i["city"].split(" "))
                for k,v in city_area.items():
                    if i["city"] in v:
                        i["area"] = k     
                new_datas.append(i)
    with open('clean_university.json', 'w') as outfile:
        json.dump(new_datas, outfile,ensure_ascii=False, indent=4)
























# # ADD MORE INFO TO CLEAN_DATA WITHOUT REMOVE MUNUAL FEATURE 
# new_new_datas = []
# uni = json.load(open("data/university.json"))

# for i in new_datas:
#     for j in uni:
#         if(i["abbr"] == j["abbr"]):
#             i["logo"] = j["logo"]
#             break
#     new_new_datas.append(i)
# with open('clean_university.json', 'w') as outfile:
#     json.dump(new_new_datas, outfile,ensure_ascii=False, indent=4)





# majors = []
# for i in new_datas:
#     majors.extend(i["major_name"])

# INTAB = "ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđẠẢÃÀÁÂẬẦẤẨẪĂẮẰẶẲẴÓÒỌÕỎÔỘỔỖỒỐƠỜỚỢỞỠÉÈẺẸẼÊẾỀỆỂỄÚÙỤỦŨƯỰỮỬỪỨÍÌỊỈĨÝỲỶỴỸĐ"
# OUTTAB = "a" * 17 + "o" * 17 + "e" * 11 + "u" * 11 + "i" * 5 + "y" * 5 + "d" + \
#          "A" * 17 + "O" * 17 + "E" * 11 + "U" * 11 + "I" * 5 + "Y" * 5 + "D"
# r = re.compile("|".join(INTAB))
# replaces_dict = dict(zip(INTAB, OUTTAB))

# majors = [r.sub(lambda m: replaces_dict[m.group(0)], re.sub(r'[^àáãạảăắằẳẵặâấầẩẫậèéẹẻẽêềếểễệđìíĩỉịòóõọỏôốồổỗộơớờởỡợùúũụủưứừửữựỳỵỷỹýÀÁÃẠẢĂẮẰẲẴẶÂẤẦẨẪẬÈÉẸẺẼÊỀẾỂỄỆĐÌÍĨỈỊÒÓÕỌỎÔỐỒỔỖỘƠỚỜỞỠỢÙÚŨỤỦƯỨỪỬỮỰỲỴỶỸÝa-zA-Z\s]+', '', i, flags=re.MULTILINE)).lower() for i in majors]
# majors.sort()

# gr_major = set()
# for i in majors:
#     x = "_".join(i.split(" ")[:2])
#     gr_major.update([x])






# new_new_datas = json.load(open("clean_university.json"))
# new_new_new_datas = []
# for i in new_new_datas:
#     for m in s:
#         if(i["code"] == m["university_meta"]["university_code"]):

#             subject_group_all = [j["subject_group"].replace(" ","").split(";") for j in m["diemchuan_datas"]]
#             subject_group = set()
#             for t in subject_group_all:
#                 if t != "":
#                     subject_group.update(t)
#             subject_group = [t for t in subject_group if ("A" in t or "B" in t, "C" in t, "D" in t) and len(t)==3]

#             # for i in subject_group_all:
#             #     if i != "" and ("A" in i or "B" in i or "C" in i or "D" in i) and len(i)==3:
#             #         subject_group.update(i)
            
#             point_all = []
#             for l in subject_group:
#                 point_all.append((l,[]))
#             point_all = dict(point_all)
#             for u in m["diemchuan_datas"]:
#                 if(is_number(u["point"]) and float(u["point"]) < 40 and u["subject_group"] in subject_group):
#                     if("Ngôn ngữ" in u["major_name"] or "Thang điểm 40" in u["note"]):  
#                         point_all[u["subject_group"]].append(float(u["point"])*3/4)
#                     else:
#                         point_all[u["subject_group"]].append(float(u["point"]))
            
            
#             point = []            
#             for l in subject_group:
#                 if(len(point_all[l]) >0):
#                     point.append((l,sum(point_all[l])/len(point_all[l])))
#             point = dict(point)
            
#             print(i)
#             i["subject_group"] =  subject_group
#             i["point_all"] = point_all
#             i["point"] = point
#             break
#     new_new_new_datas.append(i)
# with open('clean_university_.json', 'w') as outfile:
#     json.dump(new_new_new_datas, outfile,ensure_ascii=False, indent=4)