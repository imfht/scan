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
        print u"连接",host,u"FTP失败！！！！"
        ftpID=0
        try:
            ftp.quit() #退出ftp服务器
        except:
            print u"FTP退出异常"
            ftp.close()
        sql_sel() #SQL查询
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
        print u"上传文件文件",localpath,u"成功"
        ftpID=2
        return 1
    except:
        print u"上传文件失败！！！！"
        return 0

def delete(ftpD): #删除文件
    try:
        global ftpID
        remotepath = "Server.ini" #远程路径
        ftpD.delete(remotepath)        #删除远程文件
        print u"删除文件",remotepath,u"成功"
        ftpID=3
        return 1
    except:
        print u"删除文件失败！！！！"
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

import random  #产生一个随机数
def sql_sel(): #SQL查询
    try:
        sql="select * from ftppassword"
        #sql="select * from ftppassword where data is NULL limit 1"
        mysql.cursor.execute(sql)
        mysql.cursor.scroll(0)
        for row in mysql.cursor.fetchall():
            time.sleep(1) #确保先运行Seeker中的方法
            print u"连接测试URLFTP开始:",row[0]
            if ftpconnect(row[0],row[1],row[2]):    #连接FTP
            #print "连接成功"
                print row[0],u"扫描完成===FTP状态：",ftpID
                print u"IP:",row[0],u"用户名:",row[1],u"密码:",row[2],u"连接成功"
            else:
                #print "连接失败"
                print row[0],u"扫描完成===FTP状态：",ftpID
                print u"IP:",row[0],u"用户名:",row[1],u"密码:",row[2],u"连接失败"
            up = "update  ftppassword set  data='%d',time='%s' where IP='%s' and user='%s' and password='%s'"%(ftpID,time.strftime('%Y.%m.%d-%H.%M.%S'),row[0],row[1],row[2])
            if mysql.mysql_update(up):  #修改数据
                print row[0],u"修改数据库成功\n"
                mysql.mysql_S()  #保存数据
            else:
                print row[0],u"修改数据库失败\n"
                mysql.mysql_S()  #保存数据

        print u"遍历数据库完成"
    except:
        print u"SQL读取URL异常！！！！！"
        return 0

import mysql #数据库操作文件
if __name__=='__main__':
    mysql.mysql_open()  #连接数据库
    sql_sel() #SQL查询