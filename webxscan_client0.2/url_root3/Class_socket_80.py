#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import re
import threading
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间

from class_Queue import url_exp

class Class_socket_80:

    def assign(self,service, arg=None):
        if service == '80':
            return True, arg

    def scan(self,arg):
        try:
            self.url0, self.url1 = arg
            self.penurl=self.url1.split('//')[1]
            self.socket_80(self.penurl)
        except:
            return 0

    def socket_80(self,url):
        try:
            port=80
            ip = socket.gethostbyname(url)  #www.51jmyj.com
            data="OPTIONS / HTTP/1.1\nHost:%s\r\n\r\n"%(ip)  #OPTIONS返回服务器的各种信息
            OPTIONS=self.socket_sendall(ip,port,data)
            p = re.compile( r'(Server:.*?)(\n)')  #(Server):(.*?)(?:\n)    (Server:.*?)(\n)
            sarr = p.findall(OPTIONS)
            data=sarr[0][0]
            if data=="":
                return 0

            EXP_list=[1,self.url0,self.url1,"socket_port80",data,"",""]
            #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
            #print EXP_list
            url_exp.put(EXP_list,0.5)   #插入队列
            print "url:%s port80:%s"%(url,data)
        except:
            return 0

    def socket_sendall(self,IP,port,message):
        try:
            S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            S.connect((IP,port))
            S.sendall(message)
            return S.recv(1024)
        except:
            return 0


################################################
if __name__=='__main__':
    class_www=Class_socket_80()
    class_www.scan(class_www.assign('80', (URL[0],URL[1]))[1])