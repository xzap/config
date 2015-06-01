#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import urllib.request
import re
import gzip
import os
import urllib.parse
import time
import pickle
# baseurl = '5.yao.cl'
baseurl = '1024diss.info'

headers ={
'Host': baseurl,
'Connection': 'keep-alive',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',
'Accept-Encoding': 'gzip,deflate,sdch',
'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
'Cookie': '227c9_lastfid=0; 227c9_lastvisit=0%091424438202%09%2Fread.php%3Ftid%3D1388398; CNZZDATA950900=cnzz_eid%3D1830932612-1424436522-http%253A%252F%252F'+baseurl+'%252F%26ntime%3D1424436522',
}

  
try :
    with open('old.pickle', 'rb') as f: 
        old = pickle.load(f)
except :
    old = []  
def doreg(code):
    params = {'regname':u'阴错阳差'.encode('gbk'),
        'regpwd':'1982628',
        'regpwdrepeat':'1982628',
        'regemail':'xzap@163.com',
        'invcode':code,
        'forward':'',
        'step':'2'
        }
    params = urllib.parse.urlencode(params)
    regurl = "http://%s/register.php" % baseurl
    req = urllib.request.Request(regurl,headers=headers,data=params.encode('gbk'))
    cc = urllib.request.urlopen(req).read()
    if cc.startswith(b'\x1f\x8b'):
	    cc = gzip.decompress(cc).decode('gbk')
    else :
	    cc = cc.decode('gbk')
    if cc.find(u'邀請碼錯誤')>-1:
        return 'incorrect'
    else:
        return 'found' 

def mask(mcode):
    logfile = os.path.expanduser('~/yaoqinglog.html')
    maskCount = 0
    chars= '0123456789abcdefghijklmnopqrstuvwxyz'
    for ch in mcode:
        if ch == '*':
            maskCount += 1
    if maskCount>2:
        print(u'暂时不能处理大于2个隐藏字符的邀请码')
        return
    if maskCount == 0:
        result = doreg(mcode)
        if result == 'found':
            print('%s found!' % (mcode))
            with open (logfile,'a') as x:
                x.write('%s found!\n' % (mcode))
            exit()
            return
        else:
            print('%s %s!' % (mcode,result))
            with open (logfile,'a') as x:
                x.write('%s %s!\n' % (mcode,result))
                    
    elif maskCount == 1: 
        for ch in chars:
            code = mcode.replace('*','%s')
            code = code % (ch)
            result = doreg(code)
            if result == 'found':
                print('%s found!' % (code))
                with open (logfile,'a') as x:
                    x.write('%s found!\n' % (code))  
                exit()
                return
            else:
                print('%s %s!' % (code,result))
                with open (logfile,'a') as x:
                    x.write('%s %s!\n' % (code,result))

    elif maskCount == 2:
        for ch1 in chars:
            for ch2 in chars:
                code = mcode.replace('*','%s')
                code = code % (ch1,ch2)
                result = doreg(code)
                if result == 'found':
                    print('%s found!' % (code))
                    with open (logfile,'a') as x:
                        x.write('%s found!\n' % (code))
                    exit()
                    return
                else:
                    print('%s %s!' % (code,result))
                    with open (logfile,'a') as x:
                        x.write('%s %s!\n' % (code,result))

def getyouke():
    url = 'http://' + baseurl + '/thread0806.php?fid=7'
    req = urllib.request.Request(url,headers=headers)
    cc = urllib.request.urlopen(req).read()
    if cc.startswith(b'\x1f\x8b'):
        cc = gzip.decompress(cc).decode('gbk')
    else :
        cc = cc.decode('gbk')
    pattern = re.compile("<h3><a href=\"(.*?)\" target=\"_blank\" id=\"\">(.*?)</a></h3",re.S)
    rr =re.findall (pattern,cc)
    a=[]
    for i in rr[9:]:
        if i[1] in old :
            continue
        # if "游客" in i[1]  or "福利" in i[1] :
        if "游客" in i[1] :  
            a.append(i)
    if a == [] :  
        print ('没找到游客福利')     
        return "null"
    if a[0][1] in old :
        
        print (old)
        print (a[0][1],'这个找过了')
        return
    old.append(a[0][1])
    with open('old.pickle', 'wb') as f: 
        pickle.dump(old, f) 
    print (a[0][1])
    curl = "http://%s/%s" % (baseurl,a[0][0])
    print (curl)
    creq = urllib.request.Request(curl,headers=headers)
    ccc = urllib.request.urlopen(creq).read()
    if ccc.startswith(b'\x1f\x8b'):
        ccc = gzip.decompress(ccc).decode('gbk')
    else :
        ccc = ccc.decode('gbk')
    pattern = re.compile("[^a-z0-9]([a-z0-9*]{16})[^a-z0-9]")
    crr =re.findall (pattern,ccc)
    if crr == [] :
        os.system('xdg-open %s' % curl)
    for i in crr :
        print(i)
        mask(i)
while 1:
    getyouke()
    now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print('将在1分钟后重试……',now)
    time.sleep (60)
