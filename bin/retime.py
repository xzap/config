#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import os
import re
import time
import sys

movie_dir = os.path.realpath('/data/movie')
newdir = os.path.realpath('/data/movie')
r_part = re.compile('2015-[0-9]{2}-[0-9]{2}_') #2015-03-07_11_28_17
for root,dirs,files in os.walk(movie_dir) :
	for onefile in files :
		oldfile = os.path.join(root,onefile)
		if len(sys.argv) > 1 :
			try :
				rr = re.search(r_part,oldfile).group()
			except:
				continue
			if rr :
				newfile = oldfile.replace(rr,'')
				os.rename (oldfile,newfile)

		else :
			if re.search(r_part,oldfile) : continue
			atime = time.strftime('%Y-%m-%d',time.localtime(os.path.getatime(oldfile)))
			# ctime = time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(os.path.getctime(oldfile)))
			mtime = time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(os.path.getmtime(oldfile)))
			newfile = os.path.join(root,atime+"_"+onefile)
			os.rename(oldfile,newfile)