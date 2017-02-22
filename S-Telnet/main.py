#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#FTP采集爆破
import Sip #IP端口扫描
import STelnet #对Telnet实现暴力破解

import time
import ctypes   #DLL调用
import thread


def Crun():  #启动
    thrint=1
    #print "-"*60
    Sip_nthreads=10
    STelnet_nthreads=50
    #time.sleep(10)
    ###########################
    #IP端口扫描
    Sip_threads = []  #线程
    for i in range(Sip_nthreads):  #nthreads=10  创建10个线程
        Sip_threads.append(Sip.S_ip(thrint))
        thrint=thrint+1

    for thread in Sip_threads:
        time.sleep(2) #确保先运行Seeker中的方法
        thread.start()  #start就是开始线程
    ###########################
    #IP端口扫描
    STelnet_threads = []  #线程
    for i in range(STelnet_nthreads):  #nthreads=10  创建10个线程
        STelnet_threads.append(STelnet.CS_Telnet(thrint))
        thrint=thrint+1

    for thread in STelnet_threads:
        time.sleep(2) #确保先运行Seeker中的方法
        thread.start()  #start就是开始线程
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
    print u"      欢迎使用Telnet暴力破解-----BY：落雪                               "
    print u"      谢谢灰帽程序员论坛对本软件技术支持--http://hmhacker.org/            "
    print u"                落雪网络技术--QQ交流群293663651                         "
    print u"----------------------------------------------------------------------"
    #time.sleep(10)
    Crun()  #启动
#    try:
#        if Aintet_close():
#            print u"在线"
#            Crun()  #启动
#            thread.start_new_thread(intet_close())#检测网络在线状态
#        else:
#            print u"不在线---自动重启本程序延时10S"
#            time.sleep(5)
#            atexit.register(close)#自动重启本程序
#    except:
#    #    user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
#    #    user32.MessageBoxA(0, u'内容', u'标题', 0)   # 调用MessageBoxA函数
#        time.sleep(10)
#        atexit.register(close)










