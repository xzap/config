#!/bin/env python3

import urllib.request
import shutil  
import os

hosts = "/etc/hosts"
hostsbak = "/etc/hosts_bak"
if os.path.exists(hostsbak):os.remove(hostsbak)
shutil.copy(hosts,hostsbak)
url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
urllist = ['https://raw.githubusercontent.com/racaljk/hosts/master/hosts','https://hosts-smounives.rhcloud.com/hosts','http://www.racalinux.cn/hosts.txt']
cc = urllib.request.urlopen(url).read().decode('UTF-8')
print (cc)
try:
    url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
    cc = urllib.request.urlopen(url).read().decode('UTF-8')
    with open (hosts,"w") as x :
        x.write(cc)

except Exception as e:
    raise e