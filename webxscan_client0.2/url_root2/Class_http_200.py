#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import sys, os, time, httplib
import re
import threading
import gzip,StringIO
from class_Queue import url_exp
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间

class class_http_200(threading.Thread):
    def __init__(self,penurl):
        threading.Thread.__init__(self)
        self.penurl=penurl
        self.url=self.penurl[1].split('//')[1]
        self.list_http=[]  #http数组
        self.past=[]
        self.open_file()  #打开TXT文本写入数组
        ###############
        self.pst_http(self.url)
        if len(self.list_http)<=10:
            self.rfid_list() #读取储存
        self.del_list()  #删除数组

    def open_file(self):  #遍历文件
        try:
            passlist = []
            list_passlist=[]
            #合并字典
            doclist = os.listdir(os.getcwd()+r'\http_200')
            doclist.sort()
            for i in doclist:
                for url in open('http_200/'+i,'r'):
                    data=url.strip().decode("gbk")
                    passlist.append(data)


            for i in passlist:  #python 列表去重
                if i not in list_passlist:
                    list_passlist.append(i)

            E = 0 #得到list的第一个元素
            while E < len(list_passlist):
                self.past.append(list_passlist[E])  #添加到数组里
                E = E + 1

            #print len(self.past)
        except Exception,e:
            #print e
            return 0

    def rfid_list(self):  #读取数组
        try:
            for i in self.list_http:
                #print i
                EXP_list=[1,self.penurl[0],self.penurl[1],"http_200",i,"",""]
                #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                url_exp.put(EXP_list,0.5)   #插入队列

        except Exception,e:
            print e
            return 0

    def del_list(self):  #删除数组
        try:
            i = 0 #得到list的第一个元素
            while i < len(self.list_http):
                del self.list_http[i]
        except Exception,e:
            print e
            return 0

#    def run(self):
#        try:
#            print self.penurl
#            self.pst_http(self.penurl)
#            if len(self.list_http)<=10:
#                self.rfid_list() #读取储存
#            self.del_list()  #删除数组
#            #getUnRedirectUrl("http://www.anzhuo.com/soft/index_main.php")
#        except Exception,e:
#            print e
#            return 0
#http://www.it165.net/pro/html/201211/4068.html
#http://www.baidu.com/s?bs=python+%E5%88%A4%E6%96%AD+302%E9%87%8D%E5%AE%9A%E5%90%91&ie=utf-8&f=8&rsv_bp=2&rsv_spt=3&wd=python+httplib+302%E9%87%8D%E5%AE%9A%E5%90%91
    def pst_http(self,host):   #获取是否开放  #pst_http("127.0.0.1")
        try:
            #print self.past
            for admin in self.past:
                admin = admin.replace("\n","")
                #print admin
                #admin = "/" + admin
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
                        self.list_http.append("http://"+host+admin)
                else:
                    continue  #跳过
                    #print "H",
                connection.close()
            return 1
        except:
            pass
            return 0

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
    list=["http://www.baidu.com","http://www.anzhuo.com"]
    for i in range(1):
        threads.append(class_http_200(list))
    for t in threads:
        t.start()


