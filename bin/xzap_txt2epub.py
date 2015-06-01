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

def randid(num):
    randchr = ''
    for i in range(num):
        idc = chr(random.randint(97,122))
        idn = random.randint(0,9)
        icc = random.randint(0,5)
        if icc >3 :
            randchr+=idc
        else :
            randchr+=str(idn)
    return randchr

def zh2unicode(stri):
    for c in ('utf-8', 'gbk', 'big5', 'jp','euc_kr','utf16','utf32'):
        try:
            return stri.decode(c)
        except:
            continue                
        return stri

bookid = randid(8) +'-'+randid(4)+'-'+randid(4)+'-'+randid(4)+'-'+randid(12)
currenttime = time.strftime('%Y-%m-%dT%H:%M:%SZ',time.localtime())
txtfile = sys.argv[1]
bookpath,txtname = os.path.split(os.path.abspath(txtfile))
bookname = os.path.splitext(txtname)[0].replace(" ","_")
epubdir = os.path.join(bookpath,"epub_"+bookname)
oebpsdir = os.path.join(epubdir,"OEBPS")
metainfdir = os.path.join(epubdir,"META-INF")
cssdir = os.path.join(oebpsdir,"css")
imagesdir = os.path.join(oebpsdir,"images")
textdir = os.path.join(oebpsdir,'text')

if not os.path.isdir(epubdir):os.makedirs(epubdir)
if not os.path.isdir(oebpsdir):os.makedirs(oebpsdir)
if not os.path.isdir(metainfdir):os.makedirs(metainfdir)
if not os.path.isdir(cssdir):os.makedirs(cssdir)
if not os.path.isdir(imagesdir):os.makedirs(imagesdir)
if not os.path.isdir(textdir):os.makedirs(textdir)
mimetypefile = os.path.join(epubdir,'mimetype')
if not os.path.isfile(mimetypefile):
    with open (mimetypefile,'w') as f:f.write('application/epub+zip')
containerfile = os.path.join(metainfdir,'container.xml')
if not os.path.isfile(containerfile) :
    with open (containerfile,'w') as f:f.write('''<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
   <rootfiles>
      <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>   
   </rootfiles>
</container>''')
contentfile = os.path.join(oebpsdir,'content.opf')
tocfile = os.path.join(oebpsdir,'toc.ncx')
coverfile = os.path.join(imagesdir,'cover.jpg')
cssfile = os.path.join(cssdir,'main.css')
coverpage = os.path.join(textdir,'coverpage.html')
confile = os.path.join(textdir,'content.html')
jianjiefile = os.path.join(textdir,'summary.html')
params = {'count':1,'q':bookname}
url = "https://api.douban.com/v2/book/search?"+urllib.parse.urlencode(params)
# print (url)
cc = urllib.request.urlopen(url).read().decode('utf-8')
jc= json.loads(cc)

try:
    jcc = jc['books'][0]
    author = jcc['author'][0]
    jpgfile = jcc['images']["large"]
    summary = jcc['summary']
except :

    author = input('请输入作者：').strip()
    jpgfile = input('请输入封面地址：').strip()
    summary = input('输入简介：').strip()

    # author = '梦入神机'
    # jpgfile = 'http://wfqqreader.3g.qq.com/cover/886/236886/t7_236886.jpg'
    # summary = '当人类开始踏入星河时代，古老的修行就焕发出来了新的生命力。 修行，无论在任何时代永远不会过时。 金刚经中，须菩提问释迦牟尼，“要成佛，如何降服其心？”。 一句话，就道尽了修行的真谛，四个字，降服其心。 心神通广大，所以孙悟空又叫做心猿。每一个人的心灵就是一尊孙悟空，降服心猿，就可成斗战胜佛。 在星河大帝之中，梦入神机为你阐述修行的真谛。'

if not os.path.isfile(coverfile):
    try :
        urllib.request.urlretrieve(jpgfile,coverfile)
    except  Exception as e :
        print ('没有封面')
        # raise e



