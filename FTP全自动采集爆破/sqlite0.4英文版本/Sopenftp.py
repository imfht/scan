#!/usr/local/bin/python
##################################################
#qq:29295842
#BLOG:http://hi.baidu.com/alalmn


from ftplib import FTP
import urllib2, time
import Csqlite3
import socket
import threading
socket.setdefaulttimeout(10)
import thread


class CS_openftp(threading.Thread):
    def __init__(self,htint):
        threading.Thread.__init__(self)
        self.Ht=htint
        self.INI_data1=0
        self.INI_data2=0
        self.INI_data3=0
        self.Internet=100
        self.printf=10
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()

    def run(self):
        try:
            print "====CS_openftp%d run===="%(self.Ht)
            self.open_mysql()
        except:
            print "====%d--CS_openftp---run--try: except:===="%(self.Ht)
            time.sleep(60)
            self.run()

    def open_mysql(self):
        try:
            sql="select * from openurl where openftp is NULL limit 1"
            data = self.sql3.mysqlite3_select(sql)
            if ~data.find("null123456"):
                time.sleep(10)
                self.open_mysql()
            update = "update openurl set openftp='send' where url='%s'"%(data)
            self.sql3.mysqlite3_update(update)
            self.INI_data1=self.INI_data1+1
            self.host_ftp(data)
        except:
            print "====%d--CS_openftp--openurl URL--try: except:===="%(self.Ht)
            time.sleep(300)
            self.open_mysql()

    def host_ftp(self,host):
        try:
            if host == '':
                time.sleep(5)
                self.open_mysql()
                return 0

            ftpB = FTP()
            ftpB.connect(host,21)
            ftpB.quit()

            self.INI_data3=self.INI_data3+1
            sql="insert into openftp (url,time) VALUES ('%s','%s')"%(host,time.strftime('%Y.%m.%d-%H.%M.%S'))
            self.sql3.mysqlite3_insert(sql)
            if self.printf>=10:
                print u"====%d--%sFTP OK-URL:%s/NOFTP:%s/OKFTP:%s===="%(self.Ht,host,self.INI_data1,self.INI_data2,self.INI_data3)
                self.printf=0
            self.printf=self.printf+1
            if self.INI_data1>=3000 and self.INI_data3>=1000:
                self.INI_data1=0
                self.INI_data2=0
                self.INI_data3=0
            self.open_mysql()
        except:
            up = "update openurl set openftp='%s' where url='%s'"%("no21",host)
            self.sql3.mysqlite3_insert(up)
            self.INI_data2=self.INI_data2+1
            time.sleep(5)
            self.open_mysql()
            return 0

################################################
if __name__=='__main__':
    threads = []
    nthreads=10
    for i in range(nthreads):
        threads.append(CS_openftp(i))

    for thread in threads:
        thread.start()

