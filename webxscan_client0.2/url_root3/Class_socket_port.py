#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import threading

from threading import Thread
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
from class_Queue import url_exp
from Queue import Queue

def scan(url0,url1,url,ip,port):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #s.connect((ip,port))
        result=s.connect_ex((ip,port))
        if(result==0):
            print 'url:%s IP:%s:%d open'%(url,ip,port)
            EXP_list=[1,url0,url1,"url:port:socket_port",str(port)+"--open","",""]
            #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
            url_exp.put(EXP_list,0.5)   #插入队列
        s.close()
    except:
        return 0


class Worker(Thread):
    def __init__(self,taskQueue):
        Thread.__init__(self)
        self.setDaemon(True)
        self.taskQueue=taskQueue
        self.start()
    def run(self):
        while True:
            try:
                callable,args,kwds=self.taskQueue.get(block=False)
                callable(*args,**kwds)
            except:
                break

class Class_socket_port1:
    def __init__(self,url0,url1,url,ip):
        self.threads=[]
        self.taskQueue=Queue()
        self.threadNum=50
        self.__create_taskqueue(url0,url1,url,ip)
        self.__create_threadpool(self.threadNum)

    def __create_taskqueue(self,url0,url1,url,ip):
        for i in range(0,6000):
            self.add_task(scan,url0,url1,url,ip,i)

    def __create_threadpool(self,threadNum):
        for i in range(threadNum):
            thread=Worker(self.taskQueue)
            self.threads.append(thread)

    def add_task(self,callable,*args,**kwds):
        self.taskQueue.put((callable,args,kwds))

    def waitfor_complete(self):
        while len(self.threads):
            thread=self.threads.pop()
            thread.join()
            if thread.isAlive() and not self.taskQueue.empty():
                self.threads.append(thread)
        #print 'scaning is over!'


class Class_socket_port:
#    def __init__(self,penurl):
#        threading.Thread.__init__(self)
#        self.penurl=""
#        if "http://" in penurl:
#            self.penurl=penurl[7:]
#        else:
#            self.penurl=penurl
#        IP=self.socket_sendall(self.penurl)
#        if IP==0:
#            return
#        print "url:%s  IP:%s  port:1-6000"%(penurl,IP)
#        tp=Class_socket_port1(self.penurl,IP)
#        tp.waitfor_complete()

    def assign(self,service, arg=None):
        if service == 'port':
            return True, arg

    def scan(self,arg):
        try:
            url0, url1 = arg
            self.url=url1.split('//')[1]
            IP=self.socket_sendall(self.url)
            if IP==0:
                return
            print "url:%s  IP:%s  port:1-6000"%(self.url,IP)
            tp=Class_socket_port1(url0,url1,self.url,IP)
            tp.waitfor_complete()
        except:
            return 0

    def socket_sendall(self,IP):
        try:
            return socket.gethostbyname(IP)  #www.51jmyj.com
        except:
            return 0
################################################
if __name__=='__main__':
    class_www=Class_socket_port()
    class_www.scan(class_www.assign('port', ("http://www.baidu.com","http://www.163.com"))[1])


