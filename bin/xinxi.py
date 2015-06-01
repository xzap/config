#!/usr/bin/env python
# coding:utf-8

import os
import sys
import re
import urllib.request
from http import cookiejar

def uniq(ll):
    new = []
    for i in ll:
        if i not in new :
            new.append(i)
    return new
cj = cookiejar.CookieJar()
opener = urllib.request.build_opener()
opener.add_handler(urllib.request.HTTPCookieProcessor(cj))



header = {
'Host': 'www.xzjy.com.cn',
'Connection': 'keep-alive',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36',
'Referer': 'http://www.xzjy.com.cn/Special_Newsxian.asp?SpecialID=14&typeID=4&page=7',
'Accept-Encoding': 'gzip, deflate, sdch',
'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
'Cookie': 'ASPSESSIONIDAADBCDQB=FGHMHKPDOCDMLBAAGABHMOMI; Forcast2004%2D0001=ViewUrl=%2FReadNews%2Easp%3FNewsID%3D8083; _gscu_1143676518=27688582smyeq516; _gscs_1143676518=27688582fiiew116|pv:44; _gscbrs_1143676518=1',
}
for v,k in header.items():
    print (v,k)
    opener.addheaders.append((v, k))

urllib.request.install_opener(opener)
# r_part = re.compile('href="ReadNews.asp?NewsID=[0-9]*" target="_blank" title="[^"]*">')
r_part = re.compile('href="(ReadNews.asp\?NewsID=[0-9]*)" target=_blank title="([^"]*)"')
r_part2 = re.compile('down.asp\?FileName=doc/[0-9]*-[0-9]*/[0-9]*.doc')


# down.asp?FileName=doc/2013-6/20136417957662.doc"
url = "http://www.xzjy.com.cn/Special_Newsxian.asp?SpecialID=14&typeID=4&page=7"
cc = urllib.request.urlopen(url).read().decode('gbk')

rr = re.findall(r_part,cc)
for i in uniq(rr)[3:]:
    print (i)
    url2 = "http://www.xzjy.com.cn/"+i[0]
    cc2 = urllib.request.urlopen(url2).read().decode('gbk')
    url3 = re.findall(r_part2,cc2)
    print (url3)
    if url3 :
        url5 =  'http://www.xzjy.com.cn/'+url3[0]
        ff = i[1]+".doc"
        print (url5,ff)
        urllib.request.urlretrieve(url5,ff)