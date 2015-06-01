#!/bin/bash


case $1 in 
    +)
    vol=`audtool get-volume`
    vol=$((vol+5))
    audtool set-volume $vol
    audtool get-volume
    ;;
    -)
    vol=`audtool get-volume`
    vol=$((vol-5))
    audtool set-volume $vol
    audtool get-volume
    ;;
    next)
    audtool playlist-advance 
    ;;
    prev)  
    audtool playlist-reverse 
    ;;
    *)
    audtool current-song-filename
    audtool current-song
    echo -n '时间:'`audtool current-song-output-length`/`audtool current-song-length`" " 
    echo -n '比特率:'`audtool current-song-bitrate-kbps`kbs" " 
    echo -n "音量:"`audtool get-volume`"% "
    echo -n "重复:"`audtool playlist-repeat-status`" "
    echo "随机:"`audtool playlist-shuffle-status`" "
  
    ;;


esac
