# -*- coding: utf-8 -*-
#windows  #无控制台 
#console   #有控制台

from distutils.core import setup  

import py2exe

#setup(version = "1.0",description = "QQ:892768447",
#      name = "STCP",zipfile=None,
#      windows=[{"script": "STCP.py", "icon_resources": [(1, "windowws.ico")]}],
#      options={"py2exe":{"includes":["sip"]}},
#      includes = ["ini.py"])

#setup(options={"py2exe": {"dll_excludes":["MSVCP90.dll"],}},
#windows=[{"script": "STCP.py"}, "icon_resources": [(1, "App.ico")]}],
#options={"py2exe":{"includes":["exe"]}},
#      includes = ["ini.py"])  


setup(version = "1.0",description = "QQ:2602159946",name = "FTP",zipfile=None,windows=[{"script": "WWWwindow.py", "icon_resources": [(1, "App.ico")]}],
      options={"py2exe":{"dll_excludes":["MSVCP90.dll"],"includes":["sip"]}},includes = ["Cmysql.py","Chost.py"])
