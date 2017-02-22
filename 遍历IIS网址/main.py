#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import re
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

def IIS_xml1():
    try:
        data=open_file()
        if data==0:
            print u"Cannot find the file path in the C IIsWebServerfile"  #无法找到IIS配置文件
            return 0
        p2 = re.compile(r'<IIsWebVirtualDir.+?Path="(.+?)"')  #网站路径  LogFileDirectory="D:\nwwwroot\jisiw\logfiles"
        p3 = re.compile(r'<IIsWebServer.+?ServerBindings="(.+?)"')#.+?:  #获取网址 ServerBindings=":80:jisi.pdwh.cn			:80:www.jisiw.cn"
        data2=data.replace("\n", ':')  #去除换行符好匹配
        ###########################################################
        IISWEB = p2.findall(data2)#网站路径
        for every1 in IISWEB:#网站路径
            #print "===%s==="%(every1)
            fileurl="%s"%(every1)
            TXT_file("weburl.txt",fileurl)  #写入文本 中文
            time.sleep(0.1)
        IISWEB = p3.findall(data2)#获取网址
        for every2 in IISWEB:#获取网址
            #print "-%s-"%(every2)
            wwwlist=every2.split(":")
            for url in wwwlist:
                if len(url)>=4:
                    url2=str(url).strip().lstrip().rstrip('')
                    #urlyjh="http://%s/%s"%(url2,argv1)  #一句话地址
                    print url2
                    TXT_file("weburl.txt",url2)  #写入文本 中文
            time.sleep(0.1)
        ###########################################################
    except BaseException, e:
        print(str(e))
        return 0



def TXT_file(name,data):  #写入文本 中文
    try:
        #file_nem=time.strftime('%Y.%m.%d')   #file_nem+".txt"
        file_object = open(name,'a+')
        file_object.write(data) #成功
        file_object.writelines("\n")
        file_object.close()
    except Exception,e:
        print "Write TXT failed",e
        return 0
####################################################################
import re,httplib
import gzip,StringIO
import socket
socket.setdefaulttimeout(10)
import sys
import time
if __name__ == "__main__":
    IIS_xml1()  #iis操作


