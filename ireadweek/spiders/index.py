# -*- coding: utf-8 -*-
import scrapy
import  re
from ..items import IreadweekItem
from scrapy import Selector
from requests import get
import os



class IndexSpider(scrapy.Spider):
    name = 'index'
    allowed_domains = ['ireadweek.com']
    base_url = 'http://www.ireadweek.com'
    start_urls = ['http://www.ireadweek.com/index.php/index/1.html', 'http://www.ireadweek.com/index.php/index/2.html', 'http://www.ireadweek.com/index.php/index/3.html', 'http://www.ireadweek.com/index.php/index/4.html', 'http://www.ireadweek.com/index.php/index/5.html', 'http://www.ireadweek.com/index.php/index/6.html', 'http://www.ireadweek.com/index.php/index/7.html', 'http://www.ireadweek.com/index.php/index/8.html', 'http://www.ireadweek.com/index.php/index/9.html', 'http://www.ireadweek.com/index.php/index/10.html', 'http://www.ireadweek.com/index.php/index/11.html', 'http://www.ireadweek.com/index.php/index/12.html', 'http://www.ireadweek.com/index.php/index/13.html', 'http://www.ireadweek.com/index.php/index/14.html', 'http://www.ireadweek.com/index.php/index/15.html', 'http://www.ireadweek.com/index.php/index/16.html', 'http://www.ireadweek.com/index.php/index/17.html', 'http://www.ireadweek.com/index.php/index/18.html', 'http://www.ireadweek.com/index.php/index/19.html', 'http://www.ireadweek.com/index.php/index/20.html', 'http://www.ireadweek.com/index.php/index/21.html', 'http://www.ireadweek.com/index.php/index/22.html', 'http://www.ireadweek.com/index.php/index/23.html', 'http://www.ireadweek.com/index.php/index/24.html', 'http://www.ireadweek.com/index.php/index/25.html', 'http://www.ireadweek.com/index.php/index/26.html', 'http://www.ireadweek.com/index.php/index/27.html', 'http://www.ireadweek.com/index.php/index/28.html', 'http://www.ireadweek.com/index.php/index/29.html', 'http://www.ireadweek.com/index.php/index/30.html', 'http://www.ireadweek.com/index.php/index/31.html', 'http://www.ireadweek.com/index.php/index/32.html', 'http://www.ireadweek.com/index.php/index/33.html', 'http://www.ireadweek.com/index.php/index/34.html', 'http://www.ireadweek.com/index.php/index/35.html', 'http://www.ireadweek.com/index.php/index/36.html', 'http://www.ireadweek.com/index.php/index/37.html', 'http://www.ireadweek.com/index.php/index/38.html', 'http://www.ireadweek.com/index.php/index/39.html', 'http://www.ireadweek.com/index.php/index/40.html', 'http://www.ireadweek.com/index.php/index/41.html', 'http://www.ireadweek.com/index.php/index/42.html', 'http://www.ireadweek.com/index.php/index/43.html', 'http://www.ireadweek.com/index.php/index/44.html', 'http://www.ireadweek.com/index.php/index/45.html', 'http://www.ireadweek.com/index.php/index/46.html', 'http://www.ireadweek.com/index.php/index/47.html', 'http://www.ireadweek.com/index.php/index/48.html', 'http://www.ireadweek.com/index.php/index/49.html', 'http://www.ireadweek.com/index.php/index/50.html', 'http://www.ireadweek.com/index.php/index/51.html', 'http://www.ireadweek.com/index.php/index/52.html', 'http://www.ireadweek.com/index.php/index/53.html', 'http://www.ireadweek.com/index.php/index/54.html', 'http://www.ireadweek.com/index.php/index/55.html', 'http://www.ireadweek.com/index.php/index/56.html', 'http://www.ireadweek.com/index.php/index/57.html', 'http://www.ireadweek.com/index.php/index/58.html', 'http://www.ireadweek.com/index.php/index/59.html', 'http://www.ireadweek.com/index.php/index/60.html', 'http://www.ireadweek.com/index.php/index/61.html', 'http://www.ireadweek.com/index.php/index/62.html', 'http://www.ireadweek.com/index.php/index/63.html', 'http://www.ireadweek.com/index.php/index/64.html', 'http://www.ireadweek.com/index.php/index/65.html', 'http://www.ireadweek.com/index.php/index/66.html', 'http://www.ireadweek.com/index.php/index/67.html', 'http://www.ireadweek.com/index.php/index/68.html', 'http://www.ireadweek.com/index.php/index/69.html', 'http://www.ireadweek.com/index.php/index/70.html', 'http://www.ireadweek.com/index.php/index/71.html', 'http://www.ireadweek.com/index.php/index/72.html', 'http://www.ireadweek.com/index.php/index/73.html', 'http://www.ireadweek.com/index.php/index/74.html', 'http://www.ireadweek.com/index.php/index/75.html', 'http://www.ireadweek.com/index.php/index/76.html', 'http://www.ireadweek.com/index.php/index/77.html', 'http://www.ireadweek.com/index.php/index/78.html', 'http://www.ireadweek.com/index.php/index/79.html', 'http://www.ireadweek.com/index.php/index/80.html', 'http://www.ireadweek.com/index.php/index/81.html', 'http://www.ireadweek.com/index.php/index/82.html', 'http://www.ireadweek.com/index.php/index/83.html', 'http://www.ireadweek.com/index.php/index/84.html', 'http://www.ireadweek.com/index.php/index/85.html', 'http://www.ireadweek.com/index.php/index/86.html', 'http://www.ireadweek.com/index.php/index/87.html', 'http://www.ireadweek.com/index.php/index/88.html', 'http://www.ireadweek.com/index.php/index/89.html', 'http://www.ireadweek.com/index.php/index/90.html', 'http://www.ireadweek.com/index.php/index/91.html', 'http://www.ireadweek.com/index.php/index/92.html', 'http://www.ireadweek.com/index.php/index/93.html', 'http://www.ireadweek.com/index.php/index/94.html', 'http://www.ireadweek.com/index.php/index/95.html', 'http://www.ireadweek.com/index.php/index/96.html', 'http://www.ireadweek.com/index.php/index/97.html', 'http://www.ireadweek.com/index.php/index/98.html', 'http://www.ireadweek.com/index.php/index/99.html', 'http://www.ireadweek.com/index.php/index/100.html', 'http://www.ireadweek.com/index.php/index/101.html', 'http://www.ireadweek.com/index.php/index/102.html', 'http://www.ireadweek.com/index.php/index/103.html', 'http://www.ireadweek.com/index.php/index/104.html', 'http://www.ireadweek.com/index.php/index/105.html', 'http://www.ireadweek.com/index.php/index/106.html', 'http://www.ireadweek.com/index.php/index/107.html', 'http://www.ireadweek.com/index.php/index/108.html', 'http://www.ireadweek.com/index.php/index/109.html', 'http://www.ireadweek.com/index.php/index/110.html', 'http://www.ireadweek.com/index.php/index/111.html', 'http://www.ireadweek.com/index.php/index/112.html', 'http://www.ireadweek.com/index.php/index/113.html', 'http://www.ireadweek.com/index.php/index/114.html', 'http://www.ireadweek.com/index.php/index/115.html', 'http://www.ireadweek.com/index.php/index/116.html', 'http://www.ireadweek.com/index.php/index/117.html', 'http://www.ireadweek.com/index.php/index/118.html', 'http://www.ireadweek.com/index.php/index/119.html', 'http://www.ireadweek.com/index.php/index/120.html', 'http://www.ireadweek.com/index.php/index/121.html', 'http://www.ireadweek.com/index.php/index/122.html', 'http://www.ireadweek.com/index.php/index/123.html', 'http://www.ireadweek.com/index.php/index/124.html', 'http://www.ireadweek.com/index.php/index/125.html', 'http://www.ireadweek.com/index.php/index/126.html', 'http://www.ireadweek.com/index.php/index/127.html', 'http://www.ireadweek.com/index.php/index/128.html', 'http://www.ireadweek.com/index.php/index/129.html', 'http://www.ireadweek.com/index.php/index/130.html', 'http://www.ireadweek.com/index.php/index/131.html', 'http://www.ireadweek.com/index.php/index/132.html', 'http://www.ireadweek.com/index.php/index/133.html', 'http://www.ireadweek.com/index.php/index/134.html', 'http://www.ireadweek.com/index.php/index/135.html', 'http://www.ireadweek.com/index.php/index/136.html', 'http://www.ireadweek.com/index.php/index/137.html', 'http://www.ireadweek.com/index.php/index/138.html', 'http://www.ireadweek.com/index.php/index/139.html', 'http://www.ireadweek.com/index.php/index/140.html', 'http://www.ireadweek.com/index.php/index/141.html', 'http://www.ireadweek.com/index.php/index/142.html', 'http://www.ireadweek.com/index.php/index/143.html', 'http://www.ireadweek.com/index.php/index/144.html', 'http://www.ireadweek.com/index.php/index/145.html', 'http://www.ireadweek.com/index.php/index/146.html', 'http://www.ireadweek.com/index.php/index/147.html', 'http://www.ireadweek.com/index.php/index/148.html', 'http://www.ireadweek.com/index.php/index/149.html', 'http://www.ireadweek.com/index.php/index/150.html', 'http://www.ireadweek.com/index.php/index/151.html', 'http://www.ireadweek.com/index.php/index/152.html', 'http://www.ireadweek.com/index.php/index/153.html', 'http://www.ireadweek.com/index.php/index/154.html', 'http://www.ireadweek.com/index.php/index/155.html', 'http://www.ireadweek.com/index.php/index/156.html', 'http://www.ireadweek.com/index.php/index/157.html', 'http://www.ireadweek.com/index.php/index/158.html', 'http://www.ireadweek.com/index.php/index/159.html', 'http://www.ireadweek.com/index.php/index/160.html', 'http://www.ireadweek.com/index.php/index/161.html', 'http://www.ireadweek.com/index.php/index/162.html', 'http://www.ireadweek.com/index.php/index/163.html', 'http://www.ireadweek.com/index.php/index/164.html', 'http://www.ireadweek.com/index.php/index/165.html', 'http://www.ireadweek.com/index.php/index/166.html', 'http://www.ireadweek.com/index.php/index/167.html', 'http://www.ireadweek.com/index.php/index/168.html', 'http://www.ireadweek.com/index.php/index/169.html', 'http://www.ireadweek.com/index.php/index/170.html', 'http://www.ireadweek.com/index.php/index/171.html', 'http://www.ireadweek.com/index.php/index/172.html', 'http://www.ireadweek.com/index.php/index/173.html', 'http://www.ireadweek.com/index.php/index/174.html', 'http://www.ireadweek.com/index.php/index/175.html', 'http://www.ireadweek.com/index.php/index/176.html', 'http://www.ireadweek.com/index.php/index/177.html', 'http://www.ireadweek.com/index.php/index/178.html', 'http://www.ireadweek.com/index.php/index/179.html', 'http://www.ireadweek.com/index.php/index/180.html', 'http://www.ireadweek.com/index.php/index/181.html', 'http://www.ireadweek.com/index.php/index/182.html', 'http://www.ireadweek.com/index.php/index/183.html', 'http://www.ireadweek.com/index.php/index/184.html', 'http://www.ireadweek.com/index.php/index/185.html', 'http://www.ireadweek.com/index.php/index/186.html', 'http://www.ireadweek.com/index.php/index/187.html', 'http://www.ireadweek.com/index.php/index/188.html', 'http://www.ireadweek.com/index.php/index/189.html', 'http://www.ireadweek.com/index.php/index/190.html', 'http://www.ireadweek.com/index.php/index/191.html', 'http://www.ireadweek.com/index.php/index/192.html', 'http://www.ireadweek.com/index.php/index/193.html', 'http://www.ireadweek.com/index.php/index/194.html']

    # start_urls = ['http://www.ireadweek.com/index.php/index/1.html']
    author_flag = '作者：'
    classify_flag = '分类：'
    content_flag = '简介：'
    file_path = '/Users/chengfei/ireadweek/'

    def parse(self, response):
        # print(response.text)
        html = response.text
        # print(html)
        urls_list = re.findall(re.compile(r"/index.php/bookInfo/\d+.html"), html)
        # print(urls_list)
        full_urls_list = [self.base_url + url for url in urls_list]  # 完整列表
        # n = 1
        for url in full_urls_list:
            # print(full_urls_list)
            if url.find('8822.html') == -1 and url.find('1503.html') == -1:
                yield scrapy.Request(url, callback=self.parse_url)
        pass

    def parse_url(self, response):
        # print(response.text)
        item = IreadweekItem()
        selector = Selector(response)
        all_content = selector.xpath("//div[@class='hanghang-shu-content-font']")
        content_start = False
        content_text = ''
        for content_item in all_content.xpath("p/text()").extract():
            if not content_start:
                # 获取作者
                if content_item.find(self.author_flag) >= 0:
                    item['author'] = content_item[content_item.find(self.author_flag)+len(self.author_flag): len(content_item)]
                # 获取分类
                elif content_item.find(self.classify_flag) >= 0:
                    item['classify'] = content_item[
                                     content_item.find(self.classify_flag) + len(self.classify_flag): len(content_item)]
                # 获取简介，如果到达简介部分，后面所有的内容拼接成「书的简介」
                elif content_item.find(self.content_flag) >= 0:
                    content_start = True
                    # print(content_start)
            else:
                content_text = content_item


        if selector.xpath('//div[@class="hanghang-shu-content-img"]/img/@src')[0].extract().startswith('http://'):
            item['src_img'] = selector.xpath('//div[@class="hanghang-shu-content-img"]/img/@src')[0].extract()
        else:
            item['src_img'] = self.base_url+selector.xpath('//div[@class="hanghang-shu-content-img"]/img/@src')[0].extract()
        item['book_img'] = (item['src_img'])[item['src_img'].rfind('/')+1:len(item['src_img'])]
        item['content'] = content_text
        item['baidu_url'] = selector.xpath('//a[@class="downloads"]/@href').extract()
        item['src_url'] = response.url
        item['book_name'] = selector.xpath('//div[@class="hanghang-za-title"]/text()').extract()[0]
        # print(item)
        # print(selector.xpath('//div[@class="hanghang-za-title"]/text()').extract())
        # print("~~~~~~~~~~~~~~~~~~~~~")
        # 获取图片并保存
        img_req  = get(item['src_img'])
        pic = open(self.file_path + item['book_img'], 'wb')
        pic.write(img_req.content)
        pic.close()
        yield item


