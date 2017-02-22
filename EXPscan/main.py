#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import Class_thread
import Class_Queue #消息队列机制
import threading
import time
import sys

def add_Queue():  #添加到消息队列
    try:
        list=[]
        list_2=[]
        xxx = file(TXT_file, 'r')
        for xxx_line in xxx.readlines():  #读取数据
            #如果输入的内容读取有回车符号，可以用strip来消除，可得到完美的输出

            data=xxx_line.strip()
            list.append(str(data))  #添加数据
            #print data
            # if "http://" in data:
            #     print u"%s网址请不要http://"%(data)
            # else:
                #print data
                #list.append(data)  #添加数据
            #    Class_Queue.Bopenurl.put(data,0.3)   #插入队列

        for i in list:  #去重重复数据
            if i not in list_2:
                list_2.append(i)

        for i in list_2:  #添加到数组
            if "http" in i:
                print u"%s网址请不要http://"%(i)
                continue  #跳过
            Class_Queue.Bopenurl.put(i,0.3)   #插入队列

        print u"初始数据%d 过滤掉重复%s条可以URL地址"%(len(list),Class_Queue.Bopenurl.qsize())
    except Exception,e:
        print u"添加到消息队列   错误",e
        return 0

def Crun():
    try:
        #启动消息队列
        threads = []  #线程
        for i in range(1):  #nthreads=10  创建10个线程
            threads.append(Class_Queue.C_Queue())
        for t in threads:   #不理解这是什么意思    是结束线程吗
            t.start()  #start就是开始线程

        #添加到消息队列   先临时使用
        add_Queue()
        time.sleep(5)

        #启动爬虫采集

        #启动线程控制漏洞扫描
        threads = []  #线程
        for i in range(7):  #nthreads=10  创建10个线程
            threads.append(Class_thread.class_threading())
        for t in threads:   #不理解这是什么意思    是结束线程吗
            t.start()  #start就是开始线程

    except Exception,e:
        #print e
        Crun()
        return 0


################################################
if __name__=='__main__':
    print u"---------------------------------------------------------------------"
    print u"   软件只是娱乐测试  软件使用方法   main.exe 1.txt     软件名 扫描URL            "
    print u"漏洞自动利用工具            "
    print u"下面为EXP漏洞            "
    print u"1.IIS-写入漏洞                      exp_IISwebdav_move        "
    print u"2.cmseasy文件上传+IIS6解释漏洞      exp_cmseasy_IIS6_jx          "
    print u"3.dedecms-5.7-getshell              exp_dedecms_getshell       "
    print u"4.PHPcms-V9-任意文件读取漏洞        exp_phpcmsv9_getshell       "
    print u"5.dede-5.66官方一句话               exp_dedecms_yijuhua        "
    print u"6.kingcms-Getshell漏洞              exp_kingcms_getshell         "
    print u"7.易通cms上传shell漏洞              exp_etcms_Upload_shell        "
    print u"8.ewebeditor-asp-2.1.6版-上传漏洞   exp_ewebeditor_Upload_asp  提供者:Xzz           "
    print u""
    print u"下面为SQL注入            "
    print u"1.dedecms-search-5.7-sp1注入        sql_dede_57_sp1X2       "
    print u""
    print u"下面为暴库            "
    print u"1.DedeCms-5.x  本地文件包含漏洞     bc_DedeCms_5x "
    print u"2.dedecms-/plus/search.php注入      bc_dedecms_search_php1"
    print u"3.Shopex-4.8.5 SQL-Injection        bc_shopex_4_8_5    提供者:MXi4oyu"
    print u"4.通杀南方数据、良精系统、网软天下等    bc_nfsj_jlxt_wrtx  提供者:落泪红尘   "
    print u"         https://forum.90sec.org/      http://hmhacker.org/         "
    print u"--------大家有什么比较好的漏洞(老的也没问题)发到  29295842@qq.com----------"
    print u"-----------------time:---2013.6.29---版本号:0.1------------------------"
    print u"----------------------------------------------------------------------"
    global TXT_file #导入文本
    TXT_file = None
    #TXT_file ="2013.06.22.txt"
    if len(sys.argv) < 2:
        print u"无参数传入"
        print u"无参数传入   \r\n软件使用方法   main.exe 1.txt     软件名 扫描URL "
        print u"无参数传入   \r\n软件使用方法   main.exe 1.txt     软件名 扫描URL "
        time.sleep(200)
    TXT_file=sys.argv[1]
    Crun()







