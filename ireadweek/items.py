# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IreadweekItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    author = scrapy.Field()
    classify = scrapy.Field()
    content = scrapy.Field()
    baidu_url = scrapy.Field()
    src_url = scrapy.Field()
    book_img = scrapy.Field()
    src_img = scrapy.Field()
    pass
