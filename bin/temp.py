#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import urllib.request
import os
import re
from bs4 import BeautifulSoup

webfile = os.path.realpath('/home/xzap/yw.html')
# with open(webfile,'r',encoding='GBK') as x :
with open(webfile,'rb') as x :
	cc = x.read()
soup = BeautifulSoup(cc,from_encoding="GBK")
print (soup.findAll('dl'))