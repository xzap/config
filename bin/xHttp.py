#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys
import gzip
import socket
import urllib.request, urllib.parse, urllib.error
import http.cookiejar

class xHttp:
    def __init__(self, timeout=10, addHeaders=True):
        socket.setdefaulttimeout(timeout)   # 设置超时时间
        self.__opener = urllib.request.build_opener()
        urllib.request.install_opener(self.__opener)
        if addHeaders: self.__addHeaders()

    def __error(self, e):
        '''错误处理'''
        print(e)

    def __addHeaders(self):
        '''添加默认的 headers.'''
        self.__opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'),
                                    ('Connection', 'keep-alive'),
                                    ('Cache-Control', 'no-cache'),
                                    ('Accept-Language:', 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'),
                                    ('Accept-Encoding', 'gzip, deflate'),
                                    ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]

    def __decode(self, webPage, charset):
        '''gzip解压，并根据指定的编码解码网页'''
        if webPage.startswith(b'\x1f\x8b'):
            return gzip.decompress(webPage).decode(charset)
        else:
            return webPage.decode(charset)

    def addCookiejar(self):
        '''为 self.__opener 添加 cookiejar handler。'''
        cj = http.cookiejar.CookieJar()
        self.__opener.add_handler(urllib.request.HTTPCookieProcessor(cj))

    def addProxy(self, host, type='http'):
        '''设置代理'''
        proxy = urllib.request.ProxyHandler({type: host})
        self.__opener.add_handler(proxy)

    def addAuth(self, url, user, pwd):
        '''添加认证'''
        pwdMsg = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        pwdMsg.add_password(None, url, user, pwd)
        auth = urllib.request.HTTPBasicAuthHandler(pwdMsg)
        self.__opener.add_handler(auth)

    def get(self, url, params={}, headers={}, charset='UTF-8'):
        '''HTTP GET 方法'''
        if params: url += '?' + urllib.parse.urlencode(params)
        request = urllib.request.Request(url)
        for k,v in headers.items(): request.add_header(k, v)    # 为特定的 request 添加指定的 headers

        try:
            response = urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:
            self.__error(e)
        else:
            return self.__decode(response.read(), charset)

    def post(self, url, params={}, headers={}, charset='UTF-8'):
        '''HTTP POST 方法'''
        params = urllib.parse.urlencode(params)
        request = urllib.request.Request(url, data=params.encode(charset))  # 带 data 参数的 request 被认为是 POST 方法。
        for k,v in headers.items(): request.add_header(k, v)

        try:
            response = urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:
            self.__error(e)
        else:
            return self.__decode(response.read(), charset)

    def download(self, url, savefile):
        '''下载文件或网页'''
        header_gzip = None

        for header in self.__opener.addheaders:     # 移除支持 gzip 压缩的 header
            if 'Accept-Encoding' in header:
                header_gzip = header
                self.__opener.addheaders.remove(header)

        __perLen = 0
        def reporthook(a, b, c):    # a:已经下载的数据大小; b:数据大小; c:远程文件大小;
            if c > 1000000:
                nonlocal __perLen
                per = (100.0 * a * b) / c
                if per>100: per=100
                per = '{:.2f}%'.format(per)
                print('\b'*__perLen, per, end='')     # 打印下载进度百分比
                sys.stdout.flush()
                __perLen = len(per)+1

        print('--> {}\t'.format(url), end='')
        try:
            urllib.request.urlretrieve(url, savefile, reporthook)   # reporthook 为回调钩子函数，用于显示下载进度
        except urllib.error.HTTPError as e:
            self.__error(e)
        finally:
            self.__opener.addheaders.append(header_gzip)
            print()