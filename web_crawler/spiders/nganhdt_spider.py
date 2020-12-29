import scrapy
from scrapy.http import Request

class NganhdtSpider(scrapy.Spider):
    page_number = 1
    name = "nganh"
    start_urls = [
        'https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_tr%C6%B0%E1%BB%9Dng_%C4%91%E1%BA%A1i_h%E1%BB%8Dc,_h%E1%BB%8Dc_vi%E1%BB%87n_v%C3%A0_cao_%C4%91%E1%BA%B3ng_t%E1%BA%A1i_H%C3%A0_N%E1%BB%99i',
        # 'https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_tr%C6%B0%E1%BB%9Dng_%C4%91%E1%BA%A1i_h%E1%BB%8Dc_t%E1%BA%A1i_Th%C3%A0nh_ph%E1%BB%91_H%E1%BB%93_Ch%C3%AD_Minh',
        # 'https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_tr%C6%B0%E1%BB%9Dng_%C4%91%E1%BA%A1i_h%E1%BB%8Dc_v%C3%A0_cao_%C4%91%E1%BA%B3ng_t%E1%BA%A1i_%C4%90%C3%A0_N%E1%BA%B5ng',
        ]
    
    def parse(self, response):
        type =1
        tables = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "wikitable", " " ))]')
        for i,table in enumerate(tables):
            if (type ==1):
                rows = table.css('tbody tr')[1:]
                for row in rows:
                    label = row.css('td::text')[2].get().replace("\n","")
                    nganh = row.css('td')[3].css('*::text').extract()
                    if label != "" and len(label) < 4:
                        yield({label:nganh})
            elif(type == 2):

                rows = table.css('tbody tr')[1:]
                for row in rows:
                    label = row.css('td::text')[1].get().replace("\n","")
                    if i == 2:
                        label = row.css('td')[2].css("::text").get().replace("\n","")
                    nganh = row.css('td')[3].css('*::text').extract()
                    if label != "" and len(label) < 4:
                        yield({label:nganh})
                    
            else:
                rows = table.css('tbody tr')[2:]
                for row in rows:
                    label = row.css('td::text')[2].get().replace("\n","")
                    nganh = row.css('td')[4].css('*::text').extract()
                    if label != "" and len(label) < 4:
                        yield({label:nganh})




