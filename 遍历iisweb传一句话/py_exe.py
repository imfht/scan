﻿# -*- coding: utf-8 -*-
#windows  #无控制台
#console   #有控制台

from distutils.core import setup

import py2exe
import os

#setup(version = "FTP--webshell---sqlite--0.6",description = "QQqun--293663651",
#    name = "postadmin",zipfile=None,
#    console=[{"script": "main.py", "icon_resources": [(1,"App.ico")]}],
#    options={"py2exe":{"includes":["sip"]}},
#    includes1 = ["class_openurl.py","class_Queue.py","Csqlite3.py","list.py","SlinkFTP.py","class_ftppassword.py"])

def list_file():
    global  file_list
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                data="%s\%s"%(root,file)
                print data[2:]
                file_list.append(data[2:])  #添加数据

if __name__=='__main__':
    global  file_list  #声明全局变量
    file_list=[]
    list_file()
    setup(version = "www.webxscan.com",description = "QQ:29295842",
    name = "webxscan_client",zipfile=None,
    console=[{"script": "main.py", "icon_resources": [(1,"App.ico")]}],
    #options={"py2exe":{"includes":["sip"]}},
    options = { "py2exe": { "dll_excludes": ["MSVCP90.dll"] } },
    includes1 = file_list)

#    setup(windows=[{"script": "main.py", "icon_resources": [(1,"App.ico")]}],
#        zipfile=None,   #不生成library.zip文件
#        options={"py2exe":{"dll_excludes":["msvcp90.dll"],"includes":["sip"]}}
#    )