if not os.path.isfile(cssfile) :
    with open(cssfile,'w') as f :
        f.write('''ul, ol { margin:0em; padding:0em; }

/*样式名称：JinE样式002*/
/*样式作者：bookworm*/
/*样式版本：0.4*/
/*样式日期：2014-02-25*/

/*↓↓老牛字体样式3.1.0 2014-01-11↓↓*/
/*↓↓欢迎非商业性使用，但请注明"老牛字体样式"；商业使用请与老牛联系↓↓*/
@font-face {
    font-family:"zw";
    src:
    local("宋体"),local("明体"),local("明朝"),
    local("Songti"),local("Songti SC"),local("Songti TC"),
    local("STSong"),local("Song S"),local("Song T"),local("STBShusong"),local("TBMincho"),local("HYMyeongJo"),
    local("DK-SONGTI"),
    url(../Fonts/zw.ttf),
    url(res:///opt/sony/ebook/FONT/zw.ttf),
    url(res:///Data/FONT/zw.ttf),
    url(res:///opt/sony/ebook/FONT/tt0011m_.ttf),
    url(res:///ebook/fonts/../../mnt/sdcard/fonts/zw.ttf),
    url(res:///ebook/fonts/../../mnt/extsd/fonts/zw.ttf),
    url(res:///ebook/fonts/zw.ttf),
    url(res:///ebook/fonts/DroidSansFallback.ttf),
    url(res:///fonts/ttf/zw.ttf),
    url(res:///../../media/mmcblk0p1/fonts/zw.ttf),
    url(file:///mnt/us/DK_System/system/fonts/zw.ttf),
    url(file:///mnt/us/DK_System/xKindle/res/userfonts/zw.ttf),
    url(res:///mnt/us/fonts/zw.ttf),
    url(res:///abook/fonts/zw.ttf),
    url(res:///system/fonts/zw.ttf),
    url(res:///system/media/sdcard/fonts/zw.ttf),
    url(res:///media/fonts/zw.ttf),
    url(res:///sdcard/fonts/zw.ttf),
    url(res:///system/fonts/DroidSansFallback.ttf),
    url(res:///mnt/MOVIFAT/font/zw.ttf),
    url(res:///media/flash/fonts/zw.ttf),
    url(res:///media/sd/fonts/zw.ttf),
    url(res:///opt/onyx/arm/lib/fonts/AdobeHeitiStd-Regular.otf),
    url(res:///../../fonts/zw.ttf),
    url(res:///../fonts/zw.ttf),
    url(../../../../../zw.ttf),
    url(res:///mnt/sdcard/fonts/zw.ttf),
    url(res:///fonts/zw.ttf),
    url(res:///../../../../Windows/fonts/zw.ttf);/*,
    url(res:///fonts/normal/st),
    url(res:///fonts/normal/SongTi);*/
}
@font-face {
    font-family:"zw-himalaya";
    src:
    local("Himalaya"),
    local("DK-SONGTI"),
    url(../Fonts/zw-himalaya.ttf),
    url(res:///opt/sony/ebook/FONT/zw-himalaya.ttf),
    url(res:///Data/FONT/zw-himalaya.ttf),
    url(res:///opt/sony/ebook/FONT/zw-himalaya.ttf),
    url(res:///ebook/fonts/../../mnt/sdcard/fonts/zw-himalaya.ttf),
    url(res:///ebook/fonts/../../mnt/extsd/fonts/zw-himalaya.ttf),
    url(res:///ebook/fonts/zw-himalaya.ttf),
    url(res:///ebook/fonts/DroidSansFallback.ttf),
    url(res:///fonts/ttf/zw-himalaya.ttf),
    url(res:///../../media/mmcblk0p1/fonts/zw-himalaya.ttf),
    url(file:///mnt/us/DK_System/system/fonts/zw-himalaya.ttf),
    url(file:///mnt/us/DK_System/xKindle/res/userfonts/zw-himalaya.ttf),
    url(res:///mnt/us/fonts/zw-himalaya.ttf),
    url(res:///abook/fonts/zw-himalaya.ttf),
    url(res:///system/fonts/zw-himalaya.ttf),
    url(res:///system/media/sdcard/fonts/zw-himalaya.ttf),
    url(res:///media/fonts/zw-himalaya.ttf),
    url(res:///sdcard/fonts/zw-himalaya.ttf),
    url(res:///system/fonts/DroidSansFallback.ttf),
    url(res:///mnt/MOVIFAT/font/zw-himalaya.ttf),
    url(res:///media/flash/fonts/zw-himalaya.ttf),
    url(res:///media/sd/fonts/zw-himalaya.ttf),
    url(res:///opt/onyx/arm/lib/fonts/AdobeHeitiStd-Regular.otf),
    url(res:///../../fonts/zw-himalaya.ttf),
    url(res:///../fonts/zw-himalaya.ttf),
    url(../../../../../zw-himalaya.ttf),
    url(res:///mnt/sdcard/fonts/zw-himalaya.ttf),
    url(res:///fonts/zw-himalaya.ttf),
    url(res:///../../../../Windows/fonts/zw-himalaya.ttf);/*,
    url(res:///fonts/normal/zw-himalaya);*/
}

@font-face {
    font-family:"fs";
    src:
    local("仿宋"),local("仿宋_GB2312"),
    local("Yuanti"),local("Yuanti SC"),local("Yuanti TC"),
    local("STYuan"),
    local("DK-FANGSONG"),
    url(../Fonts/fs.ttf),
    url(res:///opt/sony/ebook/FONT/fs.ttf),
    url(res:///Data/FONT/fs.ttf),
    url(res:///opt/sony/ebook/FONT/tt0011m_.ttf),
    url(res:///ebook/fonts/../../mnt/sdcard/fonts/fs.ttf),
    url(res:///ebook/fonts/../../mnt/extsd/fonts/fs.ttf),
    url(res:///ebook/fonts/fs.ttf),
    url(res:///ebook/fonts/DroidSansFallback.ttf),
    url(res:///fonts/ttf/fs.ttf),
    url(res:///../../media/mmcblk0p1/fonts/fs.ttf),
    url(file:///mnt/us/DK_System/system/fonts/fs.ttf),
    url(file:///mnt/us/DK_System/xKindle/res/userfonts/fs.ttf),
    url(res:///mnt/us/fonts/fs.ttf),
    url(res:///abook/fonts/fs.ttf),
    url(res:///system/fonts/fs.ttf),
    url(res:///system/media/sdcard/fonts/fs.ttf),
    url(res:///media/fonts/fs.ttf),
    url(res:///sdcard/fonts/fs.ttf),
    url(res:///system/fonts/DroidSansFallback.ttf),
    url(res:///mnt/MOVIFAT/font/fs.ttf),
    url(res:///media/flash/fonts/fs.ttf),
    url(res:///media/sd/fonts/fs.ttf),
    url(res:///opt/onyx/arm/lib/fonts/AdobeHeitiStd-Regular.otf),
    url(res:///../../fonts/fs.ttf),
    url(res:///../fonts/fs.ttf),
    url(../../../../../fs.ttf),
    url(res:///mnt/sdcard/fonts/fs.ttf),
    url(res:///fonts/fs.ttf),
    url(res:///../../../../Windows/fonts/fs.ttf);/*,
    url(res:///fonts/normal/fs),
    url(res:///fonts/normal/FangSong);*/

}
@font-face {
    font-family:"kt";
    src:
    local("楷体"),local("楷体_GB2312"),
    local("Kaiti"),local("Kaiti SC"),local("Kaiti TC"),
    local("MKai PRC"),local("MKaiGB18030C-Medium"),local("MKaiGB18030C-Bold"),local("STKai"),
    local("DK-KAITI"),
    url(../Fonts/kt.ttf),
    url(res:///opt/sony/ebook/FONT/kt.ttf),
    url(res:///Data/FONT/kt.ttf),
    url(res:///opt/sony/ebook/FONT/tt0011m_.ttf),
    url(res:///ebook/fonts/../../mnt/sdcard/fonts/kt.ttf),
    url(res:///ebook/fonts/../../mnt/extsd/fonts/kt.ttf),
    url(res:///ebook/fonts/kt.ttf),
    url(res:///ebook/fonts/DroidSansFallback.ttf),
    url(res:///fonts/ttf/kt.ttf),
    url(res:///../../media/mmcblk0p1/fonts/kt.ttf),
    url(file:///mnt/us/DK_System/system/fonts/kt.ttf),
    url(file:///mnt/us/DK_System/xKindle/res/userfonts/kt.ttf),
    url(res:///mnt/us/fonts/kt.ttf),
    url(res:///abook/fonts/kt.ttf),
    url(res:///system/fonts/kt.ttf),
    url(res:///system/media/sdcard/fonts/kt.ttf),
    url(res:///media/fonts/kt.ttf),
    url(res:///sdcard/fonts/kt.ttf),
    url(res:///system/fonts/DroidSansFallback.ttf),
    url(res:///mnt/MOVIFAT/font/kt.ttf),
    url(res:///media/flash/fonts/kt.ttf),
    url(res:///media/sd/fonts/kt.ttf),
    url(res:///opt/onyx/arm/lib/fonts/AdobeHeitiStd-Regular.otf),
    url(res:///../../fonts/kt.ttf),
    url(res:///../fonts/kt.ttf),
    url(../../../../../kt.ttf),
    url(res:///mnt/sdcard/fonts/kt.ttf),
    url(res:///fonts/kt.ttf),
    url(res:///../../../../Windows/fonts/kt.ttf);/*,
    url(res:///fonts/normal/kt),
    url(res:///fonts/normal/KaiTi);*/
}
@font-face {
    font-family:"ktpy";
    src:
    local("方正楷体拼音字库01"),
    local("Kaitipinyin"),local("Kaiti"),local("Kaiti SC"),local("Kaiti TC"),
    local("MKai PRC"),local("MKaiGB18030C-Medium"),local("MKaiGB18030C-Bold"),local("STKai"),
    local("DK-KAITI"),
    url(../Fonts/ktpy.ttf),
    url(res:///opt/sony/ebook/FONT/ktpy.ttf),
    url(res:///Data/FONT/ktpy.ttf),
    url(res:///opt/sony/ebook/FONT/tt0011m_.ttf),
    url(res:///ebook/fonts/../../mnt/sdcard/fonts/ktpy.ttf),
    url(res:///ebook/fonts/../../mnt/extsd/fonts/ktpy.ttf),
    url(res:///ebook/fonts/ktpy.ttf),
    url(res:///ebook/fonts/DroidSansFallback.ttf),
    url(res:///fonts/ttf/ktpy.ttf),
    url(res:///../../media/mmcblk0p1/fonts/ktpy.ttf),
    url(file:///mnt/us/DK_System/system/fonts/ktpy.ttf),
    url(file:///mnt/us/DK_System/xKindle/res/userfonts/ktpy.ttf),
    url(res:///mnt/us/fonts/ktpy.ttf),
    url(res:///abook/fonts/ktpy.ttf),
    url(res:///system/fonts/ktpy.ttf),
    url(res:///system/media/sdcard/fonts/ktpy.ttf),
    url(res:///media/fonts/ktpy.ttf),
    url(res:///sdcard/fonts/ktpy.ttf),
    url(res:///system/fonts/DroidSansFallback.ttf),
    url(res:///mnt/MOVIFAT/font/ktpy.ttf),
    url(res:///media/flash/fonts/ktpy.ttf),
    url(res:///media/sd/fonts/ktpy.ttf),
    url(res:///opt/onyx/arm/lib/fonts/AdobeHeitiStd-Regular.otf),
    url(res:///../../fonts/ktpy.ttf),
    url(res:///../fonts/ktpy.ttf),
    url(../../../../../ktpy.ttf),
    url(res:///mnt/sdcard/fonts/ktpy.ttf),
    url(res:///fonts/ktpy.ttf),
    url(res:///../../../../Windows/fonts/ktpy.ttf);/*,
    url(res:///fonts/normal/ktpy),
    url(res:///fonts/normal/kaitipinyin),
    url(res:///fonts/normal/KaiTiPinYin);*/
}
@font-face {
    font-family:"ht";
    src:
    local("微软雅黑"),local("黑体"),
    local("Heiti"),local("Heiti SC"),local("Heiti TC"),
    local("MYing Hei S"),local("MYing Hei T"),local("TBGothic"),
    local("DK-HEITI"),
    url(../Fonts/ht.ttf),
    url(res:///opt/sony/ebook/FONT/ht.ttf),
    url(res:///Data/FONT/ht.ttf),
    url(res:///opt/sony/ebook/FONT/tt0011m_.ttf),
    url(res:///ebook/fonts/../../mnt/sdcard/fonts/ht.ttf),
    url(res:///ebook/fonts/../../mnt/extsd/fonts/ht.ttf),
    url(res:///ebook/fonts/ht.ttf),
    url(res:///ebook/fonts/DroidSansFallback.ttf),
    url(res:///fonts/ttf/ht.ttf),
    url(res:///../../media/mmcblk0p1/fonts/ht.ttf),
    url(file:///mnt/us/DK_System/system/fonts/ht.ttf),
    url(file:///mnt/us/DK_System/xKindle/res/userfonts/ht.ttf),
    url(res:///mnt/us/fonts/ht.ttf),
    url(res:///abook/fonts/ht.ttf),
    url(res:///system/fonts/ht.ttf),
    url(res:///system/media/sdcard/fonts/ht.ttf),
    url(res:///media/fonts/ht.ttf),
    url(res:///sdcard/fonts/ht.ttf),
    url(res:///system/fonts/DroidSansFallback.ttf),
    url(res:///mnt/MOVIFAT/font/ht.ttf),
    url(res:///media/flash/fonts/ht.ttf),
    url(res:///media/sd/fonts/ht.ttf),
    url(res:///opt/onyx/arm/lib/fonts/AdobeHeitiStd-Regular.otf),
    url(res:///../../fonts/ht.ttf),
    url(res:///../fonts/ht.ttf),
    url(../../../../../ht.ttf),
    url(res:///mnt/sdcard/fonts/ht.ttf),
    url(res:///fonts/ht.ttf),
    url(res:///../../../../Windows/fonts/ht.ttf);/*,
    url(res:///fonts/normal/ht),
    url(res:///fonts/normal/HeiTi);*/
}
@font-face {
    font-family:"h1";
    src:
    local("方正兰亭特黑长_GBK"),local("方正兰亭特黑长简体"),local("方正兰亭特黑长繁体"),
    local("LantingTeheichang"),
    local("Yuanti"),local("Yuanti SC"),local("Yuanti TC"),
    local("MYing Hei S"),local("MYing Hei T"),local("TBGothic"),
    local("DK-HEITI"),
    url(../Fonts/h1.ttf),
    url(res:///opt/sony/ebook/FONT/h1.ttf),
    url(res:///Data/FONT/h1.ttf),
    url(res:///opt/sony/ebook/FONT/tt0011m_.ttf),
    url(res:///ebook/fonts/../../mnt/sdcard/fonts/h1.ttf),
    url(res:///ebook/fonts/../../mnt/extsd/fonts/h1.ttf),
    url(res:///ebook/fonts/h1.ttf),
    url(res:///ebook/fonts/DroidSansFallback.ttf),
    url(res:///fonts/ttf/h1.ttf),
    url(res:///../../media/mmcblk0p1/fonts/h1.ttf),
    url(file:///mnt/us/DK_System/system/fonts/h1.ttf),
    url(file:///mnt/us/DK_System/xKindle/res/userfonts/h1.ttf),
    url(res:///mnt/us/fonts/h1.ttf),
    url(res:///abook/fonts/h1.ttf),
    url(res:///system/fonts/h1.ttf),
    url(res:///system/media/sdcard/fonts/h1.ttf),
    url(res:///media/fonts/h1.ttf),
    url(res:///sdcard/fonts/h1.ttf),
    url(res:///system/fonts/DroidSansFallback.ttf),
    url(res:///mnt/MOVIFAT/font/h1.ttf),
    url(res:///media/flash/fonts/h1.ttf),
    url(res:///media/sd/fonts/h1.ttf),
    url(res:///opt/onyx/arm/lib/fonts/AdobeHeitiStd-Regular.otf),
    url(res:///../../fonts/h1.ttf),
    url(res:///../fonts/h1.ttf),
    url(../../../../../h1.ttf),
    url(res:///mnt/sdcard/fonts/h1.ttf),
    url(res:///fonts/h1.ttf),
    url(res:///../../../../Windows/fonts/h1.ttf);/*,
    url('res:///fonts/normal/h1'),
    url('res:///fonts/normal/TeHeiChang'),
    url('res:///fonts/normal/h1 TeHeiChang');*/
}
@font-face {
    font-family:"h2";
    src:
    local("方正大标宋_GBK"),local("方正大标宋简体"),local("方正大标宋繁体"),
    local("Dabiaosong"),
    local("Songti"),local("Songti SC"),local("Songti TC"),
    local("HYMyeongJo"),local("STSong"),local("Song S"),local("Song T"),local("STBShusong"),local("TBMincho"),local("HYMyeongJo"),
    local("DK-XIAOBIAOSONG"),
    url(../Fonts/h2.ttf),
    url(res:///opt/sony/ebook/FONT/h2.ttf),
    url(res:///Data/FONT/h2.ttf),
    url(res:///opt/sony/ebook/FONT/tt0011m_.ttf),
    url(res:///ebook/fonts/../../mnt/sdcard/fonts/h2.ttf),
    url(res:///ebook/fonts/../../mnt/extsd/fonts/h2.ttf),
    url(res:///ebook/fonts/h2.ttf),
    url(res:///ebook/fonts/DroidSansFallback.ttf),
    url(res:///fonts/ttf/h2.ttf),
    url(res:///../../media/mmcblk0p1/fonts/h2.ttf),
    url(file:///mnt/us/DK_System/system/fonts/h2.ttf),
    url(file:///mnt/us/DK_System/xKindle/res/userfonts/h2.ttf),
    url(res:///mnt/us/fonts/h2.ttf),
    url(res:///abook/fonts/h2.ttf),
    url(res:///system/fonts/h2.ttf),
    url(res:///system/media/sdcard/fonts/h2.ttf),
    url(res:///media/fonts/h2.ttf),
    url(res:///sdcard/fonts/h2.ttf),
    url(res:///system/fonts/DroidSansFallback.ttf),
    url(res:///mnt/MOVIFAT/font/h2.ttf),
    url(res:///media/flash/fonts/h2.ttf),
    url(res:///media/sd/fonts/h2.ttf),
    url(res:///opt/onyx/arm/lib/fonts/AdobeHeitiStd-Regular.otf),
    url(res:///../../fonts/h2.ttf),
    url(res:///../fonts/h2.ttf),
    url(../../../../../h2.ttf),
    url(res:///mnt/sdcard/fonts/h2.ttf),
    url(res:///fonts/h2.ttf),
    url(res:///../../../../Windows/fonts/h2.ttf);/*,
    url('res:///fonts/normal/h2'),
    url('res:///fonts/normal/DaBiaoSong'),
    url('res:///fonts/normal/h2 DaBiaoSong');*/
}
@font-face {
    font-family:"h3";
    src:
    local("方正华隶_GBK"),local("方正行黑简体"),local("方正行黑繁体"),
    local("Yuanti"),local("Yuanti SC"),local("Yuanti TC"),
    local("STYuan"),local("MYing Hei S"),local("MYing Hei T"),local("TBGothic"),
    local("DK-FANGSONG"),
    url(../Fonts/h3.ttf),
    url(res:///opt/sony/ebook/FONT/h3.ttf),
    url(res:///Data/FONT/h3.ttf),
    url(res:///opt/sony/ebook/FONT/tt0011m_.ttf),
    url(res:///ebook/fonts/../../mnt/sdcard/fonts/h3.ttf),
    url(res:///ebook/fonts/../../mnt/extsd/fonts/h3.ttf),
    url(res:///ebook/fonts/h3.ttf),
    url(res:///ebook/fonts/DroidSansFallback.ttf),
    url(res:///fonts/ttf/h3.ttf),
    url(res:///../../media/mmcblk0p1/fonts/h3.ttf),
    url(file:///mnt/us/DK_System/system/fonts/h3.ttf),
    url(file:///mnt/us/DK_System/xKindle/res/userfonts/h3.ttf),
    url(res:///mnt/us/fonts/h3.ttf),
    url(res:///abook/fonts/h3.ttf),
    url(res:///system/fonts/h3.ttf),
    url(res:///system/media/sdcard/fonts/h3.ttf),
    url(res:///media/fonts/h3.ttf),
    url(res:///sdcard/fonts/h3.ttf),
    url(res:///system/fonts/DroidSansFallback.ttf),
    url(res:///mnt/MOVIFAT/font/h3.ttf),
    url(res:///media/flash/fonts/h3.ttf),
    url(res:///media/sd/fonts/h3.ttf),
    url(res:///opt/onyx/arm/lib/fonts/AdobeHeitiStd-Regular.otf),
    url(res:///../../fonts/h3.ttf),
    url(res:///../fonts/h3.ttf),
    url(../../../../../h3.ttf),
    url(res:///mnt/sdcard/fonts/h3.ttf),
    url(res:///fonts/h3.ttf),
    url(res:///../../../../Windows/fonts/h3.ttf);/*,
    url('res:///fonts/normal/h3'),
    url('res:///fonts/normal/HuaLi'),
    url('res:///fonts/normal/h3 HuaLi');*/
}
/*↑↑老牛字体样式3.1.0↑↑*/
/*↑↑欢迎非商业性使用，但请注明"老牛字体样式"；商业使用请与老牛联系↑↑*/


/* 页面*/
@page {
    margin-top: 0px;
    margin-bottom: 0px;
    margin-left: 10px;
    margin-right: 10px;
}

body {
    padding: 0px;
    margin-top: 0px;
    margin-bottom: 0px;
    margin-left: 10px;
    margin-right: 10px;
    line-height:130%;
    text-align: justify;
    font-family:"zw","宋体","明体","明朝",serif;
    font-size:97%;
}
div {
    margin:0px;
    padding:0px;
    line-height:130%;
    text-align: justify;
    font-family:"zw","宋体","明体","明朝",serif;
}

p {
    text-align: justify;
    text-indent: 2em; 
    line-height: 130%;
    font-family: "zw","宋体","明体","明朝",serif;
    margin-top: 0px;
    margin-bottom: 0px;
}
a{
    text-decoration:none;
}
a:link {
      color:black;
}

/*首字上升Initial Raise*/
.raise:first-letter {
    font-size:2em;
    font-weight:bold;
}
.initialraise {
    font-size:2em;
    font-weight:bold;
}
/*首字下沉Initial Sinking*/
.sinking:first-letter  {
    font-family: "ht","微软雅黑","黑体","MYing Hei S","MYing Hei T","TBGothic","zw",sans-serif;
    font-size:1.618em;
    float:left;
    margin:5px; /*0.3em 5px 0px 0px;*/
    padding:3px;
    text-indent: 0em!important;
}
.initialsinking {
    font-family: "ht","微软雅黑","黑体","MYing Hei S","MYing Hei T","TBGothic","zw",sans-serif;
    font-size:1.618em;
    float:left;
    margin:5px; /*0.3em 5px 0px 0px;*/
    padding:3px;
    text-indent: 0em!important;
}
.center {
    text-align:center;
}
.left {
    text-align:left;
}
.right {
    text-align:right;
}
.block {
    display:block;
}
sub {
    font-size: 0.75em;
    line-height: 1.2;
    vertical-align: sub;
}
sup {
    font-size: 0.75em;
    line-height: 1.2;
    vertical-align: super;
}
.italic {
    font-style: italic;
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
}
.underline {
    text-decoration: underline;
}
/*正文中的分隔线*/
.divline {
    text-align: center;
    color:gray;
}

/*图片*/
img {
    border:none;
}
.image_left {
    float:left;
    max-width: 60%;
}
.image_right {
    float:right;
    max-width: 60%;
}

/*表格*/
table{
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
    width: 99%;
    vertical-align:center;
    padding:2px 2px 2px 2px;
    border-collapse:collapse;
    border:1px solid #000;
}

h1 {
    float:right;
    text-align:right;
    height:2.4em;
    color: #985C00;
    font-size:1.65em;
    line-height:130%;
    border-width: 0.1em;
    border-style:  none solid none none;
    border-color: #985C00;
    margin:20% 0.4em 0 0;
    padding:0 0.4em 0 0;    
    text-indent: 0em; 
    font-family: "h2","方正大标宋_GBK","方正大标宋简体","方正大标宋繁体","微软雅黑","黑体","zw",sans-serif;
}

h2 {
    margin-bottom:0.5em;
    line-height:130%;
    text-align: justify;
    padding: 5px 5px 5px 5px;
    color: #985CFF;
    border-width: 0.1em;
    border-style: none none dotted none;
    border-color: #985CFF;
    font-weight:bold;
    font-size:1.5em;
    font-family: "h2","方正大标宋_GBK","方正大标宋简体","方正大标宋繁体","微软雅黑","黑体","zw",sans-serif;
    text-indent: 0em; 
}

h3 {
    line-height:130%;
    text-align: left;
    font-weight:bold;
    font-size:1.2em;
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
    margin-top:1em;
    color: midnightblue;
    border-width: 0.3em 0.08em 0em 0.35em;
    border-style: double double double double;
    border-color: purple;
    margin-left:0%;
    margin-right:0%;
    text-indent: 0em; 
}

h4 {
    line-height:130%;
    text-align: center;
    font-weight:bold;
    font-size:100%;
    font-family: "ht","微软雅黑","黑体","zw",sans-serif;
    margin-top:0.5em;
    margin-bottom:0.5em;
    text-indent: 0em; 
}

h5 {
    line-height:130%;
    text-align: justify;
    font-weight:bold;
    font-size:medium;
    font-family:"zw","宋体","明体","明朝",serif;
    margin-top:0.5em;
    margin-bottom:0.5em;
    text-indent: 0em; 
}

h6 {
    line-height:130%;
    text-align: justify;
    font-weight:bold;
    font-size:small;
    margin-top:0.5em;
    margin-bottom:0.5em;
    text-indent: 0em; 
}

.P_Normal {
    text-align: justify;
    font-family: "zw","宋体","明体","明朝",serif;
}

.P_Body_Text {
    text-align: justify;
    text-indent: 0em; 
    line-height: 130%;
    font-family: "zw","宋体","明体","明朝",serif;
    margin-top: 0px;
    margin-bottom: 0px;
}

.P_Body_Text_First_Indent {
text-indent: 2em;
}

.P_Heading_1 {
    float:right;
    text-align:right;
    height:2.4em;
    color: #985C00;
    font-size:1.65em;
    line-height:130%;
    border-width: 0.1em;
    border-style:  none solid none none;
    border-color: #985C00;
    margin:20% 0.4em 0 0;
    padding:0 0.4em 0 0;    
    text-indent: 0em; 
    font-family: "h2","方正大标宋_GBK","方正大标宋简体","方正大标宋繁体","微软雅黑","黑体","zw",sans-serif;
}

.P_Heading_2 {
    margin-bottom:0.5em;
    line-height:130%;
    text-align: justify;
    padding: 5px 5px 5px 5px;
    color: #985C00;
    border-width: 0.1em;
    border-style: none none solid none;
    border-color: #985C00;
    font-weight:bold;
    font-size:1.5em;
    font-family: "h2","方正大标宋_GBK","方正大标宋简体","方正大标宋繁体","微软雅黑","黑体","zw",sans-serif;
    text-indent: 0em; 
}

.P_Heading_3 {
    line-height:130%;
    text-align: center;
    font-weight:bold;
    font-size:1.2em;
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
    margin-top:1em;
    color: #985C00;
    border-width: 0.1em;
    border-style: solid none;
    border-color: #985C00;
    margin-left:5%;
    margin-right:5%;
    text-indent: 0em; 
}

.P_Heading_4 {
    line-height:130%;
    text-align: center;
    font-weight:bold;
    font-size:100%;
    font-family: "ht","微软雅黑","黑体","zw",sans-serif;
    margin-top:0.5em;
    margin-bottom:0.5em;
    text-indent: 0em; 
}

.P_Heading_5 {
    line-height:130%;
    text-align: justify;
    font-weight:bold;
    font-size:medium;
    font-family:"zw","宋体","明体","明朝",serif;
    margin-top:0.5em;
    margin-bottom:0.5em;
    text-indent: 0em; 
}

.P_Heading_6 {
    line-height:130%;
    text-align: justify;
    font-weight:bold;
    font-size:small;
    margin-top:0.5em;
    margin-bottom:0.5em;
    text-indent: 0em; 
}

.P_Headers {
font-size: 1.00em;
text-align: center;
margin-top: 0.00em;
margin-bottom: 0.00em;
margin-left: 0.00em;
margin-right: 0.00em;
text-indent: 0.00em;
}

.P_Footers {
font-size: 1.00em;
text-align: right;
margin-top: 0.00em;
margin-bottom: 0.00em;
margin-left: 0.00em;
margin-right: 0.00em;
text-indent: 0.00em;
}

.P_HTML {
font-size: 0.83em;
text-align: left;
margin-top: 0.00em;
margin-bottom: 0.00em;
margin-left: 0.00em;
margin-right: 0.00em;
text-indent: 0.00em;
}

.P_Preformatted {
font-size: 0.83em;
text-align: left;
margin-top: 0.00em;
margin-bottom: 0.00em;
margin-left: 0.00em;
margin-right: 0.00em;
text-indent: 0.00em;
}

.P_Centre {
text-align: center;
text-indent: 0em!important;
}

.P_Right {
text-align: right;
text-indent: 0.00em;
}

.P_TOC_Heading {
    margin-bottom:0.5em;
    line-height:130%;
    text-align: justify;
    padding: 5px 5px 10px 5px;
    page-break-before:always;
    font-weight:bold;
    font-size:1.5em;
    font-family: "h2","方正大标宋_GBK","方正大标宋简体","方正大标宋繁体","微软雅黑","黑体","zw",sans-serif;
text-indent: 0.00em;
}

.P_TOC_Entry_1 {
font-weight: bold;
font-size: 1.00em;
text-align: left;
margin-top: 0.5em;
margin-bottom: 0.00em;
margin-left: 1.20em;
margin-right: 0.00em;
text-indent: 0.00em;
text-align: center;
font-family:"h2","方正大标宋_GBK","方正大标宋简体","方正大标宋繁体","微软雅黑","黑体","zw",sans-serif;
}

.P_TOC_Entry_2 {
font-weight: bold;
font-size: 1.00em;
text-align: left;
margin-top: 0.5em;
margin-bottom: 0.00em;
margin-left: 2.40em;
margin-right: 0.00em;
text-indent: 0.00em;
font-family:"华文中宋","zw","宋体","明体",serif;
}

.P_TOC_Entry_3 {
font-weight: bold;
font-size: 1.00em;
text-align: left;
margin-top: 0.5em;
margin-bottom: 0.00em;
margin-left: 3.60em;
margin-right: 0.00em;
text-indent: 0.00em;
font-family:"kt","楷体","楷体_gb2312","zw",serif;
}

.P_TOC_Entry_4 {
font-weight: bold;
font-family: "zw","宋体","明体","明朝" "Times New Roman",serif;
font-size: 1.00em;
text-align: left;
margin-top: 0.5em;
margin-bottom: 0.00em;
margin-left: 4.80em;
margin-right: 0.00em;
text-indent: 0.00em;
}

.P_TOC_Entry_5 {
font-weight: bold;
font-family: "zw","宋体","明体","明朝" "Times New Roman",serif;
font-size: 1.00em;
text-align: left;
margin-top: 0.5em;
margin-bottom: 0.00em;
margin-left: 6.00em;
margin-right: 0.00em;
text-indent: 0.00em;
}

.P_TOC_Entry_6 {
font-weight: bold;
font-family: "zw","宋体","明体","明朝" "Times New Roman",serif;
font-size: 1.00em;
text-align: left;
margin-top: 0.50em;
margin-bottom: 0.00em;
margin-left: 7.20em;
margin-right: 0.00em;
text-indent: 0.00em;
}

.P_Index_Heading {
font-weight: bold;
font-size: 1.33em;
text-align: justify;
margin-top: 0.00em;
margin-bottom: 1.20em;
margin-left: 0.00em;
margin-right: 0.00em;
text-indent: 0.00em;
}

.P_Index_Group_Heading {
font-weight: bold;
font-size: 1.17em;
text-align: justify;
margin-top: 1.20em;
margin-bottom: 1.20em;
margin-left: 0.00em;
margin-right: 0.00em;
text-indent: 0.00em;
}

.P_Index_Entry_1 {
font-size: 1.00em;
text-align: justify;
margin-top: 0.00em;
margin-bottom: 0.00em;
margin-left: 1.20em;
margin-right: 0.00em;
text-indent: 0.00em;
}

.P_Index_Entry_2 {
font-size: 1.00em;
text-align: justify;
margin-top: 0.00em;
margin-bottom: 0.00em;
margin-left: 2.40em;
margin-right: 0.00em;
text-indent: 0.00em;
}

.P_Index_Entry_3 {
font-size: 1.00em;
text-align: justify;
margin-top: 0.00em;
margin-bottom: 0.00em;
margin-left: 3.60em;
margin-right: 0.00em;
text-indent: 0.00em;
}

.P_Endnotes_Heading {
    margin-bottom:0.5em;
    line-height:130%;
    text-align: justify;
    padding: 5px 5px 10px 5px;
    page-break-before:always;
    font-weight:bold;
    font-size:1.5em;
    font-family: "h2","方正大标宋_GBK","方正大标宋简体","方正大标宋繁体","微软雅黑","黑体","zw",sans-serif;
text-indent: 0.00em;
}

.P_Footnote {
    text-align: justify;
    text-indent: 0em; 
    line-height: 110%;
    font-size: 0.85em;
    font-family: "zw","宋体","明体","明朝",serif;
}

.P_Endnotes_Group {
font-size: 1.17em;
text-align: center;
margin-top: 0.00em;
margin-bottom: 0.00em;
margin-left: 0.00em;
margin-right: 0.00em;
text-indent: 0.00em;
}

.P_Bookname {
    margin-top:10%;
    text-align: center;
    padding:2px 0px 2px 5px;
    font-size:xx-large;
    font-family:"h2","方正大标宋_GBK","方正大标宋简体","方正大标宋繁体","微软雅黑","黑体","zw",sans-serif;
    text-indent: 0em; 
}
.P_Only_Epub {
font-size: 1.00em;
text-align: justify;
margin-top: 0.00em;
margin-bottom: 0.00em;
margin-left: 0.00em;
margin-right: 0.00em;
text-indent: 0.00em;
}

.P_Quote {
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
    margin-left:2em;
}

.P_Booksubtitle {
    margin-top:1em;
    margin-left:50%;
    text-align: justify;
    font-size:1.2em;
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
    text-indent: 0em; 
}

.P_Author {
    margin-top:2em;
    text-align: center;
    text-indent: 0em; 
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
}

.P_Publisher {
    margin-top:30%;
    font-family:"ht","微软雅黑","黑体","zw",sans-serif;
    text-align: center;
    text-indent: 0em; 
}

.P_Pubdate {
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
    text-align: center;
    text-indent: 0em; 
}

.P_Preface {
    font-family:"fs","仿宋","仿宋_gb2312","zw",serif;
}

.P_Signature {
    padding-right:2em;
    text-align: right;
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
    text-indent: 0em; 
}

.P_Date {
font-family:"kt","楷体","楷体_gb2312","zw",serif;
text-align: right;
margin-top: 0.5em;
padding-right:2em;
text-indent: 0.00em;
}

.P_H1note {
    clear:both;
    padding-top:2em;
    margin-left:20%;
    margin-right:0;
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
}
.P_H1note :first-child {margin-top:1.2em;}
.P_H1note :last-child {margin-bottom:1.2em;}

.P_H2note {
    margin-left:2em;
    margin-right:2em;
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
}
.P_H2note :first-child {margin-top:1.2em;}
.P_H2note :last-child {margin-bottom:1.2em;}
.P_H3note {
    margin-left:2em;
    margin-right:2em;
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
}
.P_H3note :first-child {margin-top:1.2em;}
.P_H3note :last-child {margin-bottom:1.2em;}
.P_Quote_Heading {
    line-height:130%;
    text-align: center;
    font-weight:bold;
    font-size:1.2em;
    font-family: "ht","微软雅黑","黑体","zw",sans-serif;
    margin-top:1em;
    margin-bottom:0.5em;
    text-indent: 0em; 
}

.P_Box_Heading {
    line-height:130%;
    margin-left: 2em;
    margin-right: 2em;
    margin-bottom:0;
    padding:5px;
    background:#999;
    text-align: center;
    font-family:"ht","微软雅黑","黑体","zw",sans-serif;
    text-indent: 0em; 
}

.P_Box {
    margin-left: 2em;
    margin-right: 2em;
    padding:5px;
    background:#DDD;
    text-align: justify;
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
}

.P_Image {
    margin-left:0.2em;
    margin-right:0.2em;
    text-align:center;
    padding:0px;
    width:100%;
text-indent: 0em!important;
}

.P_ImageNote {
    margin-top:0em;
    margin-left:1em;
    margin-right:1em;
    margin-bottom:1em;
    text-align:center;
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
    font-size:small;
    padding: 5px 0px 5px 5px;
text-indent: 0em!important;
}

.P_CIP_Bookname {
    padding: 20px 0px 5px 0px;
    font-weight:bold;
    font-size:1.2em;
    font-family:"ht","微软雅黑","黑体","zw",sans-serif;
    text-indent: 0em!important;
}

.P_CIP_Author {
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
    text-indent: 1em!important;
    padding: 0px 0px 5px 0px;
}

.P_CIP_Translator {
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
    text-indent: 1em!important;
    padding: 0px 0px 5px 0px;
}

.P_CIP_Publisher {
    font-family:"zw","宋体","明体",sans-serif;
    text-indent: 0em!important;
    line-height:100%;
    font-weight: bold;
    padding:5px 0px 0.5em 0px;
}

.P_CIP_Heading {
    padding:5px 0px 10px 0px;
    font-family:"ht","微软雅黑","黑体","zw",sans-serif;
    font-size:1.2em;
    list-style-type:none;
    text-indent: 0em!important;
}

.P_CIP_Smalltext {
    text-align: justify;
    font-family:"zw","宋体","明体",sans-serif;
    font-size:90%;
    text-indent: 0em!important;
}

.P_CIP_Number {
    padding:0.5em 0 0 0;
    text-indent: 0em!important;
}

.P_CIP_Text {
    font-family:"zw","宋体","明体",sans-serif;
    text-indent: 0em!important;
}

.P_Footnote_text {
font-size: 0.75em;
text-align: left;
margin-top: 0.00em;
margin-bottom: 0.00em;
margin-left: 0.00em;
margin-right: 0.00em;
text-indent: 0.00em;
}

.P_BookAuthor {
font-family:"kt","楷体","楷体_gb2312","zw",serif;
font-size: 1.2em;
text-align: center;
margin-top: 2em;
text-indent: 0.00em;
}

.P_BookTranslator {
font-family:"kt","楷体","楷体_gb2312","zw",serif;
font-size: 1.2em;
text-align: center;
margin-top: 0.5em;
text-indent: 0.00em;
}

.P_Subtitle {
    margin-top:1em;
    margin-left:50%;
    text-align: justify;
    font-size:1em;
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
    text-indent: 0em; 
}

.P_Annotation_text {
font-family:"kt","楷体","楷体_gb2312","zw",serif;font-size: 0.8em;
}

.P_Note_Heading {
    margin-top:30pt;
    margin-bottom:0.5em;
    font-family:"ht","微软雅黑","黑体","zw",sans-serif;
}

.P_Title {
    line-height:130%;
    text-align: center;
    font-weight:bold;
    font-size:1.2em;
    font-family: "ht","微软雅黑","黑体","zw",sans-serif;
    margin-top:1em;
    margin-bottom:0.5em;
text-indent: 0.00em;
}

.P_Intense_Quote {
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
    margin-left:2em;
    margin-right: 2em;
    padding:5px;
    background:#DDD;
}

.P_Body_Text_2 {
font-size: 1.2em;
}

.P_Body_Text_3 {
font-size: 0.8em;
}

.P_Body_Text_Indent {
font-size: 1.00em;
margin-left: 2em;
}

.P_Body_Text_Indent_2 {
font-size: 0.9em;
margin-left: 4em;
}

.P_Body_Text_Indent_3 {
font-size: 0.8em;
margin-left: 6em;
}

.P_Caption {
font-family:"kt","楷体","楷体_gb2312","zw",serif;
font-size: 0.9em;
text-align: center;
margin-top: 0.5em;
margin-bottom: 0.3em;
text-indent: 0em!important;
}

.P_Comment{
font-family:"kt","楷体","楷体_gb2312","zw",serif;
}
.P_Quote_Centre {
font-family:"kt","楷体","楷体_gb2312","zw",serif;
text-align: center;
text-indent: 0.00em;
}

.P_Dialog_A {
font-family: "zw","宋体","明体","明朝",serif;
margin-left: 4em;
text-indent: -4em;
}

.P_Dialog_B {
font-family:"kt","楷体","楷体_gb2312","zw",sans-serif;
margin-left: 4em;
text-indent: -4em;
}

.P_Text_Centre {
text-align: center;
text-indent: 0.00em;
}

.P_H1num {
    float:right;
    font-size:3em;
    text-align:center;
    width:1.2em;
    height:1.2em;
    background-color:#985C00;
    color:#FFF;
    line-height:1.2em;
    margin-top:20%;
    padding:2px 2px 2px 2px;
    text-indent: 0em; 
    font-family:"h2","方正大标宋_GBK","方正大标宋简体","方正大标宋繁体","微软雅黑","黑体","zw",sans-serif;
}

.P_Normal__And__Left_Alignment {
font-size: 1.00em;
text-align: left;
margin-top: 0.00em;
margin-bottom: 0.00em;
margin-left: 0.00em;
margin-right: 0.00em;
text-indent: 0.00em;
}

.C_Citation {
}

.C_URL {
text-decoration: underline;
color: #0000FF;
}

.C_HTML_Text {
color: #808080;
}

.C_Drop_Caps {
line-height: 90%;
height: 0.75em;
font-size: 280%;
margin-right: 0.075em;
float:left;
}
.C_Small_Caps {
font-size: 10pt;
font-size: 80%;
}

.C_Default_Paragraph_Font {
}

.C_Heavy {
    font-family:"ht","微软雅黑","黑体","zw",sans-serif;
}

.C_URL-noline {
text-decoration: none;
color: #000;
}

.C_Hyperlink {
text-decoration: underline;
color: #0000FF;
}

.C_Intense_Emphasis {
font-family: "ht","微软雅黑","黑体","zw",sans-serif;
color: #0000FF;
}

.C_Subtle_Emphasis {
font-family: "ht","微软雅黑","黑体","zw",sans-serif;
}

.C_Intense_Reference {
text-decoration: underline;
font-family:"kt","楷体","楷体_gb2312","zw",serif;
font-size: 0.9em;
}

.C_HTML_Code {
font-size: 10pt;
}

.C_H1pre {
    margin:0;
    padding:0;
    line-height:100%;
    font-size:0.70em;
    font-family:"kt","楷体","楷体_gb2312","zw",serif;
}

.C_Current__And__Superscript {
font-size: 9pt;
vertical-align: super;
}



            ''')
 
