#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
from ftplib import FTP
import time
import mysql #数据库操作文件
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
INI_data1=0  #扫描过URL个
INI_data2=0  #未开放FTP
INI_data3=0  #开放FTP
def host_ftp(host):  #测试URL FTP是否开放
    global INI_data1  #扫描过URL个
    global INI_data2  #未开放FTP
    global INI_data3  #开放FTP
    try:
        if host == '':  #传入值等于空   返回
            print u"传入地址不能为空"
            time.sleep(1) #确保先运行Seeker中的方法
            #sql_sel()   #SQL查询
            return 0

        ftpB = FTP()  #初始化FTP类
        ftpB.connect(host,21)  #连接 服务器名  端口号
        ftpB.quit() #退出ftp服务器

        sql_up(host,"send")
        INI_data3=INI_data3+1  #开放FTP
        print u"连接成功添加url:",host
        sql="insert into ftp (url,time) VALUES ('%s','%s')"%(host,time.strftime('%Y.%m.%d-%H.%M.%S'))
        mysql.mysql_insert(sql) #添加到数据库
        mysql.mysql_S()  #保存数据
        print u"-------扫描过URL:%s个/未开放FTP:%s个/开放FTP:%s个-------"%(INI_data1,INI_data2,INI_data3)
        open_mysql()   #SQL查询
        #SQL修改数据
#        if sql_up(host,"send"):
#            print host,u"服务器FTP21端口开放-修改成功",
#            print u"(∩_∩)"  #添加成功
#            open_mysql()   #SQL查询
#            return 1
#        else:
#            print host,u"服务器FTP21端口开放-修改失败",
#            print u"(╯▽╰)"  #添加失败
#            open_mysql()   #SQL查询
#            return 0
    except:
        print host,u"服务器FTP21端口可能没有开放",
        sql_up(host,"no21") #SQL修改数据
        INI_data2=INI_data2+1  #未开放FTP
        open_mysql()   #SQL查询
        return 0
    ##########################
################################################
import random  #产生一个随机数
def sql_up(url,data): #SQL修改数据
    try:
        up = "update  url set  ftpsend='%s' where url='%s'"%(data.encode('utf-8'),url)
        if mysql.mysql_update(up):  #修改数据
            print url,u"修改数据库",data,u"成功\n"
            mysql.mysql_S()  #保存数据
            a=random.randrange(1,4)   #产生一个随机数8以内的
            time.sleep(a) #确保先运行Seeker中的方法
            return 1
        else:
            print url,u"修改数据库",data,u"失败\n"
            mysql.mysql_S()  #保存数据
            b=random.randrange(5,15)   #产生一个随机数8以内的
            time.sleep(b) #确保先运行Seeker中的方法
            return 0
            #mysql.mysql_S()  #保存数据
    except:
        print u"修改数据出错"
        mysql.mysql_S()  #保存数据
        mysql.mysql_close()  #关闭数据库
        #close()  #自动重启本程序
        atexit.register(close)#自动重启本程序

import urllib2
def open_mysql():  #读取URL
    try:
        global INI_data1  #扫描过URL个
        try:   #检测网络连接状态
            urllib2.urlopen(r"http://www.163.com",timeout=10)
            #print u"网络连接成功"
            #return 1
        except:
            print u"网络无连接 重启程序自身"
            mysql.mysql_S()  #保存数据
            mysql.mysql_close()  #关闭数据库
            atexit.register(close)#自动重启本程序
        sql="select * from url where ftpsend is NULL limit 1"
        data = mysql.mysql_select(sql)
        #print U"数据库URL",data
        if ~data.find("null123456"):
            print u"可能无读取的数据请查看数据库！！！！！"
            mysql.mysql_S()  #保存数据
            time.sleep(1)  #3秒
            atexit.register(close)#自动重启本程序
        update = "update url set ftpsend='send' where url='%s'"%(data)
        mysql.mysql_update(update)
        mysql.mysql_S()  #保存数据
        #url_data = "http://"+data
        print u"测试URLFTP：",data
        INI_data1=INI_data1+1  #扫描过URL个
        host_ftp(data)  #测试URL FTP是否开放
    except:
        print u"读取URL异常！！！！！"
        print u"3秒后,程序将结束重启..."
        mysql.mysql_S()  #保存数据
        mysql.mysql_close()  #关闭数据库
        #close()  #自动重启本程序
        atexit.register(close)#自动重启本程序
################################################
import sys
import os
import atexit
def close():  #自动重启本程序
    try:
        print u"自动重启本程序"
        time.sleep(3)
        python = sys.executable
        os.execl(python, python, * sys.argv)
        #########
    except:
        sys.exit(0)  #结束进程


if __name__=='__main__':
    try:
        #print __doc__
        mysql.mysql_open()  #连接数据库
        open_mysql()     #读取URL
    except:
        atexit.register(close)

