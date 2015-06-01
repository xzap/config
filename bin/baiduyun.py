#!/bin/env python3

import urllib.request, urllib.parse, urllib.error
# ID：1575200
# API Key：l1bygjazs7OtxskWfC8pUuRV
# Secret Key：HbFhGfG1RMIK6F7SqWjGNnOU9zvWUZxe
# 创建时间：2013-10-23 18:48:20
# 更新时间：2014-10-21 09:59:09
import json

def get_access() :
	url = 'https://openapi.baidu.com/oauth/2.0/token'
	params = {'grant_type':'client_credentials',
	'client_id':'l1bygjazs7OtxskWfC8pUuRV',
	'client_secret':'HbFhGfG1RMIK6F7SqWjGNnOU9zvWUZxe'}	
	params = urllib.parse.urlencode(params)
	req = urllib.request.Request(url,data=params.encode())
	cc = urllib.request.urlopen(req).read().decode()
	jc = json.loads(cc)
	return jc['access_token']

def get_quota(token) :
	url = 'https://pcs.baidu.com/rest/2.0/pcs/quota?method=info&access_token='+token
	req = urllib.request.Request(url)
	cc = urllib.request.urlopen(req).read().decode()
	js = json.loads(cc)
	quota = js['quota']/1073741824

	used = js['used']/1073741824
	print (quota,used)

# url ='https://openapi.baidu.com/oauth/2.0/authorize?response_type=token&client_id=l1bygjazs7OtxskWfC8pUuRV&redirect_uri=oob&scope=netdisk'
# cc =urllib.request.urlopen(url).read().decode()
# print (cc)

access_token='23.3991d55cdbe6045a8667a4c9f89c8c41.2592000.1416453504.2416182679-1575200'
# a_token = get_access()
# print (a_token)
get_quota(access_token)