#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import urllib.request
import json,os,re
import glob

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

for i in range(len(data2)):
        if os.path.exists(os.path.join(basedir,data2[i]['title'])) :
            print (str(i)+'.',data2[i]['ptime'],data2[i]['title'],'(done!)')
        else :
            print (str(i)+'.',data2[i]['ptime'],data2[i]['title'])


try:

        choice = int(input("请输入序号："))
        print ("现在开始下载",data2[choice]['title'],"接下来就是耐心等待吧……")

except :
        print ("输入错误")
        exit()

docid = data2[choice]['docid']


imgdict = {}
url = 'http://3g.163.com/touch/article/'+docid+'/full.html'
resp = urllib.request.urlopen(url).read().decode('utf-8')
news_data = json.loads(resp[12:-1])

# outdir = os.path.expanduser("~/qingsong/"+news_data[docid]['title'])
outdir = os.path.expanduser("~/qingsong/"+data2[choice]['title'])

if not os.path.exists(outdir) :
    os.mkdir(outdir)
imgdir = os.path.join(outdir,"Images")
if not os.path.exists(imgdir) :
    os.mkdir(imgdir)

html = news_data[docid]['body']
# print (news_data[docid]['img'])
n = 0
jpg=""

for key in news_data[docid]['img'] :
        imgdict[key['ref']]=key['src']
        print (key['src'])
        jpgname = os.path.basename(key['src'].replace('\"/',""))
        img = "<div class=\"imgdiv\"><img src=\"./Images/" + jpgname + "\" /></div>" 
        html=re.sub(key['ref'],img,html)
        imgfile = os.path.join(imgdir,jpgname)
        try:
            print('开始下载：',imgfile,"……")
            if os.path.exists(imgfile):
                print ('已存在，跳过！')
                continue
            urllib.request.urlretrieve(key['src'],imgfile)
            print ('成功！')
        except :
            print ('失败！')
            pass
        n+=1

# print(news_data[docid])
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

<div id="news"><h2><span>'''+ news_data[docid]['title'] +'''</span><span>'''+news_data[docid]['ptime']+'''<span></h2> 
<h3>'''+data2[choice]['digest']+'''</h3>
''')
f.write(html)
f.write('''</div> 
</body>
</html>''')
f.close()
qlist=[]
for  i in glob.glob(basedir+'/*'):
    if os.path.isdir(i):
        li = '<li><a target=\"mainFrame\"  href=\"'+i+'/index.html\">'+os.path.basename(i)+'</a></li>'
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
height:780px;
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