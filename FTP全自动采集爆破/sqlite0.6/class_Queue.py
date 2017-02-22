#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#神龙 QQ29295842
#blog http://hi.baidu.com/alalmn
#线程操作消息队列
#select * from ip order by RANDOM() limit 10   随机抽取
import threading
import Queue
import time
import Csqlite3

Aopenurl = Queue.Queue(4000) #要采集的URL    #当有多个线程共享一个东西的时候就可以用它了
Bopenurl = Queue.Queue(200) #http200 链接成功的网站放这存到数据库方便下次采集
openftp = Queue.Queue(3000) #开放FTP的
ftppassword= Queue.Queue(4000)  #保存扫描到的结果["127.0.0.1","admin","admin"]
#这个类主要是 对opinurl存储  opinurl检查数据是否过多
#开始的时候提取100条网址 供采集使用
#后面就是死循环 做数据管理维护
#出现了1个问题  消息队列添加和读取删除   没有经过我的函数也无法添加到数据库（解决方法  Bopinurl）
class C_Queue(threading.Thread):
    def __init__(self,htint,Aopenurl,Bopenurl,openftp,ftppassword):
        threading.Thread.__init__(self)
        self.Ht=htint  #线程ID
        self.Aopenurl=Aopenurl
        self.Bopenurl=Bopenurl
        self.openftp=openftp
        self.ftppassword=ftppassword
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()

    def print_Queue(self):
        try:
            print "-----------------------------------------"
            print "Aopenurl---------4000--------%s"%(self.Aopenurl.qsize())
            print "Bopenurl---------200---------%s"%(self.Bopenurl.qsize())
            print "openftp----------3000--------%s"%(self.openftp.qsize())
            print "ftppassword------4000--------%s"%(self.ftppassword.qsize())
            print "-----------------------------------------"
        except:
            return 0

    def run(self):
        try:
            print "Thread:%d--C_Queue-run"%(self.Ht)
            while True:
                #重数据库 提取100条网址 供采集使用
                self.add_SQL_slect("select * from openurl order by RANDOM() limit 50")  #从数据库 提取100条网址 供采集使用
                #opinurl检查数据是否过多   过多清除一部分
                self.delete_SQL_delete()  #删除数据
                #对Bopinurl进行存储
                self.add_SQL_insert()  #对Bopinurl进行存储
                self.print_Queue()  #线束数据量
                time.sleep(60)
        except:
            print "Thread:%d--C_Queue-run-try--except!!!!!"%(self.Ht)
            time.sleep(60)
            self.run()

    def add_SQL_insert(self):  #对Bopinurl进行存储
        try:
            int_insert=self.Bopenurl.qsize()
            if int_insert>=100: #返回队列的大小
                E = 0 #得到list的第一个元素
                while E < int_insert-1:
                    #print self.list_2[E]
                    data=self.Bopenurl.get(0.2)  #获取消息队列
                    insert="insert into openurl(url,time) VALUES('%s','%s')"%(data,time.strftime('%Y.%m.%d-%H.%M.%S'))
                    #print insert
                    self.sql3.mysqlite3_insert(insert) #添加数据
                    E = E + 1
        except:
            time.sleep(4)
            print "C_Queue--add_SQL_insert-try--except!!!!!"
            return 0

    def add_SQL_slect(self,sql):  #从数据库 提取100条网址 供采集使用
        try:
            #应该先检查  消息队列  数据是巨量是否小于100
            if self.Aopenurl.qsize()<50: # 返回队列的大小
                self.sql3.conn.commit()# 获取到游标对象
                cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
                cur.execute(sql)# 获取所有结果
                res = cur.fetchall()  #从结果中取出所有记录
                for line in res:
                    print line[0]
                    self.Aopenurl.put(line[0],0.5)   #插入队列
                cur.close()  #关闭游标
            return 1
        except:
            time.sleep(4)
            print "C_Queue--add_SQL_slect-try--except!!!!!"
            return 0

    def SQL_slect(self,sql):  #获取数量
        try:
            self.sql3.conn.commit()# 获取到游标对象
            cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
            cur.execute(sql)# 获取所有结果
            res = cur.fetchall()  #从结果中取出所有记录
            cur.close()  #关闭游标
            #print len(res)
            return len(res)
        except:
            print "C_Queue--SQL_slect-try--except!!!!!"
            time.sleep(4)
            return 0

    def delete_SQL_delete(self):  #删除数据 数据量超过2000  就清除一半
        try:
            self.i=0
            int_url=self.SQL_slect("select * from openurl")  #获取数量
            #print int_url
            if int_url>=2000:
                print "C_Queue--delete from openurl"
                int_delete=int_url/2
                self.sql3.conn.commit()# 获取到游标对象
                cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
                sql="select * from openurl order by RANDOM() limit %d"%(int_delete-1) #随机抽取
                cur.execute(sql)# 获取所有结果
                res = cur.fetchall()  #从结果中取出所有记录
                for line in res:
                    delete="delete from openurl where url='%s'"%(line[0])
                    self.sql3.mysqlite3_delete(delete)
                    if self.i>int_delete-1:  #已经删除一半数据了
                        print "C_Queue--delete from openurl  %d ok"%(self.i)
                        return 0
                    self.i=self.i+1
                cur.close()  #关闭游标
        except:
            print "C_Queue--delete_SQL_delete-try--except!!!!!"
            time.sleep(4)
            return 0
################################################
if __name__=='__main__':
    threads = []  #线程
    nthreads=1
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(C_Queue(i,Aopenurl,Bopenurl,openftp,ftppassword))
    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程