#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import re
import os
import urllib.request

file1 =  os.path.expanduser("~/cavi/cavi.txt")
file2 =  os.path.expanduser("~/cavi/cavi1.txt")
file3 =  os.path.expanduser("~/cavi/cavin.txt")
file4 =  os.path.expanduser("~/cavi/cavim2.txt")
aa = []
bb = []
ff = open (file1,'r') 
for i in ff.readlines():
    if 'null' in i :
        bb.append(i)
    else :
        aa.append(i)
ff.close()
cc = aa + bb
print (cc)
with open (file2,'w') as f:
    f.write(''.join(cc))
# list1 = []
# with open (file2,'r') as f:
#     for i in f.readlines():
#         i = i.strip()
#         ii = i.split("\t")
#         list1.append(ii)

# for i in list1:

#     j = i[1].upper().replace('_CAVI','')
#     print (j)
#     url = 'http://avdb.im/search/' + j
#     cc = urllib.request.urlopen(url).read().decode()
#     if '搜索没有结果' in cc :
#         nm = 'null'
#         pic = 'null'
#         s = i[:3]
#         s.append(nm)
#         s.append(pic)
#         li = '\t'.join(s) + '\n'
#         with open (file4,'a') as f :
#             f.write(li)

#         print ('失败了')
#         continue
#     rr = re.search("href=\"/movie/([a-z0-9_-]*?)\"",cc)
#     url2 = 'http://avdb.im/movie/'+ rr.group(1)
#     print (url2)
#     cc2 = urllib.request.urlopen(url2).read().decode()
#     nm =  re.search('<title>(.*?)</title>',cc2).group(1)
#     nm = nm.strip()
#     nm = nm.replace(' ','_')
#     wrong = '\/:*?"<>|　'
#     for k in wrong :            
#         nm = nm.replace(k,'')
#     nm = nm.replace('−_-_AvDB','')
#     print (nm)
#     try :
#         pic = re.search("http://.*?.jpg",cc2).group()
#     except:
#         pic = re.search("/upload.*?.jpg",cc2).group()
#         pic = 'http://avdb.im/' + pic
#     print (pic)
#     s = i[:3]
#     s.append(nm)
#     s.append(pic)
#     li = '\t'.join(s) + '\n'
#     with open (file4,'a') as f :
#         f.write(li)