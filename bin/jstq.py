#!/usr/bin/env python
import urllib.request
import re
import os
url = 'http://www.jsqx.com.cn/'


def getcc(url,code='UTF-8'):
	cc = urllib.request.urlopen(url).read().decode(code)
	return cc

content = getcc(url)
comp = re.search('<marquee.*/marquee>',content,re.S).group()
comp = comp.replace('\r\n','')
comp = comp.strip()
comp = comp.replace('</p>','</p>\n')
comp2 = re.findall('<p>(.*)</p>',comp)
comp3 = [ i.replace(' ','') for i in comp2 ]
comp4 = "\n".join(comp3[:-1])
compp = re.search('嘉善县气象台(.*)的天气预报',content).group(1)

rus = compp + '\n' + comp4
shell = 'echo \''+ rus + '\' |zenity --text-info'

os.system(shell)