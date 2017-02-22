#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#CMS识别  BY:神龙  QQ29295842
#http://hi.baidu.com/alalmn
import os
import re
import httplib
import Queue,threading
import time
from threading import Thread
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间

import sys
reload(sys)
sys.setdefaultencoding('utf8')   #'ascii' codec can't encode characters in position 5-7: ordinal not in range(

import Queue
openurl = Queue.Queue()
url_exp = Queue.Queue()
messagebox = Queue.Queue()

from os import path
# Get current file absolute path

#script = __file__   #绝对路径
#if path.islink(script):  #判断路径是否为空
#    script = path.realpath(script)  #函数 realpath() 函数返回绝对路径
#currentfolder = path.split(path.abspath(__file__))[0]  #获取当前脚本文件所在目录
#if not currentfolder:  #获取失败在换个函数
#    currentfolder = path.abspath(os.getcwd())
#if currentfolder:
#    messagebox.put(u"CMS当前文件夹是:%s"%(currentfolder),0.5)   #插入队列
#else:
#    messagebox.put(u"CMS(获取当前文件夹失败)错误：失败不是当前文件夹是:%s"%(currentfolder),0.5)   #插入队列



class Class_cms(threading.Thread):  #指纹识别
    def __init__(self,x_c):
        threading.Thread.__init__(self)
        self.list=[]
        self.x_c=x_c
        self.open_file()   #读取文件到数组

    def run(self):
        try:
            if openurl.empty():   #判断队列是否为空
                print u"已经没有需要CMS识别的URL了"
                time.sleep(10)
                #return 0
            URL = openurl.get(0.5)  #get()方法从队头删除并返回一个项目
            if not URL=="":
                messagebox.put(u"线程%d开始指纹识别%s"%(self.x_c,URL),0.5)   #插入队列
                self.CS_cms(URL.split('//')[1]) #遍历页里的地址
            self.run()
        except:
            self.run()
            pass

    ############################
    #self.ui.messagebox.append(self.cur_file_dir())
    #import sys,os
    def cur_file_dir(self):  #获取脚本文件的当前路径
        path = sys.path[0]#获取脚本路径
        #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
        if os.path.isdir(path):
            return path
        elif os.path.isfile(path):
            return os.path.dirname(path)

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
#            #合并字典
#            doclist = os.listdir(os.getcwd()+r'\CMS')
#            doclist.sort()
#            for i in doclist:
#                for url in open('CMS/'+i,'r'):
#                    data=url.strip().decode("gbk")
#                    self.file_add(data)  #添加数组

            downloadfolder=self.cur_file_dir()+r'/CMS/'
            messagebox.put(u"CMS当前文件夹是:%s"%(downloadfolder),0.5)   #插入队列
            doclist = os.listdir(downloadfolder)
            for i in doclist:
                if i.startswith("."):
                    continue
                for url in open(downloadfolder+i,'r'):
                    data=url.strip().decode("gbk")
                    self.file_add(data)  #添加数组
            #print self.list
            #print len(self.list)
        except Exception,e:
            #print u"找不到指纹识别文件Bin夹",e
            messagebox.put(u"文件路径可能为 中文 找不到指纹识别文件Bin夹%s"%e,0.5)   #插入队列
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
                                #print u"网址:%s  关键字:%s  版本:%s  链接:%s"%(self.URL,i[1],i[1],i[0])
                                #messagebox.put(u"网址:%s  关键字:%s  版本:%s  链接:%s"%(self.URL,i[1],i[1],i[0]),0.5)   #插入队列
                                #域名--CMS指纹--指纹详细地址
                                data=[self.URL,i[1],i[0]]
                                print data
                                url_exp.put(data,0.5)   #插入队列
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
        #print u"版本测试:%s 完成"%(url)

        da=u"版本测试:%s time用时 %s S"%(url,int(time.strftime('%H%M%S'))-self.A)
        print da
        messagebox.put(da,0.5)   #插入队列
        self.run()
        return 0
    ################################################

if __name__=='__main__':
    threads = []  #线程
    #list=["http://www.baidu.com","http://www.wuyuan168.com"]   #扫描网址   附加数据
    openurl.put("http://www.wuyuan168.com",0.5)   #插入队列
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(Class_cms(i))

    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程






