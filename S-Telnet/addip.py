#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
####################################################################
#qq:316118740
#BLOG:http://hi.baidu.com/alalmn
# python 生成IP段 添加到sqlite3
import Csqlite3 #数据库操作文件




if __name__ == '__main__':
    sql3=Csqlite3.C_sqlite3()
    sql3.mysqlite3_open()
    for IP1 in range(254,0,-1):
        for IP2 in range(254,0,-1):
        #for IP3 in range(254,0,-1):
        #for IP4 in range(254,0,-1):
        #print IP1,IP2
            if (str(IP1)=="127") or (str(IP1)=="192"):
                continue  #跳过本次循环
                ##print IP1,IP2
            #abc= '%s.%s.%s-%s.%s.%s\n' % (IP1,IP2,"1.1",IP1,IP2,"255.255")
            bengip='%s.%s.%s'%(IP1,IP2,"1.1")
            endip='%s.%s.%s'%(IP1,IP2,"255.255")
            sql="insert into ip(bengip,endip) VALUES('%s','%s')"%(bengip,endip)
            sql3.mysqlite3_insert(sql)
            print sql




