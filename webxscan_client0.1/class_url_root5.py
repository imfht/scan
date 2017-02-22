#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import threading
import sys
import os
import urllib2
import time
import class_Queue  #消息队列
url_root5 = class_Queue.url_root5

from url_root5.Class_www_ip_bing import Class_www_ip_bing  #查询C段主机绑定的域名

class class_url_root5(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def open_url_data(self,url):  #读取网页内容
        try:
            req = urllib2.Request(url)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            return s.read()
        except:
            return 0

    def run(self):
        try:
            if url_root5.empty():   #判断队列是否为空
                #print u"已经没有可操作的URL了"
                time.sleep(30)
                self.run()

            self.URL = url_root5.get(0.5)  #get()方法从队头删除并返回一个项目
            ss=self.open_url_data(self.URL)
            if ss==0:  #读取网页内容
                print u"%s:URL网站可能无法打开"%(self.URL)
                time.sleep(5)
                self.run()

            self.CS_URL(self.URL)
            #self.CS_URL("http://www.anzhuo.com")
            self.run()
        except Exception,e:
            print e
            self.run()
            return 0

    def CS_URL(self,URL):
        try:
            print "class_url_root5 Start Scan-%s-%s"%(URL,time.strftime('%Y.%m.%d-%H.%M.%S'))
            #--------------------------
            #查询C段主机绑定的域名
            threads = []  #线程
            for i in range(1):
                threads.append(Class_www_ip_bing(URL))
            for t in threads:
                t.start()
            #--------------------------
            #--------------------------
            #--------------------------
            #--------------------------
            #--------------------------
            #--------------------------
            #--------------------------
            time.sleep(120)
            return 0
        except Exception,e:
            print e
            return 0


################################################
if __name__=='__main__':
#启动线程控制漏洞扫描
    threads = []  #线程
    for i in range(1):
        threads.append(class_url_root3())
    for t in threads:
        t.start()