chapters = []
pre_title = ''
now_title = ''
titles = []
content = []
num = 0

with open(txtfile,'rb') as f : bookfile = f.readlines()
for linenum,line in enumerate(bookfile):
    try :
        line = zh2unicode (line).strip()
    except :
        continue
    # comp = re.compile('师士传说.*[正文]*\s*[第终][0123456789一二三四五六七八九十百千万零 　\s]*[章部集节卷]')
    # comp = re.compile('^[正文]*\s*[第终][0123456789一二三四五六七八九十百千万零 　\s]*[章部集节卷].+')
    comp = re.compile('^.*[正文]*\s*[第终][0123456789\- 　\s]*[章].+')

    if re.search(comp,line) and len(line) < 34: 
        pre_title = now_title
        # now_title = line.replace('师士传说','').strip() 
        now_title = line
        print (line)     
        if num == 1 :
            chapters.append((pre_title,content))
            content = []
        if num == 0 and linenum >0:
            chapters.append(('前 言',content))
            content = []
        num =1 
    else :
        if len(line) >0 :
            content.append(line)
chapters.append((now_title,content))
print ('第一个章节：',chapters[0][0])
print ('最后的章节：',chapters[-1][0])
print ('一共有',len(chapters),'个章节。')
# print (chapters[0])
# if not os.path.isfile(coverpage) :
if  os.path.isfile(coverfile) :
    # coverword = '<div style="text-align:center"><img class="cover" src="../images/cover.jpg"/></div>'    
    coverword = '<div class="cover"><img alt="cover"  src="../images/cover.jpg"/></div>'
