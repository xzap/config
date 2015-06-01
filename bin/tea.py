#!/usr/bin/env python
import datetime
import os

f=os.path.realpath("/home/xzap/todo")
all = (
(("10:15","10:55","信息","301","上午第三节"),("13:35","14:15","信息","405","下午第二节"),("14:25","15:05","信息","305","下午第三节")),
(("10:15","10:55","信息","306","上午第三节"),("12:40","13:20","信息","403","下午第一节"),("13:35","14:15","信息","406","下午第二节")),
(("10:15","10:55","信息","401","上午第三节"),("12:40","13:20","信息","506","下午第一节"),("14:25","15:05","信息","505","下午第三节")),
(("10:15","10:55","信息","504","上午第三节"),("12:40","13:20","信息","304","下午第一节"),("13:35","14:15","信息","404","下午第二节"),("14:25","15:05","信息","402","下午第三节")),
(("12:40","13:20","信息","302","下午第一节"),("13:35","14:15","信息","303","下午第二节"))
)

todo2=[]

with open(f,"r",encoding="utf8") as todo:
    for i in todo:
        todo2.append(i)

    
#print(todo2)

ot = "\n".join(todo2)
weekd = ("星期一","星期二","星期三","星期四","星期五","星期六","星期日")
z=datetime.date(2013,1,6)
n=datetime.date.today()
c=n-z
c=int(c.days)
c=c//7%2
t = datetime.datetime.now().weekday()
for i in range(t,t+7):
	l = i
	if i>6 :i-=7
	if i<5 :
		if i==t : 
			print("${color #ddaa00}今天 ("+str(n)+")：$color")
		else :
			k=l-t
			if k<0:k=+6
			# print(k)
			print("${color #98c2c7}"+weekd[i]+" ("+str(n+datetime.timedelta(k))+") :$color")
		if i==2 and c==1 and l<6: print("${color green}值日$color")
		ccc = 0
		for j in all[i] :
			if i==t :
				ti = j[0].split(":")
				atime = datetime.time(int(ti[0]),int(ti[1]))
				btime = datetime.time(datetime.datetime.now().hour,datetime.datetime.now().minute)
				# print (atime,btime)
				if atime > btime and ccc == 0:
					ccc =1
					print ("${color #eee}"+j[4],j[0]+"-"+j[1],"${alignr}"+j[3],j[2]+"$color")
				else :
					print (j[4],j[0]+"-"+j[1],"${alignr}"+j[3],j[2])
			else :
				print (j[4],j[0]+"-"+j[1],"${alignr}"+j[3],j[2])
if ot :
	print("${color #ffd700}${hr 1}$color")
	print("${color green}"+ot+"$color")
