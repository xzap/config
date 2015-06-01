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
 
def reporthook(blocknum, blocksize, totalsize):
	readsofar = blocknum * blocksize
	if totalsize > 0:
		percent = readsofar * 1e2 / totalsize
		time2 = time.time() - time1
		pp = readsofar / time2 / 1024
		tt = totalsize / 1024 /1024
		s = "\r%5.1f%% %*d / %d   %.2fM      %.2fKbps" % (percent, len(str(totalsize)), readsofar, totalsize,tt,pp)
		sys.stderr.write(s)
 
def down(soundid,year="") :
	global total
	global num
	num += 1
	url = "http://www.ximalaya.com/tracks/" + soundid + ".json"
	jc = urllib.request.urlopen(url).read().decode("utf-8")
	if jc == "null" :
		print("="*80)
		print (num,"/",total)
		print (soundid,"is a wrong sound id")
		return
	data = json.loads(jc)
	album = data["album_title"]
	title = data["title"]
	mp3url = baseurl + data["play_path"]
	formatted_created = data["formatted_created_at"].split()[0].replace("日","")
	fc1,fc2 = formatted_created.split("月")   
	if len(fc1) == 1 :
		fc1 = "0" + fc1
	if len(fc2) == 1 :
		fc2 = "0" + fc2
	fc = year + fc1 + fc2 + "_" + title
	ext = os.path.splitext(mp3url)[1]
	filename = fc + ext 
	dpath = os.path.join(path,album)
	if not os.path.exists(dpath):
		os.makedirs(dpath)
	downfile = os.path.join(dpath,filename)
	print("="*80)
	print (num,"/",total)
	#print (title,"downloading......")
	print ("URL:", mp3url)
	print ("FILE:", downfile)
	if os.path.exists (downfile):
		print (downfile,"is exists!!!")
		return
	try:
		global time1
		time1 = time.time()
		urllib.request.urlretrieve(mp3url,downfile,reporthook)
		global ok
		ok += 1
		print()
	except :
		print (downfile,"is fail !")
 
def soundlist(soundurl) :
	try :
		cc = urllib.request.urlopen(soundurl).read().decode("utf-8")
	except:
		print ("Are you sure it's a correct url?")
		return
	chaxun=re.findall("sound_id=\"[0-9]*\"",cc)
	if chaxun :
		idlist = [x.split("\"")[1] for x in chaxun]
		global total
		idlist2 = {}.fromkeys(idlist).keys()
		total = len(idlist2)
		for i in idlist2 :
			down(i)
	else :
		print ("It's a wrong url")
		return
 
if len(sys.argv) > 1 :
	total = len(sys.argv[1:])
	for j in sys.argv[1:] :
		down(j,"2014")
else :
	try:
		readurl = input ("Need a ximalaya's url: ")
 
	except :
		print()
		exit()
	print ("You are type is: ",readurl)
	try :
		readurl2 = readurl.replace("#/","")
	except :
		pass
	soundlist(readurl2)
 
print ("="*80)
print ("All done,",ok,"files is downloded.")