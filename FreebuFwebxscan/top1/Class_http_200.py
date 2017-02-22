#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#模块中调试的时候有调试  有出现 timed out   已经设置超时了
#用单线程确实有点慢   其实应该使用我之前的FTP  多线程方法
import os, httplib
import threading
import gzip,StringIO
import socket
import time
socket.setdefaulttimeout(10)  #设置了全局默认超时时间

import Queue
openurl = Queue.Queue()   #需要扫描列表
url_exp = Queue.Queue()   #扫描结果
messagebox = Queue.Queue() #要显示的消息提示

import sys
reload(sys)
sys.setdefaultencoding('utf8')   #'ascii' codec can't encode characters in position 5-7: ordinal not in range(

import Queue
openurl = Queue.Queue()   #需要扫描列表
url_exp = Queue.Queue()   #扫描结果
messagebox = Queue.Queue() #要显示的消息提示

from os import path
# Get current file absolute path

#script = __file__   #绝对路径
#if path.islink(script):  #判断路径是否为空
#    script = path.realpath(script)  #函数 realpath() 函数返回绝对路径
#currentfolder = path.split(path.abspath(__file__))[0]  #获取当前脚本文件所在目录
#if not currentfolder:  #获取失败在换个函数
#    currentfolder = path.abspath(os.getcwd())
#if currentfolder:
#    messagebox.put(u"HTTP_200当前文件夹是:%s"%(currentfolder),0.5)   #插入队列
#else:
#    messagebox.put(u"HTTP_200(获取当前文件夹失败)错误：失败不是当前文件夹是:%s"%(currentfolder),0.5)   #插入队列


class class_http_200(threading.Thread):
    def __init__(self,x_c):
        threading.Thread.__init__(self)
        self.x_c=x_c
        self.URL=""
        self.list_http=[]  #http数组
        self.past=[]
        ###############
    def run(self):
        try:
            if openurl.empty():   #判断队列是否为空
                print u"HTTP_200--已经没有需要测试的URL了"
                time.sleep(10)
            URL = openurl.get(0.5)  #get()方法从队头删除并返回一个项目
            if not URL=="":
                #print "--http 200--",URL
                messagebox.put(u"HTTP_200--线程%d开始测试后台%s"%(self.x_c,URL),0.5)   #插入队列
                self.URL=URL
                url_data=URL.split('//')[1]
                self.open_file()  #打开TXT文本写入数组
                self.pst_http(url_data)  #开始测试
            self.del_list()  #删除数组
            self.run()
        except:
            self.del_list()  #删除数组
            self.run()
            pass

    #self.ui.messagebox.append(self.cur_file_dir())
    #import sys,os
    def cur_file_dir(self):  #获取脚本文件的当前路径
        path = sys.path[0]#获取脚本路径
        #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
        if os.path.isdir(path):
            return path
        elif os.path.isfile(path):
            return os.path.dirname(path)

    def open_file(self):  #遍历文件
        try:
            passlist = []
            list_passlist=[]
            #合并字典
            downloadfolder=self.cur_file_dir()+r'/http_200/'
            messagebox.put(u"http_200当前文件夹是:%s"%(downloadfolder),0.5)   #插入队列
            doclist = os.listdir(downloadfolder)
            print doclist.sort()
            for i in doclist:
                # filter the hidden file, just for safe
                if i.startswith("."):
                    continue
                for url in open(downloadfolder+i,'r'):
                    data=url.strip().decode("gbk")
                    data.replace("\r","")
                    data.replace("\n","")
                    data.replace(" ","")
                    passlist.append(data)
                    #print "http_200-----",url
                    #print len(self.list)


            for i in passlist:  #python 列表去重
                if i not in list_passlist:
                    list_passlist.append(i)

            E = 0 #得到list的第一个元素
            while E < len(list_passlist):
                self.past.append(list_passlist[E])  #添加到数组里
                E = E + 1

            #print u"HTTP_200数组数量",len(self.past)
            messagebox.put(u"HTTP_200--线程%d URL:%s 需要测试数量:%d"%(self.x_c,self.URL,len(self.past)),0.5)   #插入队列
        except Exception,e:
            #print e
            return 0

    def del_list(self):  #删除数组
        try:
            while  len(self.list_http) > 0:
                del self.list_http[0]

            self.URL=""
            self.list_http=[]  #http数组
            self.past=[]
        except Exception,e:
            print e
            return 0

    def pst_http(self,host):   #获取是否开放  #pst_http("127.0.0.1")
        for admin in self.past:
            admin = admin.replace("\n","")
            admin = admin.replace("\r","")
            admin = admin.replace(" ","")
            if len(self.list_http)>50:
                continue  #跳过
            if len(self.list_http)==50:
                data=[self.URL,"http_200",u">=50条可能404跳转了无法确定"]
                #print "==data==",data
                url_exp.put(data,0.5)   #插入队列
                messagebox.put(u"HTTP_200--线程%d网址%s >=50条可能404跳转了无法确定"%(self.x_c,self.URL),0.5)   #插入队列
            try:
                connection = httplib.HTTPConnection(host,80,timeout=10)
                connection.request("GET",admin)
                response = connection.getresponse()#返回处理后的数据
                #print "%s %s %s" % (admin, response.status, response.reason)
                #/admin-login.php   ,错误404  ，Not Found   /moderator/ 404 File Not Found
                data=response.reason
