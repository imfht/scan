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

def decode(password=""):
    result = []
    for i in range(0, len(password)/2):
	pass_gao = password[i * 2]
	pass_di = password[i * 2 + 1]
        if(pass_di > '9' or i == 0):
	    result.append(pass_di)
	elif (pass_gao == '1'):
	    result.append(str(int(result[i - 1]) - int(pass_di)))
	elif(pass_gao == '0'):
	   result.append(str(int(result[i - 1]) + int(pass_di)))
	else:
	    return ""
    new_password = ""
    for item in result:
	new_password = new_password + item 
    return new_password

class mysql_xwq:
    def __init__(self, server, username, passwd, db):
        self.server = server
        self.username = username
        self.password = passwd
        self.db = db
        self.conn = ""
        self.cursor = ""
    def mysql_open(self):  #连接数据库
        try:
            self.conn=MySQLdb.connect(host=self.server,user=self.username,passwd=self.password,db=self.db,init_command="set names utf8")
            self.cursor = self.conn.cursor()
            print u"登录服务器成功"
            return 1
        except Exception,e:
	    print e
            print u"登录服务器失败###"
            return 0
	
    def mysql_S(self):  #保存数据
        self.conn.commit()   #提交   这句害死我了
    
    def mysql_close(self):  #关闭数据库
        self.conn.close()
    
    def mysql_select(self, data):  #查询数据
        try:
            n = self.cursor.execute(data)
            self.cursor.scroll(0)
            return self.cursor.fetchall()
        except:
            return False
	
    def mysql_exec_many(self,sql,data):
	try:
	    self.cursor.executemany(sql,data)
	    self.conn.commit()
	except Exception,e:
	    print e
	    return 0
    def mysql_exec(self, data):  #添加数据
	while self.cursor.nextset(): pass
        try:
            return self.cursor.execute(data)
        except Exception,e:
            return 0
if __name__=='__main__':
    sql = mysql_xwq("localhost", "root", "xwq0800", "ftp")
    sql.mysql_open()  #连接数据库
######################################################
    sql_str = "insert into url(url,PR) values('%s','%s')"%("www.baidu2.com","9")
    if sql.mysql_exec(sql_str): #添加
        print u"添加成功"
    else:
        print u"添加失败"
    sql_str = "insert into url(url,PR) values('%s','%s')"%("www.google.com","9")
    if sql.mysql_exec(sql_str): #添加
	print u"添加成功"
    else:
	print u"添加失败"    
######################################################
    sql_str = "update  url set  PR='2' where url='%s'"%("www.baidu.com")
    if (sql.mysql_exec(sql_str)):
        print u"修改成功"
    else:
        print u"修改失败"
######################################################
    query_cnt = 5
    sql_str = "select url from url where pr='9' limit "+ str(query_cnt)
    result = sql.mysql_select(sql_str)
    print result[1][0]
    #sql_str = "delete from url where url='%s'"%("www.baidu.com")
    #if sql.mysql_exec(sql_str):  #删除数据
    #    print u"删除成功"
    #else:
    #    print u"删除失败"
######################################################
    sql.mysql_S()  #保存数据
#    mysql_select()  #查询数据
    sql.mysql_close()  #关闭数据库
