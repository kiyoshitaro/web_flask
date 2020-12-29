# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QuoteItem(scrapy.Item):
    quote = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

class UniversityItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    code = scrapy.Field()
    phone = scrapy.Field()
    website = scrapy.Field()
    type = scrapy.Field()
    





