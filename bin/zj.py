#!/bin/env python3
import urllib.request
import urllib.parse
import os,re
from http import cookiejar
import sys

url = 'http://jcpt.zjer.cn/base/loginUnified.jspx?type=2&callBack=www.zjer.cn:80/login_unify.jspx&productTicket=10&returnUrl=http://www.zjer.cn/channel/uhome/index.jhtml?' 
cj = cookiejar.CookieJar()
opener = urllib.request.build_opener()
opener.add_handler(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
params={"username":"jgp280017",
"password":"280017",
"flag":1}
params = urllib.parse.urlencode(params)
req = urllib.request.Request(url,data=params.encode("utf-8"))
# print (cj)
cc = urllib.request.urlopen(req).read().decode("utf-8")
urlmy = "http://jskj.zjer.cn/my.do?method=main"

teachers = [
("毛丽云","mly115321","http://jskj.zjer.cn/user.do?method=main&remoteUserId=11458"),
("钱凯红","qkh12441x","http://jskj.zjer.cn/user.do?method=main&remoteUserId=18271"),
("沃珊珊","wss180089","http://jskj.zjer.cn/user.do?method=main&remoteUserId=19506"),
("沈森","ss100518","http://jskj.zjer.cn/user.do?method=main&remoteUserId=19676"),
("王彩华","wch195721","http://jskj.zjer.cn/user.do?method=main&remoteUserId=20533"),
("毛丽娟","mlj190066","http://jskj.zjer.cn/user.do?method=main&remoteUserId=26396"),
("陆羽操","lyc210311","http://jskj.zjer.cn/user.do?method=main&remoteUserId=28233"),
("沈英","sy11302x","http://jskj.zjer.cn/user.do?method=main&remoteUserId=28670"),
("纪晓玲","jxl060029","http://jskj.zjer.cn/user.do?method=main&remoteUserId=29390"),
("高爱琪","gaoaq","http://jskj.zjer.cn/user.do?method=main&remoteUserId=30140"),
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
("汪健","430782","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33019"),
("潘芝芳","pzf262529","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33028"),
("周鼎","zd040014","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33045"),
("顾渭梅","gwm152842","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33048"),
("朱伟","zw150054","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33136"),
("浦瑞芳","prf270023","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33142"),
("许黎明","xlm041229","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33144"),
("姚碧红","ybh290083","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33233"),
("陈玉珠","cyz024425","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33261"),
("陆永兴","234567","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33359"),
("胡青秀","hqx125927","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33399"),
("朱军","zj180044","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33423"),
("罗文献","lwx161328","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33432"),
("沈娅","sy210046a","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33440"),
("金建新","jjx025926","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33443"),
("王群芳","wqf250023","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33571"),
("董萍","dp055522","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33652"),
("朱颖红","zyh284121","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33662"),
("陈红","ch302045","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33665"),
("吴春燕","lansedehai","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33677"),
("缪晓菊","miaomiao123","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33680"),
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
("金宇超","jqm","http://jskj.zjer.cn/user.do?method=main&remoteUserId=34888"),
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
("鲁苑波","luyuanbo","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49449"),
("於善芳","fish595","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49513"),
("雷雪锋","lei","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49514"),
("徐月强","xyq714053","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49516"),
("杨丽红","ylh081087","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49517"),
("芮琼","rq240048","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49554"),
("李吉","liji1956","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49602"),
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
("沈晓英","djxxsxy","http://jskj.zjer.cn/user.do?method=main&remoteUserId=88647"),
("汤顺强","djxxtsq","http://jskj.zjer.cn/user.do?method=main&remoteUserId=88650"),
("王梦婕","wmj070029","http://jskj.zjer.cn/user.do?method=main&remoteUserId=88652"),
("徐斌","djxxxb","http://jskj.zjer.cn/user.do?method=main&remoteUserId=88654"),
("周鸣章","djxxzmz","http://jskj.zjer.cn/user.do?method=main&remoteUserId=88656"),
("张忠","zz120512","http://jskj.zjer.cn/user.do?method=main&remoteUserId=89056"),
("刘叶梅","lym08414X","http://jskj.zjer.cn/user.do?method=main&remoteUserId=89224"),
("嘉善县杜鹃小学","jsdjxx","http://jskj.zjer.cn/user.do?method=main&remoteUserId=209744"),
("鲁苑波","lyb11002X","http://jskj.zjer.cn/user.do?method=main&remoteUserId=247641"),
("计国平","jgp280017","http://jskj.zjer.cn/user.do?method=main&remoteUserId=254633"),
("蒋秀青","蒋秀青","http://jskj.zjer.cn/user.do?method=main&remoteUserId=300443"),
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

# teachers =[
# ("毛丽娟","mlj190066","http://jskj.zjer.cn/user.do?method=main&remoteUserId=26396"),
# ("金加岭","jjl190022","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33846"),
# ("沈娟","sj160049","http://jskj.zjer.cn/user.do?method=main&remoteUserId=33892"),
# ("刘善萍","lsp060028","http://jskj.zjer.cn/user.do?method=main&remoteUserId=35310"),
# ("魏萍","wp022041","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49347"),
# ("曹瑞月","cry110068","http://jskj.zjer.cn/user.do?method=main&remoteUserId=49636"),
# ("王梦婕","wmj070029","http://jskj.zjer.cn/user.do?method=main&remoteUserId=88652"),
# ("金婷立","jtl180520","http://jskj.zjer.cn/user.do?method=main&remoteUserId=333649"),
# ("顾林红","glh170827","http://jskj.zjer.cn/user.do?method=main&remoteUserId=1085242"),
# ]


ok = 0
fail = 0
num = 0
no =[]
for i in teachers :
	num+=1
	print (num,ok,fail,i[0],end="\t")
	cc = urllib.request.urlopen(i[2]).read().decode()
	if '空间主人尚未开通个人空间' in cc :
		print ("fail!")
		fail+=1
		no.append(i)
	else :
		ok+=1
		print ('done!')
print ("="*100)
rusult = "一共有老师%s人,开通老师%s人,未开通老师%s人.名单如下：" % (num,ok,fail)
print (rusult)
for i in no :
	print ("%s\t%s\t%s" %(i[0],i[1],i[2])) 

# 吴春燕	lansedehai	http://jskj.zjer.cn/user.do?method=main&remoteUserId=33677
# 吴春燕	wcy160026	http://jskj.zjer.cn/user.do?method=main&remoteUserId=321610
# 汤顺强	djxxtsq	http://jskj.zjer.cn/user.do?method=main&remoteUserId=88650
# 汤顺强	tsq250047	http://jskj.zjer.cn/user.do?method=main&remoteUserId=351619
# 缪晓菊	miaomiao123	http://jskj.zjer.cn/user.do?method=main&remoteUserId=33680
# 缪晓菊	mxj11202x	http://jskj.zjer.cn/user.do?method=main&remoteUserId=347029
# 蔡明孝	68235338	http://jskj.zjer.cn/user.do?method=main&remoteUserId=49630
# 蔡明孝	cmx225716	http://jskj.zjer.cn/user.do?method=main&remoteUserId=33825
# 金宇超	jqm	http://jskj.zjer.cn/user.do?method=main&remoteUserId=34888
# 金宇超	jyc300041	http://jskj.zjer.cn/user.do?method=main&remoteUserId=324404
# 雷雪锋	lei	http://jskj.zjer.cn/user.do?method=main&remoteUserId=49514
# 雷雪锋	lxf165718	http://jskj.zjer.cn/user.do?method=main&remoteUserId=321978
# 鲁苑波	luyuanbo	http://jskj.zjer.cn/user.do?method=main&remoteUserId=49449
# 鲁苑波	lyb11002X	http://jskj.zjer.cn/user.do?method=main&remoteUserId=247641
