#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import os, httplib
import re
import threading
import gzip,StringIO
import socket
import time
socket.setdefaulttimeout(10)  #设置了全局默认超时时间

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
#    messagebox.put(u"http_download当前文件夹是:%s"%(currentfolder),0.5)   #插入队列
#else:
#    messagebox.put(u"http_download(获取当前文件夹失败)错误：失败不是当前文件夹是:%s"%(currentfolder),0.5)   #插入队列


class class_download(threading.Thread):
    def __init__(self,x_c):
        threading.Thread.__init__(self)
        self.x_c=x_c
        self.URL=""
        self.list_download=[]
        self.past=[]

        ###############
    def run(self):
        while True:
            try:
                if openurl.empty():   #判断队列是否为空
                    print u"http_download--已经没有需要测试的URL了"
                    time.sleep(10)
                self.del_list()  #删除数组            # 清空数组
                res = self.worker()     # 开始工作
                if res == 0:
                    break
                self.run()
            except:
                self.run()
                pass

    def worker(self):     #处理任务的 返回0，如果做了，继续
        try:
            URL = openurl.get(0.5)  #get()方法从队头删除并返回一个项目
            if not URL=="":
                messagebox.put(u"http_download--线程%d开始测试下载%s"%(self.x_c,URL),0.5)   #插入队列
                self.URL=URL
                url_data=URL.split('//')[1]
                self.open_file(url_data)  #打开TXT文本写入数组
                if len( self.past ) <= 0:
                    #assert(False)
                    return 0
                self.pst_download(url_data)  #开始测试下载

        except:
            pass
        return 1

#    def rfid_list(self):  #读取数组
#        try:
#            messagebox.put(u"http_download--线程%d 测试%s完成"%(self.x_c,self.URL),0.5)   #插入队列
#            for i in self.list_download:
#                data=[self.URL,"http_download",i]
#                #print "==http_download==",data
#                url_exp.put(data,0.5)   #插入队列
#        except Exception,e:
#            print e
#            return 0

    def del_list(self):  #删除数组
        try:   #self.past=[]
            while  len(self.list_download) > 0:
                del self.list_download[0]
            while len(self.past) > 0:
                del self.past[0]
        except Exception,e:
            print e

        self.URL=""
        self.list_download=[]
        self.past=[]

    def pst_download(self,host):
        for admin in self.past:
            admin = admin.replace("\n","")
            admin = admin.replace("\r","")
            admin = admin.replace(" ","")
            if len(self.list_download)>30:
                continue  #跳过
            if len(self.list_download)==30:
                data=[self.URL,"http_download",u">=30条可能404跳转了无法确定"]
                #print "==data==",data
                url_exp.put(data,0.5)   #插入队列
                messagebox.put(u"http_download--线程%d网址%s >=30条可能404跳转了无法确定"%(self.x_c,self.URL),0.5)   #插入队列

            try:
                connection = httplib.HTTPConnection(host,timeout=10) #httplib.HTTPConnection(host,80,timeout=20)
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

                    #SQLdata="http://"+host+admin+"---%s %s"%(response.status, response.reason)
                    #print "http://"+host+admin+len(data)+"KB"
                    data1="http://%s%s|%dKB"%(host,admin,len(data))
                    #print data
                    self.list_download.append(data1)
                    Adata=[self.URL,"http_download",data1]
                    #print "==http_download==",data
                    url_exp.put(Adata,0.5)   #插入队列
                    
                else:
                    pass #continue  #跳过 #print "H",
                connection.close()
            except Exception,e:
                print e
        return 0

    #生成字典下面
    def get_sdomain(self,domain):  #域名拆解www.baidu.com->baidu.com
        suffixes = 'ac', 'ad', 'ae', 'aero', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'arpa', 'as', 'asia', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'biz', 'bj', 'bm', 'bn', 'bo', 'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cat', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'com', 'coop', 'cr', 'cu', 'cv', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'edu', 'ee', 'eg', 'er', 'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gov', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'info', 'int', 'io', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jobs', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mg', 'mh', 'mil', 'mk', 'ml', 'mm', 'mn', 'mo', 'mobi', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'name', 'nc', 'ne', 'net', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'org', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'pro', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'st', 'su', 'sv', 'sy', 'sz', 'tc', 'td', 'tel', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'xn', 'ye', 'yt', 'za', 'zm', 'zw'
        sdomain = []
        bdomain = False
        for section in domain.split('.'):
            if section in suffixes:
                sdomain.append(section)
                bdomain = True
            else:
                sdomain = [section]
        return '.'.join(sdomain) if bdomain  else ''

    def get_ssdomain(self,domain):  #域名拆解www.baidu.com->baidu
        sdomain = self.get_sdomain(domain)  #先解析一道
        ssdomian = sdomain.partition('.')[0] if sdomain else ''
        return ssdomian

    #self.ui.messagebox.append(self.cur_file_dir())
    #import sys,os
    def cur_file_dir(self):  #获取脚本文件的当前路径
        path = sys.path[0]#获取脚本路径
        #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
        if os.path.isdir(path):
            return path
        elif os.path.isfile(path):
            return os.path.dirname(path)

    def open_file(self,host):  #遍历文件
        try:
            domain = host   #不明白未什么还要赋值  直接使用host变量不就可以了吗
            sdomain = self.get_sdomain(domain)  #域名拆解www.baidu.com->baidu.com
            ssdomain = self.get_ssdomain(domain)  #域名拆解www.baidu.com->baidu
            ipaddress = re.compile( r'25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))' )   #正则是否是IP地址
            passlist = []
            list_passlist=[]

            #合并字典
            downloadfolder=self.cur_file_dir()+r'/download/'
            messagebox.put(u"http_download当前文件夹是:%s"%(downloadfolder),0.5)   #插入队列
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
                    #print "download-----",url
                    #print len(self.list)

            for i in passlist:  #python 列表去重
                if i not in list_passlist:
                    list_passlist.append(i)

            #遍历数组
            for dpath in list_passlist:
                #%domain%  完整域名 www.baidu.com
                #%sdomain% 域名拆解 baidu.com
                #%ssdomain% 域名拆解 baidu
                if  '%domain%' in dpath or '%sdomain%' in dpath or '%ssdomain%' in dpath:
                    if sdomain == '' or ipaddress.findall(domain): # ignore
                        continue  #跳过
                    dpath = dpath.replace('%domain%',domain)  #返回根据正则表达式进行文字替换后的字符串的复制
                    dpath = dpath.replace('%sdomain%',sdomain)
                    dpath = dpath.replace('%ssdomain%',ssdomain)
                self.past.append(dpath)

            #print u"http_download数组数量",len(self.past)
            messagebox.put(u"http_download--线程%d URL:%s 需要测试数量:%d"%(self.x_c,self.URL,len(self.past)),0.5)   #插入队列
        except Exception,e:
            print "aaaaaaaa",e
            pass



################################################
#==data== ['http://goldhao.com', 'http_download', u'http://goldhao.com/www.rar|611KB']
#==data== ['http://goldhao.com', 'http_download', u'http://goldhao.com/data1.rar|20KB']
#下载测试 已经没有需要测试的URL了
if __name__=='__main__':
#启动线程控制漏洞扫描
    threads = []  #线程
    openurl.put("http://goldhao.com",0.5)   #插入队列
    for i in range(1):
        threads.append(class_download(i))
    for t in threads:
        t.start()



