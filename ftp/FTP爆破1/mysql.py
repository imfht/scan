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

def mysql_open():  #连接数据库
    global conn   #声明全局变量
    conn=MySQLdb.connect(host="localhost",user="root",passwd="316118740",db="urldata",charset="utf8")
    global cursor  #声明全局变量
    cursor = conn.cursor()

def mysql_S():  #保存数据
    conn.commit()   #提交   这句害死我了

def mysql_close():  #关闭数据库
    conn.close()


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
    except:
        return 0


def mysql_update(data):  #修改数据
    try:
        return cursor.execute(data)
    except:
        return 0

def mysql_delete(data):  #删除数据
    try:
        return cursor.execute(data)
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