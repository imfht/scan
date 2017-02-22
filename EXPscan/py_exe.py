# -*- coding: utf-8 -*-
#windows  #无控制台 
#console   #有控制台

from distutils.core import setup  

import py2exe

try:
    setup(version = "webshell",description = "0.1",
        name = "postadmin",zipfile=None,
        console=[{"script": "main.py", "icon_resources": [(1,"App.ico")]}],
        options={"py2exe":{"includes":["sip"]}},
        includes1 = ["Class_Queue.py","Class_thread.py","yijuhua_CS.py",
                     "cms\\exp_cmseasy_IIS6_jx.py","cms\\exp_dedecms_getshell.py","cms\\exp_dedecms_yijuhua.py",
                     "cms\\exp_etcms_Upload_shell.py","cms\\exp_kingcms_getshell.py","cms\\exp_phpcmsv9_getshell.py",
                     "cms\\UPLOAD.py","cms\\yijuhua_CS.py","cms\\bc_DedeCms_5x","cms\\sql_dede_57_sp1.py",
                     "IIS\\exp_IIS_webdav.py","IIS\\yijuhua_CS.py",
                     "e_x_p\\exp_Upload_ewebeditor_asp_2_1_6","e_x_p\\yijuhua_CS.py",
                     "b_c\\bc_shopex_4_8_5.py","b_c\\bc_nfsj_jlxt_wrtx.py"])
# 你的代码
except BaseException, e:
    print "1111111111111111111111111111111",(str(e))