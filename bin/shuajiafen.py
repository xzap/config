#!/bin/env python3
import urllib.request
import urllib.parse
import os,re
from http import cookiejar
import sys
import time
import random
try :
	username = str(input("请输入用户名：")).replace(" ","").replace("　","")
	if len(username)<6:
		print("用户名不正确")
		exit()
	password = str(input("请输入密码：")).replace(" ","").replace("　","")
	if len(password)<6:
		print("密码不正确")
		exit()

except :
	print ("输入错误")
	exit()
print ("您输入的用户名是："+username + "  密码是："+ password)

def login(user,passwd):
	cj = cookiejar.CookieJar()
	opener = urllib.request.build_opener()
	opener.add_handler(urllib.request.HTTPCookieProcessor(cj))
	urllib.request.install_opener(opener)
	cj.clear()
	login_url = 'http://jcpt.zjer.cn/base/loginUnified.jspx?type=2&callBack=www.zjer.cn:80/login_unify.jspx&productTicket=10&returnUrl=http://www.zjer.cn/channel/uhome/index.jhtml?' 
	params_org={"username":user,"password":passwd,"flag":1}
	params = urllib.parse.urlencode(params_org)
	req = urllib.request.Request(login_url,data=params.encode("utf-8"))
	try :

		cc = urllib.request.urlopen(req).read().decode()
		urlcheck = "http://www.zjer.cn/login_status.jspx?random="+str(random.random())+"&address=http://www.zjer.cn/channel/uhome/index.jhtml?&type=2&usertype=2"
		cc2 = urllib.request.urlopen(urlcheck).read().decode()
		if "欢迎您" in cc2 :
			sub = re.findall("欢迎您:(.*)",cc2)
			name = sub[0].strip()
			print (name + " 登录成功！")
		else :
			print ("登录失败，请检查用户名和密码")
			exit()
	except Exception as e:
		print (e)

def get_last():
	url_last = "http://jskj.zjer.cn/iframe.do?method=moreLatestResource"
	cc_last = urllib.request.urlopen(url_last).read().decode("utf-8")
	# http://www.zjer.cn/resource/view.jspx?id=407985
	comp = re.compile('view.jspx\?id=([0-9]*)',re.IGNORECASE)	
	rr = re.findall(comp,cc_last)
	return (rr)

def down(s_id):
	try :
		url2 = "http://www.zjer.cn/download/check.jspx?id="+str(s_id)
		print (url2)
		url3 = "http://www.zjer.cn/resource/download.jspx?id="+str(s_id)+"&classifyId="
		url4 = "http://jskj.zjer.cn/my.do?method=main"
		cc2 = urllib.request.urlopen(url2)
		cc3 = urllib.request.urlopen(url3)
		cc4 = urllib.request.urlopen(url4)
		print("done !")
	except :
		print("fail !")



num =1 
for i in get_last() :
	try:
		login(username,password)
		print ("下载第 "+str(num)+" 个,id是"+str(i)+"",end="  ")
		down(i)
		num+=1
	except Exception as e:
		print(e)
		continue
	if num > 10 :
		break
	# print ("现在时间是："+time.strftime("%X")+" 五分钟后继续下载，请等待……")
	# time.sleep(310)

for j in range(5):
	print (j+1)
	print ("现在时间是："+time.strftime("%X")+" 一小时后继续登录，请等待……")
	login(username,password)
	time.sleep(3660)