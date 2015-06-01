#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

import os
import re
aa = ['一','二','三','四','五','六','七','八','九','十']
bb = ['1','2','3','4','5','6','7','8','9','0']
pwd='/home/xzap/ximalaya/听泡爸改编《西游记》'
for a,b,c in os.walk(pwd):
	cc = c
for i in cc:
	# print(i)
	new = i.replace(' ','').replace('回','回_')
	# com = re.search('[一二三四五六七八九十]+',i)
	# com2 = com.group()
	# if '十' in com2 :
	# 	if len(com2) == 3 :
	# 		com2 = com2.replace('十','')
		
	# 	if com2[0] == '十' :
	# 		com2 = com2.replace('十','1')
	# 	else :
	# 		com2 = com2.replace('十','0')
	
	# for j in range(9) :
	# 	com2 = com2.replace(aa[j],bb[j])
	# if len(com2) == 1:
	# 	com2 = '0'+com2
	# new = com2+i
	oldf = os.path.join(pwd,i)
	newf = os.path.join(pwd,new)
	print (newf)
	os.rename(oldf,newf)


	http://scanmem.googlecode.com/files/scanmem-0.13.tar.gz