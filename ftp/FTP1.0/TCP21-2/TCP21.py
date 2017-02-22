#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
####################################################################
##################################################
#qq:316118740
#BLOG:http://hi.baidu.com/alalmn
# Python 扫描IP段  指定端口是否开放
#  刚学写的不好请大家见谅
##################################################
import socket
import threading,time
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
#查看IP端口是否开放
class socket_port(threading.Thread):
    def __init__(self,cond, name):
        super(socket_port, self).__init__()
        self.cond = cond
        self.cond.set()#将标识位设为Ture
        self.HOST = name
    def run(self):
        #time.sleep(1) #确保先运行Seeker中的方法
        try:
            PORT=21
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.HOST,PORT))
            print""
            print self.HOST,u":",PORT,u"端口开放",

            sql_desc = "insert into port21(IP,TIME) VALUES('%s','%s')"%(self.HOST,time.strftime('%Y.%m.%d-%H.%M.%S'))
            if mysql.mysql_insert(sql_desc): #添加
                print u"添加成功"
            else:
                print u"添加失败"
            mysql.mysql_S()  #保存数据
            #self.cond.wait()#堵塞线程，直到Event对象内部标识位被设为True或超时（如果提供了参数timeout）。
            self.cond.set()#将标识位设为Ture
            return 1
        except:
            print ".",
            #print self.HOST,u":",PORT,u"端口未开放"
            #self.cond.wait()#堵塞线程，直到Event对象内部标识位被设为True或超时（如果提供了参数timeout）。
            self.cond.set()#将标识位设为Ture
        return 0
##
#socket_port("192.168.2.1")
#if socket_port("192.168.2.100"):
#    print "开放"
#else:
#    print "未开放"

def ip2num(ip):
    ip = [int(x) for x in ip.split('.')]
    return ip[0]<<24 | ip[1]<<16 | ip[2]<<8 | ip[3]

def num2ip(num):
    #time.sleep(0.05) #50ms
    #time.sleep(0.1) #s
#    data='%s.%s.%s.%s' % (  (num & 0xff000000) >> 24,
#                                 (num & 0x00ff0000) >> 16,
#                                 (num & 0x0000ff00) >> 8,
#                                  num & 0x000000ff  )
#    #socket_port(data)  #查看IP端口是否开放
    if num>=IPend:
        print u"IP导入数组完成"
    return '%s.%s.%s.%s' % (  (num & 0xff000000) >> 24,
                              (num & 0x00ff0000) >> 16,
                              (num & 0x0000ff00) >> 8,
                              num & 0x000000ff  )

def gen_ip(ip1,ip2):  #返回数组
#    ip
#    global IPend
#    start, IPend = [ip2num(x) for x in ip.split('-')]
    global IPend
    IPend=ip2
    return [num2ip(num) for num in range(ip1,ip2+1) if num & 0xff]
##################################################
import sys
import os
import atexit
def close():  #自动重启本程序
    try:
        print u"------------------自动重启本程序------------------"
        mysql.mysql_S()  #保存数据
        mysql.mysql_close()  #关闭数据库
    #    python = sys.executable
    #    os.execl(python, python, * sys.argv)
    #    mysql.mysql_close()  #关闭数据库
        time.sleep(10)
        #    os.system('python txt.py')
        python = sys.executable
        os.execl(python, python, * sys.argv)
        #########
    except:
        print u"------------------自动重启本程序---异常------------------"
        sys.exit(0)  #结束进程


def dqsqlite_bcini():  #扫描完成后  读取配置信息后在自+1  在读取数据库相应信息  在保存信息  重启程序就可以了
    try:
        ini.ini_get()  #读取INI
        abc=int(ini.ID)+1   #获取要查询的ID
        sql_desc = "SELECT * FROM ip where ID='%s'"%(abc)
        n = mysql.cursor.execute(sql_desc)
        mysql.cursor.scroll(0)
        for row in mysql.cursor.fetchall():
            ini.ini_write(abc,row[1],row[2])  #修改INI
    #获取游标
#        sqlite_cursor = sqlite.sqlite_conn.cursor()
#        sql_desc = "SELECT * FROM ip where ID='%s'"%(abc)
#        sqlite_cursor.execute(sql_desc)
#        for row in sqlite_cursor:
#            ini.ini_write(abc,row[1],row[2])  #修改INI
#        sqlite.sqlite_cursor.close()   #关闭游标
        #return 1
        atexit.register(close)#自动重启本程序
    except:
        print u"数据库读取异常！！"
        #return 0
#    sqlite.sqlite_S()  #保存数据
 #   sqlite.sqlite_close()  #关闭数据库
        atexit.register(close)#自动重启本程序

import ini
import mysql
if __name__=='__main__':
    try:
        mysql.mysql_open()  #连接数据库
        ini.ini_get()  #读取INI
        print u"开始IP:",ini.IP1,u"-------",u"结束IP:",ini.IP2
        if ini.IP1>=ini.IP2:
            print u"IP以扫描完成"
            dqsqlite_bcini()  #扫描完成后  读取配置信息后在自+1  在读取数据库相应信息  在保存信息  重启程序就可以了

        print u"IP还没扫描完"
        list_ip=gen_ip(ip2num(ini.IP1),ip2num(ini.IP2))
        I1 = 0 #得到list的第一个元素
        print u"开始扫描IP"
        ip=0
        while I1 < len(list_ip):
            if ip>=255:
                ini.ini_write(int(ini.ID),list_ip[I1],ini.IP2)  #修改INI
                ip=0
                print list_ip[I1]
            ip = ip + 1
            #print list_ip[I1]
            time.sleep(0.1) #确保先运行Seeker中的方法
            cond = threading.Event()
            hider = socket_port(cond,list_ip[I1])
            hider.start()

            I1 = I1 + 1   #一层

        print u"IP扫描完成将从新导入"
        dqsqlite_bcini()  #扫描完成后  读取配置信息后在自+1  在读取数据库相应信息  在保存信息  重启程序就可以了
    except:
        #dqsqlite_bcini()  #扫描完成后  读取配置信息后在自+1  在读取数据库相应信息  在保存信息  重启程序就可以了
        atexit.register(close)


#######################################################################















































