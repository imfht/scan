#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#根据数据量判断线程
#from __future__ import division
import Csqlite3 #数据库操作文件
import threading
import thread
import ConfigParser  #INI读取数据
import time

class CS_Cthread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()
        self.run()

    def run(self):
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("gost.ini"))
            self.th_openurl = int(config.get("DATA","th_openurl"))
            self.th_openftp = int(config.get("DATA","th_openftp"))
            self.th_ftppassword = int(config.get("DATA","th_ftppassword"))
            print u"扫描openurl原始线程数",self.th_openurl
            print u"扫描openftp原始线程数",self.th_openftp
            print u"扫描ftppassword原始线程数",self.th_ftppassword
        except:
            print u"=================CS_mysql_delete---run异常！！！！！================="

    def SQL_slect(self,sql):  #获取数量
        self.i=0
        try:
            self.sql3.conn.commit()# 获取到游标对象
            cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
            cur.execute(sql)# 获取所有结果
            res = cur.fetchall()  #从结果中取出所有记录
            for line in res:
                self.i=self.i+1
            cur.close()  #关闭游标
            return self.i
        except:
            print u"获取数量=======出现异常"
            return self.i

    def openurl(self):
        try:
            sql="select * from openurl where openurl is NULL"
            data=self.SQL_slect(sql)
            print u"openurl要扫描数量",data,
            if data==0:
                print u"小于100--启动线程1"
                return 1
            if data<=100:
                print u"小于100--启动线程",self.th_openurl
                return self.th_openurl
            if data<=1000:
                print u"小于1000--启动线程",self.th_openurl/2
                return self.th_openurl/2
            if data<=5000:
                print u"小于5000--启动线程",self.th_openurl/3
                return self.th_openurl/3
            if data<=10000:
                print u"小于e10000--启动线程",self.th_openurl/5
                return self.th_openurl/5
            if data>10000:
                print u"大于10000--启动线程1"
                return 1
        except:
            return 1

    def openftp(self):
        try:
            sql="select * from openurl where openftp is NULL"
            data=self.SQL_slect(sql)
            print u"openftp要扫描数量",data,
            if data==0:
                print u"小于100--启动线程1"
                return 1
            if data<=100:
                print u"小于100--启动线程",self.th_openftp
                return self.th_openftp
            if data<=1000:
                print u"小于1000--启动线程",self.th_openftp/2
                return self.th_openftp/2
            if data<=3000:
                print u"小于3000--启动线程",self.th_openftp/5
                return self.th_openftp/5
            if data<=5000:
                print u"小于5000--启动线程",self.th_openftp
                return self.th_openftp
            if data>5000:
                print u"大于5000--启动线程",self.th_openftp
                return self.th_openftp
        except:
            return 3

    def linkftp(self):
        try:
            sql="select * from openftp where linkftp is NULL"
            data=self.SQL_slect(sql)
            print u"linkftp要扫描数量",data,
            if data==0:
                print u"小于100--启动线程1"
                return 1
            if data<=100:
                print u"小于100--启动线程1"
                return 1
            if data<=1000:
                print u"小于1000--启动线程",self.th_ftppassword/2
                return self.th_ftppassword/2
            if data<=3000:
                print u"小于3000--启动线程",self.th_ftppassword/3
                return self.th_ftppassword/3
            if data<=4000:
                print u"小于4000--启动线程",self.th_ftppassword/4
                return self.th_ftppassword/4
            if data<=5000:
                print u"小于5000--启动线程",self.th_ftppassword
                return self.th_ftppassword
            if data>5000:
                print u"大于5000--启动线程",self.th_ftppassword
                return self.th_ftppassword
        except:
            return 1

if __name__=='__main__':
    t_h=CS_Cthread()
    print t_h.linkftp()
    print t_h.openurl()
    print t_h.openftp()
