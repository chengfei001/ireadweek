from pymongo import MongoClient
from requests import get
import os
import time
from  bson.objectid import ObjectId

from ireadweek.items import IreadweekItem

client = MongoClient(host={'localhost'}, port=27017)
db = client.kaoshibaodian_base
db_question_item = db.QuestionItem

class DownLoadImg:
    def __init__(self):
        self.file_path = '/Users/chengfei/ireadweek'
        self.client = MongoClient(host='localhost', port=27017)
        self.db = self.client.ireadweek
        self.book = self.db.book
        self.i = 0
        self.headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
}

    # def download_img(self):
    #     book_itmes = self.book.find({})
        book_itmes = self.book.find({'_id': {'$gte': ObjectId('5a7bf59a8ce81312be57c3ee')}})

        x = 0
        for book in book_itmes:
            x += 1
            print(str(book['_id']) + ' '+str(x)+'.'+book['book_name']+' '+book['src_img'])
            if book['src_img'] !=  'http://www.ireadweek.com':
                self.get_img(book['book_img'], book['src_img'])
        pass
    def get_img(self,img,url):
        path = self.file_path
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)

        if self.i <= 50:
            self.i += 1
        else:
            self.i = 0
            time.sleep(5)
        response = get(url=url, headers=self.headers)

        pic = open(path + '/' + img, 'wb')
        pic.write(response.content)
        pic.close()
    def run(self):
        self.download_img()

if __name__ == '__main__':
    download = DownLoadImg()
    download.run()