else :
    coverword =''

with open (coverpage,'w',encoding='utf-8') as f :
    f.write('''<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href="../css/main.css"/>
<title>bookcover</title>

</head>
<body>
%s
</body>
</html>''' % coverword)

with open (jianjiefile,'w',encoding='utf-8') as f :
    f.write('''<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href="../css/main.css"/>
<title>简介</title>
</head>
<body>
<div>
<h1>%s</h1>
<h2>%s</h2>
<b>简介</b>
<p>%s</p>
</div>
</body>
</html>''' % (bookname,author,summary.replace('\n','</p>\n<p>')))

items = ''
itemrefs = ''
navPoints = ''
mulus = ''
for chapternum,chapter in enumerate(chapters):
    pagenum = chapternum +1
    htmlfile = os.path.join(textdir,'chapter'+str(pagenum)+'.html')
    olli = ''
    for ppp in chapter[1] :
        olli += '<p>' + ppp + "</p>\n"
    with open (htmlfile,'w',encoding='utf-8') as f :
        f.write('''<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="builder" content="xzap's txt2epub(python3)"/>
<link rel="stylesheet" type="text/css" href="../css/main.css"/>
<title>%(chaptertitle)s</title>
</head>
<body>
<div>
<h3>%(chaptertitle)s</h3>
%(olli)s
</div>
</body>
</html>''' % {'chaptertitle':chapter[0],'olli' : olli})
    num2 = pagenum + 2
    mulus += '''<p><a href="chapter%(num)s.html">%(chaptertitle)s</a></p>\n''' % {'chaptertitle':chapter[0],'num':pagenum}
    items +='''<item id="chapter%(num)s"  href="text/chapter%(num)s.html"  media-type="application/xhtml+xml"/>\n''' % {'num':pagenum}
    itemrefs +='''<itemref idref="chapter%s" linear="yes"/>\n''' % pagenum
    navPoints += '''    <navPoint id="chapter%(num)s" playOrder="%(num2)s">
        <navLabel><text>%(chaptertitle)s</text></navLabel>
        <content src="text/chapter%(num)s.html"/>
    </navPoint>\n''' % {'chaptertitle':chapter[0],'num':pagenum,'num2':num2}
