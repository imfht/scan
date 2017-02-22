#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
# 子域名枚举

import urllib2, re, time
import urllib
import socket
import threading
socket.setdefaulttimeout(10)  #设置了全局默认超时时间

import class_Queue  #消息队列
url_root1 = class_Queue.url_root1  #网站版本漏洞  webFTP  iis写入   CMS程序识别

class Class_www(threading.Thread):  #查找2级域名
    def __init__(self,penurl):
        threading.Thread.__init__(self)
        self.penurl=""
        if "http://" in penurl:
            self.penurl=penurl[7:]
        else:
            self.penurl=penurl

    def open_url_data(self,url):  #读取网页内容
        try:
            req = urllib2.Request(url)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            return s.read()
        except:
            return 0

    def run(self):
        try:
            url_data="http://www.alexa.com/data/details/traffic_details?url=%s"%(self.penurl)
            ss=self.open_url_data(url_data)
            if ss==0:  #读取网页内容
                return 0

            p = re.compile( r"<td class='' ><span class='word-wrap'>(.*?)</span></td>")

            sarr = p.findall(ss)

            for every in sarr:
                url_root1.put(every,0.3)   #插入队列

        except:
            pass
        #####################

###############################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(Class_www("http://www.baidu.com"))

    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程


