#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##################################################
#qq:316118740
#BLOG:http://hi.baidu.com/alalmn
#
#  刚学写的不好请大家见谅
##################################################
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

import sqlite
if __name__ == '__main__':
    sqlite.sqlite_open()  #连接数据库
    global  passlist  #声明全局变量
    passlist = []    #用户名：anonymous 密码为空

    open_txt()  #打开TXT文本写入数组

    E = 0 #得到list的第一个元素
    while E < len(passlist):
        start, IPend = [x for x in passlist[E].split('-')]
        sql_desc = "INSERT INTO ip(ip1,ip2) values('%s','%s')"%(start,IPend)
        sqlite.sqlite_insert(sql_desc)  #添加数据
        print passlist[E]
        E = E + 1

    sqlite.sqlite_S()  #保存数据
    sqlite.sqlite_close()  #关闭数据库
