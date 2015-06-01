#!/usr/bin/env python

import os
import sys
import time

pelican_dir = os.path.realpath("/data/blog/pelican")
pelican_content = os.path.join(pelican_dir, "content")

pelican_articles = os.path.join(pelican_content, "articles")
if len(sys.argv) > 1:
    Slug = "_".join(sys.argv[1:])
    new_articles = os.path.join(pelican_articles, Slug + ".md")
    if os.path.isfile(new_articles):
        print ("这个文件已经存在，请重新输入文件名！")
        exit()
else:
    print ("请输入文件名")
    exit()
print (new_articles)

Date = time.strftime("%Y-%m-%d %H:%M")

Title = input("请输入标题：").strip()
Category_org = input("请输入分类：").strip()
Category = Category_org[:1].upper() + Category_org[1:].lower()

Tags_org = input ("请输入标签：").strip()
Taglist = Tags_org.split()
Tags =", ".join([tag[:1].upper() + tag[1:].lower() for tag in Taglist ])
Author = "xzap"
Summary = '''<!-- PELICAN_BEGIN_SUMMARY -->


<!-- PELICAN_END_SUMMARY -->'''


content = '''\
Title: %s
Date: %s
Category: %s
Tags: %s
Slug: %s
Author: xzap

<!-- PELICAN_BEGIN_SUMMARY -->


<!-- PELICAN_END_SUMMARY -->
'''% (Title, Date, Category, Tags, Slug)

print (content)
with open (new_articles,"w",encoding="utf-8") as f:
    f.write(content)

os.system("retext " + new_articles)

shell = "cd " + pelican_dir + " && make publish"  
os.system(shell)
