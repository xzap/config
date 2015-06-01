import urllib.parse
import urllib.request
import os,re
from http import cookiejar
import sys

login_url = 'http://www.hi-pda.com/forum/logging.php?action=login&loginsubmit=yes&inajax=1' 
cj = cookiejar.CookieJar()
opener = urllib.request.build_opener()
opener.add_handler(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders.append(('Cookie', 'JSESSIONID=8D8AFC38294F8FBE126D698F74E1892B'))

urllib.request.install_opener(opener)

params={"startDate":"2014-10",
"endDate":"2014-10",
"realname":'',
"pageSize":"20"}
url5= "http://stat.zjer.cn/statview.do?method=user&print=112&orderColumn=&order=&pageIndex=1&unit="

params = urllib.parse.urlencode(params)
req = urllib.request.Request(url5,data=params.encode("utf-8"))
# print (cj)
cc = urllib.request.urlopen(req).read().decode('GBK')
print (cc)