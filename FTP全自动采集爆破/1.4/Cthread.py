#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#根据数据量判断线程
#from __future__ import division
import Cmysql #数据库操作文件
import threading
import thread
import ConfigParser  #INI读取数据

class CS_Cthread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sql=Cmysql.mysql_handle()
        self.sql.mysql_open()
        self.run()

    def run(self):
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("gost.ini"))
            self.th_openurl = int(config.get("DATA","th_openurl"))
            self.th_openftp = int(config.get("DATA","th_openftp"))
            self.th_ftppassword = int(config.get("DATA","th_ftppassword"))
        except:
            print u"=================CS_mysql_delete---run异常！！！！！================="

    def SQL_slect(self,sql):  #获取数量
        self.i=0
        try:
            self.cursor=self.sql.conn.cursor()
            n = self.cursor.execute(sql)
            self.cursor.scroll(0)
            for row in self.cursor.fetchall():
                self.i=self.i+1
            self.cursor.close()
            return self.i
        except:
            print u"获取数量=======出现异常"

    def openurl(self):
        try:
            sql="select * from openurl where openurl is NULL"
            data=self.SQL_slect(sql)
            print u"openurl要扫描数量",data,
            if data<=100:
                print u"小于100--启动线程",self.th_openurl
                return self.th_openurl
            if data<=1000:
                print u"小于1000--启动线程",self.th_openurl/2
                return self.th_openurl/2
            if data>=10000:
                print u"大于10000--启动线程",self.th_openurl/5
                return self.th_openurl/5
        except:
            return 1

    def openftp(self):
        try:
            sql="select * from openurl where openftp is NULL"
            data=self.SQL_slect(sql)
            print u"openftp要扫描数量",data,
            if data<=100:
                print u"小于100--启动线程1"
                return 1
            if data<=1000:
                print u"小于1000--启动线程",self.th_openftp/2
                return self.th_openftp/2
            if data>=5000:
                print u"大于5000--启动线程",self.th_openftp/5
                return self.th_openftp/5
        except:
            return 3

    def linkftp(self):
        try:
            sql="select * from openftp where linkftp is NULL"
            data=self.SQL_slect(sql)
            print u"linkftp要扫描数量",data,
            if data<=100:
                print u"小于100--启动线程1"
                return 1
            if data<=1000:
                print u"小于1000--启动线程",self.th_ftppassword/2
                return self.th_ftppassword/2
            if data>=5000:
                print u"大于5000--启动线程",self.th_ftppassword
                return self.th_ftppassword
        except:
            return 1



if __name__=='__main__':
    t_h=CS_Cthread()
    print t_h.openurl()
#    threads = []  #线程
#    nthreads=1
#    for i in range(nthreads):  #nthreads=10  创建10个线程
#        threads.append(CS_passwordFTP())
#
#    for thread in threads:   #不理解这是什么意思    是结束线程吗
#        thread.start()  #start就是开始线程