# COLLEGE RECOMMENDER
## CRAWL DATA

https://www.youtube.com/playlist?list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t

scrapy startproject  amazon_crawler : Create project

scrapy crawl spider_name(define in class QuoteSpider)

Open shell : scrapy shell “url”

### CSS
    Selector gadget in chrome to get css 
    response.css(".column-width:nth-child(25) li::attr(href)").extract() 
        .column-width is class, 
        li is another card
        href is attr

### XPATH
    response.xpath("//span[@class='text']/text()"): 
        get all span card with class = "text"
        can use that to get info from card like href, ...

        
    i.xpath("//li/a") =  i.xpath("/ol/li/a")

    use $x(x_path string) to test xpath in console


add FEED_EXPORT_ENCODING = 'utf-8' in settings.py to export readable json file


### Step to crawl

    data city.json available in folder data

    scrapy crawl university -o data/university.json : get uni info but not "code" info, consider "abbr" instead of "code"
    --> university.json

    we get "code" info then map to university from html file (data/url.html) that capture from website (because i not  knew how to use splash yet ;<<> ). see script extract_info_from_html in utils.py
    --> university_add_code.json

    we have available data/university_diemchuan file (from bee project <3 >), with that we can get "point", "major", "subject" data, add all of that with "area" and reformat . See add_uni_detail_info script
    --> clean_university.json

    Manually add "fee" info :,> , may be extract from "info" if u can process nlp <33 It is too hard @.@
    
    ENOUGH, get out of other trash code in utils.py :,<
    
## TOPSIS ALGORITHM

### Build matrix: 


### Run algorithm

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

## FLASK WEB
mkdir app
add basic code in app/__init__.py , app/routes.py , 

export FLASK_APP=college_recommend.py
flask run

install python-dotenv to save env arg in .flaskenv

mkdir app/templates to save html file


### Up to global

flask run
git add .                        
git commit -a -m "adđ match word"
git push heroku deploy:master

http://hungnt-flask.herokuapp.com/

https://thaitpham.com/huong-dan-lap-trinh-flask-phan-4-su-dung-co-so-du-lieu/
