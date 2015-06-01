#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 
"""
下载喜马拉雅上节目的一个小脚本
两种模式：
1、下载单曲，直接在脚本后面参数形式加上节目id，下载单个节目。可以加多个，用空格分隔。
	如：页面链接为“http://www.ximalaya.com/#/2629577/sound/1127462”
	其中的“1127462”就是节目id。
2、下载当前页面的所有节目，直接运行脚本，在提示符号后直接粘贴页面地址即可。
 
Coding by xzap
2014年5月26日
"""
import urllib.request
import json
import os
import re
import sys
import time
 
baseurl = "http://fdfs.xmcdn.com/"
num = 0
ok = 0
total = 0
time1 =time.time()
path = os.path.expanduser("~/ximalaya")
if not os.path.exists(path):
	os.makedirs(path)
opener = urllib.request.build_opener()
opener.addheaders.append(('Referer', 'http://www.ximalaya.com'))
opener.addheaders.append(('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36'))
urllib.request.install_opener(opener)
url = 'http://www.ximalaya.com/9216785/album/257813'
cc = urllib.request.urlopen(url).read().decode("utf-8")
chaxun=re.findall('sound_id="([0-9]*)"',cc)
for i in chaxun[:-40]:
	
	url2 = "http://www.ximalaya.com/tracks/" + i + ".json"
	jc = urllib.request.urlopen(url2).read().decode("utf-8")

	data = json.loads(jc)
	album = data["album_title"]
	title = data["title"]
	mp3url = baseurl + data["play_path"]
	formatted_created = data["formatted_created_at"].split()[0].replace("日","")
	fc1,fc2 = formatted_created.split("月")
	if fc1 >3 :
		year = 2014
	else :
		year = 2015
	if len(fc1) == 1 :
		fc1 = "0" + fc1
	if len(fc2) == 1 :
		fc2 = "0" + fc2
	fc = year+fc1 + fc2 + "_" + title
	ext = os.path.splitext(mp3url)[1]
	filename = fc + ext 
	dath = os.path.join('/home/xzap/ximala',album)
	cc = '''%s
  dir=%s
  out=%s
  header=Cookie: appver=1.7.6
  continue=true
  max-connection-per-server=5
  split=10
  parameterized-uri=true

''' % (mp3url,dath,filename)
	print (cc)