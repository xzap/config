#!/usr/bin/python
import libtorrent as bt
import sys
import urllib.parse
torrent="/data/2013110216111347.torrent"
#try :
#	torrent=sys.argv[1]
#except :
#	print("need a arg")
#	sys.exit()
info = bt.torrent_info(torrent)
tt=""
for i in info.trackers() :
	tt+="&tr="+i.url
name = urllib.parse.quote(info.name())
link="xt=urn:btih:{}&dn={}&xl={}{}".format(info.info_hash(), info.name(),info.total_size(),tt)
link="magnet:?"+urllib.parse.quote(link)
#for i in info.files():
#	print(dir(i))
#	print(i.path)
print(link)
