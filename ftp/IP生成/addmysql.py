#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##################################################
import mysql #数据库操作文件

def open_txt():  #打开TXT文本写入数组
    try:
        xxx = file('test.txt', 'r')
        for xxx_line in xxx.readlines():
            passlist.append(xxx_line)
        xxx.close()
    except:
        return 0

def ip2num(ip):
    ip = [int(x) for x in ip.split('.')]
    return ip[0]<<24 | ip[1]<<16 | ip[2]<<8 | ip[3]

if __name__ == '__main__':
    #sqlite.sqlite_open()  #连接数据库
    mysql.mysql_open()  #连接数据库
    global  passlist  #声明全局变量
    passlist = []    #用户名：anonymous 密码为空

    open_txt()  #打开TXT文本写入数组

    E = 0 #得到list的第一个元素
    while E < len(passlist):
        start, IPend = [x for x in passlist[E].split('-')]
        sql = "INSERT INTO port21(ip1,ip2) values('%s','%s')"%(start,IPend)
        if mysql.mysql_insert(sql): #添加
            print "添加成功"
        else:
            print "添加失败"
        print passlist[E]
        E = E + 1

    mysql.mysql_S()  #保存数据
    mysql.mysql_close()  #关闭数据库
    #sqlite.sqlite_S()  #保存数据
    #sqlite.sqlite_close()  #关闭数据库