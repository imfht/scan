#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import threading
import sys
import os
import urllib2
import time
import class_Queue  #消息队列
url_root4 = class_Queue.url_root4
#通用 网站漏洞  上传入口  表单提交  SQL注入类的

from url_root4.Class_www import Class_www  # 子域名枚举

class class_url_root4(threading.Thread):
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
            if url_root4.empty():   #判断队列是否为空
                #print u"已经没有可操作的URL了"
                time.sleep(30)
                self.run()

            self.URL = url_root4.get(0.5)  #get()方法从队头删除并返回一个项目
            ss=self.open_url_data(self.URL[1])
            if ss==0:  #读取网页内容
                print u"class_url_root4 %s:URL网站可能无法打开"%(self.URL[1])
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
            print "class_url_root4 Start Scan-%s-%s"%(URL,time.strftime('%Y.%m.%d-%H.%M.%S'))
            #--------------------------
#            # 子域名枚举
            www=Class_www()
            www.scan(www.assign('www', (URL[0],URL[1]))[1])
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