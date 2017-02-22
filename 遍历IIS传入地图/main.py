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

import urllib2
def Aurl_post(URL):   #提交数据
    try:
        req = urllib2.Request(URL)
        req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
        s = urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        #ss = s.read()
    except Exception,e:
        print e
        return 0

def IIS_xml1():
    try:
        data=open_file()
        if data==0:
            print u"Cannot find the file path in the C IIsWebServerfile"  #无法找到IIS配置文件
            return 0
        p2 = re.compile(r'<IIsWebVirtualDir.+?Path="(.+?)"')  #网站路径  LogFileDirectory="D:\nwwwroot\jisiw\logfiles"
        data2=data.replace("\n", ':')  #去除换行符好匹配
        ###########################################################
        IISWEB = p2.findall(data2)#网站路径
        for every1 in IISWEB:#网站路径
            print "===%s==="%(every1)
            bl_dt(every1)  #遍历地图
            time.sleep(0.5)
        ###########################################################
    except BaseException, e:
        print(str(e))
        return 0

def bl_dt(openurl):   #遍历地图
    try:
        xxx = file('sitemap.html', 'r')  #读取要写入的文件
        data1=xxx.read()
        TXT_file(openurl+"\sitemap.html",data1)  #写入文本 中文

        xxx = file('sitemap.xml', 'r')  #读取要写入的文件
        data2=xxx.read()
        TXT_file(openurl+"\sitemap.xml",data2)  #写入文本 中文

        xxx = file('sitemap.xsl', 'r')  #读取要写入的文件
        data3=xxx.read()
        TXT_file(openurl+"\sitemap.xsl",data3)  #写入文本 中文

        TXT_file_long(openurl)  #写入文本 中文
    except Exception,e:
        print "Write TXT failed",e
        return 0

def TXT_file_long(data):  #写入文本 中文
    try:
        #file_nem=time.strftime('%Y.%m.%d')   #file_nem+".txt"
        file_object = open("long.txt",'a+')
        file_object.write(data) #成功
        file_object.writelines("\n")
        file_object.close()
    except Exception,e:
        print "long.txt",e
        return 0

def TXT_file(name,data):  #写入文本 中文
    try:
        #file_nem=time.strftime('%Y.%m.%d')   #file_nem+".txt"
        file_object = open(name,'w+')
        file_object.write(data) #成功
        file_object.writelines("\n")
        file_object.close()
    except Exception,e:
        print "Write TXT failed",e
        return 0
####################################################################
####################################################################

list_file=[]    #文件路径
list_url=[]    #URL地址
list_file2=[]    #文件路径  去重复
list_url2=[]    #URL地址  去重复
import socket
socket.setdefaulttimeout(10)
import time
if __name__ == "__main__":
    IIS_xml1()  #iis操作

    bl_dt("C:\\123")   #遍历地图

