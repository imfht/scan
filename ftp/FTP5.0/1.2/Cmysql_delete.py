#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#检测更新数据库
import time
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import Cmysql #数据库操作文件
import threading
import thread
import ConfigParser  #INI读取数据

class CS_mysql_delete(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sql=Cmysql.mysql_handle()
        self.sql.mysql_open()
        self.ftppassword=0  #读取表顺序

    def run(self):
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("gost.ini"))
            self.openurl = int(config.get("DATA","openurl"))
            self.openftp = int(config.get("DATA","openftp"))
            self.ftppassword0 = int(config.get("DATA","ftppassword0"))
            self.ftppassword1 = int(config.get("DATA","ftppassword1"))
            print u"=================CS_mysql_delete线程启动================="
            #print self.Auploadfile
            self.open_mysql()     #读取URL
        except:
            print u"=================CS_mysql_delete---run异常！！！！！================="
            time.sleep(60)
            self.run()

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
            #print u"ftppassword3出现异常"
            time.sleep(4)
            self.sql.mysql_S()  #保存数据
            self.open_mysql()     #读取URL

    def delete_ftppassword1(self):  #清除表ftppassword1
        try:
            sql="select * from ftppassword1"
            data=self.SQL_slect(sql)
            if data>=self.ftppassword1:
                print u"=================开始清理表ftppassword1中多余数据================="
                self.cursor=self.sql.conn.cursor()
                n = self.cursor.execute(sql)
                self.cursor.scroll(0)
                for row in self.cursor.fetchall():
                    delete="delete from ftppassword1 where IP='%s'"%(row[0])
                    self.cursor.execute(delete)
                    self.sql.mysql_S()  #保存数据
                self.cursor.close()

            time.sleep(60)
            self.sql.mysql_S()  #保存数据
            self.open_mysql()     #读取URL
        except:
            time.sleep(4)
            self.sql.mysql_S()  #保存数据
            self.open_mysql()     #读取URL

    def delete_ftppassword0(self):  #清除表ftppassword0
        try:
            sql="select * from ftppassword0 where root IS NOT NULL"
            data=self.SQL_slect(sql)
            if data>=self.ftppassword0:
                print u"=================开始清理表ftppassword0中多余数据================="
                self.cursor=self.sql.conn.cursor()
                n = self.cursor.execute(sql)
                self.cursor.scroll(0)
                for row in self.cursor.fetchall():
                    delete="delete from ftppassword0 where IP='%s'"%(row[0])
                    self.cursor.execute(delete)
                    self.sql.mysql_S()  #保存数据
                self.cursor.close()

            time.sleep(60)
            self.sql.mysql_S()  #保存数据
            self.open_mysql()     #读取URL
        except:
            time.sleep(4)
            self.sql.mysql_S()  #保存数据
            self.open_mysql()     #读取URL

    def delete_openftp(self):  #清除表openftp
        try:
            sql="select * from openftp where linkftp IS NOT NULL"
            data=self.SQL_slect(sql)
            if data>=self.openftp:
                print u"=================开始清理表openftp中多余数据================="
                self.cursor=self.sql.conn.cursor()
                n = self.cursor.execute(sql)
                self.cursor.scroll(0)
                for row in self.cursor.fetchall():
                    delete="delete from openftp where url='%s'"%(row[0])
                    self.cursor.execute(delete)
                    self.sql.mysql_S()  #保存数据
                self.cursor.close()

            time.sleep(60)
            self.sql.mysql_S()  #保存数据
            self.open_mysql()     #读取URL
        except:
            time.sleep(4)
            self.sql.mysql_S()  #保存数据
            self.open_mysql()     #读取URL

    def delete_openurl(self):  #清除表openurl
        try:
            sql="select * from openurl where openurl IS NOT NULL and openftp IS NOT NULL"
            data=self.SQL_slect(sql)
            if data>=self.openurl:
                print u"=================开始清理表openurl中多余数据================="
                self.cursor=self.sql.conn.cursor()
                n = self.cursor.execute(sql)
                self.cursor.scroll(0)
                for row in self.cursor.fetchall():
                    delete="delete from openurl where url='%s'"%(row[0])
                    self.cursor.execute(delete)
                    self.sql.mysql_S()  #保存数据
                self.cursor.close()

            time.sleep(60)
            self.sql.mysql_S()  #保存数据
            self.open_mysql()     #读取URL
        except:
            time.sleep(4)
            self.sql.mysql_S()  #保存数据
            self.open_mysql()     #读取URL



    def open_mysql(self):  #读取URL
        try:
            self.ftppassword=self.ftppassword+1  #读取表顺序
            print self.ftppassword
            if self.ftppassword==1:
                time.sleep(60*10)
                self.delete_openurl()  #清除表openurl
            if self.ftppassword==2:
                time.sleep(60*10)
                self.delete_openftp()  #清除表openftp
            if self.ftppassword==3:
                time.sleep(60*10)
                self.delete_ftppassword0()  #清除表ftppassword0
            if self.ftppassword==4:
                time.sleep(60*10)
                self.delete_ftppassword1()  #清除表ftppassword1

            if self.ftppassword>=4:
                self.ftppassword=0

            time.sleep(60)
            self.sql.mysql_S()  #保存数据
            self.open_mysql()     #读取URL
        except:
            print u"=================CS_mysql_delete异常！！！！！================="
            time.sleep(4)
            self.sql.mysql_S()  #保存数据
            self.open_mysql()     #读取URL


################################################
if __name__=='__main__':
    threads = []  #线程
    nthreads=1
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(CS_mysql_delete())

    for thread in threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程