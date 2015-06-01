#!/bin/bash
for i in 2015* 
	do 

	cd $i
	pwd
 	find . -iname "*.avi" -or -iname "*.rmvb" -or -iname "*.mp4" -or -iname "*.wmv" -or -iname "*.mkv" -or -iname "*.flv" |xargs mv --target-directory=/data/movie
  	cd ..
done
