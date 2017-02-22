# -*- coding: cp936 -*-

'''操作mysql数据库'''
from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

class mysql_handle():
    def __init__(self,hostname,username,password,dbname='',db_mod=1):
        self.mysql_host=hostname
        self.mysql_user=username
        self.mysql_pwd=password
        self.mysql_dbname=dbname
        self.mysql_db_mod=db_mod
        self.connect_handler=''
        self.connect_config=''
    def construct_connect_para(self):
        self.connect_config={
            'user':self.mysql_user,
            'password':self.mysql_pwd,
            'host':self.mysql_host,
            'database':self.mysql_dbname
        }
    def mysql_connect(self):
        #self.connect_handler=mysql.connector.connect(user=self.mysql_user,password=self.mysql_pwd,host=self.mysql_host,\
        #database=self.mysql_dbname)
        self.construct_connect_para()
        try:
            self.connect_handler=mysql.connector.connect(**self.connect_config)
            print('connect ok')
            return True
        except mysql.connector.Error as err:
            if(str(err).find('Unknown database')):
                print("Failed connect database: {}".format(err))
                if(self.mysql_db_mod==1):
                    try:
                        print("try to create the specified database:{}".format(self.mysql_dbname))
                        del self.connect_config['database']
                        self.connect_handler=mysql.connector.connect(**self.connect_config)
                        print("create database {}: ".format(self.mysql_dbname),end='')
                        self.mysql_cursor()
                        self.mysql_create_db()
                        print("ok")
                        self.mysql_close_connect()
                        self.connect_config['database']=self.mysql_dbname
                        self.connect_handler=mysql.connector.connect(**self.connect_config)
                        return True
                    except mysql.connector.Error as err:
                        print("Failed connect database: {}".format(err))
    def mysql_close_connect(self):
        self.connect_handler.close()
    def mysql_cursor(self):
        #self.mysql_connect()
        self.cnx=self.connect_handler
        self.cursor=self.cnx.cursor()
    def mysql_create_db(self):
        try:
            self.cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.mysql_dbname))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)
    def mysql_construct_table(self):
        self.tables={}
    def mysql_create_table(self,table_dic):
        for name, ddl in table_dic.iteritems():
            try:
                print("Creating table {}: ".format(name), end='')
                self.cursor.execute(ddl)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(format(err))
            else:
                print("OK")
        #self.cursor.close()
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
        self.cursor.execute(add_employee, data_employee)
        emp_no =self.cursor.lastrowid
        # Insert salary information
        data_salary = {
            'emp_no': emp_no,
            'salary': 50000,
            'from_date': tomorrow,
            'to_date': date(9999, 1, 1),
            }
        self.cursor.execute(add_salary, data_salary)
        #Make sure data is committed to the database
        self.cnx.commit()
        self.cursor.close()
    def mysql_query(self,data):
        try:
            #self.mysql_connect()
            self.mysql_cursor()
            self.cursor.execute(data)
            #Make sure data is committed to the database
            self.cnx.commit()
            self.cursor.close()
            print("query succ")
            return True
        except mysql.connector.Error as err:
            print("query err: {}".format(err))

def mysql_create_fields():
    '''创建MYSQL语句表'''
    table_dic={}

if __name__=="__main__":
    new=mysql_handle('localhost','root','','urldata')
    if(new.mysql_connect()):
        new.mysql_cursor()
        #new.mysql_construct_table()
        data="insert into ftppassword(IP,user,password,time) values('admani.80code.com','web','pass','2012.11.07-23.26.33')"
        new.mysql_query(data)
        data="insert into test (test) values('testaaccc')"
        new.mysql_query(data)

