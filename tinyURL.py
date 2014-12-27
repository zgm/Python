#!/usr/bin/env python
# -*- coding:GBK

import urllib2
import requests
import time
import json
import logging
import hashlib


def here():
    print('PrimeMusic')


class Crawler(object):
    def __init__(self):
        self._timeout = 60
        requests.adapters.DEFAULT_RETRIES = 3
        #self.logger = logging.getLogger('novel.officical.crawler')
        self.err = logging.getLogger('err.official.crawler')


    def get(self, src):
        try:
            r = requests.get(src, timeout = self._timeout)
            if r.status_code != requests.codes.ok:
                self.err.warning('[path: {0}, err: {1}]'.format(src, r.status_code))
                return False
            return r.text
            #result = r.json()
            #return result
        except Exception as e:
            self.err.warning('[path: {0}, err: {1}]'.format(src, e))
            return False


    def get_content(self, src):
        try:
            r = urllib2.urlopen(src, timeout=self._timeout)
            if r.getcode() != 200:
                self.err.warning('[path: {0}, err: {1}]'.format(src, r.getcode()))
                return False
            return r
            #result = json.loads(r.read())
            #return result
        except Exception as e:
            self.err.warning('[path: {0}, err: {1}]'.format(src, e))
            return False


class tinyURL(object):
    def __init__(self):
        self.url_list = []
        self.decode_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    def get_id(self, c):
        if 'a'<=c and c<='z':
            return ord(c)-ord('a')
        if 'A'<=c and c<='Z':
            return ord(c)-ord('A')+26
        if '0'<=c and c<='9':
            return ord(c)-ord('0')+52
        return 0

    def encode(self, id):
        url = ''
        for i in range(6):
            url += self.decode_list[id%62]
            id /= 62
        return url[::-1]

    def decode(self, url):
        id = 0
        for i in range(6):
            id = id*62 + self.get_id(url[i])
        return id

    def get_tinyURL(self, url):
        self.url_list.append(url)
        id = len(self.url_list)-1
        return 'http://tinyURL/' + self.encode(id)

    def get_originURL(self,url):
        return self.url_list[self.decode(url[-6:])]




if __name__ == '__main__':
    urls = ['http://poj.org/problem?id=4054',
           'http://www.baidu.com',
           'http://www.itwhy.org',
           'http://www.zhidaow.com',
           'http://www.google.com'
    ]

    tinyURL = tinyURL()
    for url in urls:
        #md5 = hashlib.md5()
        #md5.update(url)
        #print md5.digest(), len(md5.digest())
        #for r in md5.digest():
        #    print ord(r),
        tiny = tinyURL.get_tinyURL(url)
        print url, tiny, tinyURL.get_originURL(tiny)


    #Crawler = Crawler()
    #print Crawler.get(url[0])
    #print Crawler.get_content(url[0])


    here()
