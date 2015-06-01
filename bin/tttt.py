#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

import urllib.request
import os
import time
import re
headers = {
'Cookie':'JSESSIONID=3882EA4A460C978348BF2F39D6A4F45B; CNZZDATA1253333710=758560650-1422411902-http%253A%252F%252Fmrg.eduyun.cn%252F%7C1422411902; JSESSIONID=8A69C0378C36DFFD8BCA7D2B99B1EA08; CNZZDATA1253416210=482517104-1421989544-http%253A%252F%252Ftz.1s1k.eduyun.cn%252F%7C1422501815',
'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
'Referer': 'http://mrg.eduyun.cn/portal/1s1k/portal/school_manager_check.jsp',
'X-Requested-With': 'XMLHttpRequest' ,
'Connection': 'keep-alive' 
}
listl = [['ff8080814aeb872e014aec01a2c20184','2','1'],
['ff8080814b119556014b23d6921e0b2b','2','1'],
['ff8080814b29b196014b2dec3d510450','2','1'],
['ff8080814b29b196014b2dec60940451','2','1'],
['ff8080814b29b196014b2e11b60004a7','2','1'],
['ff8080814b29b196014b2e585a7b05e0','2','1'],
['ff8080814b29b19f014b2e002d8f04a1','2','1'],
['ff8080814b29b19f014b2e4c9670054d','2','1'],
['ff8080814b29b1a2014b2deb098b047e','2','1'],
['ff8080814b29b1a2014b2dff5a1c04e7','2','1'],
['ff8080814b29b1a2014b2e093d10051b','2','2'],
['ff8080814b29b1a2014b2e53cce0057d','2','2'],
['ff8080814b29b1ac014b2df4be3804cc','2','2'],
['ff8080814b29b1ac014b2df9bc3504e6','2','2'],
['ff8080814b29b1ac014b2e1bde02059e','2','2'],
['ff8080814b29b1ac014b2e1c571605a6','2','2'],
['ff8080814b29b1ac014b2e4f625805ef','2','2'],
['ff8080814b29b1ac014b2e5097530600','2','2'],
['ff8080814b29b1ac014b2e50f18c0606','2','2'],
['ff8080814b29b1ac014b2e511c7a060a','2','2'],
['ff8080814b29b1ae014b2dfef3d004ea','2','3'],
['ff8080814b29b1ae014b2e08df75051d','2','3'],
['ff8080814b29b1ae014b2e4e5d530572','2','3'],
['ff8080814b29b1ae014b2f220ef408f1','2','3'],
['ff8080814b29b1ae014b2f23b71908fe','2','3'],
['ff8080814b29b1ae014b2f2e06c50946','2','3'],
['ff8080814b29b1d5014b2e5332700649','2','3'],
['ff8080814b29b1d5014b2e7d3522079f','2','3'],
['ff8080814b29b1d5014b2ed5657f0886','2','3'],
['ff8080814b29b1d6014b2dfe57b505ab','2','3'],
['ff8080814b29b1d6014b2e06c4f305ed','2','4'],
['ff8080814b29b1d6014b2ecf345f08ce','2','4'],
['ff8080814b29b1d6014b2f6fb6190b4a','2','4'],
['ff8080814b29b1d7014b2de958470505','2','4'],
['ff8080814b29b1d7014b2dff49ba0519','2','4'],
['ff8080814b29b1d7014b2e09e0d40549','2','4'],
['ff8080814b29b1d7014b2e0ff84b0595','2','4'],
['ff8080814b29b1d7014b2e106330059b','2','4'],
['ff8080814b29b1d7014b2ed7c80d07f7','2','4'],
['ff8080814b29b1d7014b2ed93ab00807','2','4'],
['ff8080814b29b1e6014b2e4cebbf04d5','2','5'],
['ff8080814b29b1e6014b2e5381b9052c','2','5'],
['ff8080814b29b1e6014b2e71c02605c2','2','5'],
['ff8080814b29b1e6014b2eb6c16306b9','2','5'],
['ff8080814b29b1e6014b2ed71bf50733','2','5'],
['ff8080814b29b1e9014b2e0146cd056b','2','5'],
['ff8080814b29b1e9014b2e046199059a','2','5'],
['ff8080814b29b1e9014b2e04b29805a6','2','5'],
['ff8080814b29b1e9014b2e0e64600602','2','5'],
['ff8080814b29b1e9014b2e4efc0c0666','2','5'],
['ff8080814b29b1ee014b2de37bff03f6','2','6'],
['ff8080814b29b1ee014b2df37820041a','2','6'],
['ff8080814b29b1ee014b2dfcbd8c0433','2','6'],
['ff8080814b29b1ee014b2e01fd35045a','2','6'],
['ff8080814b29b1ee014b2e02562e045e','2','6'],
['ff8080814b29b1ee014b2e560e87050c','2','6'],
['ff8080814b29b1f2014b2df4881d055b','2','6'],
['ff8080814b29b1f2014b2df52a4c0561','2','6'],
['ff8080814b29b1f2014b2e1a6e9c05ec','2','6'],
['ff8080814b29b1f2014b2e6193230692','2','6'],
['ff8080814b29b1f2014b2e6195380693','2','7'],
['ff8080814b29b1f2014b2e6411fe06ca','2','7'],
['ff8080814b29b1f2014b2e64754706d0','2','7'],
['ff8080814b29b1f2014b2e9e71290886','2','7'],
['ff8080814b29b1f6014b2df1cf0105ee','2','7'],
['ff8080814b29b1f6014b2e11d9700650','2','7'],
['ff8080814b29b1f6014b2f31a1fb0a23','2','7'],
['ff8080814b29b1f7014b2de6a5ff04d2','2','7'],
['ff8080814b29b1f7014b2e6102ed0679','2','7'],
['ff8080814b29b1f7014b2e627b650693','2','7'],
['ff8080814b29b1f7014b2e629d2e0696','2','8'],
['ff8080814b29b204014b2e01c3b50635','2','8'],
['ff8080814b29b204014b2e0d49bd066f','2','8'],
['ff8080814b29b204014b2e0e66fb0673','2','8'],
['ff8080814b29b204014b2e500f8006a3','2','8'],
['ff8080814b29b20e014b2e0c3810049f','2','8'],
['ff8080814b29b20e014b2e0ea0c204bc','2','8'],
['ff8080814b29b20e014b2e0ee55004c8','2','8'],
['ff8080814b29b20e014b2e4df6540579','2','8'],
['ff8080814b29b20e014b2e4e2979057d','2','8'],
['ff8080814b29b20e014b2e6b3dcb05f1','2','9'],
['ff8080814b29b20f014b2e07bf120676','2','9'],
['ff8080814b29b20f014b2e0aa57e06b1','2','9'],
['ff8080814b29b20f014b2e135c3006e6','2','9'],
['ff8080814b29b20f014b2e5187af0763','2','9'],
['ff8080814b29b20f014b2e539a940786','2','9'],
['ff8080814b29b20f014b2ea9c8bf08b3','2','9'],
['ff8080814b29b215014b2dfb4e95054d','2','9'],
['ff8080814b29b215014b2ed23885085d','2','9'],
['ff8080814b29b223014b2e501958060c','2','9'],
['ff8080814b30d66a014b33aa69c20360','2','10']]

for i in listl :
	tt = str(time.time()).replace('.','')[:13]
	url = 'http://mrg.eduyun.cn/ysyk/base/BaseUser/setSchoolCheckStatus.jspx?pageNo='+i[2]+'&status=2&teacherId='+i[0]+'&date='+tt
	req = urllib.request.Request(url,headers=headers)
	cc = urllib.request.urlopen(req).read().decode()
	print(cc)
