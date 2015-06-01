#!/usr/bin/env python


import urllib.request
import os,re
from http import cookiejar
import sys
import json
import gzip

def gdecode(webPage, charset='UTF-8'):
    if webPage.startswith(b'\x1f\x8b'):
        return gzip.decompress(webPage).decode(charset)
    else:
        return webPage.decode(charset)

downfile = os.path.realpath('/data/115pan/115.down')
if os.path.isfile(downfile) : os.remove(downfile)
headers = {
'Host': '115.com',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36',
'Referer': 'http://passport.115.com/?ct=login&ac=logining&goto=http%3A%2F%2F115.com%2F&request_url=http%3A%2F%2F115.com%2F%3Fct%3Dsso%26user_id%3D3024177%26ssostr%3DB4477A17BBD4022WGM44HIHQH49DMMENIJ09TI4HG9DST0HQJMEM9DH1306145228A1%26rsatime%3D1429170317%26rsa%3D43a2e100e1a8b9a7dfc2667be5bbed3bf9c2e5a1%26json%3D',
'Accept-Encoding': 'gzip, deflate, sdch',
'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
'Cookie': '115_lang=zh; loginType=; ssov_3024177=0_3024177_f5de6add724bcfca8110d049ac77e71a; PHPSESSID=h4fbsenhmd1q0hid0s0m37hk91; bank_soopay=25; payment=alipay; UUID=115552F67569AE81; UUTK=fa7848F4UEw%2BOxVcTQ74iGjyWo81Y9Jc905sX7mi7CLTqF3cSwA4ATcDq2SO15BbrHGcU4Nf7XwyBcPquAX%2BoFMHSQzvAZ7DjdYcc; ssoidA1=2a5fae0887c34fe6e5fee83e7c1c43fe60b106d0; ssoinfoA1=3024177%3AA1%3A2061581850; OORA=19228f4e6981e2019049117ea386922939b91446; OOFA=%2506%2507SRWU%2506%250COMY%2512%250CX%2507%2506%2500%2501WS%2509%2505%2502R%2508_S_%2505V%255DP%2505TUV%2507Z%2505UR%2503%250B%2507%250F%255B%2507VS%2500TQ_%2503%2500SSRT%2500; OOFV=00b2a1b56424f4ce743a375060993acddbf283a32790831651b1b297d67bcbc97b1598383af1bd816ad9234f07b663c2; UID=3024177_A1_1429170017; CID=112889c1c5eadfe9c36294a4e22ca7da; SEID=798b5d859eb29b51ad322b5327c8896727f4b0eb229cbca7eed67fd8a6df998208be80964c56eed5fdff6ff4a65eacaf56536216ae5dd4954b9bcf10; OOFL=xzap%40163.com; IM_ALERT_IND=91; 3024177_settings=b6589fc6ab0dc82cf12099d1c2d40ab994e8410c; tjj_repeat=0; tjj_u=1; tjj_id=142917001956987234641; __utmt=1; __utma=48116967.1043189105.1409632571.1429060820.1429170020.34; __utmb=48116967.1.10.1429170020; __utmc=48116967; __utmz=48116967.1413338887.5.4.utmcsr=bbs.fuli.ba|utmccn=(referral)|utmcmd=referral|utmcct=/forum.php'

}

cj = cookiejar.CookieJar()
opener = urllib.request.build_opener()
opener.add_handler(urllib.request.HTTPCookieProcessor(cj))

for v , k in headers.items() :
    opener.addheaders.append((v,k))
urllib.request.install_opener(opener)


url = 'http://web.api.115.com/files?aid=1&cid=321822214725040916&o=user_ptime&asc=0&offset=0&show_dir=1&limit=40&code=&scid=&snap=0&natsort=1&source=&format=json&type=4&star=&is_share='
# url = 'http://web.api.115.com/files?aid=1&cid=487707211703958897&o=user_ptime&asc=0&offset=0&show_dir=1&limit=32&code=&scid=&snap=0&natsort=1&source=&format=json&type=&star=&is_share=&is_q='
# url = 'http://web.api.115.com/files?aid=1&cid=487707211703958897&o=user_ptime&asc=0&offset=0&show_dir=1&limit=32&code=&scid=&snap=0&natsort=1&source=&format=json&type=4&star=&is_share=&is_q='
cc= gdecode(urllib.request.urlopen(url).read())

jc = json.loads(cc)
# print (jc['data'])
urls = []
for i in jc['data']:
    url2 = 'http://web.api.115.com/files/download?pickcode='+i['pc']
    cc2 = gdecode(urllib.request.urlopen(url2).read())
    jc2 = json.loads(cc2)
    print (jc2)
    urls.append ((jc2['file_name'],jc2['file_url']))
print (urls)

for i in urls:
    acc = '''%s
 header=User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 115Browser/5.1.3 
 header=Referer: http://115.com/ 
 header=Cookie: %s
 out=%s
 continue=true
 max-connection-per-server=10
 split=10

''' % (i[1],headers['Cookie'],i[0])
    with open (downfile,'a') as  x :
        x.write(acc)