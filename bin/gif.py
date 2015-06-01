#!/usr/bin/env python
# coding:utf-8

import os
import re
import urllib.request
import urllib.parse

divs = []
divs2 = []
part = re.compile('[a-zA-Z0-9]{2,6}[-_]?[0-9]{2,5}')
gifpath = os.path.realpath('/data/123/gif')
# gifpath = os.path.realpath('/home/xzap/图片/1')

htmlpath = os.path.realpath('/data/123')
for root,d,f in os.walk(gifpath):
    for ff in f :
        fff = os.path.join(root,ff)
        truename = os.path.splitext(os.path.basename(fff))[0]
        # print (truename,end = '====')
        if re.search (part,truename):
            rr = re.findall(part,truename)[0]
            print (rr)
            
            divs.append('''<div class="magnet">\n    <div><img src="%s" /></div>\n    <div>%s</div>\n    <div>%s</div>\n</div>\n''' % (urllib.parse.quote(fff),truename,rr))
        else :
            divs2.append('''<div class="magnet">\n    <div><img src="%s" /></div>\n    <div>%s</div>\n</div>\n''' % (urllib.parse.quote(fff),truename))


# print (divs)

html = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Gif页面</title>
<style type="text/css">
.llist{
    float:left;
    width:340px;

}
.magnet{

    word-wrap: break-word;
    padding: 10px;
    background: #eef;
    margin: 5px;
    line-height: 171%% ;
    text-align: center ;
}
img {
    width:300px;

}
.lianjie{
 width: 50px;
list-style: none;
margin: 5px;
display: inline-block;
padding: 4px 10px;
line-height: 100%%;
margin-right: 10px;
border: solid 1px #aaa;
background-color: #eee;
border-radius: 10px;
text-align: center;
}
.lianjie:hover{
    background-color:#96FED1
}
    </style>
    </head>
    <body>
        <div id='content'>
        %s
            %s
        </div>
    </body>
</html>''' 

a = {}


pagenum = len(divs) // 52 +1
href ="<div>\n"
for i in range (pagenum+1) :
    href+= '''<a href="%s.html"><span class="lianjie">%s</span></a>\n''' % (i,i) 
href += "</div>"

for i in range (pagenum):
    j = i +1
    aas = ''
    aa = divs[i*52:j*52]
    num3 = len(aa) //4 
    for k in range(5):
        aas += '''<div class="llist">\n%s</div>\n''' % "".join(aa[k*num3:k*num3+num3])
    a[i] = aas 
aaaa=""
num2 = len(divs2) //4+1
print (len(divs2))
print (num2)
for k in range (5):
    aaaa += '''<div class="llist">\n%s</div>\n''' % "".join(divs2[k*num2:k*num2+num2])


for i in range (pagenum):
    with open (os.path.join(htmlpath,str(i+1)+".html"),'w') as f2:
        f2.write(html % (href,a[i]))
with open (os.path.join(htmlpath,"0.html"),'w') as f2:
        f2.write(html % (href , aaaa))

