#!/usr/local/bin/python
#from __future__ import division
import Csqlite3
import threading
import thread
import ConfigParser
import time

class CS_Cthread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()
        self.run()

    def run(self):
        try:
            self.th_openurl =10
            self.th_openftp =10
            self.th_ftppassword =50
            try:
                config = ConfigParser.ConfigParser()
                config.readfp(open("gost.ini"))
                self.th_openurl = int(config.get("DATA","th_openurl"))
                self.th_openftp = int(config.get("DATA","th_openftp"))
                self.th_ftppassword = int(config.get("DATA","th_ftppassword"))
            except:
                print "INI--try: except:close_open"
            print "openurl",self.th_openurl
            print "openftp",self.th_openftp
            print "ftppassword",self.th_ftppassword
        except:
            print "=================CS_mysql_delete---run================="

    def SQL_slect(self,sql):
        self.i=0
        try:
            time.sleep(3)
            self.sql3.conn.commit()
            cur = self.sql3.conn.cursor()
            cur.execute(sql)
            res = cur.fetchall()
            for line in res:
#                if self.i>=10000:
#                    return self.i
                self.i=self.i+1
            cur.close()
            return self.i
        except:
            return self.i

    def openurl(self):
        try:
            sql="select * from openurl where openurl is NULL"
            data=self.SQL_slect(sql)
            print "openurl",data,
            if data==0:
                print "<100--run thread 1"
                return 1
            if data<=100:
                print "<100--run thread",self.th_openurl
                return self.th_openurl
            if data<=1000:
                print "<1000--run thread",self.th_openurl/2
                return self.th_openurl/2
            if data<=5000:
                print "<5000--run thread",self.th_openurl/3
                return self.th_openurl/3
            if data<=10000:
                print "<10000--run thread",self.th_openurl/5
                return self.th_openurl/5
            if data<=30000:
                print "<30000--run thread"
                return 1
            if data>=30000:
                print ">30000--run thread--0"
                return 0
        except:
            return 1

    def openftp(self):
        try:
            sql="select * from openurl where openftp is NULL"
            data=self.SQL_slect(sql)
            print "openftp",data,
            if data==0:
                print "<100--run thread 1"
                return 1
            if data<=100:
                print "<100--run thread",self.th_openftp
                return self.th_openftp
            if data<=1000:
                print "<1000--run thread",self.th_openftp/2
                return self.th_openftp/2
            if data<=3000:
                print "<3000--run thread",self.th_openftp/5
                return self.th_openftp/5
            if data<=5000:
                print "<5000--run thread",self.th_openftp
                return self.th_openftp
            if data>=5000:
                print ">5000--run thread",self.th_openftp
                return self.th_openftp
        except:
            return 3

    def linkftp(self):
        try:
            sql="select * from openftp where linkftp is NULL"
            data=self.SQL_slect(sql)
            print "linkftp",data,
            if data==0:
                print "<100--run thread 1"
                return 1
            if data<=100:
                print "<100--run thread 1"
                return 1
            if data<=1000:
                print "<1000--run thread",self.th_ftppassword/2
                return self.th_ftppassword/2
            if data<=3000:
                print "<3000--run thread",self.th_ftppassword/3
                return self.th_ftppassword/3
            if data<=4000:
                print "<4000--run thread",self.th_ftppassword/4
                return self.th_ftppassword/4
            if data<=5000:
                print "<5000--run thread",self.th_ftppassword
                return self.th_ftppassword
            if data>=5000:
                print ">100--run thread",self.th_ftppassword
                return self.th_ftppassword
        except:
            return 1

if __name__=='__main__':
    t_h=CS_Cthread()
    print t_h.linkftp()
    print t_h.openurl()
    print t_h.openftp()
