#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

import xHttp 
import re
import os

path = os.path.expanduser("~/115lb.html")
http = xHttp.xHttp()
print(1)
url = 'http://www.xunleicili.com/115/index.html'
cc = http.get(url,charset='GBK')
rr = re.findall ('<li>.*</li>',cc)

# print (rr)
for i in range(2,4):
	print(i)
	url = 'http://www.xunleicili.com/115/'+str(i)+'.html'
	cc = http.get(url,charset='GBK')
	rr.extend(re.findall ('<li>.*</li>',cc))
for j in rr :
	if '免费看片' in j : rr.remove(j)
with open(path,'w') as x :
	for i in rr:
		x.write(i+"\n")