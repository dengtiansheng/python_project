#coding=utf-8
import logging
import requests
from collections import deque
from threading import Thread
class Crawler(object):
    def __init__(self):
        self.customeHeaders()
        self.pageSource = None
        self.unVisitedUrls = deque()
        self.visitedUrls = set()
        #self.threadPool =

    def prepareUrl(self):
        return None

    '''prepare url from a dict'''
    def prepareUrl(self,dictPath,processFunc):
        f = open(dictPath)
        for line in f.readlines():
            url = processFunc(line)
            self.unVisitedUrls.append(url)
    '''main function,start threads'''

    def fetch_all(self):
        url = self.unVisitedUrls.pop()
        print  url

    def fetch_url(self,url,retry=2,proxies=None):
        try:
            response = requests.get(url,headers=self.headers,timeout=10,proxies=proxies)
            if self._isResponseAvaliable(response):
                self.pageSource = response.text
                return self.pageSource
            else:
                print  "Page not available,url:%s,code:%d \n"%(url,response.status_code)
        except Exception,e:
            if retry > 0:
                return self.fetch_url(url,retry-1,proxies)
            else:
                print str(e)+"url:%s"%(url)
        return None

    def customeHeaders(self, **kargs):
        # 自定义header,防止被禁,某些情况如豆瓣,还需制定cookies,否则被ban
        # 使用参数传入可以覆盖默认值，或添加新参数，如cookies
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'gb18030,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive',
            # 设置Host会导致TooManyRedirects, 因为hostname不会随着原url跳转而更改,可不设置
            # 'Host':urlparse(self.url).hostname
            'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4',
        }
        self.headers.update(kargs)

    def _isResponseAvaliable(self, response):
        # 网页为200时再获取源码, 只选取html页面。
        if response.status_code == requests.codes.ok:
            return True
        return False

    # def congifLogger(logFile="logs", logLevel=5):
    #     '''配置logging的日志文件以及日志的记录等级'''
    #     LEVELS = {
    #         1: logging.CRITICAL,
    #         2: logging.ERROR,
    #         3: logging.WARNING,
    #         4: logging.INFO,
    #         5: logging.DEBUG,  # 数字最大记录最详细
    #     }
    #     formatter = logging.Formatter(
    #         '%(asctime)s %(threadName)s %(levelname)s %(message)s')
    #     try:
    #         fileHandler = logging.FileHandler(logFile)
    #     except IOError, e:
    #         return False
    #     else:
    #         fileHandler.setFormatter(formatter)
    #         logger.addHandler(fileHandler)
    #         logger.setLevel(LEVELS.get(logLevel))
    #         return True
