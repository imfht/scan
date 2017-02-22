#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##################################################
#qq:316118740
#BLOG:http://hi.baidu.com/alalmn
#
#  刚学写的不好请大家见谅
##################################################
import sqlite3
#SQLite数据库名称
DB_SQLITE_PATH = "ip.db"

def sqlite_open(): #连接数据库
    global sqlite_conn
    try:
        sqlite_conn = sqlite3.connect(DB_SQLITE_PATH)
        print u"连接SQL ite数据库成功"
        return 1
    except sqlite3.Error, e:
        print u'conntect SQL ite数据库失败。错误:%s' %(e.args[0])
        return 0

def sqlite_S():  #保存数据
    try:
        sqlite_conn.commit()   #提交   这句害死我了
        return 1
    except:
        return 0

def sqlite_close(): #关闭数据库
    try:
        sqlite_conn.close()  #关闭数据库句柄
        return 1
    except:
        return 0

def sqlite_select():  #查询数据
    try:
    #获取游标
        sqlite_cursor = sqlite_conn.cursor()
        sql_desc = "SELECT * FROM ip"
        sqlite_cursor.execute(sql_desc)
        for row in sqlite_cursor:
            print row[0]
            print row[1]
            print row[2]
        sqlite_cursor.close()   #关闭游标
        return 1
    except:
        return 0

def sqlite_insert(data):  #添加数据
    try:
        print data
        sqlite_cursor = sqlite_conn.cursor()
        sqlite_cursor.execute(data)
        print u"添加数据成功"
        #return 1
    except:
        print u"添加数据失败"
        return 0

def sqlite_update(data):  #修改数据
    try:
        sqlite_cursor = sqlite_conn.cursor()
        sqlite_cursor.execute(data)
        return 1
    except:
        print u"修改数据失败"
        return 0

def sqlite_delete(data):  #删除数据
    try:
        sqlite_cursor = sqlite_conn.cursor()
        sqlite_cursor.execute(data)
        return 1
    except:
        print u"删除数据失败"
        return 0

#if __name__ == '__main__':
#    sqlite_open()  #连接数据库

#    sql_desc = "INSERT INTO ip(ip1,ip2) values('111111111111111111','2222222222222')"
#    sqlite_insert(sql_desc)  #添加数据
#    sqlite_S()  #保存数据

#    sql_desc = "update ip set  ip2='zzzGGGG' where ip1='111111111111111111'"
#    sqlite_update(sql_desc)  #修改数据
#    sqlite_S()  #保存数据

#    sql_desc = "delete from ip where ip1='111111111111111111'"
#    sqlite_delete(sql_desc)  #删除数据
#    sqlite_S()  #保存数据

#    sqlite_select()  #查询数据
#    sqlite_close()  #关闭数据库


