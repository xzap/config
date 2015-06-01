#!/usr/bin/env python3
# encoding: UTF-8

import time
import sys
import gzip
import socket
import urllib.request, urllib.parse, urllib.error
from http import cookiejar
import re
import json
import os
import random

class baidupan(object):
    def __init__(self, username,password,timeout=10, addHeaders=True,downdir='/data/baidupan'):
        socket.setdefaulttimeout(timeout)   # 设置超时时间
        self.cookiefile = os.path.join(os.path.expanduser('~'), '.baidupan.cookies')
        self.cj = cookiejar.MozillaCookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))
        urllib.request.install_opener(self.opener)
        #if addHeaders: self.addHeaders()
        self.opener.addheaders =[]
        self.opener.addheaders.append(('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'))
        self.username = username
        self.password = password
        self.downdir = downdir
        self.time = "%.3f".replace('.','') % time.time()
        self.check_url = 'https://passport.baidu.com/v2/api/?logincheck&callback=bdPass.api.login._needCodestring' \
                          'CheckCallback&tpl=mn&charset=utf-8&index=0' \
                          '&username={self.username}&time={self.time}'.format(self=self)
        self.token_url = 'https://passport.baidu.com/v2/api/?getapi&class=login&tpl=mn&tangram=true'
        self.post_url = 'https://passport.baidu.com/v2/api/?login'

        if os.path.exists(self.cookiefile):   
            self.loadcookie()         
            self.chechklogin()
        else :
            self.login()

    def cprint(self,text,color="rand"):
        # colordict ={"Black":"30","Red":"31","Green":"32","Yellow":"33","Blue":"34","Purple":"35","Cyan":"36","White":"37"}
        colordict ={"Red":"31","Green":"32","Yellow":"33","Blue":"34","Purple":"35","Cyan":"36","White":"37"}   

        if color == "rand" :
            cc = random.choice(list(colordict.values()))
        else :
            cc = colordict[color]
        res = '\x1b[%sm' % cc + str(text) + '\x1b[0m' 
        print(res)  

    def chechklogin(self):
        cc = self.get('http://www.baidu.com')
        if 'xzap' in cc :      
            self.cprint ('登录成功')
            return True
        else:
        
            self.cprint ('登录失败')
            self.login()
            return False

    def error(self, e):
        '''错误处理'''
        print(e)

    def savecookie (self):
        self.cj.save(self.cookiefile,True,True)

    def loadcookie (self) :
        self.cj.load(self.cookiefile,True,True)
    
    def addHeaders(self):
        '''添加默认的 headers.'''
        self.opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'),
                                    #('Connection', 'keep-alive'),
                                    ##('Cache-Control', 'no-cache'),
                                    #('Accept-Language:', 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'),
                                    #('Accept-Encoding', 'gzip, deflate'),
                                    #('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
                                    ]

    def decode(self, webPage, charset):
        '''gzip解压，并根据指定的编码解码网页'''
        if webPage.startswith(b'\x1f\x8b'):
            return gzip.decompress(webPage).decode(charset)
        else:
            return webPage.decode(charset)


    def get(self, url, params={}, headers={}, charset='UTF-8'):
        '''HTTP GET 方法'''
        if params: url += '?' + urllib.parse.urlencode(params)
        request = urllib.request.Request(url)
        for k,v in headers.items(): request.add_header(k, v)    # 为特定的 request 添加指定的 headers

        try:
            response = urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:
            self.error(e)
        else:
            return self.decode(response.read(), charset)

    def post(self, url, params={}, headers={}, charset='UTF-8'):
        '''HTTP POST 方法'''
        params = urllib.parse.urlencode(params)
        request = urllib.request.Request(url, data=params.encode(charset))  # 带 data 参数的 request 被认为是 POST 方法。
        for k,v in headers.items(): request.add_header(k, v)

        try:
            response = urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:
            self.error(e)
        else:
            return self.decode(response.read(), charset)

    def getcookie(self,cookname):
        for cook in self.cj:
            if cook.name == cookname :
                return cook.value
            else :
                return False

    def gettoken(self) :
        url = 'http://www.baidu.com'
        self.get(url)
        baiduid = self.getcookie('BAIDUID')
        #print (baiduid)
        cc = self.get(self.check_url)
        cc = self.get(self.token_url)
        rr = re.search("token='(\w*)'",cc)
        return rr.group(1)

    def login(self):       

        post_data = {
            'ppui_logintime': '9379',
            'charset': 'utf-8', 
            'codestring': '',
            'token': self.gettoken(),
            'isPhone': 'false', 
            'index': '0', 
            'u': '', 
            'safeflg': 0,
            'staticpage': 'http://www.baidu.com/cache/user/html/jump.html', 
            'loginType': '1', 
            'tpl': 'mn',
            'callback': 'parent.bdPass.api.login._postCallback', 
            'username': self.username,
            'password': self.password, 
            'verifycode': '', 
            'mem_pass': 'on',
            'tt':self.time
        }
        cc = self.post(self.post_url,params=post_data)
        self.savecookie()


if __name__ == '__main__':

    #url = 'http://pan.baidu.com/s/1i35W9Zv'
    s = baidupan("27873983@qq.com",'jixinyan2008')
    s.login()
    #s.gettoken()
