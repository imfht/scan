#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#检测更新数据库
import time
import Csqlite3 #数据库操作文件
import threading
import thread
import ConfigParser  #INI读取数据

class CS_mysql_delete(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()
        self.ftppassword=0  #读取表顺序

        self.openurl =20000
        self.openftp =3000
        self.ftppassword0 =500
        self.ftppassword3 =100
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("gost.ini"))
            self.openurl = int(config.get("DATA","openurl"))
            self.openftp = int(config.get("DATA","openftp"))
            self.ftppassword0 = int(config.get("DATA","ftppassword0"))
            self.ftppassword3 = int(config.get("DATA","ftppassword3"))
        except:
            print u"INI读取异常openurl,openftp,ftppassword0,ftppassword3"
        print u"=================CS_mysql_delete线程启动================="


    def run(self):
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("gost.ini"))
            self.openurl = int(config.get("DATA","openurl"))
            self.openftp = int(config.get("DATA","openftp"))
            self.ftppassword0 = int(config.get("DATA","ftppassword0"))
            self.ftppassword3 = int(config.get("DATA","ftppassword3"))
            print u"=================CS_mysql_delete线程启动================="
            #print self.Auploadfile
            time.sleep(600)
            self.open_mysql()     #读取URL
        except:
            print u"=================CS_mysql_delete---run异常！！！！！================="
            time.sleep(60)
            self.run()

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
            #print u"ftppassword3出现异常"
            time.sleep(4)
            return self.i
            #self.open_mysql()     #读取URL
    #######################################################################
    def delete_ftppassword3(self):  #清除表ftppassword3
        try:
            sql="select * from ftppassword3"
            data=self.SQL_slect(sql)
            if data>=self.ftppassword3:
                print u"=================开始清理表ftppassword1中多余数据================="
                self.sql3.conn.commit()# 获取到游标对象
                cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
                cur.execute(sql)# 获取所有结果
                res = cur.fetchall()  #从结果中取出所有记录
                for line in res:
                    delete="delete from ftppassword3 where IP='%s'"%(line[0])
                    self.sql3.mysqlite3_delete(delete)
                cur.close()
            time.sleep(5)
            self.open_mysql()     #读取URL
        except:
            time.sleep(4)
            self.open_mysql()     #读取URL

    def delete_ftppassword0(self):  #清除表ftppassword0
        try:
            sql="select * from ftppassword0 where root IS NOT NULL"
            data=self.SQL_slect(sql)
            if data>=self.ftppassword0:
                print u"=================开始清理表ftppassword0中多余数据================="
                self.sql3.conn.commit()# 获取到游标对象
                cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
                cur.execute(sql)# 获取所有结果
                res = cur.fetchall()  #从结果中取出所有记录
                for line in res:
                    delete="delete from ftppassword0 where IP='%s'"%(line[0])
                    self.sql3.mysqlite3_delete(delete)
                cur.close()
            time.sleep(5)
            self.open_mysql()     #读取URL
        except:
            time.sleep(4)
            self.open_mysql()     #读取URL

    def delete_openftp(self):  #清除表openftp
        try:
            sql="select * from openftp where linkftp IS NOT NULL"
            data=self.SQL_slect(sql)
            if data>=self.openftp:
                print u"=================开始清理表openftp中多余数据================="
                self.sql3.conn.commit()# 获取到游标对象
                cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
                cur.execute(sql)# 获取所有结果
                res = cur.fetchall()  #从结果中取出所有记录
                for line in res:
                    delete="delete from openftp where url='%s'"%(line[0])
                    self.sql3.mysqlite3_delete(delete)
                cur.close()
            time.sleep(5)
            self.open_mysql()     #读取URL
        except:
            time.sleep(4)
            self.open_mysql()     #读取URL

    def delete_openurl(self):  #清除表openurl
        try:
            sql="select * from openurl where openurl IS NOT NULL and openftp IS NOT NULL"
            data=self.SQL_slect(sql)
            if data>=self.openurl:
                print u"=================开始清理表openurl中多余数据================="
                self.sql3.conn.commit()# 获取到游标对象
                cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
                cur.execute(sql)# 获取所有结果
                res = cur.fetchall()  #从结果中取出所有记录
                for line in res:
                    delete="delete from openurl where url='%s'"%(line[0])
                    print delete
                    self.sql3.mysqlite3_delete(delete)
                cur.close()
            time.sleep(5)
            self.open_mysql()     #读取URL
        except:
            time.sleep(4)
            self.open_mysql()     #读取URL
    #######################################################################

    def open_mysql(self):  #读取URL
        try:
            self.ftppassword=self.ftppassword+1  #读取表顺序
            if self.ftppassword==1:
                print u"检测更新数据库-----开始检测openurl"
                self.delete_openurl()  #清除表openurl
                time.sleep(2)
            if self.ftppassword==2:
                print u"检测更新数据库-----开始检测openftp"
                self.delete_openftp()  #清除表openftp
                time.sleep(2)
            if self.ftppassword==3:
                print u"检测更新数据库-----开始检测ftppassword0"
                self.delete_ftppassword0()  #清除表ftppassword0
                time.sleep(2)
            if self.ftppassword==4:
                print u"检测更新数据库-----开始检测ftppassword3"
                self.delete_ftppassword3()  #清除表ftppassword3
                time.sleep(2)

            if self.ftppassword>=4:
                print u"检测更新数据库-----结束"
                return 1

        except:
            print u"=================CS_mysql_delete异常！！！！！================="
            #return 0
            self.open_mysql()     #读取URL


################################################
if __name__=='__main__':
    threads = []  #线程
    nthreads=1
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(CS_mysql_delete())

    for thread in threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程