#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##################################################
#qq:316118740
#BLOG:http://hi.baidu.com/alalmn
# MYSQL 添加 删除 修改  查询
#  刚学写的不好请大家见谅
#网上搜索到一个http://www.technicalbard.com/files/MySQL-python-1.2.2.win32-py2.6.exe
##################################################

import time, MySQLdb
import ConfigParser  #INI读取数据
def mysql_open():  #连接数据库
    Server="localhost"
    Username="root"
    password="316118740"
    db="urldata"
    try:
        config = ConfigParser.ConfigParser()
        config.readfp(open("Server.ini"))
        Server = config.get("DATA","Server")
        Username = config.get("DATA","Username")
        password = config.get("DATA","password")
        db = config.get("DATA","db")
    except:
        print u"读取INI错误"
        return 0
    try:
        global conn   #声明全局变量
        conn=MySQLdb.connect(host=Server,user=Username,passwd=password,db=db,init_command="set names utf8")
        global cursor  #声明全局变量
        cursor = conn.cursor()
        #print u"服务器:",Server,u"用户名:",Username,u"密码:",password,u"连接数据库:",db,u"登录服务器成功"
        #print u"mysql:---登录服务器成功"
    except:
        print u"###服务器:",Server,u"用户名:",Username,u"密码:",password,u"连接数据库:",db,u"登录服务器失败###"
        return 0



def mysql_S():  #保存数据
    try:
        conn.commit()   #提交   这句害死我了
    except:
        print u"保存数据异常"
        return 0

def mysql_close():  #关闭数据库
    try:
        conn.close()
    except:
        print u"关闭数据异常"
        return 0


def mysql_select(data):  #查询数据
    try:
        n = cursor.execute(data)
        cursor.scroll(0)
        for row in cursor.fetchall():
            #print '%s-%s-%s'%(row[0],row[1],row[2])
            return row[0]
    except:
        return "null123456"

#def mysql_select():  #查询数据
#    n = cursor.execute("select * from url")
#    cursor.scroll(0)
#    for row in cursor.fetchall():
#        print '%s-%s-%s'%(row[0],row[1],row[2])
#        #print row[0]
#        #print row[1]
#        #print row[2]

def mysql_insert(data):  #添加数据
    try:
        return cursor.execute(data)
        mysql_S()  #保存数据
    except:
        return 0


def mysql_update(data):  #修改数据
    try:
        return cursor.execute(data)
        mysql_S()  #保存数据
    except:
        return 0

def mysql_delete(data):  #删除数据
    try:
        return cursor.execute(data)
        mysql_S()  #保存数据
    except:
        return 0


#if __name__=='__main__':
#    mysql_open()  #连接数据库
######################################################
#    sql = "insert into url(url,time,ftpsend) values('%s','%s','%s')"%("ttttoo","2222","33333")
#    if mysql_insert(sql): #添加
#        print "添加成功"
#    else:
#        print "添加失败"
######################################################
#    sql = "update  url set  time='<----',ftpsend='---->' where url='%s'"%("111")
#    if mysql_update(sql):  #修改数据
#        print "修改成功"
#    else:
#        print "修改失败"
######################################################
#    sql = "delete from url where url='%s'"%("111")
#    if mysql_delete(sql):  #删除数据
#        print "删除成功"
#    else:
#        print "删除失败"
######################################################
#    mysql_S()  #保存数据
#    mysql_select()  #查询数据
#    mysql_close()  #关闭数据库