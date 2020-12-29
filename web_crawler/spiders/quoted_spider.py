import scrapy
from ..items import QuoteItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class QuoteSpider(scrapy.Spider):
    page_number = 1
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com'
        ]

    def start_scraping(self, response):

        # VER_1
        title = response.css("span::text").extract()
        quotes = response.css("span.text::text").extract()
        # quotes = response.xpath("//span[@class='text']/text()").extract()
        authors = response.css("small.author::text").extract()
        # authors = response.xpath("//small[@class='author']/text()").extract()
        

        # VER_2
        # all_div_quotes = response.css("div.quote")
        # for i in all_div_quotes:
        #     quote = i.css("span.text::text").extract()
        #     author = i.css("small.author::text").extract()
        #     tags = i.css(".tag::text").extract()
        #     yield {
        #         "quote" : quote,
        #         "author": author,
        #         "tag": tags,
        #         }


        # VER_3
        items = QuoteItem()
        all_div_quotes = response.css("div.quote")
        for i in all_div_quotes:
            items["quote"] = i.css("span.text::text").extract()
            items["author"] = i.css("small.author::text").extract()
            items["tags"] = i.css(".tag::text").extract()
            yield items



        # NEXT_PAGE_VER_!
        next_page = response.css("li.next a::attr(href)").get()
        next_page = response.css("li.next a").xpath("@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)


        # NEXT_PAGE_VER_2
        next_page = "https://quotes.toscrape.com/page/" + str(QuoteSpider.page_number) + "/"
        if QuoteSpider.page_number <= 11:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)

        open_in_browser(response)

    def parse(self,response):
        token = response.css("form input::attr(value)").extract_first()
        return FormRequest.from_response(response,formdata={
            "csrf_token" : token,
            'username' : "",
            'password': '',

        }, callback = self.start_scraping)
        