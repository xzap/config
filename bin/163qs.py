#!/usr/bin/env python
# -*- coding: utf-8 -*-  
 

import urllib.request
import json,os,re
import glob
import sys

qlist=[]
url = 'http://c.m.163.com/nc/article/list/T1350383429665/0-20.html'
resp = urllib.request.urlopen(url).read().decode('utf-8')
data = json.loads(resp)
data2 = []
basedir = os.path.expanduser("~/qingsong/")
if not os.path.exists(basedir) :
    os.mkdir(basedir)   
for i in data['T1350383429665'] :
    if '每日轻松一刻' in i['title'] :
        data2.append(i)

for page in data2 :
    print ()
    print ("现在开始下载",page['title'],"接下来就是耐心等待吧……")
    docid = page['docid']
    url = 'http://3g.163.com/touch/article/'+docid+'/full.html'
    resp = urllib.request.urlopen(url).read().decode('utf-8')
    news_data = json.loads(resp[12:-1])
    outdir = os.path.expanduser("~/qingsong/"+page['title'])
    if not os.path.exists(outdir) :
        os.mkdir(outdir)
    imgdir = os.path.join(outdir,"Images")
    if not os.path.exists(imgdir) :
        os.mkdir(imgdir)
    html = news_data[docid]['body']
    imgdict = {}
    for key in news_data[docid]['img'] :
    
        imgdict[key['ref']]=key['src']
        jpgname = os.path.basename(key['src'].replace('\"/',""))
        img = "<div class=\"imgdiv\"><img src=\"./Images/" + jpgname + "\" /></div>" 
        html=re.sub(key['ref'],img,html)
        imgfile = os.path.join(imgdir,jpgname)
        # print (imgfile+'……  ',end='')
        sys.stderr.write("\r {}".format(imgfile))
        try:
            if os.path.exists(imgfile):
                # print('---> 已存在，跳过')
                sys.stderr.write('\r ---> 已存在，跳过')
                continue
            urllib.request.urlretrieve(key['src'],imgfile)
            # print('---> 完成')
            sys.stderr.write('\r ---> 完成')


        except :
            # print('---> 失败')
            sys.stderr.write('\r ---> 失败')
  
            pass
    html=re.sub('</p>','</p>\n',html)
    html=re.sub('</div>','</div>\n',html)
    html=re.sub('<!--.*-->','',html)    
    out = os.path.join(outdir,'index.html' )
    f = open (out,'w',encoding='utf-8') 
    f.write(u'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
    <meta charset="UTF-8"/> 
    <meta content="width=device-width,user-scalable=no" name="viewport"/> 
    <meta name="apple-itunes-app" content="app-id=425349261"/>
    <title>'''+ news_data[docid]['title'] +'''</title> 
<style type="text/css"> 
#news {margin:auto;width:720px;padding:0 3%; }
.imgdiv{margin:auto;width:80%}
img {
max-width: 500px;
position: relative;
margin: 0 auto;
padding-top: 10px;
padding-bottom: 10px;
text-align: center;
}
</style> 
</head>
<body>

<div id="news"><h2><span>'''+ page['title'] +'''</span><span>'''+page['ptime']+'''<span></h2> 
<h3>'''+page['digest']+'''</h3>
''')
    f.write(html)
    f.write('''</div> 
</body>
</html>''')
    f.close()

    li = '<li class="rounded-list"><span><a target=\"mainFrame\"  href=\"'+page['title']+'/index.html\">'+os.path.basename(page['title'])+'</a></span></li>'
    qlist.append(li)
qli = '\n'.join(qlist)
index = os.path.join(basedir,'index.html')
with open (index,'w') as x :
    x.write(u'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
    <meta charset="UTF-8"/> 
    <meta content="width=device-width,user-scalable=no" name="viewport"/> 
    <meta name="apple-itunes-app" content="app-id=425349261"/>
    <title>网易轻松一刻</title> 
<style type="text/css"> 
#news {margin:auto;width:92%;padding: 0 3%}
.imgdiv{margin:auto;width:80%}
img {
width: 100%;
max-width: 480px;
position: relative;
margin: 0 auto;
padding-top: 10px;
padding-bottom: 10px;
text-align: center;
}
iframe {
border-top-width: 0px;
border-right-width: 0px;
border-bottom-width: 0px;
border-left-width: 0px;
width: 100%;
height:760px;
}
#content{
width:1200px;
background-color:#eee;
margin: auto;
}
#left{
    float:left;
    width:300px;
}
#right{
        float:left;
        width:810px;
        background:#eee;
        margin:15px;
        border-radius: 10px;

}
ol {	
counter-reset: li; /* 创建一个计数器 */
list-style: none; /* 清除列表默认的编码*/
*list-style: decimal; /* 让IE6/7具有默认的编码 */
font: 'WenQuanYi Zen Hei', 'trebuchet MS', 'lucida sans';
padding: 0;
text-shadow: 0 1px 0 rgba(255,255,255,.5);
}
	/*rounded shaped numbers*/
		.rounded-list a {
			position: relative;
			display: block;
			padding: 0.4em 0.4em 0.4em 2em;
			*padding: 0.4em;/*for ie6/7*/
			margin: 0.5em 0;
			background: #ddd;
			color: #444;
			text-decoration: none;
			/*CSS3属性*/
			border-radius: 0.3em;/*制作圆角*/
			/* transition动画效果*/
			-moz-transition: all 0.3s ease-out;
			-webkit-transition: all 0.3s ease-out;
			-o-transition: all 0.3s ease-out;
			-ms-transition: all 0.3s ease-out;
			transition: all 0.3s ease-out;
		}
		.rounded-list a:hover {
			background: #eee;
		}
		.rounded-list a:hover::before {
			/*悬停时旋转编码*/
			-moz-transform: rotate(360deg);
			-webkit-transform: rotate(360deg);
			-o-transform: rotate(360deg);
			-ms-transform: rotate(360deg);
			transform: rotate(360deg);
		}
		.rounded-list a::before {
			
			content: counter(li);
			counter-increment: li;
			
			position: absolute;
			left: -1.3em;
			top: 50%;
			margin-top: -1.3em;
			background: #87ceeb;
			height: 2em;
			width: 2em;
			line-height: 2em;
			border: 0.3em solid #fff;
			text-align: center;
			font-weight: bold;
			border-radius: 2em;
			-webkit-transition: all 0.3s ease-out;
			-moz-transition: all 0.3s ease-out;
			-ms-transition: all 0.3s ease-out;
			-o-transition: all 0.3s ease-out;
			transition: all 0.3s ease-out;
		}
</style> 
</head>
<body>
<div id="content">
<div id="left">
<ol>'''
+qli+
'''</ol>
</div>
<div id="right">
<iframe  name="mainFrame" ></iframe>
</div>
</div>
</body>
</html>''')