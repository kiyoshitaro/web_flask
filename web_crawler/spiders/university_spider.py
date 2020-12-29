import scrapy
from ..items import UniversityItem
from scrapy.http import Request
from scrapy_splash import SplashRequest

# import sys
# import codecs
# sys.stdout = codecs.getwriter('utf_16')(sys.stdout)

# sys.stdin = codecs.getreader('utf_8')(sys.stdin)

items = UniversityItem()
class UniversitySpider(scrapy.Spider):
    # page_number = 1
    # name = "university"
    # start_urls = [
    #     'https://diendantuyensinh24h.com/danh-sach-cac-truong-dai-hoc-va-hoc-vien-toan-quoc',
    #     ]
    
    # def parse(self, response):
        
    #     # university = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "column-width", " " )) and (((count(preceding-sibling::*) + 1) = 25) and parent::*)]//li/a')
    #     university = response.xpath('//table').css('tbody tr a')
    #     # university = response.css(".column-width:nth-child(25)")
        
    #     for i in university:
    #         detail_url = "https://diendantuyensinh24h.com" + i.xpath("@href").get()[8:]
    #         # items["name"] = i.css("a::text").extract()
    #         # print(i.css("a::text").extract())
    #         if i.xpath("@href").get()[8:] != "":
    #             yield Request(url = detail_url, callback = self.start_scraping)



    # def start_scraping(self,response):
    #     code = ""
    #     address = ""
    #     website = ""
    #     phone = ""
    #     type = ""

    #     image = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-md-5", " " ))]/img/@src').get()
    #     area = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-md-7", " " ))]')   
    #     name = area[1].xpath("//div/h1/text()").extract()[0] 
    #     # detail = area[1].xpath('//p[@class="stylekh"]')
    #     if len(area[1].css("div")) == 1:
    #         detail = area[1].css("div p")
    #     else:
    #         detail = area[1].css("div")
    #     for i in detail:
    #         if len(i.xpath("strong/text()")) > 0:
    #             label = i.xpath("strong/text()").get()
    #             info =  i.xpath("text()").extract()
    #         elif len(i.xpath("span/strong/text()")) > 0 :
    #             label = i.xpath("span/strong/text()").get()
    #             info =  i.xpath("span/text()").extract()
    #         else:
    #             label = i.xpath("strong/span/text()").get()
    #             info =  i.xpath("span/text()").extract()

    #         if len(info) > 1:
    #             info = info[-1]
    #         elif(len(info) == 1):
    #             info = info[0]
    #         else:
    #             info = ""

    #         if (label is not None):
    #             print(label,"sssss")
    #             # break
    #             if("Mã" in label or "Ký" in label):
    #                 code = i.xpath("span/text()").get()
    #                 if(code is None or len(code) < 3):
    #                     code = i.xpath("span/strong/text()").get() 
    #                 if(code is None or len(code) < 3):
    #                     code = i.xpath("text()").get() 
    #                 if(code is None or len(code) < 3):
    #                     code = i.css("span span::text").get()
    #             if("Địa" in label or "Cơ" in label ):
    #                 address = info
    #             if("Loại" in label):
    #                 type = info
    #             if("Website" in label):
    #                 website = info      
    #             if("Điện" in label):
    #                 phone = info
    #     if code and len(code) > 2 and address != "":
    #         detail = {"name": name,"address" : address,"code" : code, "type": type, "website": website, "phone" : phone, "image" : image}
    #         # items.address = detail.address
    #         # items.phone = detail.phone
    #         # items.type = detail.type
    #         # items.code = detail.code
    #         # items.website = detail.website
    #         yield detail





    # page_number = 1
    # name = "university"
    # start_urls = [
    #     'https://diemthi.tuyensinh247.com/danh-sach-truong-dai-hoc-cao-dang.html',
    #     ]
    
    # def parse(self, response):
        
    #     # university = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "column-width", " " )) and (((count(preceding-sibling::*) + 1) = 25) and parent::*)]//li/a')
    #     university = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-513", " " ))]').css("tr a::attr(href)")[1:599]                                                             
    #     # university = response.css(".column-width:nth-child(25)")
        
    #     for i in university:
    #         detail_url = "https://diemthi.tuyensinh247.com" + i.extract()
    #         # items["name"] = i.css("a::text").extract()
    #         # print(i.css("a::text").extract())
    #         yield Request(url = detail_url, callback = self.start_scraping)

    # def start_scraping(self,response):
    #     code = ""
    #     address = ""
    #     website = ""
    #     phone = ""
    #     type = ""

    #     area = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "cont-news", " " ))]')
    #     data = area.css("div p::text").extract()
    #     for i in data:
            
    #         if("Địa chỉ" in i):
    #             address = i.split("Địa chỉ: ")[-1]
    #         elif("site" in i and "www" in i):
    #             website = i
    #         elif("Điện" in i or "ĐT:" in i ):
    #             phone = i

    #     name_code = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "s14", " " ))]/text()').get().split("-")
    #     code = name_code[-1].replace(" ","")
    #     name = " - ".join(name_code[:-1])
    #     if code and len(code) > 2 and address != "":
    #         detail = {"name": name,"address" : address,"code" : code, "website": website, "phone" : phone}
    #         print(detail)
    #         yield detail


    page_number = 1
    name = "university"
    start_urls = [
        'https://kenhtuyensinh.vn/danh-sach-truong-dai-hoc-cao-dang',
        ]
    script = """
            function main(splash)
                assert(splash:go(splash.args.url))
                assert(splash:set_viewport_full())
                for i = 1,19,1 do
                    assert(splash:wait(1))
                    assert(splash:runjs("document.getElementById('timtruong_viewmore').click()"))
                    assert(splash:wait(1))
                end

                return {
                    html = splash:html(),
                    url = splash:url(),
                    }
            end
            """
    def parse(self, response):
        # university = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "link", " " ))]/@href')                                                            

        university = ['dai-hoc-my-tai-viet-nam-u-298',
                    'dai-hoc-buon-ma-thuot-u-4',
                    'hoc-vien-cong-nghe-buu-chinh-vien-thong-phia-bac-u-6',
                    'hoc-vien-cong-nghe-buu-chinh-vien-thong-phia-nam-u-7',
                    'dai-hoc-ba-ria-vung-tau-u-8',
                    'dai-hoc-cong-nghiep-det-may-ha-noi-u-9',
                    'dai-hoc-kinh-te-nghe-an-u-10',
                    'cao-dang-ky-thuat-cao-thang-u-11',
                    'dai-hoc-dong-a-u-14',
                    'dai-hoc-nong-lam-bac-giang-u-16',
                    'dai-hoc-bac-lieu-u-17',
                    'dai-hoc-cong-nghe-dong-nai-u-19',
                    'dai-hoc-tu-thuc-cong-nghe-thong-tin-gia-dinh-u-20',
                    'dai-hoc-cuu-long-u-22',
                    'dai-hoc-cong-nghiep-ha-noi-u-23',
                    'dai-hoc-cong-nghiep-thuc-pham-tp-hcm-u-24',
                    'dai-hoc-cong-nghiep-vinh-u-25',
                    'dai-hoc-thanh-dong-u-26',
                    'dai-hoc-ngoai-ngu-dai-hoc-da-nang-u-29',
                    'dai-hoc-bach-khoa-dai-hoc-da-nang-u-31',
                    'dai-hoc-dien-luc-u-32',
                    'dai-hoc-cong-nghiep-quang-ninh-u-33',
                    'dai-hoc-dai-nam-u-34',
                    'phan-hieu-dai-hoc-da-nang-tai-kon-tum-u-35',
                    'dai-hoc-su-pham-dai-hoc-da-nang-u-37',
                    'khoa-y-duoc-dai-hoc-da-nang-u-39',
                    'dai-hoc-tai-chinh-quan-tri-kinh-doanh-u-40',
                    'dai-hoc-luat-dai-hoc-hue-u-41',
                    'khoa-giao-duc-the-chat-dai-hoc-hue-u-42',
                    'khoa-du-lich-dai-hoc-hue-u-43',
                    'dai-hoc-ngoai-ngu-dai-hoc-hue-u-44',
                    'dai-hoc-kinh-te-dai-hoc-hue-u-45',
                    'dai-hoc-nong-lam-dai-hoc-hue-u-46',
                    'dai-hoc-nghe-thuat-dai-hoc-hue-u-47',
                    'phan-hieu-dai-hoc-hue-tai-quang-tri-u-49',
                    'dai-hoc-su-pham-dai-hoc-hue-u-50',
                    'dai-hoc-khoa-hoc-dai-hoc-hue-u-51',
                    'dai-hoc-hung-vuong-tphcm-u-52',
                    'dai-hoc-y-duoc-dai-hoc-hue-u-53',
                    'dai-hoc-kinh-te-ky-thuat-binh-duong-u-54',
                    'dai-hoc-cong-nghe-tphcm-hutech-u-55',
                    'dai-hoc-duoc-ha-noi-u-56',
                    'dai-hoc-kinh-te-ky-thuat-cong-nghiep-u-57',
                    'dai-hoc-tai-chinh-ke-toan-u-58',
                    'dai-hoc-ky-thuat-y-te-hai-duong-u-61',
                    'dai-hoc-kinh-te-cong-nghiep-long-an-u-62',
                    'dai-hoc-lac-hong-u-63',
                    'dai-hoc-lao-dong-xa-hoi-co-so-phia-nam-u-64',
                    'dai-hoc-lao-dong-xa-hoi-co-so-son-tay-u-65',
                    'dai-hoc-lao-dong-xa-hoi-co-so-ha-noi-u-66',
                    'dai-hoc-cong-nghe-mien-dong-u-67',
                    'dai-hoc-tai-chinh-marketing-u-68',
                    'dai-hoc-tai-nguyen-va-moi-truong-ha-noi-u-69',
                    'dai-hoc-nam-can-tho-u-71',
                    'dai-hoc-ngoai-ngu-tin-hoc-tphcm-u-73',
                    'dai-hoc-dong-nai-u-74',
                    'dai-hoc-noi-vu-u-75',
                    'dai-hoc-dan-lap-phuong-dong-u-76',
                    'dai-hoc-pham-van-dong-u-77',
                    'dai-hoc-phan-thiet-u-78',
                    'dai-hoc-dan-lap-phu-xuan-u-79',
                    'dai-hoc-phu-yen-u-80',
                    'dai-hoc-quang-binh-u-81',
                    'dai-hoc-kinh-doanh-va-cong-nghe-ha-noi-u-83',
                    'dai-hoc-quy-nhon-u-84',
                    'dai-hoc-quang-nam-u-86',
                    'dai-hoc-san-khau-dien-anh-tphcm-u-87',
                    'dai-hoc-cong-nghe-sai-gon-u-88',
                    'dai-hoc-thanh-tay-u-89',
                    'dai-hoc-cong-nghe-thong-tin-va-truyen-thong-dai-hoc-thai-nguyen-u-91',
                    'dai-hoc-tay-do-u-92',
                    'dai-hoc-kinh-te-quan-tri-kinh-doanh-dai-hoc-thai-nguyen-u-93',
                    'khoa-ngoai-ngu-dai-hoc-thai-nguyen-u-94',
                    'dai-hoc-hoa-sen-u-95',
                    'dai-hoc-thang-long-u-97',
                    'dh-tai-nguyen-moi-truong-tphcm-u-98',
                    'dai-hoc-nong-lam-dai-hoc-thai-nguyen-u-99',
                    'phan-hieu-dai-hoc-thai-nguyen-tai-lao-cai-u-100',
                    'khoa-quoc-te-dai-hoc-thai-nguyen-u-101',
                    'dai-hoc-su-pham-dai-hoc-thai-nguyen-u-102',
                    'dai-hoc-ton-duc-thang-u-103',
                    'dai-hoc-y-duoc-dai-hoc-thai-nguyen-u-104',
                    'dai-hoc-khoa-hoc-dai-hoc-thai-nguyen-u-105',
                    'dai-hoc-van-hoa-the-thao-va-du-lich-thanh-hoa-u-106',
                    'dai-hoc-van-hien-u-107',
                    'dai-hoc-van-lang-u-108',
                    'dai-hoc-tra-vinh-u-109',
                    'dai-hoc-cong-nghe-van-xuan-u-110',
                    'dai-hoc-quoc-te-mien-dong-u-112',
                    'dai-hoc-giao-thong-van-tai-co-so-phia-bac-u-115',
                    'dai-hoc-giao-thong-van-tai-co-so-phia-nam-u-116',
                    'dai-hoc-cong-nghe-giao-thong-van-tai-u-117',
                    'dai-hoc-giao-thong-van-tai-tphcm-u-118',
                    'hoc-vien-bao-chi-tuyen-truyen-u-119',
                    'dai-hoc-quoc-te-hong-bang-u-120',
                    'hoc-vien-chinh-sach-va-phat-trien-u-125',
                    'hoc-vien-hau-can-he-quan-su-u-128',
                    'truong-si-quan-phong-hoa-u-130',
                    'dai-hoc-hang-hai-u-131',
                    'hoc-vien-hang-khong-viet-nam-u-132',
                    'dai-hoc-ha-long-u-134',
                    'dai-hoc-thu-do-ha-noi-u-135',
                    'hoc-vien-y-duoc-hoc-co-truyen-viet-nam-u-146',
                    'dai-hoc-ky-thuat-cong-nghe-can-tho-u-147',
                    'dai-hoc-kinh-te-quoc-dan-u-149',
                    'dai-hoc-kinh-te-tphcm-u-152',
                    'dai-hoc-kinh-te-tai-chinh-tphcm-u-154',
                    'truong-si-quan-luc-quan-1-dai-hoc-tran-quoc-tuan-u-157',
                    'truong-si-quan-luc-quan-2-dai-hoc-nguyen-hue-u-158',
                    'dai-hoc-mo-tphcm-u-166',
                    'dai-hoc-mo-dia-chat-u-168',
                    'dai-hoc-ngan-hang-tphcm-u-178',
                    'dai-hoc-ngoai-thuong-co-so-phia-bac-u-183',
                    'dai-hoc-ngoai-thuong-phia-nam-u-184',
                    'dai-hoc-nguyen-tat-thanh-u-185',
                    'hoc-vien-phong-khong-khong-quan-u-191',
                    'dai-hoc-bach-khoa-dai-hoc-quoc-gia-tphcm-u-202',
                    'dai-hoc-cong-nghe-thong-tin-u-203',
                    'dai-hoc-kinh-te-luat-dai-hoc-quoc-gia-tphcm-u-204',
                    'dai-hoc-quoc-te-dai-hoc-quoc-gia-tphcm-u-205',
                    'dai-hoc-khoa-hoc-tu-nhien-u-206',
                    'dai-hoc-khoa-hoc-xa-hoi-va-nhan-van-u-207',
                    'khoa-y-dai-hoc-quoc-gia-tphcm-u-208',
                    'dai-hoc-sai-gon-u-210',
                    'dai-hoc-su-pham-tphcm-u-219',
                    'dai-hoc-an-giang-u-221',
                    'dai-hoc-da-lat-u-226',
                    'dai-hoc-nha-trang-u-237',
                    'dai-hoc-van-hoa-ha-noi-u-249',
                    'dai-hoc-y-duoc-tphcm-u-260',
                    'dai-hoc-cong-nghe-va-quan-ly-huu-nghi-u-282',
                    'dai-hoc-cong-nghe-dong-a-u-283',
                    'dai-hoc-phan-chau-trinh-u-285',
                    'dai-hoc-yersin-da-lat-u-288',
                    'dai-hoc-luat-tphcm-u-290',
                    'dai-hoc-su-pham-nghe-thuat-trung-uong-u-294',
                    'dai-hoc-dan-lap-hai-phong-u-48',
                    'dai-hoc-hoa-lu-u-70',
                    'dai-hoc-quang-trung-u-85',
                    'dai-hoc-tai-chinh-ngan-hang-ha-noi-u-113',
                    'dai-hoc-ha-tinh-u-133',
                    'hoc-vien-thanh-thieu-nien-viet-nam-u-141',
                    'dai-hoc-nguyen-trai-u-186',
                    'dai-hoc-dau-khi-viet-nam-u-192',
                    'dai-hoc-dong-thap-u-216',
                    'dai-hoc-su-pham-ha-noi-u-217',
                    'dai-hoc-su-pham-ky-thuat-tphcm-u-218',
                    'dai-hoc-can-tho-u-223',
                    'dai-hoc-thu-dau-mot-u-227',
                    'dai-hoc-vinh-u-229',
                    'dai-hoc-dan-lap-duy-tan-u-38',
                    'dai-hoc-kiem-sat-ha-noi-u-59',
                    'dai-hoc-hong-duc-u-127',
                    'hoc-vien-phu-nu-viet-nam-u-136',
                    'hoc-vien-ngoai-giao-u-138',
                    'hoc-vien-toa-an-u-139',
                    'hoc-vien-tai-chinh-u-140',
                    'hoc-vien-nong-nghiep-viet-nam-u-144',
                    'truong-si-quan-khong-quan-he-dai-hoc-u-148',
                    'hoc-vien-ky-thuat-mat-ma-u-150',
                    'hoc-vien-ky-thuat-quan-su-he-quan-su-u-151',
                    'dai-hoc-kien-truc-ha-noi-u-153',
                    'dai-hoc-kien-truc-tphcm-u-156',
                    'dai-hoc-cong-doan-u-162',
                    'dai-hoc-luat-ha-noi-u-165',
                    'vien-dai-hoc-mo-ha-noi-u-169',
                    'dai-hoc-ha-noi-u-175',
                    'hoc-vien-khoa-hoc-quan-su-he-quan-su-u-182',
                    'dai-hoc-phong-chay-chua-chay-phia-bac-u-189',
                    'dai-hoc-phong-chay-chua-chay-phia-nam-u-190',
                    'dai-hoc-kinh-te-dai-hoc-quoc-gia-ha-noi-u-193',
                    'dai-hoc-ngoai-ngu-dai-hoc-quoc-gia-ha-noi-u-194',
                    'dai-hoc-cong-nghe-dai-hoc-quoc-gia-ha-noi-u-195',
                    'khoa-luat-dai-hoc-quoc-gia-ha-noi-u-196',
                    'khoa-quoc-te-dai-hoc-quoc-gia-ha-noi-u-197',
                    'dai-hoc-giao-duc-dai-hoc-quoc-gia-ha-noi-u-198',
                    'dai-hoc-khoa-hoc-tu-nhien-dai-hoc-quoc-gia-ha-noi-u-199',
                    'dai-hoc-khoa-hoc-xa-hoi-va-nhan-van-dai-hoc-quoc-gia-ha-noi-u-200',
                    'khoa-y-duoc-dai-hoc-quoc-gia-ha-noi-u-201',
                    'dai-hoc-sao-do-u-209',
                    'dai-hoc-su-pham-ky-thuat-hung-yen-u-212',
                    'dai-hoc-su-pham-ha-noi-2-u-215',
                    'khoa-cong-nghe-dai-hoc-da-nang-u-27',
                    'dai-hoc-kinh-te-dai-hoc-da-nang-u-36',
                    'hoc-vien-an-ninh-nhan-dan-u-1',
                    'dai-hoc-an-ninh-nhan-dan-u-2',
                    'hoc-vien-bien-phong-u-5',
                    'hoc-vien-canh-sat-nhan-dan-u-12',
                    'dai-hoc-canh-sat-nhan-dan-u-13',
                    'truong-si-quan-dac-cong-u-21',
                    'phan-hieu-dai-hoc-nong-lam-tp-hcm-tai-gia-lai-u-179',
                    'phan-hieu-dai-hoc-nong-lam-tp-hcm-tai-ninh-thuan-u-180',
                    'dai-hoc-nong-lam-tphcm-u-181',
                    'dai-hoc-y-ha-noi-u-261',
                    'dai-hoc-cong-nghiep-tphcm-u-142',
                    'hoc-vien-hai-quan-u-137',
                    'truong-si-quan-chinh-tri-dai-hoc-chinh-tri-u-160',
                    'dai-hoc-my-thuat-viet-nam-u-171',
                    'hoc-vien-ngan-hang-u-176',
                    'truong-si-quan-phao-binh-u-188',
                    'dai-hoc-hai-phong-u-231',
                    'dai-hoc-thuong-mai-u-235',
                    'truong-si-quan-ki-thuat-quan-su-he-quan-su-u-252',
                    'hoc-vien-quan-y-he-quan-su-u-264',
                    'dai-hoc-su-pham-ky-thuat-vinh-u-296',
                    'dai-hoc-bach-khoa-ha-noi-u-3',
                    'dai-hoc-y-te-cong-cong-u-266',
                    'hoc-vien-can-bo-tphcm-u-143',
                    'dai-hoc-su-pham-ky-thuat-nam-dinh-u-213',
                    'dai-hoc-kien-giang-u-293',
                    'dai-hoc-rmit-viet-nam-u-280',
                    'dai-hoc-tay-nguyen-u-242',
                    'cao-dang-cong-nghe-thong-tin-dai-hoc-da-nang-u-30',
                    'dai-hoc-xay-dung-ha-noi-u-255',
                    'hoc-vien-ki-thuat-quan-su-he-dan-su-u-82',
                    'dai-hoc-viet-duc-u-247',
                    'dai-hoc-thuy-loi-co-so-1-u-233',
                    'dai-hoc-thuy-loi-co-so-2-u-234',
                    'dai-hoc-ky-thuat-cong-nghiep-dai-hoc-thai-nguyen-u-96',
                    'dai-hoc-lam-nghiep-co-so-1-u-163',
                    'dai-hoc-lam-nghiep-co-so-2-u-164',
                    'dai-hoc-y-khoa-pham-ngoc-thach-u-244',
                    'dai-hoc-my-thuat-tphcm-u-172',
                    'dai-hoc-binh-duong-u-15',
                    'hoc-vien-hanh-chinh-quoc-gia-phia-bac-u-123',
                    'hoc-vien-hanh-chinh-quoc-gia-phia-nam-u-126',
                    'dai-hoc-ky-thuat-hau-can-cong-an-nhan-dan-phia-bac-u-122',
                    'dai-hoc-ky-thuat-hau-can-cong-an-nhan-dan-phia-nam-u-124',
                    'hoc-vien-chinh-tri-cong-an-nhan-dan-u-121',
                    'dai-hoc-my-thuat-cong-nghiep-u-170',
                    'dai-hoc-van-hoa-nghe-thuat-quan-doi-u-268',
                    'dai-hoc-van-hoa-tphcm-u-250',
                    'dai-hoc-san-khau-dien-anh-u-211',
                    'nhac-vien-tphcm-u-187',
                    'dai-hoc-su-pham-the-duc-the-thao-tphcm-u-220',
                    'dai-hoc-quoc-te-sai-gon-u-243',
                    'truong-si-quan-ki-thuat-quan-su-he-dan-su-u-269',
                    'hoc-vien-khoa-hoc-quan-su-he-dan-su-u-72',
                    'hoc-vien-quan-y-he-dan-su-u-111',
                    'hoc-vien-hau-can-he-dan-su-u-129',
                    'hoc-vien-ngan-hang-phan-vien-bac-ninh-u-174',
                    'hoc-vien-ngan-hang-phan-vien-phu-yen-u-177',
                    'hoc-vien-quan-ly-giao-duc-u-145',
                    'dai-hoc-kien-truc-da-nang-u-155',
                    'dai-hoc-y-hai-phong-u-263',
                    'dai-hoc-the-ducthe-thao-da-nang-u-239',
                    'dai-hoc-y-duoc-can-tho-u-257',
                    'truong-si-quan-chinh-tri-he-dan-su-u-161',
                    'dai-hoc-the-duc-the-thao-tphcm-u-228',
                    'truong-si-quan-tang-thiet-giap-u-230',
                    'truong-si-quan-thong-tin-he-quan-su-dai-hoc-thong-tin-lien-lac-u-241',
                    'dai-hoc-cong-nghiep-viet-hung-u-248',
                    'dai-hoc-ky-thuat-y-duoc-da-nang-u-259',
                    'dai-hoc-y-khoa-vinh-u-262',
                    'dai-hoc-y-duoc-thai-binh-u-265',
                    'truong-si-quan-cong-binh-he-dan-su-u-267',
                    'dai-hoc-xay-dung-mien-tay-u-173',
                    'dai-hoc-xay-dung-mien-trung-u-256',
                    'dai-hoc-tay-bac-u-238',
                    'dai-hoc-khanh-hoa-u-246',
                    'dai-hoc-hai-duong-u-60',
                    'dai-hoc-thai-binh-u-90',
                    'dai-hoc-chu-van-an-u-18',
                    'dai-hoc-dan-lap-dong-do-u-28',
                    'dai-hoc-nguyen-hue-u-159',
                    'dai-hoc-my-thuat-cong-nghiep-a-chau-u-167',
                    'truong-si-quan-cong-binh-he-quan-su-u-214',
                    'dai-hoc-thai-binh-duong-u-222',
                    'dai-hoc-the-duc-the-thao-bac-ninh-u-224',
                    'dai-hoc-thanh-do-u-225',
                    'dai-hoc-hung-vuong-u-232',
                    'dai-hoc-tan-trao-u-236',
                    'dai-hoc-tien-giang-u-240',
                    'dai-hoc-kinh-bac-u-245',
                    'dai-hoc-su-pham-ky-thuat-vinh-long-u-251',
                    'dai-hoc-vo-truong-toan-u-253',
                    'dai-hoc-cong-nghiep-viet-tri-u-254',
                    'dai-hoc-dieu-duong-nam-dinh-u-258',
                    'dai-hoc-fpt-u-277',
                    'dai-hoc-quoc-te-bac-ha-u-281',
                    'dai-hoc-viet-bac-u-284',
                    'dai-hoc-dan-lap-luong-the-vinh-u-286',
                    'dai-hoc-trung-vuong-u-287',
                    'dai-hoc-hoa-binh-u-289',
                    'truong-si-quan-thong-tin-he-dan-su-dai-hoc-thong-tin-lien-lac-u-291',
                    'dai-hoc-su-pham-the-duc-the-thao-ha-noi-u-292',
                    'truong-fast-tarck-se-u-295']
        for i in university:
            print(i)
            detail_url = "https://kenhtuyensinh.vn/" + i + "/hoc-phi"
            # items["name"] = i.css("a::text").extract()
            # print(i.css("a::text").extract())
            # yield {"url" : detail_url}
            yield Request(url = detail_url, callback = self.start_scraping)

    def start_scraping(self,response):
        abbr = ""
        address = ""
        website = ""
        phone = ""
        type = ""
        info = ""
        area = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-lg-8", " " ))]')

        name = area.css("h1::text").get()
        abbr = ""+area.css(".uni-code::text").get()
        year = area.css(".year::text").get().replace(" ","")
        city = area.css("div.address a::text").get()
        address = area.xpath("div[@class='address']")[1].xpath('span/text()')[1].get()
        website = area.xpath('div[@class="website"]/a/text()').get()
        
        
        logo = response.css('.flex-wrapper img::attr(src)').get()
        # tables = response.xpath("//table")
        # info = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-main", " " ))] | //*[contains(concat( " ", @class, " " ), concat( " ", "b-error", " "))]').css('.pc *::text').get()
        info = " ".join(response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "pc", " " ))]').css('*::text').extract())
        
        if city != "":
            detail = {"name": name,"address" : address,"abbr" : abbr, "website": website, "year" : year, "city" :  city,"fee":"", "info" : info,"logo": logo}
            # print(detail)
            yield detail