# print (navPoints)
with open (confile,'w',encoding='utf-8') as f :
    f.write('''<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href="../css/main.css"/>
<title>%s_目录</title>
</head>
<body>
<div>
<p></p>
<p>目录<hr/></p>
<p></p>
%s
</div>
</body>
</html>''' % (bookname,mulus))

with open (contentfile,'w',encoding='utf-8') as f:
    f.write('''<?xml version="1.0" encoding="UTF-8" ?>
<package version="2.0" unique-identifier="PrimaryID" xmlns="http://www.idpf.org/2007/opf">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
<dc:title>%(bookname)s</dc:title>
<dc:identifier opf:scheme="ISBN"></dc:identifier>
<dc:language>zh-CN</dc:language>
<dc:creator>%(author)s</dc:creator>
<dc:publisher>xzap</dc:publisher>
<dc:description>%(summary)s</dc:description>
<dc:coverage></dc:coverage>
<dc:date>%(currenttime)s</dc:date>
<dc:rights>本电子书由xzap制作，仅供交流使用，未经授权，不得用于商业用途。</dc:rights>
<dc:subject></dc:subject>
<dc:contributor></dc:contributor>
<dc:type></dc:type>
<dc:format></dc:format>
<dc:relation></dc:relation>
<dc:builder>xzap txt2epub(python3)</dc:builder>
<dc:builder_version>1.0</dc:builder_version>
<meta name="cover" content="cover-image"/>
<meta property="dcterms:modified">%(currenttime)s</meta>
</metadata>
<manifest>
<!-- Content Documents -->
<item id="main-css" href="css/main.css" media-type="text/css"/>
<item id="coverpage"  href="text/coverpage.html"  media-type="application/xhtml+xml"/>
<item id="summary"  href="text/summary.html"  media-type="application/xhtml+xml"/>
<!-- <item id="content"  href="text/content.html"  media-type="application/xhtml+xml"/> -->
%(items)s
<item id="ncx"  href="toc.ncx" media-type="application/x-dtbncx+xml"/>
<item id="css" href="css/main.css" media-type="text/css"/>
<item id="cover-image" href="images/cover.jpg" media-type="image/jpeg"/>
</manifest>
<spine toc="ncx">
<!-- <itemref idref="coverpage" properties="duokan-page-fullscreen" linear="yes"/> -->
<itemref idref="coverpage" linear="yes"/>

<itemref idref="summary" linear="yes"/>
 <!-- <itemref idref="content" linear="yes"/> -->
%(itemrefs)s
</spine>
<guide>
<reference type="cover" title="封面"  href="text/coverpage.html"/>
</guide>
</package>
        ''' % {'bookname':bookname,
        'author':author,
        'summary':summary,
        'currenttime':currenttime,
        'items':items,
        'itemrefs':itemrefs

        })


