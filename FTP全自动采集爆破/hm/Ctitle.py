# coding: utf-8

################################################查看采集到的URL地址FTP是否开发
from ftplib import FTP
import urllib2, time
import Cmysql #数据库操作文件
import socket
import threading
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import thread
import urllib
import re
import sys


class CS_title(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sql=Cmysql.mysql_handle()
        self.sql.mysql_open()
        self.ftppassword=0

    def run(self):
            self.ftppassword=self.ftppassword+1  #读取表顺序
            if self.ftppassword==1:
                #time.sleep(60)
                self.ftppassword3()
            if self.ftppassword==2:
                #time.sleep(60)
                self.ftppassword2()

#            if self.ftppassword>=5:
#                self.ftppassword=0
            return 0   #在软件开始的时候检测一次就行了
#                time.sleep(60*10)
#                self.sql.mysql_S()  #保存数据
#                self.run()     #读取URr


    def ftppassword2(self):  #2  有上传权限
        try: #password1  有权限的就提升  连接失败的返回到表0
            sql="select * from ftppassword2"
            self.cursor=self.sql.conn.cursor()
            n = self.cursor.execute(sql)
            self.cursor.scroll(0)
            for row in self.cursor.fetchall():
                #print row[0],row[1],row[2]
                try:
                    url="http://"+row[0]
                    data=self.open_title(url)
                    print u"XXXX%s网站名字是==%s"%(url,data)

                    #A1 = "update ftppassword2 set title='%s' where IP='%s' and user='%s'"%(data,row[0],row[1])
                    A1="update ftppassword2 set title='"+data.encode("utf8")+"' where IP='"+row[0]+"' and user='"+row[1]+"'".encode("utf8")
                    self.sql.mysql_update(A1)
                    self.sql.mysql_S()  #保存数据
                except:
                    print u"添加%s网站标题异常"%(row[0])
            self.cursor.close()

            time.sleep(60)
            self.sql.mysql_S()  #保存数据
            self.run()     #读取URL
        except:
            print u"====--CS_title---ftppassword2异常！！！！！===="
            time.sleep(60)
            self.run()

    def ftppassword3(self):  #2  有上传权限
        try: #password1  有权限的就提升  连接失败的返回到表0
            sql="select * from ftppassword3"
            self.cursor=self.sql.conn.cursor()
            n = self.cursor.execute(sql)
            self.cursor.scroll(0)
            for row in self.cursor.fetchall():
                #print row[0],row[1],row[2]
                try:
                    url="http://"+row[0]
                    data=self.open_title(url)
                    print u"XXXX%s网站名字是==%s"%(url,data)
                    #A1 = "update ftppassword3 set title='%s' where IP='%s' and user='%s'"%(data.encode("utf8"),row[0],row[1])
                    A1="update ftppassword3 set title='"+data+"' where IP='"+row[0]+"' and user='"+row[1]+"'".encode("utf8")
                    self.sql.mysql_update(A1)
                    self.sql.mysql_S()  #保存数据
                except:
                    print u"添加%s网站标题异常"%(row[0])
            self.cursor.close()

            time.sleep(60)
            self.sql.mysql_S()  #保存数据
            self.run()     #读取URL
        except:
            print u"====--CS_title---ftppassword3异常！！！！！===="
            time.sleep(60)
            self.run()

    def open_title(self,url):
        try:
            sys.getdefaultencoding()
            #url='http://www.163.com'
            s = urllib2.urlopen(url,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            ss = s.read()
            p = re.compile(r'<title>[\s\S]*?</title>')   ##p = re.compile( r'<a>[\s\S]*?</a>' )
            sarr = p.findall(ss)#找出一条一条的<a></a>标签

            As=sarr[0]
            if isinstance(As, unicode):
                #print u"1111中文"
                return As.decode('utf-8').encode('gb2312')
            else:
                #print u"22222中文"
                return As.decode('gb2312').encode('utf-8')

        except:
            return u"获取不到网站名称"
################################################
if __name__=='__main__':
    threads = []  #线程
    nthreads=1
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(CS_title())

    for thread in threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程
#    url='http://126.com'
#    print open_title(url)
