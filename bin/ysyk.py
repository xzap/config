#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

import urllib.request
import os
import time
import re
headers = {
'Cookie':'JSESSIONID=3882EA4A460C978348BF2F39D6A4F45B; CNZZDATA1253333710=758560650-1422411902-http%253A%252F%252Fmrg.eduyun.cn%252F%7C1422411902; JSESSIONID=8A69C0378C36DFFD8BCA7D2B99B1EA08; CNZZDATA1253416210=482517104-1421989544-http%253A%252F%252Ftz.1s1k.eduyun.cn%252F%7C1422501815',
'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
'Referer': 'http://mrg.eduyun.cn/portal/1s1k/portal/school_manager_check.jsp',
'X-Requested-With': 'XMLHttpRequest' ,
'Connection': 'keep-alive' 
}
body = '''<!DOCTYPE html PUBliC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta http-equiv="Cache-Control" content="no-cache" />
		<meta http-equiv="Content-Type" content="text/html" />
        <title></title>
        <style>
			.page p{float:right;line-height:22px;margin-left:10px;}
		</style>
		
		
        <link rel="stylesheet" type="text/css" href="http://mrg.eduyun.cn/portal/1s1k/skins/css/all.css" />
        <script type="text/javascript" src="http://mrg.eduyun.cn/portal/portal/skins/blue/js/jquery-1.8.3.min.js"></script>
        <script src="http://mrg.eduyun.cn/portal/common/js/lhgdialog/lhgdialog_1.min.js?skin=idialog"></script>
        <link href="http://mrg.eduyun.cn/portal/common/js/lhgdialog/skins/idialog.css" type="text/css" rel="stylesheet"/>
        <script type="text/javascript" src="http://mrg.eduyun.cn/portal/portal/skins/blue/js/form.js"></script>
		<script type="text/javascript"> 
			function doAction(value){
				if(confirm("确定要将老师移出本校吗？")){
					document.location.href="/ysyk/base/BaseUser/"+value;
				}
			}
			function goToPage(value){
				$.ajax({
				    url: 'http://mrg.eduyun.cn/ysyk/base/BaseUser/schoolManagerCheckList1s1k.jspx?pageNo='+value+'&date='+new Date().getTime(),
				    type:'get',
					contentType: "application/x-www-form-urlencoded; charset=utf-8",
				    error: function(XMLHttpRequest, textStatus, errorThrown) {
				        alert(errorThrown);
				    },
				    success: function(responseText){
				    	$('#case_list').html(responseText);
				    	autoHeight(parent.parent, 'mainIframe', 'http://mrg.eduyun.cn/ysyk');
				    }
				});
			}
/**
 * 学校管理员的审核
 */
			function schoolManagerdoStatus(root,teacherId,status,pageNo){
				if(confirm("确定要执行此操作么吗？")){
					$.ajax({
						   type: 'post',
						   url: root+'/base/BaseUser/setSchoolCheckStatus.jspx?pageNo=2&status='+status+'&teacherId='+teacherId+'&date='+new Date().getTime(),
						   error: function(XMLHttpRequest, textStatus, errorThrown) {
						        //alert(errorThrown);
						    },
						   async:false,
						   success: function(msg){
							   if(status=="2"){
								  var msgs= msg.split("::");
								   if(msgs[0]!="000000"&&msgs[0]!="012017"){
									   alert("执行通过失败，错误代码:"+msgs[0]+"请联系管理员！");
									   document.getElementById("errorMsg").innerHTML=msgs[1];
								   }
							   }
							   if(status=="-1"){
								  var msgs= msg.split("::");
								   if(msgs[0]!="000000"){
									   alert("执行不通过失败，错误代码:"+msgs[0]+"请联系管理员！");
									   document.getElementById("errorMsg").innerHTML=msgs[1];
								   }
							   }
							   
						    	againAction(root,pageNo);
						    	
						   }
						}); 
					}
				}

			function againAction(root,pageNo){
				$.ajax({
					   type: 'post',
					   url: root+'/base/BaseUser/schoolManagerCheckList1s1k.jspx?pageNo='+pageNo+'&date='+new Date().getTime(),
					   error: function(XMLHttpRequest, textStatus, errorThrown) {
					        //alert(errorThrown);
					    },
					   success: function(msg){
							   
					    	$('#case_list').html(msg);
					    	
					   }
					}); 
			}
				
		</script>

    </head>
    
    <body>
<div class="main shaike" style="min-height: 50px;float:none;">
    <div style="display:none;" id="errorMsg"></div>
    <form id="BaseUser_mySchoolUserList1s1k_jspx" name="frm" action="/ysyk/base/BaseUser/mySchoolUserList1s1k.jspx" method="post">

    <div class="sort"></div>
    <div class="workTab workTab2"> <em class="em1"></em><em class="em2"></em>
      <table style="width:100%;font-size:12px;">

<tbody>
 <tr>
            <th>序号</th>
            <th>姓名</th>
            <th>学科</th>
            <th>通过审查</th>
            <th>未通过审查</th>
            <th>待完成</th>
            <th>报名时间</th>
            <th>审核时间</th>
            <th>审核</th>
            <th>操作</th>
          </tr>

'''
for i in range(1,12) :
	tt = str(time.time()).replace('.','')[:13]
	url = 'http://mrg.eduyun.cn/ysyk/base/BaseUser/schoolManagerCheckList1s1k.jspx?pageNo='+str(i)+'&date='+tt
	req = urllib.request.Request(url,headers=headers)
	cc = urllib.request.urlopen(req).read().decode('UTF-8')
	bb = re.findall('<tbody>.*</tbody>',cc,re.S)
	bb2 = bb[0].replace('<tbody>','').replace('</tbody>','')
	body = body+bb2

body = re.sub('<th>.*</th>','',body)
body = re.sub('<tr>\s*</tr>','',body)


body = body + '''
</tbody>
</table>

   </div>
    <div class="page" style="padding-top:1px;"><div class="page"><p>共74条</p> <a href="javascript:goToPage(1)" class="pre">pre</a> <a class="num" href="javascript:goToPage(1)">1</a></li> <a href="###" class="num cur">2</a> <a class="num" href="javascript:goToPage(3)">3</a></li> <a class="num" href="javascript:goToPage(4)">4</a></li> <a class="num" href="javascript:goToPage(5)">5</a></li> <a class="num" href="javascript:goToPage(6)">6</a></li> <a class="num" href="javascript:goToPage(7)">7</a></li> <a class="num" href="javascript:goToPage(8)">8</a></li> <a class="next" href="javascript:goToPage(3)">next</a></div>  </div>
    <div style="height:10px;">&nbsp;</div>
    </form>




    <div style="clear:both;"></div>
  </div>



 </body>
</html>
'''

print (body)