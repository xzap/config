#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import os
import re

movie_dir = os.path.realpath('/data')
newdir = os.path.realpath('/data/movie')
r_part = re.compile('2015-[0-9]{2}-[0-9]{2}_[0-9]{2}_[0-9]{2}_[0-9]{2}') #2015-03-07_11_28_17
for root,dirs,files in os.walk(movie_dir) :
    for onefile in files :

        pp = os.path.join(root,onefile)
        if re.search(r_part,pp):
            olddir,oldfile = os.path.split(pp)
            newfile = os.path.join(newdir,oldfile)
            os.renames(pp,newfile)
            print (olddir)
    if len(os.listdir(root)) == 0 and re.search(r_part,root) :
        os.rmdir (root)

if os.path.exists('/data/movie/aria2.down'):os.remove('/data/movie/aria2.down')