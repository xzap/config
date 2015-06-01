#!/bin/env python3

import os,re
from http import cookiejar
import sys
import urllib.request
import urllib.parse
import time

url = 'http://jcpt.zjer.cn/base/loginUnified.jspx?type=2&callBack=www.zjer.cn:80/login_unify.jspx&productTicket=10&returnUrl=http://www.zjer.cn/channel/uhome/index.jhtml?' 
cj = cookiejar.CookieJar()
opener = urllib.request.build_opener()
opener.add_handler(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
params={"username":"jgp280017",
"password":"280017",
"flag":1}
params = urllib.parse.urlencode(params)
req = urllib.request.Request(url,data=params.encode("utf-8"))
cc = urllib.request.urlopen(req).read().decode("utf-8")



urlmy = "http://jskj.zjer.cn/my.do?method=main"
ccmy = urllib.request.urlopen(urlmy)


url4 = "http://jskj.zjer.cn/iframe.do?method=moreLatestResource"
cc4 = urllib.request.urlopen(url4).read().decode("utf-8")
# http://www.zjer.cn/resource/view.jspx?id=407985
comp = re.compile('view.jspx\?id=([0-9]*)',re.IGNORECASE)

rr = re.findall(comp,cc4)

for i in range(10):
	
	cc = urllib.request.urlopen(req).read().decode("utf-8")
	url2 = "http://www.zjer.cn/download/check.jspx?id="+str(rr[i])
	url3 = "http://www.zjer.cn/resource/download.jspx?id="+str(rr[i])+"&classifyId="
	url4 = "http://jskj.zjer.cn/my.do?method=main"
	cc2 = urllib.request.urlopen(url2)
	cc3 = urllib.request.urlopen(url3)
	cc4 = urllib.request.urlopen(url4)
	time.sleep(300)