#                result=response.getresponse()
#                print data
#                print result
                if "OK" in data or "Forbidden" in data:  #302
                    if ('content-encoding', 'gzip') in response.getheaders():
                        compressedstream = StringIO.StringIO(response.read())
                        gzipper = gzip.GzipFile(fileobj=compressedstream)
                        data = gzipper.read()
                    else:
                        data = response.read()

                    if (len(data)>=100):
                        #SQLdata="http://"+host+admin+"---%s %s"%(response.status, response.reason)
                        #print "%s"%SQLdata
                        data1="http://%s|%dKB"%(host+admin,len(data))
                        #print data
                        self.list_http.append(data1)
                        Adata=[self.URL,"http_200",data1]
                        #print "==HTTP_200==",data
                        url_exp.put(Adata,0.5)   #插入队列
                else:
                    pass #continue  #跳过 #print "H",
                connection.close()
            except Exception,e:
                print "sssssssss",e
                pass

## 302 301
#    ##########################################################
#import httplib2
#class RedirctHandler(urllib2.HTTPRedirectHandler):
#    """docstring for RedirctHandler"""
#    def http_error_301(self, req, fp, code, msg, headers):
#        pass
#    def http_error_302(self, req, fp, code, msg, headers):
#        pass
#    def http_error_404(self, req, fp, code, msg, headers):
#        pass
#
#def getUnRedirectUrl(url,timeout=10):
#    opener = urllib2.build_opener(RedirctHandler)
#    response = opener.open(url,timeout=timeout)
#    print response.read()
##    req = urllib2.Request(url)
##    debug_handler = urllib2.HTTPHandler(debuglevel = 1)
##    opener = urllib2.build_opener(debug_handler, RedirctHandler)
##
##    html = None
##    response = None
##    try:
##        response = opener.open(url,timeout=timeout)
##        html = response.read()
##    except urllib2.URLError as e:
##        if hasattr(e, 'code'):
##            error_info = e.code
##        elif hasattr(e, 'reason'):
##            error_info = e.reason
##    finally:
##        if response:
##            response.close()
##    if html:
##        return html
##    else:
##        return error_info
#    ##########################################################



################################################
if __name__=='__main__':
#启动线程控制漏洞扫描
    threads = []  #线程
    openurl.put("http://www.anzhuo.com",0.5)   #插入队列
    for i in range(1):
        threads.append(class_http_200(i))
    for t in threads:
        t.start()