with open (tocfile,'w',encoding='utf-8') as f :
    f.write('''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE ncx PUBLIC
     "-//NISO//DTD ncx 2005-1//EN"
     "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">
<ncx version="2005-1"
     xml:lang="en-US"
     xmlns="http://www.daisy.org/z3986/2005/ncx/">
<head>
    <!-- The following four metadata items are required for all
        NCX documents, including those conforming to the relaxed
        constraints of OPS 2.0 -->
    <meta name="dtb:uid" content="%(bookid)s"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
    <meta name="provider" content=""/>
    <meta name="builder" content="xzap txt2epub(python3)"/>
    <meta name="right" content="该文档由xzap制作。仅供个人交流与学习使用，不得用于任何商业用途。"/>
  </head>
<docTitle><text>%(bookname)s</text></docTitle>
<docAuthor><text>%(author)s</text></docAuthor>
<navMap>
    <navPoint id="coverpage" playOrder="0">
        <navLabel><text>封面</text></navLabel>
        <content src="text/coverpage.html"/>
    </navPoint>
    <navPoint id="summary" playOrder="1">
        <navLabel><text>简介</text></navLabel>
        <content src="text/summary.html"/>
    </navPoint>
<!--    <navPoint id="content" playOrder="2">
        <navLabel><text>目录</text></navLabel>
        <content src="text/content.html"/>
    </navPoint> -->
%(navPoints)s
</navMap>
</ncx>''' % {"bookid":bookid,
             "bookname":bookname,
             "author":bookname,
             "navPoints":navPoints})

with zipfile.ZipFile(os.path.join(bookpath, '{bookname}.epub'.format(bookname = bookname)), "w", zipfile.ZIP_DEFLATED) as out:
    for root, dirs, files in os.walk(epubdir):  
        for name in files:  
            
            fname = os.path.join(root, name)
            new_path = os.path.normpath(fname.replace(epubdir,''))
            out.write(fname, new_path)

