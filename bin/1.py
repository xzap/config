#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 

import urllib.request
import re


def pcurl(url,encode='gbk'):
	req = urllib.request.Request(url)
	content = urllib.request.urlopen(req).read().decode(encode)
	return content

def rre(part,content):
	re_part = re.compile(part,re.S)
	re_c = re.findall(re_part,content)
	return re_c

url = 'http://www.xici.net.co/nn/'
part = '([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})</td>.*?<td>([0-9]{2,4})</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?<td>(.*?)</td>'
for i in rre(part,pcurl(url,'utf-8')) :
	print ('("%s:%s","%s"),' % (i[0],i[1],i[2]))
