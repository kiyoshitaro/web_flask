import scrapy
from ..items import QuoteItem


class SubjectSpider(scrapy.Spider):
    page_number = 1
    name = "subject"
    start_urls = [
        'http://tuyensinh.ussh.edu.vn/Danh-sach-cac-to-hop-xet-tuyen-khoi-thi-dai-hoc-chinh-quy-nam-2018-325.html'
        ]

    def parse(self,response):
        data = response.xpath('//table/tbody/tr')

        for d in data[1:]:
            (_,code,name) = d.css("td::text").extract()
            yield {code : name}
                

