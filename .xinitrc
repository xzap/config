#!/bin/sh
#
# ~/.xinitrc
#
# Executed by startx (run your window manager from here)

if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

export LANG="zh_CN.UTF-8"
XIM=fcitx
export XMODIFIERS=@im=fcitx
XIM_PROGRAM=/usr/bin/fcitx
XIM_ARGS=""
export QT4_IM_MODULE=fcitx 
export GTK_IM_MODULE=fcitx
DEPENDS="fcitx"
killall fcitx
fcitx  &
export XDG_MENU_PREFIX="lxde-"
export XDG_CURRENT_DESKTOP='LXDE'
#exec dbus-launch openbox-session
exec openbox-session
#exec ck-launch-session openbox-session
#exec awesome
#exec  xbmc-standalone                             
#exec cinnamon-session
