#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import urllib.request
import re
import gzip

def pcurl(url):
	req = urllib.request.Request(url)
	content = urllib.request.urlopen(req).read().decode('gbk')
	return content

def rre(part,content):
	re_part = re.compile(part)
	re_c = re.findall(re_part,content)
	return re_c

url = input('输入网址：').strip()
try :
	for i in rre('(ed2k|ftp)(://[^#"]*)',pcurl(url)) :
		print ("".join(i))
except:
	print ('输入无效')

