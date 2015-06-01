#!/bin/bash
namelist=('\[迅雷下载www.2tu.cc\]'
'【6v电影www.dy131.com】'
'【6v电影www.6vdy.com】'
'【6v电影域名被盗,新地址www.6vhao.net】'
'【6v电影域名被盗\,新地址www.6vhao.net】'
'\[电影天堂www.dy2018.com\]'
'【6v电影www.6vhao.net】')

find -type f |while read j
	do
	for i in ${namelist[@]}
		do
		h=`echo "${j}" |sed "s/$i//g"`

		if [ "${j}" != "${h}" ]
			then
			echo "${j}" "${h}"
			mv "${j}" "${h}"
		fi

	done
done