#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import threading
import sys
import os
import urllib2
import time
import class_Queue  #消息队列
url_root1 = class_Queue.url_root1
#网站版本漏洞  webFTP  iis写入   CMS程序识别

from url_root1.b_c.bc_nfsj_jlxt_wrtx import bc_nfsj_jlxt_wrtx           #通杀南方数据、良精系统、网软天下等 管理员帐号密码
from url_root1.b_c.bc_shopex_4_8_5 import bc_shopex_4_8_5               #Shopex 4.8.5 暴库

from url_root1.I_I_S.exp_IIS_webdav import IIS                          #IIS写入漏洞

from url_root1.c_m_s.bc_DedeCms_5x import bc_DedeCms_5x                 #DedeCms 5.x 本地文件包含漏洞
from url_root1.c_m_s.bc_dedecms_search_php import bc_dedecms_search_php #dedecms 注入
from url_root1.c_m_s.exp_cmseasy_IIS6_jx import cmseasy_iis6            #cmseasy文件上传+IIS6解释漏洞
from url_root1.c_m_s.exp_dedecms_getshell import dedecms_getshell       #dedecms漏洞getshell EXP最新可用鬼哥的洞洞
from url_root1.c_m_s.exp_dedecms_yijuhua import dedecms_yijuhua         #dedeCMS  官方一句话
from url_root1.c_m_s.exp_etcms_Upload_shell import etcms_Upload_shell   #易通cms上传shell漏洞
from url_root1.c_m_s.exp_kingcms_getshell import kingcms_getshell       #kingcms Getshell漏洞
from url_root1.c_m_s.exp_phpcmsv9_getshell import phpcmsv9_getshell     #PHPcms V9 任意文件读取漏洞
from url_root1.c_m_s.sql_dede_57_sp1 import sql_dede_57_sp1             #dedecms search注入  dede 5.7 sp1

from url_root1.e_x_p.exp_Upload_ewebeditor_asp_2_1_6 import ewebeditor_Upload   #ewebeditor asp版 2.1.6 上传漏洞

from url_root1.Class_url_cms import Class_url_cms  #CMS版本识别

from url_root1.SlinkFTP import CS_linkftp   #WEB FTP弱口令

class class_url_root1(threading.Thread):
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
            if url_root1.empty():   #判断队列是否为空
                #print u"已经没有可操作的URL了"
                time.sleep(30)
                self.run()

            self.URL = url_root1.get(0.5)  #get()方法从队头删除并返回一个项目
            ss=self.open_url_data(self.URL)
            if ss==0:  #读取网页内容
                print u"%s:URL网站可能无法打开"%(self.URL)
                time.sleep(5)
                self.run()

            self.CS_URL(self.URL)
            #self.CS_URL("http://www.wuyuan168.com")
            self.run()
        except Exception,e:
            print e
            self.run()
            return 0

    def CS_URL(self,URL):
        try:
            print "class_url_root1 Start Scan-%s-%s"%(URL,time.strftime('%Y.%m.%d-%H.%M.%S'))
            #--------------------------
            #--------------------------
            #cms 版本识别
            threads = []
            for i in range(1):
                threads.append(Class_url_cms(URL))
            for tA in threads:
                tA.start()
            #--------------------------
            #WEB FTP弱口令
            threads = []  #线程
            for i in range(1):  #nthreads=10  创建10个线程
                threads.append(CS_linkftp(URL))
            for t in threads:
                t.start()
            #--------------------------
            #通杀南方数据、良精系统、网软天下等 管理员帐号密码
            threads = []  #线程
            for i in range(1):  #nthreads=10  创建10个线程
                threads.append(bc_nfsj_jlxt_wrtx(URL))
            for t in threads:
                t.start()
            #--------------------------
            #Shopex 4.8.5
            threads = []  #线程
            for i in range(1):
                threads.append(bc_shopex_4_8_5(URL))
            for t in threads:
                t.start()
            #--------------------------
            #IIS写入
            threads = []  #线程
            for i in range(1):
                threads.append(IIS(URL))
            for t in threads:
                t.start()
            #--------------------------
            #DedeCms 5.x 本地文件包含漏洞
            threads = []  #线程
            for i in range(1):
                threads.append(bc_DedeCms_5x(URL))
            for t in threads:
                t.start()
            #--------------------------
            #dedecms 注入
            threads = []  #线程
            for i in range(1):
                threads.append(bc_dedecms_search_php(URL))
            for t in threads:
                t.start()
            #--------------------------
            #cmseasy文件上传+IIS6解释漏洞
            threads = []  #线程
            for i in range(1):
                threads.append(cmseasy_iis6(URL))
            for t in threads:
                t.start()
            #--------------------------
            #dedecms漏洞getshell EXP最新可用鬼哥的洞洞
            threads = []  #线程
            for i in range(1):
                threads.append(dedecms_getshell(URL))
            for t in threads:
                t.start()
            #--------------------------
            #dedecms官方一句话扫描
            threads = []  #线程
            for i in range(1):
                threads.append(dedecms_yijuhua(URL))
            for t in threads:
                t.start()
            #--------------------------
            #易通cms上传shell漏洞
            threads = []  #线程
            for i in range(1):
                threads.append(etcms_Upload_shell(URL))
            for t in threads:
                t.start()
            #--------------------------
            #kingcms Getshell漏洞
            threads = []  #线程
            for i in range(1):
                threads.append(kingcms_getshell(URL))
            for t in threads:
                t.start()
            #--------------------------
            #PHPcms V9 任意文件读取漏洞
            threads = []  #线程
            for i in range(1):
                threads.append(phpcmsv9_getshell(URL))
            for t in threads:
                t.start()
            #--------------------------
            #dedecms search注入  dede 5.7 sp1
            threads = []  #线程
            for i in range(1):
                threads.append(sql_dede_57_sp1(URL))
            for t in threads:
                t.start()
            #--------------------------
            #ewebeditor asp版 2.1.6 上传漏洞
            threads = []  #线程
            for i in range(1):
                threads.append(ewebeditor_Upload(URL))
            for t in threads:
                t.start()
            #--------------------------
            #--------------------------
            #--------------------------
            #--------------------------
            #--------------------------
            #--------------------------
            #--------------------------
            #--------------------------
            time.sleep(20)
            return 0
        except Exception,e:
            print e
            return 0


################################################
if __name__=='__main__':
#启动线程控制漏洞扫描
    threads = []  #线程
    for i in range(1):
        threads.append(class_url_root1())
    for t in threads:
        t.start()