
#自己的设置
# rox-filer
# 桌面由 rox 接管
#killall rox > /dev/null 2>&1
#rox -p default &

# xscreensaver
# 屏幕保护
# killall xscreensaver > /dev/null 2>&1
# xscreensaver &

# wallpapers
# 设置桌面，这里注释掉了，因为桌面已经交由 rox 管理。
# 如果不需要 rox 管理桌面，可以在这里设置桌面的壁纸
eval `cat /home/xzap/.fehbg`

sudo /home/xzap/bin/net
# set panel
# 挂载上 panel
#killall fbpanel > /dev/null 2>&1
#fbpanel &
killall tint2> /dev/null 2>&1
tint2 &


# Conky  
# 挂上漂亮的监视器，这里被我注释掉了，因为和 rox 搭配还有一些小问题未解决。
killall conky > /dev/null 2>&1
conky &

# 音量控制软件
killall volwheel > /dev/null 2>&1
volwheel &

#透明和阴影
#xcompmgr -Ss -n -Cc -fF -I-10 -O-10 -D3 -t-3 -l-4 -r4 &

# 检测是否有未下载完的东西，有就启动mlnet
#ls /data/mlnet/temp/* >/dev/null 2>&1 && mlnet &
# 运行音乐播放器
#mpd ~/.mpdconf &
#osdlyrics &

#一个简单漂亮的dock--wbar
#killall wbar > /dev/null 2>&1
#wbar &


#ibus
#ibus-daemon &
numlockx on &
sudo modprobe vboxdrv
killall python2 > /dev/null 2>&1
python2 /home/xzap/goagent/goagent-gtk.py &
wine-qqintl  &
#qq2013 &

killall xautolock > /dev/null 2>&1
xautolock -time 10 -locker slock &
#xautolock &
#killall parcellite > /dev/null 2>&1
#parcellite &
#ls /data/bt/torrent/* >/dev/null 2>&1 && urxvt -e screen rtorrent &
#killall fcitx > /dev/null 2>&1
#fcitx &
#killall compton > /dev/null 2>&1
#compton --config ~/.config/compton.conf &

