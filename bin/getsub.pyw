#!/usr/bin/env python
#coding:utf-8
from tkinter import *
import tkinter.filedialog as filedialog
import sub
import os

def fd():
    file = filedialog.askopenfilenames(title="请选择要下载字幕的文件，可多选",
    filetypes=[('视频文件', '*.mkv *.avi *.rmvb *.mp4 *.MKV'),
    ('All files', '*'),])
    # a=file.split(None)
    a=root.tk.splitlist(file)
    print(a)
    for i in a :
        print (i)
        sub._getsubs(i)
def dd():
    path = filedialog.askdirectory(root)
    print(path)
def die(event):
	root.quit()
root = Tk()
root.geometry("400x200+10+20")
root.title("Xzap's 射手字幕下载器")
buttonfiles=Button(root,text="打开文件",command=fd)
buttonpath=Button(root,text="选择目录",command=dd)
buttonfiles.pack(pady=10)
buttonpath.pack(pady=10) 
root.bind("<Escape>",die)
root.mainloop()  

