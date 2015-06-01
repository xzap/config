#!/usr/bin/env python3
# encoding: UTF-8

import urllib.request
import os,re
from http import cookiejar
import sys
import json
from urllib.parse import urlencode
from hashlib import sha1
import time 
import random
import pickle

class one15pan (object) :
    def __init__(self,username,password,downdir=os.path.join(os.path.expanduser('~'), '115downloads')) :
        if not os.path.exists(downdir) : os.mkdir(downdir)
        self.username = username
        self.password = password
        self.downdir = downdir
        self.cookiefile = os.path.join(os.path.expanduser('~'), '.115.cookies')
        self.cj = cookiejar.LWPCookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))
        self.opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')]
        urllib.request.install_opener(self.opener)
        if os.path.exists(self.cookiefile):
            self.loadcookie()
            print (self.colortxt('发现本地Cookie文件，检查是否有效……'))
            if self.checklogin() :
                print (self.colortxt(self.username + '  本地文件有效，登陆成功！^_^'))
            else :
                print (self.colortxt('本地Cookie文件登陆失败，尝试账号密码登陆……'))
                self.login()
        else:
            print (self.colortxt('本地没有Cookie文件，尝试账号密码登陆……'))
            self.login()


    def colortxt(self,text,color="rand"):
        # colordict ={"Black":"30","Red":"31","Green":"32","Yellow":"33","Blue":"34","Purple":"35","Cyan":"36","White":"37"}
        colordict ={"Red":"31","Green":"32","Yellow":"33","Blue":"34","Purple":"35","Cyan":"36","White":"37"}   

        if color == "rand" :
            cc = random.choice(list(colordict.values()))
        else :
            cc = colordict[color]
        res = '\x1b[%sm' % cc + str(text) + '\x1b[0m' 
        return res  

    def utf8_encode(self,s):
        res = s.encode('utf-8')
        return res  

    def get_vcode(self):
        s = '%.6f' % time.time()
        whole, frac = map(int, s.split('.'))
        res = '%.8x%.5x' % (whole, frac)
        return res  

    def get_ssopw(self,vcode):
        p = sha1(self.utf8_encode(self.password)).hexdigest()
        u = sha1(self.utf8_encode(self.username)).hexdigest()
        v = vcode.upper()
        pu = sha1(self.utf8_encode(p + u)).hexdigest()
        return sha1(self.utf8_encode(pu + v)).hexdigest()

    def login(self):
        login_url = 'http://passport.115.com/?ct=login&ac=ajax&relogin=1&is_ssl=1'
        vcode = self.get_vcode()
        sspow = self.get_ssopw(vcode)
        body = {
            'login[ssoent]':'A1',
            'login[version]':'2.0',
            'login[ssoext]':vcode,
            'login[ssoln]': self.username,
            'login[ssopw]': sspow,
            'login[ssovcode]':vcode,
            'login[safe]':'1',
            'login[time]':'0',
            'login[safe_login]':'0',
            'goto':'http://115.com/'  
            }
        rr = self.opener.open(login_url,data=urlencode(body).encode('UTF-8'))
        if self.checklogin() : 
            print (self.colortxt(self.username + '  登陆成功！^_^'))
            self.savecookie()
        else:           
            print (self.colortxt(self.username + '  登陆失败！T_T'))
            sys.exit()
        
    def checklogin(self):
        check_url = 'http://passport.115.com/?ct=ajax&ac=ajax_check_point'  
        cc = self.opener.open(check_url).read().decode('UTF-8')
        jc = json.loads(cc)
        if jc['state'] == False :
            return True
        else :
            return False

    def savecookie (self):
        self.cj.save(self.cookiefile,True,True)

    def loadcookie (self) :
        self.cj.load(self.cookiefile,True,True)

    def zipdecode(self,webPage, charset='UTF-8'):
        if webPage.startswith(b'\x1f\x8b'):
            return gzip.decompress(webPage).decode(charset)
        else:
            return webPage.decode(charset)
    
    def getjson(self,url):
        c = self.opener.open(url).read()
        c = self.zipdecode(c)
        jc = json.loads(c)
        return jc
    
    def getweb(self,url):
        c = self.opener.open(url).read()
        c = self.zipdecode(c)
        return c    

    def downlixianpc(self,url):
        jc = self.getjson(url)
        pcs = []
        for i in jc['data']:
            pcs.append(i['pc'])
        return (pcs)

    def getusergent(self):
        header = self.opener.addheaders

        return header[0][1]

    def playlink(self,pc):
        url = 'http://115.com/api/video/m3u8/%s.m3u8' % pc
        c = self.getweb(url)
        purl = c.split()[-1]
        cmd = 'mpv  --really-quiet --cache 8140 --cache-default 8140 ' \
            '--http-header-fields "user-agent:%s" '\
            '--http-header-fields "Referer:http://m.115.com" ' \
            '--http-header-fields "Cookie:%s" "%s"' \
            % (self.getusergent(),self.makecookie() ,purl)
        print ('正在链接服务器，请耐心等待播放……')
        # print (cmd)
        os.system(cmd)

    def downlinks(self,durl):
        pcs = self.downlixianpc(durl)
        links = []
        for pc in pcs :
            url = 'http://web.api.115.com/files/download?pickcode='+ pc
            jc = self.getjson(url)
            filename = jc['file_name']
            downlink = jc['file_url']
            filesize = self.formatsize(jc['file_size'])
            links.append([pc,filename,downlink,filesize])
        return links

    def downfile (self,name,url):
        cmd = 'aria2c "%s" -c  -m 0 '\
                '-o "%s" -d "%s" '  \
                '-x 5 -s 3 -j 5 ' \
                '--user-agent "%s" ' \
                '--header "Referer:http://m.115.com/" ' \
                '--header "Cookie:%s"' \
                % (url,name,self.downdir,self.getusergent(),self.makecookie())
        # print (cmd)
        os.system(cmd)
        # print (self.opener.addheaders)
        # print (self.cj)


    def formatsize(self, size):
        size = int(size)
        if size > 1024*1024*1024 :
            s = "%.2f" % (size/1024/1024/1024) +'G'
        elif size > 1024*1024 :
            s = "%.2f" % (size/1024/1024) + 'M'
        elif size > 1024 :
            s = "%.2f" % (size/1024) + 'K'
        else :
            s = "%s" % size +'B'
        return s

    def makearia2c(self,links):
        downfile = os.path.join(self.downdir,"115.down")
        content = ''
        for link in links:
            content += '%s \n' \
            '  header=User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 115Browser/5.1.3 \n' \
            '  header=Referer: http://115.com/ \n' \
            '  header=Cookie: %s \n' \
            '  out=%s\n' \
            '  dir=%s\n' \
            '  continue=true \n' \
            '  max-connection-per-server=10 \n' \
            '  split=10 \n\n' % (link[2],self.makecookie(),link[1],self.downdir)
        with open (downfile,'w') as f :
            f.write(content)
        cmd = "aria2c -i " + downfile
        os.system(cmd)

    def makecookie(self):
        cooktxt=''
        for cook in self.cj:
            cooktxt+= "%s=%s; " %(cook.name,cook.value)
        return cooktxt

    def addtask(self,u):       
        url = 'http://my.115.com/?ct=ajax&ac=get_user_aq'
        jc = self.getjson(url)
        uid = jc['data']['uid']
        url = 'http://115.com/?ct=offline&ac=space'
        jc = self.getjson(url)
        sign = jc['sign']
        tm = jc['time']
        data = {
            'url': urllib.request.quote(u),
            'uid': uid,
            'sign': sign,
            'time': str(tm)
        }
        url = 'http://115.com/lixian/?ct=lixian&ac=add_task_url'
        cc = self.opener.open(url,data=urlencode(data).encode('utf-8')).read().decode()
        jc = json.loads(cc)
        if jc['info_hash']:
            print (self.colortxt(u + '\t添加成功'))
        elif jc['error_msg']:
            print (u + "\t"+jc['error_msg'])
        else:
            print (u + "\t" +"失败了！")

    def playall(self,links):
        plays = []
        playlist = os.path.join(self.downdir,'115.m3u')
        for link in links :
            pc = link[0]
            url = 'http://115.com/api/video/m3u8/%s.m3u8' % pc
            c = self.getweb(url)
            purl = c.split()[-1]
            plays.append(purl)
        with open(playlist,'w') as f:
            f.write('\n'.join(plays))

        cmd = 'mpv  -loop inf --really-quiet --cache 8140 --cache-default 8140 ' \
            '--http-header-fields "user-agent:%s" '\
            '--http-header-fields "Referer:http://m.115.com" ' \
            '--http-header-fields "Cookie:%s" ' \
            '--playlist %s' \
            % (self.getusergent(),self.makecookie() ,playlist)
        print ('正在链接服务器，请耐心等待播放……')
        # print (cmd)
        os.system(cmd)



    def downandplay (self,durl):
        links =self.downlinks(durl)
        print ("="*40)
        print (self.colortxt("特殊命令：",'Yellow'),self.colortxt('0.下载所有文件 a.播放所有文件 q.退出','Red'))
        for num,link in enumerate(links) :

            show = "%s. %s\t%s" %(num+1,link[1],link[3])
            print (self.colortxt(show))
        print("="*40)
        choice = input ("请输入序号：")
        c= choice.strip()
        if c.isalpha():
            if c=='q' or c=='exit':
                sys.exit()
            elif c == 'a' :
                self.playall(links)
            else:
                sys.exit()

        if c.isdigit():
            c=int(c)
            if c == 0 :
                self.makearia2c(links)
            elif c <= len(links):
                c=c-1
                linkc = links[c]
                print ("选择了" + self.colortxt(linkc[1])+"请选择要播放还是下载？(1、播放 2、下载 其他提出)")
                cc = input ("请输入：")
                cc = cc.strip()
                if cc.isdigit:
                    if int(cc) == 1 :
                        self.playlink(linkc[0])
                    elif int(cc) == 2 :
                        self.downfile(link[1],link[2])
                    else:
                        sys.exit()
                else :
                    sys.exit()

    def magfile (self,path):
        path = os.path.abspath(path)
        with open (path,'r') as f :
            maglist = f.readlines()
        urls=[]
        for i in maglist:
            i = i.replace('\n','')
            self.addtask(i)
            time.sleep(1)
        

    def main(self) :
        import argparse
        parser = argparse.ArgumentParser(description='Xzap\'s 115pan Api Class')
        parser.add_argument("-v", "--version", version='%(prog)s 0.1',help='显示版本号',
                        action="version")
        parser.add_argument("-f", "--file", help='打开文件中的链接并添加。',dest='magfile',
                        action="store")
        parser.add_argument("-m", "--magnet", help='添加magnet链接。',dest='magnetlist',
                        action="store",nargs='+')
        parser.add_argument("-l", "--list", help='显示url中的文件',dest='listlink',
                        action="store")
        parser.add_argument("-t", "--type", help='选择显示类型.0。全部 1.文档 2.图片 3.音乐 4.视频 5.压缩包 6.应用 99.仅文件',
                        action="store")
        args = parser.parse_args()

        if args.listlink :
            url = args.listlink
            cid = re.search("cid=([a-z0-9]*?)&",url).group(1)
            if args.type :
                url = 'http://web.api.115.com/files?format=json&limit=40&aid=1&cid=%s&type=%s' % (cid,args.type)
            else :
                url = 'http://web.api.115.com/files?format=json&limit=40&aid=1&cid=%s' % cid
            s.downandplay(url)

        if args.magnetlist:
            for mag in args.magnetlist:
                self.addtask(mag)  
        if args.magfile :
            self.magfile(args.magfile) 
        if len(sys.argv) <= 1:   
            # url = 'http://web.api.115.com/files?aid=1&cid=321822214725040916&o=user_ptime&asc=0&offset=0&show_dir=1&limit=40&code=&scid=&snap=0&natsort=1&source=&format=json&type=4&star=&is_share='
            url = 'http://web.api.115.com/files?aid=1&cid=321822214725040916&o=user_ptime&asc=0&offset=0&show_dir=1&limit=32&code=&scid=&snap=0&natsort=1&source=&format=json&type=4&star=&is_share='
            self.downandplay(url)   

# format=json&type=4&star=&is_share=

if __name__ == '__main__':
    s= one15pan('xzap@163.com','1982628','/data/115pan')
    s.main()

