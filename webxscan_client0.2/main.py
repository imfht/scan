#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import urllib2, re, time
import ConfigParser  #INI读取数据
import threading
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import class_Queue  #消息队列


#   神龙QQ29295842  webxscan_client0.1


url_root1 = class_Queue.url_root1  #网站版本漏洞  webFTP  iis写入   CMS程序识别
url_root2 = class_Queue.url_root2  #通用 网站漏洞  上传入口  登陆后台  敏感压缩包  表单提交  SQL注入类的
url_root3 = class_Queue.url_root3  #服务器配置漏洞  查看开放端口和服务  ftp弱口令  mysql  sqlserver
url_root4 = class_Queue.url_root4  #IP反查域名  子域名枚举
url_root5 = class_Queue.url_root5  #C段扫描
url_exp = class_Queue.url_exp  #保存扫描到的结果["127.0.0.1","admin","admin"]

class oprn_url(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.name=""
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("server.ini"))
            self.name = config.get("DATA","name")  #测试上传文件
        except:
            print "--name-ini-try--except!!!!!"

    def open_url_data(self,url):  #读取网页内容
        try:
            req = urllib2.Request(url)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            #req.add_header('User-Agent','userAgentIE9')
            #req.add_header('User-Agent', "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)")
            s = urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            return s.read()
        except:
            return 0

    def str_data(self,data):  #data="b1b111111 benghttp://www.126.com|1end"  对内容截取处理
        try:
            if ~data.find("beng"):  #~取反
                nPos = data.index('beng') #查找字符
                data=data[nPos+4:] #字符串删除
                nPos = data.index('end') #查找字符        #print nPos
                sStr1 = data[0:nPos] #复制指定长度的字符
                return sStr1
        except:
            return 0

    def url_data(self,data):#http://www.126.com|135
        try:
        #结果截取了  在发送给1个函数单独处理
        #函数对结果进行分析  判断扫描等级
            ss = data.split("|")
            #print data
            self.scan_dj=ss[1]
            self.A= int(time.strftime('%H%M%S'))
            print u"扫描网址:%s 扫描等级:%s"%(ss[0],ss[1])
            #把结果添加到消息队列
            # url_root1  #网站版本漏洞  webFTP  iis写入   CMS程序识别
            # url_root2  #通用 网站漏洞  上传入口  登陆后台  敏感压缩包  表单提交  SQL注入类的
            # url_root3  #服务器配置漏洞  查看开放端口和服务  ftp弱口令  mysql  sqlserver
            # url_root4  #IP反查域名  子域名枚举
            # url_root5  #C段扫描
            list=[ss[0],ss[0]]   #扫描网址   附加数据
            if '1' in ss[1]:
                url_root1.put(list,0.3)   #插入队列
            if '2' in ss[1]:
                url_root2.put(list,0.3)   #插入队列
            if '3' in ss[1]:
                url_root3.put(list,0.3)   #插入队列
            if '4' in ss[1]:
                url_root4.put(list,0.3)   #插入队列
            if '5' in ss[1]:
                url_root5.put(list,0.3)   #插入队列
        except:
            return 0

    def run(self):
        try:
            self.time_data=1
            data=""
            while True:
                print "time.sleep:%d S"%(self.time_data)
                time.sleep(self.time_data)
                if not(url_root1.empty() and url_root2.empty() and url_root3.empty() and url_root4.empty() and url_root5.empty()):   #判断队列是否为空
                    ss = data.split("|")
                    print u"%s还未扫描完成请等待--扫描等级%s--以用时%ds"%(ss[0],self.scan_dj,int(time.strftime('%H%M%S'))-self.A)
                    time.sleep(5)
                    continue

                url='http://www.webxscan.com/openurl.php?user=%s'%(self.name)
                data=self.open_url_data(url)
                if len(data)>=7:
                    self.time_data=20
                    data=self.str_data(data)
                    self.url_data(data)
                else:
                    print u"无法获取到扫描内容 请到后天添加扫描内容!"
                    if self.time_data<=1200:
                        self.time_data+=20

        except:
            return 0

from class_Queue import C_Queue  #消息队列
from class_url_root1 import class_url_root1 #url_root1  #网站版本漏洞  webFTP  iis写入   CMS程序识别
from class_url_root2 import class_url_root2 #通用 网站漏洞  上传入口  登陆后台  敏感压缩包  表单提交  SQL注入类的
from class_url_root3 import class_url_root3 # url_root3  #服务器配置漏洞  查看开放端口和服务  ftp弱口令  mysql  sqlserver
from class_url_root4 import class_url_root4  # url_root4  #IP反查域名  子域名枚举
from class_url_root5 import class_url_root5  #查询C段主机绑定的域名
if __name__=='__main__':
    print "           www.webxscan.com"
    print "           webxscan_client"
    print "           OS:Windows   VS:0.2"
    print "           time:6/8/2013"
    try:
        threads = []  #线程
        for i in range(1):
            threads.append(C_Queue())
        for t in threads:
            t.start()

        threads = []  #线程
        for i in range(1):
            threads.append(oprn_url())
        for t in threads:
            t.start()

        time.sleep(1)
        threads = []  #线程
        for i in range(1):
            threads.append(class_url_root1())
        for t in threads:
            t.start()

        time.sleep(1)
        threads = []  #线程
        for i in range(1):
            threads.append(class_url_root2())
        for t in threads:
            t.start()

        time.sleep(1)
        threads = []  #线程
        for i in range(1):
            threads.append(class_url_root3())
        for t in threads:
            t.start()

        # url_root4  #IP反查域名  子域名枚举
        time.sleep(1)
        threads = []  #线程
        for i in range(1):
            threads.append(class_url_root4())
        for t in threads:
            t.start()

        time.sleep(1)
        threads = []  #线程
        for i in range(1):
            threads.append(class_url_root5())
        for t in threads:
            t.start()

    except BaseException, e:
        print(str(e))


