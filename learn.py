


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

import pdb 
pdb.set_trace()
extract_info_from_html()