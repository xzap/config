#!/usr/bin/env python
import httplib2
import json
import datetime
addr = "101210302" #嘉善
#url = "http://m.weather.com.cn/data/{}.html".format(addr)
url = "http://www.weather.com.cn/data/cityinfo/{}.html".format(addr)
#url = "http://www.weather.com.cn/data/sk/{}.html".format(addr)
h = httplib2.Http()
r,c = h.request(url)
cc = c.decode("utf8")
jc = json.loads(cc)
jcc=jc["weatherinfo"]
#dt = datetime.date.today()
#sj=("今天","明天","后天")
print("${color #ffd700}"+jcc["city"]+"天气: (更新时间："+jcc["ptime"]+")$color")
#for i in range(3):
#	j=str(i+1)
#	print("${color #98c2c7}"+sj[i]+": $color",jcc["weather"+j],jcc["wind"+j],"${alignr}"+jcc["temp"+j])
print(jcc["weather"],"${alignr}"+jcc["temp2"]+"～"+jcc["temp1"])
print ('${color #ffd700}${hr 1}$color')
