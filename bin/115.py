#!/usr/bin/env python

import hashlib
import urllib.request
import os,re
from http import cookiejar
import sys
import json
import gzip
import urllib.parse
import time
def gdecode(webPage, charset='UTF-8'):
    if webPage.startswith(b'\x1f\x8b'):
        return gzip.decompress(webPage).decode(charset)
    else:
        return webPage.decode(charset)

headers = {
    "Accept":"Accept: application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding":"text/html",
    "Accept-Language":"en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Referer":"http://m.115.com/",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 "\
        "(KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"}
cj = cookiejar.CookieJar()
opener = urllib.request.build_opener()
opener.add_handler(urllib.request.HTTPCookieProcessor(cj))
'''
ct:login
ac:logining
goto:http://115.com/
request_url:http://115.com/?ct=sso&user_id=3024177&ssostr=8DE6790197A1CF0FQHDGQN440N44FW9DWEWQ4MSN0GF9JNEDGHHGGQW1306577312A1&rsatime=1429602401&rsa=1cc0cad4ebc6bd296a22431e6e7e5cb8e21c7906&json=
'''                                                       

tt = str(int(time.time())).encode("utf-8")
sha = hashlib.sha1()

sha.update("xzap@163.com".encode("utf-8"))
sha.update("1982628".encode("utf-8"))
sha.update(tt)
print (sha.hexdigest())

p = hashlib.new("xzap@163.com")
# a = hashlib.new("1982628")
# t = hashlib.new(p + a).hexdigest()
# print (t)