# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals

import  json
import  codecs
from pymongo import MongoClient
from .items import IreadweekItem, IreadweekUrlItem

class IreadweekPipeline(object):
    def __init__(self):
        # self.file = codecs.open('books.json', 'w', encoding='utf-8')
        self.client = MongoClient(host='localhost',port=27017)
        self.db = self.client.ireadweek
        self.book = self.db.book
        self.book_url = self.db.book_url

    def process_item(self, item, spider):
        if isinstance(item, IreadweekItem):
            # self.book.insert(dict(item))
            print(" 没保存")

        else:
            # self.book_url.insert(dict(item))
            print(" 没保存")
        # print(item)
        # line = json.dumps(dict(item),ensure_ascii=False) + '\n'
        # # self.file.write(line)
        # print("xXXXXXXXXXXXXXXXXXXXx")
        # print(line)
        return item

    def spider_closed(self,spider):
        # self.file.close()
        self.client.close()
    #
    # # 下载图片保存到IMAGE_STORE
    # def get_img_requests(self,item, info):
    #     yield scrapy.Request(item['src_img'])
