#!/bin/bash
while :
do
echo "___________________________"
echo "1.禁用虚拟内存"
echo "2.启用虚拟内存"
echo "3.释放不活跃内存"
echo "4.显示隐藏文件"
echo "5.隐藏隐藏文件"
echo "6.将Widget放在桌面"
echo "7.关闭鼠标加速度"
echo "q.退出"
echo "__________________________"
read -p  "请选择所要使用的功能: " i

echo $i

case $i in 
	1)
		echo "sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.metadata.mds.plist"
		echo "sudo rm /private/var/vm/swapfile*"
		;;
	2)
		echo "sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.metadata.mds.plist"		
		;;
	3)
		echo "sudo purge"
		;;

	4)
		echo "defaults write com.apple.finder AppleShowAllFiles -bool true"
		echo "killall Finder"
		;;
	5)
		echo "defaults write com.apple.finder AppleShowAllFiles -bool false"
		echo "killall Finde"
		;;
	6)
		echo "defaults write com.apple.dashboard devmode YES"
		echo "killall Dock"
		;;
	7)
		echo "defaults write .GlobalPreferences com.apple.mouse.scaling -1"
		;;
	q|Q)
		exit 0
		;;
	*)
		echo "没有这个选项"
		continue
		;;
esac
done
