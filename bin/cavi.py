#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import urllib.request
import re
import gzip
import os
from http import cookiejar
import time
# reload(sys)
# sys.setdefaultencoding('utf-8')

cj = cookiejar.LWPCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
headers={
'Host': 'www.javlibrary.com',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',
'Referer': 'http://www.javlibrary.com/cn/',
'Accept-Encoding': 'gzip, deflate, sdch',
'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
'Cookie': '__cfduid=d998f7716df55a54ae8ebfa648d915c0f1430676748; timezone=-480; over18=18; __qca=P0-1247211407-1430676754045; HstCfa2142417=1430676754134; HstCmu2142417=1430676754134; __utma=45030847.412340292.1430676753.1430912204.1430925709.6; __utmb=45030847.3.10.1430925709; __utmc=45030847; __utmz=45030847.1430676753.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __atuvc=19%7C18; __atuvs=554a32419ab5b6d8000; HstCla2142417=1430925890463; HstPn2142417=3; HstPt2142417=32; HstCnv2142417=4; HstCns2142417=7',
'If-None-Match': 'W/"6b6cf50aed7ea0059591cf91acdc8b23"',
'If-Modified-Since': 'Wed, 06 May 2015 14:25:54 GMT',
}
opener.addheaders=[]
for v,k in headers.items():
    opener.addheaders.append((v,k))
# print (opener.addheaders)
file1 = os.path.expanduser("~/cavi2.txt")
# if os.path.exists(file1):os.remove(file1)
filec = open(file1,'r')
# for i in range(1,51):
#     print (i)
#     url = 'http://www.btspread.com/search/cavi/currentPage/%s' % i
#     # print (url)
#     cc = opener.open(url).read()
#     # print (cc)
#     cc = gzip.decompress(cc).decode('utf-8') 
#     rc = re.compile = ("http://www.btspread.com/magnet/detail/hash/([0-9A-Za-z]*)\" title=\"(.*?)\".*?class=\"files-size\">(.*?)<")
#     rr = re.findall (rc,cc)
#     print (rr)

#     for j in rr :
#         print (j[0]+"\t"+j[1])
#         mag = "magnet:?xt=urn:btih:" + j[0]
#         filec.write(mag+"\t"+j[1]+"\t"+j[2]+"\n")
#     time.sleep(5)
# filec.close()
rrs = []
for i in filec.readlines():
    i = i.strip()
    j = i.split('\t')
    rrs.append(j)
filec.close()
file2 = os.path.expanduser("~/cavi3.txt")
# if os.path.exists(file2):os.remove(file2)

for i in rrs:
    
 
    if i[4] != 'null' or  re.match('[0-9]+[-_]+[0-9]+',i[1])  :
        li = '\t'.join(i)+'\n'
        with open(file2,'a',encoding='utf-8') as f :
            f.write(li)
        continue

    j = i[1].upper().replace('_CAVI','')
    print (j)
    fanhao = j
    mag = i[0]
    big = i[2]
    s_url = 'http://www.javlibrary.com/cn/vl_searchbyid.php?keyword='+j
    try :
        gzip_c=opener.open(s_url).read()
        content=gzip.decompress(gzip_c).decode('utf8',"ignore")
        p = re.compile("<title>(.*)-", re.IGNORECASE)
        re_link=re.findall(p,content)
        nm = re_link[0]
        p2 = re.compile('http://pics.dmm.co.jp/mono/movie/adult/[0-9a-z_-]*/[0-9a-z_-]*.jpg')
        p22 = re.findall(p2,content)[0]
        print (p22)
        print (nm)
        if '识别码搜寻结果' in nm :
            p2 = re.compile("\?v=jav[a-zA-Z0-9]*", re.IGNORECASE)
            url2 = re.findall(p2,content)
            if url2 :
                url3 = "http://www.javlibrary.com/cn/"+url2[0]
                request = urllib.request.Request(url3,headers = headers)
                gzip_c=urllib.request.urlopen(request).read()
                content=gzip.decompress(gzip_c).decode('utf8',"ignore")
                p = re.compile("<title>(.*)-", re.IGNORECASE)
                re_link=re.findall(p,content)
                nm = re_link[0]
                p2 = re.compile('http://pics.dmm.co.jp/mono/movie/adult/[0-9a-z_-]*/[0-9a-z_-]*.jpg')
                p22 = re.findall(p2,content)[0]    

            else :
                print ("这个是真找不到")
                nm = 'null'
                p22 = 'null'
        print ('ok')
    except Exception as e:
        
        nm = 'null'
        p22 = 'null'
        print (e)
    nm = nm.strip()
    nm = nm.replace(' ','_')
    wrong = '\/:*?"<>|'
    for k in wrong :            
        nm = nm.replace(k,'')
    # li = "<li><div><img src=\"%s\" /></div><p><div><span style=\"margin: 0 10 0 0;\">%s</span><span>%s</span></div><div>%s</div></p><p>%s</p></div><hl />\n" % (p22,fanhao,big,nm,mag)
    s = i[0:3]
    s.append(nm)
    s.append(p22)
    # print(i)
    li = '\t'.join(s)+'\n'
    with open(file2,'a',encoding='utf-8') as f :
        f.write(li)
    time.sleep(2)



