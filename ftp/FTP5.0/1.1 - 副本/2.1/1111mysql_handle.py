# -*- coding: cp936 -*-
#需要安装 mysql-connector-python-1.0.8-py2.7.rar
#'''操作mysql数据库'''
from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
import ConfigParser  #INI读取数据

class mysql_handle():
    def __init__(self):
        self.mysql_host="localhost"
        self.mysql_user="root"
        self.mysql_pwd="316118740"
        self.mysql_dbname="ftp"
        self.mysql_db_mod=1
        self.connect_handler=''
        self.connect_config=''

    def construct_connect_para(self):  #连接主机信息
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("Server.ini"))
            self.mysql_host = config.get("DATA","Server")
            self.mysql_user = config.get("DATA","Username")
            self.mysql_pwd = config.get("DATA","password")
            self.mysql_dbname = config.get("DATA","db")
        except:
            print (u"读取INI错误")
        self.connect_config={
            'user':self.mysql_user,
            'password':self.mysql_pwd,
            'host':self.mysql_host,
            'database':self.mysql_dbname
        }

    def mysql_connect(self):  #连接主机
        #self.connect_handler=mysql.connector.connect(user=self.mysql_user,password=self.mysql_pwd,host=self.mysql_host,\
        #database=self.mysql_dbname)
        self.construct_connect_para()  #连接主机信息
        try:
            self.connect_handler=mysql.connector.connect(**self.connect_config)  #连接数据库
            print(u'mysql 连接成功')
            return True
        except mysql.connector.Error as err:
            if(str(err).find('Unknown database')):  #未知数据库
                print(u"连接数据库失败: {}".format(err))
                if(self.mysql_db_mod==1):
                    try:
                        print(u"尝试创建数据库:{}".format(self.mysql_dbname))
                        del self.connect_config['database']
                        self.connect_handler=mysql.connector.connect(**self.connect_config)
                        print(u"创建数据库 {}: ".format(self.mysql_dbname),end='')
                        self.mysql_cursor()
                        self.mysql_create_db()
                        print(u"ok")
                        self.mysql_close_connect()   #关闭连接
                        self.connect_config['database']=self.mysql_dbname
                        self.connect_handler=mysql.connector.connect(**self.connect_config)
                        return True
                    except mysql.connector.Error as err:
                        print(u"连接数据库失败: {}".format(err))
    def mysql_close_connect(self):#关闭连接
        self.connect_handler.close()  #关闭连接
    def mysql_cursor(self):
        #self.mysql_connect()
        self.cnx=self.connect_handler
        self.cursor=self.cnx.cursor() #获取操作句柄
    def mysql_create_db(self):   #创建数据库
        try:
            self.cursor.execute(    #执行sql
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.mysql_dbname))
        except mysql.connector.Error as err:
            print(u"未能创建数据库: {}".format(err))
            exit(1)
    def mysql_construct_table(self):
        self.tables={}
    def mysql_create_table(self,table_dic):
        for name, ddl in table_dic.iteritems():
            try:
                print(u"创建表 {}: ".format(name), end='')
                self.cursor.execute(ddl)  #执行sql
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print(u"已经存在.")
                else:
                    print(format(err))
            else:
                print(u"OK")
        #self.cursor.close()#关闭连接
    def mysql_insert_data(self):
        tomorrow = datetime.now().date() + timedelta(days=1)
        add_employee = ("INSERT INTO employees "
                "(first_name, last_name, hire_date, gender, birth_date) "
                "VALUES (%s, %s, %s, %s, %s)")
        add_salary = ("INSERT INTO salaries "
              "(emp_no, salary, from_date, to_date) "
              "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
        data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))
        # Insert new employee
        self.cursor.execute(add_employee, data_employee)#执行sql
        emp_no =self.cursor.lastrowid
        # Insert salary information
        data_salary = {
            'emp_no': emp_no,
            'salary': 50000,
            'from_date': tomorrow,
            'to_date': date(9999, 1, 1),
            }
        self.cursor.execute(add_salary, data_salary)#执行sql
        #Make sure data is committed to the database
        self.cnx.commit()
        self.cursor.close()#关闭连接
    def mysql_query(self,data):
        try:
            #self.mysql_connect()
            self.mysql_cursor()
            self.cursor.execute(data)#执行sql
            #Make sure data is committed to the database
            self.cnx.commit()
            self.cursor.close() #关闭连接
            print(u"查询成功")
            return True
        except mysql.connector.Error as err:
            print(u"查询错误: {}".format(err))

def mysql_create_fields():
    '''创建MYSQL语句表'''
    table_dic={}

if __name__=="__main__":
    new=mysql_handle()
    if(new.mysql_connect()):
        print ("111111111111")
#    if(new.mysql_connect()):
#        new.mysql_cursor()
#        #new.mysql_construct_table()
#        data="insert into ftppassword(IP,user,password,time) values('admani.80code.com','web','pass','2012.11.07-23.26.33')"
#        new.mysql_query(data)
#        data="insert into test (test) values('testaaccc')"
#        new.mysql_query(data)

