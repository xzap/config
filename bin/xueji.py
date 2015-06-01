#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import urllib.request
import re
headers ={
'Host':'xjglpt.zjedu.gov.cn',
'Connection':'keep-alive',
'Pragma':'no-cache',
'Cache-Control':'no-cache',
'X-Requested-With':'XMLHttpRequest',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',
'Accept':'*/*',
'Referer':'https://xjglpt.zjedu.gov.cn/index.action',
'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
'Cookie':'route=df0f004d96ad4377f8fd675afe75d9fd; JSESSIONID=EF5359DE8627D3561B79A5007B65AF16-n1.tomcat101'
}
aa = {'26':'A','27':'P','28':'E'}
bb = {'22':'A','23':'B','24':'C','25':'D'}
url1 = 'https://xjglpt.zjedu.gov.cn/jc/jyjxx/jyjxx!czIndex.action?syxsjb=7&reid=351&cgz=6'
req = urllib.request.Request(url1,headers=headers)
cc = urllib.request.urlopen(req).read().decode('utf-8')
pattern = re.compile("id='([0-9]*)' text='(.年级[^']*)'")
rr =re.findall (pattern,cc)
for j in rr :
	url2 = 'https://xjglpt.zjedu.gov.cn/jc/jyjxx/jyjxx!getSubSytreeXdXs.action?grandId=27&currjb=6&syxsjb=7&treeid='+j[0]+'&reid=351&cgz=6'
	req = urllib.request.Request(url2,headers=headers)
	cc = urllib.request.urlopen(req).read().decode('utf-8')
	pattern = re.compile("id='([0-9]*)' text='([^']*)'")
	rr =re.findall (pattern,cc)
	for i in rr:
		jg = i[1].split(' - ')
		jg.insert(0,j[1][:8])
		url3 = 'https://xjglpt.zjedu.gov.cn/cz/zhsz/zhszdj!loadXsxxData.action?xsxxId='+i[0]
		req = urllib.request.Request(url3,headers=headers)
		cc = urllib.request.urlopen(req).read().decode('utf-8')
		pattern = re.compile("editable=\"0\">([0-9]*)<optio")
		rr =re.findall (pattern,cc)
		try :
			jg.append(aa[rr[0]])
			for i in rr[1:] :
				jg.append(bb[i])
		except:
			pass
		print (",".join(jg))