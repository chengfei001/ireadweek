from requests import request,post
from json import loads
import  re
import  logging
from  bson import ObjectId
from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)

db_book = client.ireadweek.book
db_book_download_error = client.ireadweek.book_download_error



#正则表达式获取资源文件的重要信息
res_content = r'"app_id":"(\d*)".*"path":"([^"]*)".*"uk":(\d*).*"bdstoken":"(\w*)".*"shareid":(\d*)'  # 正则，获取参数值
#本地文件路径
filename = '/Users/chengfei/Downloads/baidu_download.txt'
path = '/'


class baiduPanSpider:
    def __init__(self):
        self.parameter = re.compile(res_content)
        self.path = '/'
        self.app_id = ''
        self.uk = ''
        self.bdstoken = ''
        self.shareid = ''
        self.headers = {
            'Host': 'pan.baidu.com',
            'User-Agent': 'User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0',
            'Accept': 'Accept=application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'Accept-Language=zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://pan.baidu.com/s/1bp0csmN',
            #cookie需要从浏览器登录后获取
            'Cookie': 'BAIDUID=8EABBBCF21E67405C1A2985ED1DC201B:FG=1; BIDUPSID=8EABBBCF21E67405C1A2985ED1DC201B; PSTM=1518330302; H_PS_PSSID=25639_1465_21109_20927; FP_UID=474d6207aaf0ffc98bd86f36f3c00fdd; pan_login_way=1; PANWEB=1; SCRC=29471bba3231478b98e86b777fcb931c; STOKEN=a8b1c76b55f0553021184587223801762c88e8839be8ab4f0e27691513319e7e; PANPSC=12604585720508035519%3A9qIJoSpryQ%2Fb41ZnUGXO%2BMxDaFs%2FKMrufnkgCRPBFD%2Bqv5jBm4hVt4M6La9EbgvRk3U9gPuxnU6PebNTXTLIzeckY2sOTxob9i4CW8ceHnrqPo4uQmxPcVfUDd9arCIiYTASXnFzAgG1T%2BAf1Zi%2BmWNtiaXV6jA2rsgnNL%2BLYct9tn9thbnTpv7IiW4JizVanZlv3sbf6BI%3D; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1518330542; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1518330617; cflag=15%3A3; BDUSS=2E2b05pMU91SVAybHR2ZDhUckRmdFZaZDlGNU9jaEY3QXJpdTNDUzJmSDNiNmRhQVFBQUFBJCQAAAAAAAAAAAEAAACZxAMAY2hlbmdmZWkwMDEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPfif1r34n9aZ',
            # 'Cookie': 'BAIDUID=D32E0E6A74B4E4C441C9F738F621367F:FG=1; PANWEB=1; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1509008858,1509347006,1509347062; cflag=15%3A3; FP_UID=49f66836d766350e8883279c0479925a; BDUSS=9Dd0p1aFo2b0N0UkRxUEszUFJrckNuVENYc3R6SWFmTXkyZGJ1eHRJNU5OQmxhSVFBQUFBJCQAAAAAAAAAAAEAAACZxAMAY2hlbmdmZWkwMDEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE2n8VlNp~FZMG; STOKEN=f462ded76da2ea1e9bf4a766b686670cd65740b84d7f41b6ec088751f8bc19f1; SCRC=a8095d2ab2d97437660899ad204b5a9c; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1509422353; PANPSC=12306614851535711420%3A9qIJoSpryQ%2Fb41ZnUGXO%2BMxDaFs%2FKMrufnkgCRPBFD%2Bqv5jBm4hVt4M6La9EbgvRTo4X8eRImYrkTnVbWpsideckY2sOTxob9i4CW8ceHnrqPo4uQmxPcVfUDd9arCIiYTASXnFzAgG1T%2BAf1Zi%2BmWNtiaXV6jA2rsgnNL%2BLYct9tn9thbnTpv7IiW4JizVanZlv3sbf6BI%3D',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0'
        }

    def run(self):
        books = db_book.find({})
        # books = db_book.find({'_id': ObjectId('5a7c007e8ce813133b4fdadb')})
        i = 0
        for book_item in books:
            i = i + 1
            print(str(book_item['_id']) + ' ' + str(i) + '.' + book_item['book_name'] + ' ' + book_item['baidu_url'])
            self.get_source_page(url=book_item['baidu_url'])
            self.save_as_to_mybaidu()

        pass

    # 获取共享资源页面
    def get_source_page(self, url):
        try:
            url = url.replace('http:/', 'https:/')

            response = request(method='get', url=url, headers=self.headers)

            # 转换编码为utf-8
            content = response.text.encode('ISO-8859-1').decode('utf-8')
            parameterValue = self.parameter.findall(content)
            self.app_id = parameterValue[0][0]
            self.path = parameterValue[0][1]
            self.uk = parameterValue[0][2]
            self.bdstoken = parameterValue[0][3]
            self.shareid = parameterValue[0][4]

        except Exception as e:
            logging.error('Error in 「get_source_page」:', str(e))
            item = {'baidu_url':url}
            db_book_download_error.insert(item)
        pass

    # 另存到我的百度云盘，headers中cookie中是另存的用户信息
    def save_as_to_mybaidu(self):
        url_post = 'https://pan.baidu.com/share/transfer?shareid=' + self.shareid + '&from=' + self.uk + '&ondup=newcopy&async=1&bdstoken=' + self.bdstoken + '&channel=chunlei&clienttype=0&web=1&app_id=' + self.app_id + '&logid=MTUwOTM0NzA4MDA5MjAuMzc5MjgwNzI0ODg3Mzc5Mg=='
        payload = 'filelist=%5B%22' + self.path + '%22%5D&path=/my_book/'  # 资源名称与要保存的路径 %5B%22=【，%22%5D=】
        try:
            response = post(url=url_post, headers=self.headers, data=payload)

            result = loads(response.text)
            logging.error(result)
            tag = result['errno']
            if tag == 0:
                logging.info(result['info'][0]['path'])
            else:
                logging.error(result)
        except Exception as e:
            item = {'payload': payload }
            db_book_download_error.insert(item)
            logging.error('Error in [addToDisk]:', str(e))


if __name__ == '__main__':
    save_as = baiduPanSpider()
    save_as.run()