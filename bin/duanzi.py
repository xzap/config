#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import urllib.request
import json
import os
import re
import sys
import time

def delRepeat(liebiao):
	for x in liebiao:
		while liebiao.count(x)>1:
			del liebiao[liebiao.index(x)]
	return liebiao

def down(soundid,year="") :
	print(soundid)

	url = "http://www.ximalaya.com/tracks/" + soundid + ".json"
	print(url)
	jc = urllib.request.urlopen(url).read().decode("utf-8")
	if jc == "null" :
		print("="*80)
		print (soundid,"is a wrong sound id")
		return
	data = json.loads(jc)
	album = data["album_title"]
	title = data["title"]
	try:
		mp3url = baseurl + data["play_path"]
	except:
		mp3url = baseurl + data["play_path_64"]
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
	mp3_dl = os.path.join(dpath,'aria2.down')
	if not os.path.exists(dpath):
		os.makedirs(dpath)
	downfile = os.path.join(dpath,filename)
	print("="*80)
	#print (title,"downloading......")
	print ("URL:", mp3url)
	print ("FILE:", downfile)
	if os.path.exists (downfile):
		print (downfile,"is exists!!!")
		return
	cc = '''%s
  dir=%s
  out=%s
  header=Cookie: appver=1.7.6
  continue=true
  max-connection-per-server=5
  split=10
  parameterized-uri=true

''' % (mp3url,dpath,filename)


	with open (mp3_dl,'a') as  x :
		x.write(cc)

baseurl = "http://fdfs.xmcdn.com/"
path = os.path.expanduser("~/ximalaya")
if not os.path.exists(path):
	os.makedirs(path)
opener = urllib.request.build_opener()
opener.addheaders.append(('Referer', 'http://www.ximalaya.com'))
opener.addheaders.append(('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36'))
urllib.request.install_opener(opener)
duanzi_down = os.path.realpath('/tmp/duanzi.down') 
if os.path.exists(duanzi_down):
	os.remove(duanzi_down)

url = 'http://www.ximalaya.com/2629294/album/214706' #段子来了
url2 = 'http://www.ximalaya.com/2629294/album/273674.ajax' #段子来了羞羞版
url3 = 'http://www.ximalaya.com/9216785/album/257813?page=2' #一千零一夜
cc = urllib.request.urlopen(url3).read().decode("utf-8")
# print (cc)
chaxun = re.findall("sound_id=\"[0-9]*\"",cc)
idlist = [x.split("\"")[1] for x in chaxun]
id2 = delRepeat(idlist) 
for i in id2 :
	down(i)
	print(i)
# print(len(id2[:10]))