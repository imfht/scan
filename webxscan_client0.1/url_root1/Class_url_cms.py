#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import os
import re
import sys
import socket
import httplib
import gzip,StringIO
import Queue,threading
import time
from threading import Thread
socket.setdefaulttimeout(10)

from class_Queue import url_exp

class Class_url_cms(threading.Thread):  #指纹识别
    def __init__(self,penurl):
        threading.Thread.__init__(self)
        self.list=[]
        self.penurl=penurl[7:]
        self.open_file()   #读取文件到数组
        self.CS_cms(self.penurl) #遍历页里的地址


    ############################
    def file_add(self,data):  #添加数组
        try:
            if "#" in data:
                return 0
                #print data
            ss = data.split("------")
            self.list.append(ss)  #添加数据
        except Exception,e:
            #print e
            return 0
    def open_file(self):  #遍历文件
        try:
            #合并字典
            doclist = os.listdir(os.getcwd()+r'\Bin')
            doclist.sort()
            for i in doclist:
                for url in open('Bin/'+i,'r'):
                    data=url.strip().decode("gbk")
                    self.file_add(data)  #添加数组
            #print self.list
            #print len(self.list)
        except Exception,e:
            #print e
            return 0
    ############################
    def CS_cms(self,url): #遍历页里的地址
        self.A= int(time.strftime('%H%M%S'))  #计时
        class crackThread(Thread):  #研究下c++类的继承  和嵌套看怎么继承CS_linkftp类
                def __init__(self,URL,list):
                    Thread.__init__(self)
                    self.URL=URL
                    self.list=list
                    self.for_list()

                def for_list(self):
                    try:
                        for i in self.list:
                            #print i
                            if self.open_url_cms(self.URL,i[0],i[1]):  #url 地址 版本
                                #print u"网址:%s  链接:%s  关键字:%s  版本:%s"%(self.URL,i[0],i[1],i[1])
                                #list=[self.URL,i[1]]
                                #print list
                                EXP_list=[1,self.URL,"cms",self.URL,i[1],"",""]
                                #["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","漏洞地址","密码","备注"]7个
                                url_exp.put(EXP_list,0.5)   #插入队列
                                break #跳出整个循环
                    except Exception,e:
                        #print e
                        return 0

                def open_url_cms(self,url,hand_url,cms_name):  #url 地址 版本
                    headers = {'User-agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
                    try:
                        conn = httplib.HTTPConnection(url)
                        conn.request('GET',hand_url,None,headers)
                        httpres = conn.getresponse()
                        if httpres.status == 200:
                            data=httpres.read()
                            pname = re.compile(cms_name)
                            sarr = pname.findall(data)
                            if sarr:
                                #print cms_name
                                return 1
                        return 0
                    except Exception,e:
                        #print e
                        return 0


        threads = []  #线程
        for i in range(1):  #nthreads=10  创建10个线程
            threads.append(crackThread(url,self.list))

        for thread in threads:   #不理解这是什么意思    是结束线程吗
            thread.start()  #start就是开始线程

        #print u"版本测试:%s time用时 %s S\r\n"%(url,int(time.strftime('%H%M%S'))-self.A)
        return 0
################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(Class_url_cms("http://www.wuyuan168.com"))
    for tA in threads:   #不理解这是什么意思    是结束线程吗
        tA.start()  #start就是开始线程






