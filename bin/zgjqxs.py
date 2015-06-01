#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
import urllib.request
import os
import re
import sys
import time
import json
bookid = 505430
id1 = 4
id2 = 30
num = 0



baseurl = 'http://m.ac.qq.com/View/mGetPicHash?id='+ str(bookid) +'&cid='
path = os.path.expanduser("~/海贼王")
if not os.path.exists(path):
        os.makedirs(path)
def reporthook(blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
                percent = readsofar * 1e2 / totalsize
                time2 = time.time() - time1
                pp = readsofar / time2 / 1024
                if totalsize < 1024 :
                        tt = "%.2fB" % totalsize
                elif totalsize < 1024*1024 :
                        tt = "%.2fK" % (totalsize / 1024)
                elif totalsize < 1024*1024*1024 :
                        tt = "%.2fM" % (totalsize/1024/1024)
                elif totalsize < 1024*1024*1024*1024 :
                        tt = "%.2fG" % (totalsize/1024/1024/1024)
                else :
                        tt = "%.2fT" % (totalsize/1024/1024/1024/1024)
                s = "\r%5.1f%% %*d / %d   %s     %.2fKbps" % (percent, len(str(totalsize)), readsofar, totalsize,tt,pp)
                sys.stderr.write(s)

for i in range(707,800):
        url = baseurl + str(i)
        cc = urllib.request.urlopen(url).read().decode("utf-8")
        aa = re.findall("\"pid\":[0-9]*",cc)
        bb = [x.split(":")[1] for x in aa]
        for j in bb :
                num += 1
                if num < 10 :
                        jpg = "000" + str(num) + ".jpg"
                elif num < 100 :
                        jpg = "00" + str(num) + ".jpg"
                elif num < 1000 :
                        jpg = "0" + str(num) + ".jpg"                        
                else :
                        jpg = str(num) + ".jpg"
                jpgfile = os.path.join(path,jpg)
                uin = bookid + i + int(j) 
                jpgurl = 'http://ac.tc.qq.com/store_file_download?buid=15017&uin=%s&dir_path=/mif800/%s/%s/%s/%s/&name=%s.mif2' % (uin,id1,id2,bookid,i,j)
                print ("="*80)
                print (num)
                print (jpgurl)
                time1 = time.time()
                urllib.request.urlretrieve(jpgurl,jpgfile,reporthook)
                print()
