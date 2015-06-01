#!/usr/bin/env python
# coding:utf-8

import os
import sys
import re
import zipfile
import urllib.request
import urllib.parse
import json
import time
import random


url  = 'http://www.bxwx.la/b/0/77/'
cc =urllib.request.urlopen(url).read().decode()
rp = re.compile('<a style="" href="([0-9]*.html)">([^<]*)</a>')
rr = rp.findall (cc)
for i in rr[:1]:
    print (i[1])
    url = 'http://www.bxwx.la/b/0/77/' + i[0]
    print (url)