# COLLEGE RECOMMENDER

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/kiyoshitaro/web_flask)


Build an app to recommend college to student in Viet Nam and complete assignment in school (yep it's the main reason)

I also have a little note about scrapy, flask ,... to remind myself, just ignore this stuff :')

## CRAWL DATA

https://www.youtube.com/playlist?list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t

```sh

scrapy startproject  amazon_crawler : Create project

scrapy crawl spider_name(define in class QuoteSpider)

Open shell : scrapy shell “url”

```


### CSS
- Selector gadget in chrome to get css 
> response.css(".column-width:nth-child(25) li::attr(href)").extract() 
- .column-width is class, 
- li is another card
- href is attr

### XPATH
>    response.xpath("//span[@class='text']/text()"): 
- get all span card with class = "text"
- can use that to get info from card like href, ...

        
>    i.xpath("//li/a") =  i.xpath("/ol/li/a")

- use $x(x_path string) to test xpath in console


> add FEED_EXPORT_ENCODING = 'utf-8' in settings.py to export readable json file


### Step to crawl

-    data city.json available in folder data

>    scrapy crawl university -o data/university.json : get uni info but not "code" info, consider "abbr" instead of "code"
-    --> university.json

>    we get "code" info then map to university from html file (data/url.html) that capture from website (because i not  knew how to use splash yet ;<<> ). see script extract_info_from_html in utils.py
-    --> university_add_code.json

>    we have available data/university_diemchuan file (from bee project <3 >), with that we can get "point", "major", "subject" data, add all of that with "area" and reformat . See add_uni_detail_info script
-    --> clean_university.json

>    Manually add "fee" info :,> , may be extract from "info" if u can process nlp <33 It is too hard @.@
    
- ENOUGH, get out of other trash code in utils.py :,<
    
## TOPSIS ALGORITHM

### Build matrix: 

#### **Thuộc tính 1: Khoảng cách địa lý**
  - Dựa trên khoảng vị trí địa lý của trường đại học với thí sinh
  - Thí sinh sẽ chọn tỉnh thành nơi mình sinh sống, từ đó tham chiếu đến các vùng được đánh số thứ tự
  - Khoảng cách sẽ được tính tương đối
    - (𝑣u𝑛𝑔𝑇𝑆 − 𝑣u𝑛𝑔𝑇Đ𝐻)^2
  - Giá trị càng **nhỏ** càng tốt

#### **Thuộc tính 2: Kinh tế**

  - Dựa trên tương quan hoàn cảnh gia đình thí sinh với mức học phí 1 kì của các trường đại học đưa ra
  - Ưu tiên trường có mức học phí gần với thí sinh đưa ra và hạn chế cao hơn quá nhiều
  - Công thức:
    - Nếu mức học phí của trường nhỏ hơn mức độ chi trả của sinh viên:
      - kte𝑇𝑆 − hocphi𝑇Đ𝐻

    - Nếu mức học phí của trường lớn hơn mức độ chi trả của sinh viên
      - (hocphi𝑇Đ𝐻− kte𝑇𝑆)∗3 


Giá trị càng **nhỏ** càng tốt

#### *Thuộc tính 3: Điểm thi**

- Dựa trên điểm thi đại học thí sinh với TB điểm chuẩn trường đại học theo tổ hợp thi (A00, A01, B01, ….) các năm trước
- Mỗi thí sinh sẽ nhập tổng điểm 3 môn + ưu tiên của mình trong 2 tổ hợp thi THPT Quốc Gia(nếu chỉ đăng kí 1 thì nhập 2 điểm giống nhau)
- Công thức:
  - Nếu điểm chuẩn TB của trường nhỏ hơn điểm thi của sinh viên:
    - diemthi𝑇𝑆 − diemchuan𝑇Đ𝐻
  - Nếu điểm chuẩn TB của trường lớn hơn điểm thi của sinh viên
    - (diemchuan𝑇Đ𝐻− diemthi𝑇𝑆)∗4 
  - Nếu trường không xét tuyển tổ hợp thi của thí sinh  gán giá trị 100

Giá trị càng **nhỏ** càng tốt


#### **Thuộc tính 4: Đào tạo**

- Dựa trên nguyện vọng thí sinh với chương trình đào tạo của trường đại học
- Mỗi thí sinh sẽ nhập nguyện vọng của mình (kĩ thuật , kinh tế , hội hoạ, … )
- Đo khoảng cách chuỗi nhập của thí sinh với tên các ngành đào tạo của các trường bằng khoảng cách **Levenshtein**
- Công thức:
    - ∑0-3〖sorted([Lev(nguyenvong, chtrdaotao)])〗
- Giá trị càng **lớn** càng tốt

### Run algorithm

``` python
    See function in file topsis.py
    Run : 
        from topsis import topsis
        a =[
        ...     [250, 16, 12, 5],
        ...     [200, 16, 8, 3],
        ...     [300, 32, 16, 4],
        ...     [275, 32, 8, 4],
        ...     [225, 16, 16, 2]
        ... ]
        >>> w = [1,1,1,1]
        >>> sign = [-1, 1, 1, 1]
        >>> tp.topsis(a, w, sign)
```
## FLASK WEB
``` sh
mkdir app
add basic code in app/__init__.py , app/routes.py , 

export FLASK_APP=blog.py
flask run
```
- install python-dotenv to save env arg in .flaskenv

- mkdir app/templates to save html file


### DEPLOY
- Create heroku account
> git checkout -b deploy

- Assign an app with Heroku
> heroku apps:create hungnt-flask(name is exclusive)

- Heroku will make URL assign to app and remote repository , check
> git remote -v

- Prepare requirements.txt

- Heroku not supply Web Server for app, instead it suppose that we use our own Web server. So we use **gunicorn**

- Create Procfile: instruct Heroku how to execute the app

- Setup env arg
> heroku config:set FLASK_APP=blog.py

### Up to server:

```sh
flask run
git add .                        
git commit -a -m "adđ match word"
git push heroku deploy:master
```

**View**

http://hungnt-flask.herokuapp.com/college_recommend

