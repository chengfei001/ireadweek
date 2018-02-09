import scrapy
from scrapy import Selector
from requests import get
from ..items import IreadweekItem, IreadweekUrlItem
from pymongo import MongoClient
import os



class IndexSpider(scrapy.Spider):
    name = 'index_super'
    allowed_domains = ['ireadweek.com']
    base_url = 'http://www.ireadweek.com'
    start_urls = ['http://www.ireadweek.com/index.php/index/194.html']

    def __init__(self):
        # self.client = MongoClient(host='locahost',port=27017)
        # self.db = self.client.ireadweek
        # self.book = self.db.books
        # self.book_url = self.db.book_url
        self.author_flag = '作者：'
        self.classify_flag = '分类：'
        self.content_flag = '简介：'

    def parse(self, response):
        # selector = Selector(response)
        # 获取下一页的链接
        next_page = response.xpath('//nav[@class="action-pagination"]/ul/li[a/text()="下一页>>"]/a/@href')
        if(len(next_page)>0):
            url = self.base_url + next_page.extract_first()
            yield scrapy.Request(url, callback=self.parse)

        # urls_list = response.xpath('//nav[@class="action-pagination"]/ul/li[a/text()="下一页>>"]/a/@href').extract()
        # 获取列表链接 书名 下载量 作者
        selector = response.xpath('//ul[@class="hanghang-list"]/a')
        # i = 0
        for selector_item in selector:
            urlItem = IreadweekUrlItem()
            # book_item = {}
            # 书名
            urlItem['book_name'] = selector_item.xpath('li/div[@class="hanghang-list-name"]/text()').extract_first()
            # response.xpath('//ul[@class="hanghang-list"]/a/li/div[@class="hanghang-list-name/text()"]').extract()
            # 下载量
            urlItem['book_download_num'] = selector_item.xpath('li/div[@class="hanghang-list-num"]/text()').extract_first()
            # 作者
            urlItem['book_author'] = selector_item.xpath('li/div[@class="hanghang-list-zuozhe"]/text()').extract_first()
            # 图书详细链接
            urlItem['book_url'] = self.base_url + selector_item.xpath('@href').extract_first()
            yield urlItem
            # print(IreadweekUrlItem)
            if urlItem['book_url'].find('8822.html') == -1 and urlItem['book_url'].find('1503.html') == -1:
                yield scrapy.Request(urlItem['book_url'], callback=self.parse_book)

            # pass

    # 抓取列表
    def parse_book(self, response):
        item = IreadweekItem()
        selector = Selector(response)
        all_content = selector.xpath("//div[@class='hanghang-shu-content-font']")
        content_start = False
        content_text = ''
        for content_item in all_content.xpath("p/text()").extract():
            if not content_start:
                # 获取作者
                if content_item.find(self.author_flag) >= 0:
                    item['author'] = content_item[
                                     content_item.find(self.author_flag) + len(self.author_flag): len(content_item)]
                # 获取分类
                elif content_item.find(self.classify_flag) >= 0:
                    item['classify'] = content_item[
                                       content_item.find(self.classify_flag) + len(self.classify_flag): len(
                                           content_item)]
                # 获取简介，如果到达简介部分，后面所有的内容拼接成「书的简介」
                elif content_item.find(self.content_flag) >= 0:
                    content_start = True
                    # print(content_start)
            else:
                content_text = content_item

        if selector.xpath('//div[@class="hanghang-shu-content-img"]/img/@src').extract_first().startswith('http://'):
            item['src_img'] = selector.xpath('//div[@class="hanghang-shu-content-img"]/img/@src').extract_first()
        else:
            item['src_img'] = self.base_url + selector.xpath('//div[@class="hanghang-shu-content-img"]/img/@src')[
                0].extract()
        item['book_img'] = (item['src_img'])[item['src_img'].rfind('/') + 1:len(item['src_img'])]
        item['content'] = content_text
        item['baidu_url'] = selector.xpath('//a[@class="downloads"]/@href').extract_first()
        item['src_url'] = response.url
        item['book_name'] = selector.xpath('//div[@class="hanghang-za-title"]/text()').extract_first()

        yield item
        # print(item)
        # print(selector.xpath('//div[@class="hanghang-za-title"]/text()').extract())
        # print("~~~~~~~~~~~~~~~~~~~~~")
        # 获取图片并保存
        # img_req = get(item['src_img'])
        # pic = open(self.file_path + item['book_img'], 'wb')
        # pic.write(img_req.content)
        # pic.close()
        pass