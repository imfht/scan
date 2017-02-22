#!/usr/local/bin/python
################################################
import sqlite3
import threading
import thread
import ConfigParser

class C_sqlite3():
    def __init__(self):
        self.db="S.db"
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("gost.ini"))
            self.db= config.get("DATA","sqlitedb")
        except:
            print "INI--try: except:sqlitedb"

    def mysqlite3_open(self):
        try:
            #self.conn = sqlite3.connect(self.db)
            self.conn = sqlite3.connect(self.db,check_same_thread = False)
            self.conn.isolation_level = None
            self.conn.text_factory = str

        except:
            print "SQLite:",self.db,u"NO###"

    def mysqlite3_close(self):
        try:
            self.conn.close()
        except:
            return 0


    def mysqlite3_select(self,data):
        try:
           # print data
            self.conn.commit()
            cur = self.conn.cursor()
            cur.execute(data)
            res = cur.fetchall()
            for line in res:
                self.url_data=line[0]
            cur.close()
            return self.url_data
        except:
            print "select try: except:"
            return "null123456"

    def mysqlite3_insert(self,data):
        try:
            return self.conn.execute(data)
        except:
            #print "insert try: except:"
            return 0

    def mysqlite3_update(self,data):
        try:
            return self.conn.execute(data)
        except:
            #print u"update try: except:"
            return 0

    def mysqlite3_delete(self,data):
        try:
            return self.conn.execute(data)
        except:
            print "update try:  except:"
            return 0


if __name__=='__main__':
    new=C_sqlite3()
    new.mysqlite3_open()
    new.mysqlite3_select("select * from openurl where openurl is NULL limit 1")

