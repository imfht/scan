#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
####################################################################
#IP端口扫描
import Csqlite3 #数据库操作文件
import threading
import thread
import time
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间


class S_ip(threading.Thread):
    def __init__(self,htint):
        threading.Thread.__init__(self)
        self.Ht=htint  #线程ID
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()

    def run(self):
        try:
            print u"<<<端口扫描-线程%d启动"%(self.Ht)
            self.open_sqlite()     #读取IP
            #self.socket_ip("254.250.1.1","254.250.255.255")#生成IP扫描
        except:
            print u"=================S_ip---run异常！！！！！================="
            time.sleep(60)
            self.run()

    def mysql_update(self):  #修改数据库
        try:
            print u"端口扫描-修改数据库-线程%d--"%(self.Ht)
            self.Asql="select * from ip"
            self.sql3.conn.commit()# 获取到游标对象
            cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
            cur.execute(self.Asql)# 获取所有结果
            res = cur.fetchall()  #从结果中取出所有记录
            for line in res:
                #print line[0],"-----",line[1]
                self.update = "update ip set send='' where bengip='%s'"%(line[0])
                self.sql3.mysqlite3_update(self.update)
            time.sleep(10)
            self.open_sqlite()     #读取IP
        except:
            print u"<<<端口扫描-线程%d--mysql_update异常！！！！！"%(self.Ht)
            time.sleep(20)
            self.open_sqlite()     #读取IP

    def open_sqlite(self):     #读取IP
        try:
            self.bengip=""
            self.endip=""
            self.Asql="select * from ip  where send='' or  send is NULL limit 1"
            self.sql3.conn.commit()# 获取到游标对象
            cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
            cur.execute(self.Asql)# 获取所有结果
            res = cur.fetchall()  #从结果中取出所有记录
            for line in res:
                #print line[0],"-----",line[1]
                self.bengip=line[0]
                self.endip=line[1]
            cur.close()  #关闭游标

            self.update = "update ip set send='send' where bengip='%s'"%(self.bengip)
            self.sql3.mysqlite3_update(self.update)
            #print u"测试：",self.bengip,"-----",self.endip  #254.250.1.1 ----- 254.250.255.255
            print u"<<<端口扫描-线程%d--测试：%s-----%s"%(self.Ht,self.bengip,self.endip)
            self.socket_ip(self.bengip,self.endip)#生成IP扫描
            time.sleep(2)
            self.open_sqlite()     #读取URL
        except:
            print u"<<<端口扫描-线程%d--S_ip--open_sqlite表读取URL异常！！！！！"%(self.Ht)
            time.sleep(60)
            self.mysql_update()  #修改数据库
            self.open_sqlite()     #读取URL



    def socket_ip(self,bengip,endip):#生成IP扫描
        try:
            self.t=time.time()  #扫描计时
            list_ip=self.gen_ip(self.ip2num(bengip),self.ip2num(endip))
            print u"<<<端口扫描-线程%d--需要扫描%s个IP-----------%s"%(self.Ht,str(len(list_ip)),time.strftime('%Y.%m.%d-%H.%M.%S'))
            I1 = 0 #得到list的第一个元素
            while I1 < len(list_ip):
                #print list_ip[I1]
                time.sleep(0.3) #确保先运行Seeker中的方法
                I1 = I1 + 1   #一层
                try:
                    thread.start_new_thread(self.socket_port,(list_ip[I1],int(23)))
                except:
                    #print ".",
                    continue #跳过本次循环

            print u"<<<端口扫描-线程%d--%s---%s--==IP扫描完成结束%s=====用时%s<<<"%(self.Ht,bengip,endip,time.strftime('%Y.%m.%d-%H.%M.%S'),time.time()-self.t)
            self.open_sqlite()     #读取URL
        except:
            print u"<<<端口扫描-线程%d--S_ip--open_sqlite表读取URL异常！！！！！"%(self.Ht)

    def socket_port(self,ip,PORT):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,PORT))
            print (str(ip)+u":"+str(PORT)+u"端口开放")
            self.insert = "insert into port23(ip,time) VALUES('%s','%s')"%(str(ip),time.strftime('%Y.%m.%d-%H.%M.%S'))
            self.sql3.mysqlite3_update(self.insert)
        except:
            return 0
            #print "s",
            #print ip,u":",PORT,u"端口未开放"
    #----------------------------------------------------------------
    def ip2num(self,ip):
        ip = [int(x) for x in ip.split('.')]
        return ip[0]<<24 | ip[1]<<16 | ip[2]<<8 | ip[3]

    def num2ip(self,num):
        #if num>=IPend:
            #self.textEdit_4.append(u"IP导入数组完成")
        return '%s.%s.%s.%s' % (  (num & 0xff000000) >> 24,
                                  (num & 0x00ff0000) >> 16,
                                  (num & 0x0000ff00) >> 8,
                                  num & 0x000000ff  )

    def gen_ip(self,Aip1,Aip2):  #返回数组
        global IPend
        IPend=Aip2
        return [self.num2ip(num) for num in range(Aip1,Aip2+1) if num & 0xff]
    #----------------------------------------------------------------

if __name__ == '__main__':
    threads = []  #线程
    nthreads=2
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(S_ip(i))

    for thread in threads:   #不理解这是什么意思    是结束线程吗
        time.sleep(2) #确保先运行Seeker中的方法
        thread.start()  #start就是开始线程








