#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
from ftplib import FTP
import time
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
#0  连接不上
#1  连接成功
#2  有上传权限
#3  有上传和删除权限
#http://blog.csdn.net/tianzhu123/article/details/7632104
ftpID=0
def ftpconnect(host,user,pwd):    #连接FTP
    global ftpID
    ftp=FTP()
    try:
        #ftp.set_debuglevel(2) #打开调试级别2，显示详细信息
        ftp.connect(host,21) #连接
        ftp.login(user,pwd) #登录，如果匿名登录则用空串代替即可
        #print u"连接",host,u"FTP成功"
        ftpID=1
        if uploadfile(ftp):   #上传文件
            delete(ftp) #删除文件

        ftp.quit() #退出ftp服务器
        return 1
    except:
        print u"adminFTP.py======连接",host,u"FTP失败！！！！"
        ftpID=0
#        try:
        ftp.quit() #退出ftp服务器
#        except:
#            print u"adminFTP.py======FTP退出异常"
#            ftp.close()
        return 0

def uploadfile(ftpU):   #上传文件
    try:
        global ftpID
        remotepath = "Server.ini" #远程路径
        bufsize = 1024
        localpath = 'Server.ini'   #本地路径
        fp = open(localpath,'rb')
        ftpU.storbinary('STOR '+ remotepath ,fp,bufsize) #上传文件
        #ftpU.set_debuglevel(0)  #关闭调试模式
        fp.close() #关闭文件
        #ftpU.quit()   #退出ftp
        print u"adminFTP.py======上传文件文件",localpath,u"成功"
        ftpID=2
        return 1
    except:
        print u"adminFTP.py======上传文件失败！！！！"
        return 0

def delete(ftpD): #删除文件
    try:
        global ftpID
        remotepath = "Server.ini" #远程路径
        ftpD.delete(remotepath)        #删除远程文件
        print u"adminFTP.py======删除文件",remotepath,u"成功"
        ftpID=3
        return 1
    except:
        print u"adminFTP.py======删除文件失败！！！！"
        return 0


#def downloadfile()  #下载文件
#    remotepath = "/home/pub/dog.jpg";
#    ftp = ftpconnect()
#    print ftp.getwelcome() #显示ftp服务器欢迎信息
#    bufsize = 1024 #设置缓冲块大小
#    localpath = 'f:\\test\\dog.jpg'
#    fp = open(localpath,'wb') #以写模式在本地打开文件
#    ftp.retrbinary('RETR ' + remotepath,fp.write,bufsize) #接收服务器上文件并写入本地文件
#    ftp.set_debuglevel(0) #关闭调试
#    fp.close()
#    ftp.quit() #退出ftp服务器


import sys
import mysql #数据库操作文件
if __name__=='__main__':
    #mysql.mysql_open()  #连接数据库
    #sql_sel() #SQL查询
    if len(sys.argv)!=4:
        print '传入参数不对python c1.py %s %s %s\n'
    else:
        mysql.mysql_open()  #连接数据库
        print u"adminFTP.py======连接测试URLFTP开始:",sys.argv[1].strip()
        if ftpconnect(sys.argv[1].strip(),sys.argv[2].strip(),sys.argv[3].strip()):    #连接FTP
        #print "连接成功"
            print sys.argv[1].strip(),u"adminFTP.py======扫描完成===FTP状态：",ftpID
            print u"adminFTP.py======IP:",sys.argv[1].strip(),u"用户名:",sys.argv[2].strip(),u"密码:",sys.argv[3].strip(),u"连接成功"
        else:
            #print "连接失败"
            print sys.argv[1].strip(),u"adminFTP.py======扫描完成===FTP状态：",ftpID
            print u"adminFTP.py======IP:",sys.argv[1].strip(),u"用户名:",sys.argv[2].strip(),u"密码:",sys.argv[3].strip(),u"连接失败"
        up = "update  ftppassword set  data='%d',time='%s' where IP='%s' and user='%s' and password='%s'"%(ftpID,time.strftime('%Y.%m.%d-%H.%M.%S'),sys.argv[1].strip(),sys.argv[2].strip(),sys.argv[3].strip())
        if mysql.mysql_update(up):  #修改数据
            print sys.argv[1].strip(),u"adminFTP.py======修改数据库成功\n"
        else:
            print sys.argv[1].strip(),u"adminFTP.py======修改数据库失败\n"
        #mysql.mysql_S()  #保存数据