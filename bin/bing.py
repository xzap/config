#!/usr/bin/env python3
# -*- coding: utf-8 -*-  
 
import urllib.request
import os
import time
import json
import xHttp

__perLen = 0
#ht = xHttp.xHttp()
#ht.addCookiejar()
#ht.get('https://www.bing.com')
def reporthook(a, b, c):    # a:已经下载的数据大小; b:数据大小; c:远程文件大小;
	if c > 1000000:
		global __perLen
		# nonlocal __perLen
		per = (100.0 * a * b) / c
		if per>100: per=100
		per = '{:.2f}%'.format(per)
		print('\b'*__perLen, per, end='')     # 打印下载进度百分比
		sys.stdout.flush()
		__perLen = len(per)+1

idx=19 #这里设置下载的天数，1就是今天。不过最多前面10几天的可以有。
downdir = os.path.expanduser("~/图片/bingwallpaper") 
if not os.path.exists(downdir):
	os.makedirs(downdir)  
choices = ('cn', 'jp', 'us') #这里就是设置国家了，不同国家有不同有一样。
#choices = ['us',]
baseurl = "http://www.bing.com"
ext = "_1920x1080.jpg"  #这里可以设置成1024x768或者1366 × 768等。
jpglist = {}
for j in range(idx):
	for i in choices :
		json_url = '%s/HPImageArchive.aspx?format=js&idx=%s&n=1&cc=%s' % (baseurl,j,i)
		print (json_url)
		url_json = urllib.request.urlopen(json_url).read().decode("utf-8")
		#url_json = ht.get(json_url)
		if url_json == "null" :
			print("it's null")
			continue
		jdata = json.loads(url_json)
		jpgurl = baseurl+jdata["images"][0]["urlbase"]+ext
		jpgtime = jdata["images"][0]["enddate"]
		jpglist[i+"_"+jpgtime]= jpgurl
print("_"*80)
for v , k in jpglist.items() :
	# print(v,k)
	jpgbase,jpgext = os.path.splitext(k)
	localfile = v + jpgext
	downfile = os.path.join(downdir,localfile)
	if os.path.exists(downfile) :
		print(downfile," 已经存在了，跳过。")
		continue
	
	print('--> {}下载到{}\t'.format(k,downfile), end='')
	try:
		urllib.request.urlretrieve(k,downfile,reporthook)

	except urllib.error.HTTPError as e:
		raise e
	finally:
		print()
