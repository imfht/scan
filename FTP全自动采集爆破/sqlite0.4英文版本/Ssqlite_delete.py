#!/usr/local/bin/python
import time
import Csqlite3
import threading
import thread
import ConfigParser

class CS_mysql_delete(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()
        self.ftppassword=0

        self.openurl =20000
        self.openftp =3000
        self.ftppassword0 =500
        self.ftppassword3 =100
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("gost.ini"))
            self.openurl = int(config.get("DATA","openurl"))
            self.openftp = int(config.get("DATA","openftp"))
            self.ftppassword0 = int(config.get("DATA","ftppassword0"))
            self.ftppassword3 = int(config.get("DATA","ftppassword3"))
        except:
            print "INI--try: except:openurl,openftp,ftppassword0,ftppassword3"
        print "=================CS_mysql_delete  run================="


    def run(self):
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("gost.ini"))
            self.openurl = int(config.get("DATA","openurl"))
            self.openftp = int(config.get("DATA","openftp"))
            self.ftppassword0 = int(config.get("DATA","ftppassword0"))
            self.ftppassword3 = int(config.get("DATA","ftppassword3"))
            print "=================CS_mysql_delete================="
            #print self.Auploadfile
            time.sleep(600)
            self.open_mysql()
        except:
            print "=================CS_mysql_delete---run try: except:================="
            time.sleep(60)
            self.run()

    def SQL_slect(self,sql):
        self.i=0
        try:
            self.sql3.conn.commit()
            cur = self.sql3.conn.cursor()
            cur.execute(sql)
            res = cur.fetchall()
            for line in res:
                self.i=self.i+1
            cur.close()
            return self.i
        except:
            time.sleep(4)
            return self.i
    #######################################################################
    def delete_ftppassword3(self):
        try:
            sql="select * from ftppassword3"
            data=self.SQL_slect(sql)
            if data>=self.ftppassword3:
                print "=================del ftppassword1================="
                self.sql3.conn.commit()
                cur = self.sql3.conn.cursor()
                cur.execute(sql)
                res = cur.fetchall()
                for line in res:
                    delete="delete from ftppassword3 where IP='%s'"%(line[0])
                    self.sql3.mysqlite3_delete(delete)
                cur.close()
            time.sleep(5)
            self.open_mysql()
        except:
            time.sleep(4)
            self.open_mysql()

    def delete_ftppassword0(self):
        try:
            sql="select * from ftppassword0 where root IS NOT NULL"
            data=self.SQL_slect(sql)
            if data>=self.ftppassword0:
                print "=================del ftppassword0================="
                self.sql3.conn.commit()
                cur = self.sql3.conn.cursor()
                cur.execute(sql)
                res = cur.fetchall()
                for line in res:
                    delete="delete from ftppassword0 where IP='%s'"%(line[0])
                    self.sql3.mysqlite3_delete(delete)
                cur.close()
            time.sleep(5)
            self.open_mysql()
        except:
            time.sleep(4)
            self.open_mysql()

    def delete_openftp(self):
        try:
            sql="select * from openftp where linkftp IS NOT NULL"
            data=self.SQL_slect(sql)
            if data>=self.openftp:
                print "=================del openftp================="
                self.sql3.conn.commit()
                cur = self.sql3.conn.cursor()
                cur.execute(sql)
                res = cur.fetchall()
                for line in res:
                    delete="delete from openftp where url='%s'"%(line[0])
                    self.sql3.mysqlite3_delete(delete)
                cur.close()
            time.sleep(5)
            self.open_mysql()
        except:
            time.sleep(4)
            self.open_mysql()

    def delete_openurl(self):
        try:
            sql="select * from openurl where openurl IS NOT NULL and openftp IS NOT NULL"
            data=self.SQL_slect(sql)
            if data>=self.openurl:
                print "=================del openurl================="
                self.sql3.conn.commit()
                cur = self.sql3.conn.cursor()
                cur.execute(sql)
                res = cur.fetchall()
                for line in res:
                    delete="delete from openurl where url='%s'"%(line[0])
                    print delete
                    self.sql3.mysqlite3_delete(delete)
                cur.close()
            time.sleep(5)
            self.open_mysql()
        except:
            time.sleep(4)
            self.open_mysql()
    #######################################################################

    def open_mysql(self):
        try:
            self.ftppassword=self.ftppassword+1
            if self.ftppassword==1:
                print "-----openurl"
                self.delete_openurl()
                time.sleep(2)
            if self.ftppassword==2:
                print "-----openftp"
                self.delete_openftp()
                time.sleep(2)
            if self.ftppassword==3:
                print "-----ftppassword0"
                self.delete_ftppassword0()
                time.sleep(2)
            if self.ftppassword==4:
                print "-----ftppassword3"
                self.delete_ftppassword3()
                time.sleep(2)

            if self.ftppassword>=4:
                return 1

        except:
            print "=================CS_mysql_delete================="
            #return 0
            self.open_mysql()


################################################
if __name__=='__main__':
    threads = []
    nthreads=1
    for i in range(nthreads):
        threads.append(CS_mysql_delete())

    for thread in threads:
        thread.start()