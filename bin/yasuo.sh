#!/bin/bash


#用脚本使用形式
function usage()
{
	echo "usage : `basename $0`  [-c|-t|-x] FileName "
}


#脚本参数含义
function  help()
{
	echo "-c 打包并压缩文件"
	echo "-t 查看压缩文件的内容"
	echo "-x 解压缩打包文件"
}


#保证参数多余两个
if [ $# -lt 2 ]; then
	usage
	exit
fi


#先判断参数$1是打包压缩还是解包解压,或者是查看压缩内容
while :
do
	case "$1" in 
	-c)	#打包压缩
		OPT="-jcvf" #指定参数，支持bzip2压缩
		shift #移除第一个参数
		for FILE in $@
		do
			tar "$OPT" "$FILE".tar.bz2 $FILE
			if [ $? -eq 0 ]; then
				echo "$FILE -->> $FILE.tar.bz2"
				continue
			else
				echo "error"
				exit 1
			fi
		done
			exit;;
	-t)	#查看压缩文件内容
		OPT="-jtvf"
		shift
		for FILE in $@
		do
			tar "$OPT" $FILE
		done
		exit 0
		;;
	-x)	#解包解压缩
		OPT="-jxvf"
		shift
		for FILE in $@
		do
			tar $OPT $FILE 
		done
		exit 0
		;;
	*)
		help
		exit 1
		;;	
	esac
done	