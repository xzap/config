#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

'''

'''
import urllib.request
import json
import os
import re
mp3_ext = ("mp3",)
songlist = []
def downlrc(song) :
	songpath = os.path.split(song)[0]
	lrcdir = os.path.realpath("/data/mp3/lrc")
	name = os.path.splitext(os.path.split(song)[1])[0]
	lrc = os.path.join(lrcdir,name+".lrc",)
	if os.path.exists(lrc):
		print (lrc,"is exists")
		return
	name2 = urllib.request.quote(name)
	url = "http://music.baidu.com/search/lrc?key="
	url2 = url + name2
	cc = urllib.request.urlopen(url2).read().decode("utf8")
	htmlurl = re.search('down-lrc-btn.{.*}',cc)
	if htmlurl:
		lrcurl = 'http://music.baidu.com'+htmlurl.group().split("'")[3]
		print("Now start downloading",song,"\'s lrc please wait......")

		urllib.request.urlretrieve(lrcurl,lrc)
	else:
		print (name+'查找失败！')


for d,fd,fl in os.walk(os.getcwd()) :
			for ff in fl :	
				f=os.path.realpath(os.path.join(d,ff))
				file_ext=os.path.splitext(f)[1][1:]
				if file_ext.lower() in mp3_ext :
					downlrc(f)
					songlist.append(f)
# print(len(songlist))
					