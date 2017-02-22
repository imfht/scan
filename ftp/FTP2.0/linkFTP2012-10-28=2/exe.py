# -*- coding: utf-8 -*-
#windows
#console

from distutils.core import setup  

import py2exe

#setup(version = "1.0",description = "Tel: 18222329851",name = "downmp3",zipfile=None,windows=[{"script": "linkFTP.py", "icon_resources": [(1, "2.ico")] }])

setup(console=['linkFTP.py'])   #需要编译的文件

