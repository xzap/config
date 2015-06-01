#!/usr/bin/env python
import os,re

ff = os.path.realpath('/home/xzap/lil.html')

with open (ff,'r') as x:
	cc = x.read()
p = re.compile('<tr class="tbody".*?</tr>',re.S)
c = re.findall(p,cc)
print(len(c))
print ('\n'.join(c))
