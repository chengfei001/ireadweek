import scrapy
from scrapy import Selector
from requests import get
# from ..items import IreadweekItem
import os

class indexSpider(scrapy.Spider):
    name = 'index_super'
    allowed_domains = ['ireadweek.com']
    base_url = 'http://www.ireadweek.com'
    start_urls ='http://www.ireadweek.com'

    def parse(self, response):
        selector = Selector(response)
        # 获取下一页的链接
        # response.xpath('//nav[@class="action-pagination"]/ul/li[a/text()="下一页>>"]/a/@href').extract()
        # urls_list = response.xpath('//nav[@class="action-pagination"]/ul/li[a/text()="下一页>>"]/a/@href').extract()
        # 获取列表链接 书名 下载量 作者
        # response.xpath('//ul[@class="hanghang-list"]/a').extract()
        # 书名
        # response.xpath('//ul[@class="hanghang-list"]/a/li/div[@class="hanghang-list-name/text()"]').extract()
        # 下载量
        # response.xpath('//ul[@class="hanghang-list"]/a/li/div[@class="hanghang-list-num"]/text()').extract()
        # 作者
        # response.xpath('//ul[@class="hanghang-list"]/a/li/div[@class="hanghang-list-zuozhe"]/text()').extract()
        # 图书详细链接
        # response.xpath('//ul[@class="hanghang-list"]/a/@href').extract()
        # print(urls_list)
        pass