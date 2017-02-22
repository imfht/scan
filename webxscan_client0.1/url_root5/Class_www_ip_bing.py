#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import urllib2, re, time
import urllib
import socket
import threading
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import class_Queue  #消息队列
url_root1 = class_Queue.url_root1  #网站版本漏洞  webFTP  iis写入   CMS程序识别

class Class_www_ip_bing(threading.Thread):  #查找2级域名
    def __init__(self,penurl):
        threading.Thread.__init__(self)
        self.penurl=""
        self.LS =[]  #初始化类
        self.list_2=[]
        self.NO_url ="msn.com|microsoft.com"
        self.NO_url_list=self.NO_url.split('|')
        if "http://" in penurl:
            self.penurl=penurl[7:]
        else:
            self.penurl=penurl

    def socket_sendall(self,IP):
        try:
            return socket.gethostbyname(IP)  #www.51jmyj.com
        except:
            return 0

    def open_url_data(self,url):  #读取网页内容
        try:
            req = urllib2.Request(url)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            return s.read()
        except:
            return 0

    def URL_STR(self,data):#判断是否是HTTP字符
        try:
            sStr2 = 'http://'
            sStr3 = 'https://'
            if data.find(sStr2) and data.find(sStr3):
                return 1
            else:
                return 0 #print "查找到了"
        except:
            return 1

    def CS_YM(self,data):  #域名排除异常
        try:
            self.AE = 0 #得到list的第一个元素
            while self.AE < len(self.NO_url_list):
                #print "1111",list[E]
                if not data.find("."+self.NO_url_list[self.AE])==-1:
                    return 0
                self.AE +=1
            return 1
        except:
            #print u"域名排除异常"
            return 1

    def URL_TQURL(self,data): #URL提取URL
        try:
            data +="/"      #data ="https://www.baidu.com/cache/sethelp/index.html"
            if ~data.find("http://"):  #~取反
                data=data[7:] #字符串删除
                nPos = data.index('/') #查找字符        #print nPos
                sStr1 = data[0:nPos] #复制指定长度的字符
                return sStr1

            if ~data.find("https://"):  #~取反
                data=data[8:] #字符串删除
                nPos = data.index('/') #查找字符
                #print nPos
                sStr1 = data[0:nPos] #复制指定长度的字符
                return sStr1
        except:
            pass
            #print "Thread:%d-CS_openurl-Extract URL:%s URL error"%\
            #      (self.Ht,data)
    def liet_lsqc(self): #列表去重复
        try:
        #列表去重复
            for i in self.LS:
                if i not in self.list_2:
                    self.list_2.append(i)
        except:
            pass

    def liet_CX(self):  #查询数据是否存在
        try:
            E = 0 #得到list的第一个元素
            while E < len(self.list_2):
                #print self.list_2[E]
                url_root1.put("http://"+self.list_2[E],0.3)   #插入队列
                E = E + 1
            return 0
        except:
            pass


    def bing_ip_www(self,ip):
        try:
            bing_data="http://cn.bing.com/search?q=IP:%s&rn=50&go=&first=0"%(ip)
            #print bing_data
            ss=self.open_url_data(bing_data)
            if ss==0:
                return
            ##################################
            #<div class="sb_meta"><cite>baidu.com/favicon.ico</cite>&nbsp;&#0183;&#32;2011-1-24</div>
            #'<div class="sb_meta"><cite>(.*?)</cite>.*?</div>'
            p = re.compile( r'<a.+?href=.+?>.+?</a>' )
            pname = re.compile( r'(?<=>).*?(?=</a>)' )
            phref = re.compile( r'(?<=href\=\").*?(?=\")')
            #构造及编译正则表达式
            sarr = p.findall(ss)#找出一条一条的<a></a>标签   #这添加到数组在过滤重复值减少mysql压力
            for every in sarr:
                sname = pname.findall( every )
                if sname:
                    sname = sname[0]
                    shref = phref.findall( every )
                if shref:
                    shref = shref[0]
                    #print shref #获取URL
                    if ~self.URL_STR(shref):
                        a1=self.URL_TQURL(shref) #URL提取URL

                        if (a1 is not None) or (a1==""):  #判断是否为 None
                            if not self.CS_YM(a1):  #域名排除异常
                                continue #进入下一次环
                            #print a1
                            self.LS.append(a1)  #添加数据
        except:
            pass

    def run(self):
        try:
            IP=self.socket_sendall(self.penurl)
            if IP==0:
                return
            id=IP.rfind('.')
            sStr1 = IP[0:id+1] #复制指定长度的字符
            for IP4 in range(254,0,-1):
                IP_data=sStr1+str(IP4)
                #print IP_data
                self.bing_ip_www(IP_data)
                time.sleep(1) #确保先运行Seeker中的方法
            self.liet_lsqc() #列表去重复
            self.liet_CX()  #查询数据是否存在
        except BaseException, e:
            print(str(e))
#        except:
#            pass
            #####################

################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(Class_www_ip_bing("http://www.126.com"))

    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程

