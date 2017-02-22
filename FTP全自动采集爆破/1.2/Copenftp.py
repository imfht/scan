#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#查看采集到的URL地址FTP是否开发
###############################################
from ftplib import FTP
import urllib2, time
import Cmysql #数据库操作文件
import socket
import threading
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import thread

class CS_openftp(threading.Thread):
    def __init__(self,htint):
        threading.Thread.__init__(self)
        self.Ht=htint
        self.INI_data1=0  #扫描过URL个
        self.INI_data2=0  #未开放FTP
        self.INI_data3=0  #开放FTP
        self.Internet=100  #控制到300次检测一次网络状态
        self.printf=10  #控制显示
        self.sql=Cmysql.mysql_handle()
        self.sql.mysql_open()

    def run(self):
        try:
            print u"====CS_openftp线程%d启动===="%(self.Ht)
            self.open_mysql()     #读取URL
        except:
            print u"====线程%d--CS_openftp---run异常！！！！！===="%(self.Ht)
            time.sleep(60)
            self.run()

    def open_mysql(self):  #读取URL
        try:
            sql="select * from openurl where openftp is NULL limit 1"
            data = self.sql.mysql_select(sql)
            #print U"数据库URL",data
            if ~data.find("null123456"):
                print u"====线程%d--CS_openftp可能无读取的数据请查看数据库！！！！！===="%(self.Ht)
                self.sql.mysql_S()  #保存数据
                time.sleep(10)  #3秒
                self.open_mysql()     #读取URL
            update = "update openurl set openftp='send' where url='%s'"%(data)
            self.sql.mysql_update(update)
            self.sql.mysql_S()  #保存数据
            #print u"测试URLFTP：",data
            self.INI_data1=self.INI_data1+1  #扫描过URL个
            self.host_ftp(data)  #测试URL FTP是否开放
        except:
            print u"====线程%d--CS_openftp读取URL异常！！！！！===="%(self.Ht)
            time.sleep(4)
            self.sql.mysql_S()  #保存数据
            self.open_mysql()     #读取URL

    def host_ftp(self,host):  #测试URL FTP是否开放
        try:
            if host == '':  #传入值等于空   返回
                #print u"传入地址不能为空"
                time.sleep(5)
                self.open_mysql()   #SQL查询
                return 0

            ftpB = FTP()  #初始化FTP类
            ftpB.connect(host,21)  #连接 服务器名  端口号
            ftpB.quit() #退出ftp服务器

            #sql_up(host,"send")   上边已经标记修改过了
            self.INI_data3=self.INI_data3+1  #开放FTP
            #print u"连接成功添加url:",host
            sql="insert into openftp (url,time) VALUES ('%s','%s')"%(host,time.strftime('%Y.%m.%d-%H.%M.%S'))
            self.sql.mysql_insert(sql) #添加到数据库
            self.sql.mysql_S()  #保存数据
            if self.printf>=10:
                print u"====线程%d--%sFTP开放-扫描过URL:%s个/未开放FTP:%s个/开放FTP:%s个===="%(self.Ht,host,self.INI_data1,self.INI_data2,self.INI_data3)
                self.printf=0
            self.printf=self.printf+1
            if self.INI_data1>=3000 and self.INI_data3>=1000:
                self.INI_data1=0
                self.INI_data2=0
                self.INI_data3=0
            self.open_mysql()   #SQL查询
        except:
            #print host,u"服务器FTP21端口可能没有开放",
            #sql_up(host,"no21") #SQL修改数据
            up = "update openurl set openftp='%s' where url='%s'"%("no21",host)
            self.sql.mysql_insert(up) #添加到数据库
            self.sql.mysql_S()  #保存数据
            self.INI_data2=self.INI_data2+1  #未开放FTP
            time.sleep(5)
            self.open_mysql()   #SQL查询
            return 0


################################################
if __name__=='__main__':
    threads = []  #线程
    nthreads=1
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(CS_openftp(i))

    for thread in threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程




