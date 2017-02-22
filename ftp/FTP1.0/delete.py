#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

####################################################################
#qq:316118740
#BLOG:http://hi.baidu.com/alalmn
# 更新数据库  更新不应该扫描的数据
#  刚学写的不好请大家见谅
####################################################################
import mysql #数据库操作文件
#select * from url where url like '%baidu.com'
def sql_cx(data): #SQL查询
    try:
        sql="select * from url where url like '%%%s'"%(data)
        mysql.cursor.execute(sql)
        mysql.cursor.scroll(0)
        for row in mysql.cursor.fetchall():
            up = "update  url set  ftpsend='NO' where url='%s'"%(row[0])
            if mysql.mysql_update(up):  #修改数据
               print row[0],u"修改成功"
            else:
                print row[0],u"修改失败"
        mysql.mysql_S()  #保存数据
    except:
        return 0


if __name__=='__main__':
    mysql.mysql_open()  #连接数据库
    mysql.cursor.execute("select * from del")
    mysql.cursor.scroll(0)
    for row in mysql.cursor.fetchall():
        sql_cx(row[0])
        #print '%s-%s'%(row[0],row[1])
        #print row[0]
        #print row[1]
        #print row[2]
    mysql.mysql_close()  #关闭数据库