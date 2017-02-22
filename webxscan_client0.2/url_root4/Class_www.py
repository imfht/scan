#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
# 子域名枚举

import urllib2, re, time
import urllib
import socket
import threading
socket.setdefaulttimeout(10)  #设置了全局默认超时时间

from class_Queue import url_root1

class Class_www:  #查找2级域名
#    def __init__(self,penurl):
#        threading.Thread.__init__(self)
#        self.penurl=""
#        if "http://" in penurl:
#            self.penurl=penurl[7:]
#        else:
#            self.penurl=penurl

    def open_url_data(self,url):  #读取网页内容
        try:
            req = urllib2.Request(url)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            return s.read()
        except:
            return 0

    def assign(self,service, arg=None):
        if service == 'www':
            return True, arg

    def scan(self,arg):
        try:
            self.url0, self.url1 = arg
            self.penurl=self.url1.split('//')[1]
            url_data="http://www.alexa.com/data/details/traffic_details?url=%s"%(self.penurl)
            ss=self.open_url_data(url_data)
            if ss==0:  #读取网页内容
                return 0

            p = re.compile( r"<td class='' ><span class='word-wrap'>(.*?)</span></td>")

            sarr = p.findall(ss)

            for every in sarr:
                list=[self.url0,"http://"+every]
                print list
                url_root1.put(list,0.3)   #插入队列

        except:
            pass
        #####################

###############################################
if __name__=='__main__':
    www=Class_www()
    www.scan(www.assign('www', ("http://www.baidu.com","http://www.163.com"))[1])
