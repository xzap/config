#!/bin/env python3
import urllib.request
import urllib.parse
import os,re
from http import cookiejar
import sys
import random

login_url = 'http://jcpt.zjer.cn/base/loginUnified.jspx?type=2&callBack=www.zjer.cn:80/login_unify.jspx&productTicket=10&returnUrl=http://www.zjer.cn/channel/uhome/index.jhtml?' 
home_url = "http://jskj.zjer.cn/my.do?method=main"
cj = cookiejar.CookieJar()
opener = urllib.request.build_opener()
opener.add_handler(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

teachers=[
("毛丽云","mly115321","http://jskj.zjer.cn/user.do?method=main&remoteUserId=11458"),
("钱凯红","qkh12441x","http://jskj.zjer.cn/user.do?method=main&remoteUserId=18271"),
("沃珊珊","wss180089","http://jskj.zjer.cn/user.do?method=main&remoteUserId=19506"),
("沈森","ss100518","http://jskj.zjer.cn/user.do?method=main&remoteUserId=19676"),
("王彩华","wch195721","http://jskj.zjer.cn/user.do?method=main&remoteUserId=20533"),
("毛丽娟","mlj190066","http://jskj.zjer.cn/user.do?method=main&remoteUserId=26396"),
("陆羽操","lyc210311","http://jskj.zjer.cn/user.do?method=main&remoteUserId=28233"),
("沈英","sy11302x","http://jskj.zjer.cn/user.do?method=main&remoteUserId=28670"),
("纪晓玲","jxl060029","http://jskj.zjer.cn/user.do?method=main&remoteUserId=29390"),
("王厦","wx165022","http://jskj.zjer.cn/user.do?method=main&remoteUserId=31907"),
("孟兰兰","mll315024","http://jskj.zjer.cn/user.do?method=main&remoteUserId=31951"),
("钱雅琼","qyq183229","http://jskj.zjer.cn/user.do?method=main&remoteUserId=31967"),
("秦强华","qqh193825","http://jskj.zjer.cn/user.do?method=main&remoteUserId=32904"),
("蒋萍","jp050047","http://jskj.zjer.cn/user.do?method=main&remoteUserId=32908"),
("袁铭英","ymy184425","http://jskj.zjer.cn/user.do?method=main&remoteUserId=32962"),
("金其琴","jqq242026","http://jskj.zjer.cn/user.do?method=main&remoteUserId=32969"),
("范炯","fj25002X","http://jskj.zjer.cn/user.do?method=main&remoteUserId=32991"),
("蔡初明","ccm180069","http://jskj.zjer.cn/user.do?method=main&remoteUserId=32993"),
("徐学东","xxd204431","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33003"),
("马微","mw244049","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33016"),
("潘芝芳","pzf262529","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33028"),
("周鼎","zd040014","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33045"),
("顾渭梅","gwm152842","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33048"),
("朱伟","zw150054","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33136"),
("浦瑞芳","prf270023","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33142"),
("许黎明","xlm041229","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33144"),
("姚碧红","ybh290083","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33233"),
("陈玉珠","cyz024425","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33261"),
("胡青秀","hqx125927","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33399"),
("朱军","zj180044","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33423"),
("罗文献","lwx161328","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33432"),
("沈娅","sy210046a","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33440"),
("金建新","jjx025926","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33443"),
("王群芳","wqf250023","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33571"),
("董萍","dp055522","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33652"),
("朱颖红","zyh284121","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33662"),
("陈红","ch302045","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33665"),
("沈文燕","swy174426","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33688"),
("蔡明孝","cmx225716","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33825"),
("金加岭","jjl190022","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33846"),
("沈娟","sj160049","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33892"),
("许建忠","xjz240015","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33904"),
("王怡","wy291027","http://jskj.zjer.cn/user.do?method=main&remoteUserId=34051"),
("于海珠","yhz243826","http://jskj.zjer.cn/user.do?method=main&remoteUserId=34054"),
("许春俭","xcj222326","http://jskj.zjer.cn/user.do?method=main&remoteUserId=34145"),
("张丽敏","zlm160826","http://jskj.zjer.cn/user.do?method=main&remoteUserId=34355"),
("赵袁兰","zyl125026","http://jskj.zjer.cn/user.do?method=main&remoteUserId=34554"),
("薛九红","xjh170021","http://jskj.zjer.cn/user.do?method=main&remoteUserId=34687"),
("章梅","zm270029","http://jskj.zjer.cn/user.do?method=main&remoteUserId=34720"),
("张小燕","zxy034421","http://jskj.zjer.cn/user.do?method=main&remoteUserId=34896"),
("顾一冬","gyd110824","http://jskj.zjer.cn/user.do?method=main&remoteUserId=35257"),
("刘善萍","lsp060028","http://jskj.zjer.cn/user.do?method=main&remoteUserId=35310"),
("曹溢慧","cyh250043","http://jskj.zjer.cn/user.do?method=main&remoteUserId=35317"),
("薛卫红","xwh280065","http://jskj.zjer.cn/user.do?method=main&remoteUserId=35492"),
("李洁","lj310025","http://jskj.zjer.cn/user.do?method=main&remoteUserId=36125"),
("沈斌","sb230029","http://jskj.zjer.cn/user.do?method=main&remoteUserId=36221"),
("俞丹","yd010047","http://jskj.zjer.cn/user.do?method=main&remoteUserId=44040"),
("芮燕飞","ryf010060","http://jskj.zjer.cn/user.do?method=main&remoteUserId=44073"),
("顾琴","gq31182x","http://jskj.zjer.cn/user.do?method=main&remoteUserId=44078"),
("张海珍","zhz290049","http://jskj.zjer.cn/user.do?method=main&remoteUserId=45142"),
("魏萍","wp022041","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49347"),
("丁建芳","djf172523","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49446"),
("徐月强","xyq714053","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49516"),
("杨丽红","ylh081087","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49517"),
("芮琼","rq240048","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49554"),
("沈叶波","syb19001X","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49610"),
("吴玲华","wlh263521","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49614"),
("蔡明孝","68235338","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49630"),
("陈小英","cxy625282","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49632"),
("曹瑞月","cry110068","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49636"),
("吴学先","wxx310029","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49676"),
("陈国红","cgh122323","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49797"),
("倪芳","nf070328","http://jskj.zjer.cn/user.do?method=main&remoteUserId=51800"),
("倪懂平","ndp243828","http://jskj.zjer.cn/user.do?method=main&remoteUserId=88475"),
("陆文权","lwq252812","http://jskj.zjer.cn/user.do?method=main&remoteUserId=88642"),
("王梦婕","wmj070029","http://jskj.zjer.cn/user.do?method=main&remoteUserId=88652"),
("张忠","zz120512","http://jskj.zjer.cn/user.do?method=main&remoteUserId=89056"),
("刘叶梅","lym08414X","http://jskj.zjer.cn/user.do?method=main&remoteUserId=89224"),
("鲁苑波","lyb11002X","http://jskj.zjer.cn/user.do?method=main&remoteUserId=247641"),
("计国平","jgp280017","http://jskj.zjer.cn/user.do?method=main&remoteUserId=254633"),
("吴春燕","wcy160026","http://jskj.zjer.cn/user.do?method=main&remoteUserId=321610"),
("雷雪锋","lxf165718","http://jskj.zjer.cn/user.do?method=main&remoteUserId=321978"),
("金宇超","jyc300041","http://jskj.zjer.cn/user.do?method=main&remoteUserId=324404"),
("金婷立","jtl180520","http://jskj.zjer.cn/user.do?method=main&remoteUserId=333649"),
("缪晓菊","mxj11202x","http://jskj.zjer.cn/user.do?method=main&remoteUserId=347029"),
("汤顺强","tsq250047","http://jskj.zjer.cn/user.do?method=main&remoteUserId=351619"),
("房晨杨","fcy250527","http://jskj.zjer.cn/user.do?method=main&remoteUserId=699674"),
("黄鑫权","hxq190519","http://jskj.zjer.cn/user.do?method=main&remoteUserId=700334"),
("钱立丰","qlf064711","http://jskj.zjer.cn/user.do?method=main&remoteUserId=700335"),
("王涛","wt223217","http://jskj.zjer.cn/user.do?method=main&remoteUserId=728857"),
("鲁婷婷","ltt05302X","http://jskj.zjer.cn/user.do?method=main&remoteUserId=728859"),
("顾艳","gy12302X","http://jskj.zjer.cn/user.do?method=main&remoteUserId=728860"),
("金涛","jt14501X","http://jskj.zjer.cn/user.do?method=main&remoteUserId=728861"),
("黄维","hw182826","http://jskj.zjer.cn/user.do?method=main&remoteUserId=728862"),
("顾林红","glh170827","http://jskj.zjer.cn/user.do?method=main&remoteUserId=1085242"),
("吴叶","wy200029","http://jskj.zjer.cn/user.do?method=main&remoteUserId=1086602"),
]

def login(user,passwd):
    cj = cookiejar.CookieJar()
    opener = urllib.request.build_opener()
    opener.add_handler(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)
    cj.clear()
    login_url = 'http://jcpt.zjer.cn/base/loginUnified.jspx?type=2&callBack=www.zjer.cn:80/login_unify.jspx&productTicket=10&returnUrl=http://www.zjer.cn/channel/uhome/index.jhtml?' 
    params_org={"username":user,"password":passwd,"flag":1}
    params = urllib.parse.urlencode(params_org)
    req = urllib.request.Request(login_url,data=params.encode("utf-8"))
    try :

        cc = urllib.request.urlopen(req).read().decode()
        urlcheck = "http://www.zjer.cn/login_status.jspx?random="+str(random.random())+"&address=http://www.zjer.cn/channel/uhome/index.jhtml?&type=2&usertype=2"
        cc2 = urllib.request.urlopen(urlcheck).read().decode()
        if "欢迎您" in cc2 :
            sub = re.findall("欢迎您:(.*)",cc2)
            name = sub[0].strip()
            print (name + " 登录成功！")
        else :
            print ("登录失败，请检查用户名和密码")
            return
    except Exception as e:
        print (e)

for i in teachers:
    user = i[1]
    passwd = i[1][-6:]

    print (user+"\t"+passwd,end="\t")
    login(user,passwd)
    # num =0

#     for j in teachers:
#         num+=1
#         url = "http://jskj.zjer.cn/user.do?method=main&username=z3u_"+j[1]
#         try:
#             print(num,j[1])
#             cc = urllib.request.urlopen(url).read().decode()
#             print (cc)
#         except Exception as e:
#             print (e)
#             continue
