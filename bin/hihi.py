#!/usr/bin/env python
import urllib.request
import os,re
from http import cookiejar
import sys

canshu = sys.argv[1]
span = []
login_url = 'http://www.hi-pda.com/forum/logging.php?action=login&loginsubmit=yes&inajax=1' 
url = 'http://www.hi-pda.com/forum/forumdisplay.php?fid=6&page='
cj = cookiejar.CookieJar()
opener = urllib.request.build_opener()
opener.add_handler(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders.append(('Cookie', 'cdb_auth=0629w3lgFlx66o%2F7afOBUerUch9mX3m2pSe29gi9k5Hk3SDtEOTDDsZsTaxafevhc6uN6nzKaukwpyfpSaR97Rs5kszY'))
opener.addheaders.append(('Cookie', 'cdb_sid=gEseEW'))
p = re.compile('<span.*'+canshu+'.*span>',re.IGNORECASE)
urllib.request.install_opener(opener)

for i in range(1,10):
        iurl = url+str(i)
        cc = opener.open(iurl).read().decode('gbk')
        comp = re.findall(p,cc)
        span.extend(comp)

span2 = [ '<li>'+i+'</li>' for i in span ]
span3 = [ i.replace('href=\"','href=\"http://www.hi-pda.com/forum/') for i in span2]
#print (span2)
htm='''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gbk" />
<title>Hi!PDA Hi!PDA xzap页面</title>
<meta name="generator" content="Discuz! 7.2" />
<meta name="MSSmartTagsPreventParsing" content="True" />
<meta http-equiv="MSThemeCompatible" content="Yes" />
<meta http-equiv="x-ua-compatible" content="ie=7" />
<link rel="archives" title="Hi!PDA" href="http://www.hi-pda.com/forum/archiver/" />
<link rel="alternate" type="application/rss+xml" title="Hi!PDA Hi!PDA 简易搜索页面" href="http://www.hi-pda.com/forum/rss.php?fid=6&amp;auth=38fdRJxvxacuoLedmqkxI3u2TjjxjQXjceaiMBMQeMWNM0RPTNDFhj0LB2VS8Q" />
<script type="text/javascript">var STYLEID = '1', IMGDIR = 'images/default', VERHASH = 'k25', charset = 'gbk', discuz_uid = 157544, cookiedomain = '', cookiepath = '/', attackevasive = '0', disallowfloat = 'login|register|sendpm|newthread|reply|viewratings|viewwarning|viewthreadmod|viewvote|tradeorder|activity|debate|nav|usergroups|task', creditnotice = '1|威望|,2|金钱|', gid = parseInt('35'), fid = parseInt('6'), tid = parseInt('0')</script>
<script src="http://www.hi-pda.com/forum/forumdata/cache/common.js?k25" type="text/javascript"></script>
</head>
<body id="forumdisplay" onkeydown="if(event.keyCode==27) return false;">
<div><h2>%s专用搜索页面</h2></div>
<div>
<ol>
%s
</ol>
</div>
<hr />
<div class="copyright">Copyright &copy; 2013 Design by Jgp</div><br />
</body>
</html>''' % (canshu,'\n'.join(span3))
with open ('/tmp/hi-pda.html','w',encoding='gbk') as f :
        f.write(htm)
exe=r'google-chrome-stable'+ " /tmp/hi-pda.html"
os.system(exe)