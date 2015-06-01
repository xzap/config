#!/usr/bin/env python

import hashlib
import os,sys
from urllib.parse import urlencode
import json
import urllib.request
#import random

def _getsubs(mvfile) :
	BlockSize = 4096
	NumOfSegments = 4
	strHash = []
	fileLength = os.path.getsize(mvfile)
	offset = []
	offset.append(BlockSize)
	offset.append(fileLength / 3 * 2)
	offset.append(fileLength / 3)
	offset.append(fileLength - 8192)
	if os.path.isfile(mvfile):
		with open(mvfile,"rb")  as movie :
			for i in range(0,NumOfSegments):
				movie.seek(int(offset[i]))
				buff = movie.read(BlockSize)
				m = hashlib.md5()
				m.update(buff)
				strHash.append(m.hexdigest())
	else :
		print ("File could not be opened")
	hashstr=";".join(strHash)
	user_agent = "SPlayer Build 1543"
	#ContentType = "multipart/form-data; boundary=----------------------------{:x}".format(random.getrandbits(48))

	headers = {
	'User-Agent' : user_agent,
	#'Content-Type' : ContentType,
	'Connection' : 'Keep-Alive',
	'Expect' : '100-continue'
	}
 
	postdata = urllib.parse.urlencode({
	'filehash': hashstr, 
	'pathinfo': mvfile,
	'format': 'json',
	'lang': 'Chn'
	})
	postdata=postdata.encode("utf8")
	for i in range(5) :

		url="http://splayer"+str(i)+".shooter.cn/api/subapi.php"
		req = urllib.request.Request(url, postdata, headers)
		c = urllib.request.urlopen(req).read()
		# print("正在 "+url+" 查找字幕请耐心等待……")
		if len(c) >10 :
			break
		url="https://splayer"+str(i)+".shooter.cn/api/subapi.php"
		req = urllib.request.Request(url, postdata, headers)
		c = urllib.request.urlopen(req).read()
		# print("正在 "+url+" 查找字幕请耐心等待……")
		if len(c) >10 :
			break
	if len(c) < 10 :
		print("没有找到任何字幕")
		return 
	jsondict = json.loads(c.decode("utf8"))
	links=[]
	ext =[]
	for i in jsondict :
		links.append(i['Files'][0]["Link"])	
		ext.append(i['Files'][0]["Ext"])
	alllinks=[links,ext]
	print("找到了",len(links),"个字幕，正在保存……")	
	for i in range(len(links)):
		# r,c=h.request(i,"GET")
		# print(i)
		 a=urllib.request.urlopen(links[i]).read()
		 #path=os.path.dirname(mvfile)
		 path="/data/srt/"
		 mvfile=os.path.basename(mvfile)
		 if i == 0 :
		 	name=os.path.join(path,mvfile[:-3]+ext[i])
		 else:
		 	extt=mvfile[:-3]+"chn"+str(i)+"."+ext[i]
		 	name=os.path.join(path,extt)
		 print (name)	 	
		 with open(name,"wb") as srtfile :
		 	srtfile.write(a)

def _run(movfile) :
	print("_"*70)
	print ("正在查找",movfile,"的字幕:")
	file_ext=os.path.splitext(movfile)[1][1:]
	if file_ext.lower() in mov_ext :
		_getsubs(movfile)
	else :
		print("不支持的文件类型")
	
	
if __name__ == '__main__':
	mov_ext=["avi","rmvb","mkv","mp4","rm"]
	if len(sys.argv) == 2 :
		f = os.path.realpath(sys.argv[1])
		_run(f)		
	else :
		for d,fd,fl in os.walk(os.getcwd()) :
			for ff in fl :	
				f=os.path.realpath(os.path.join(d,ff))
				file_ext=os.path.splitext(f)[1][1:]
				if file_ext.lower() in mov_ext :
					_run(f)



