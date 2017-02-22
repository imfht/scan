#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import sys, os, time, httplib

#def http_get(host,admin):  #验证地址是否存在
#    connection = httplib.HTTPConnection(host,80,timeout=10)
#    connection.request("GET",admin)
#    response = connection.getresponse()
#    #print "%s %s %s" % (admin, response.status, response.reason)
#    data=response.reason
#    if "OK" in ddata or "Forbidden" in data:
#        SQLdata="http://"+host+admin+"---%s %s"%(response.status, response.reason)
#        return SQLdata
#    else:
#        SQLdata="http://"+host+admin+"---%s %s"%(response.status, response.reason)
#        return SQLdata

def CS_YM(data):  #域名排除异常
    try:
        string = '.cn.gov'
        list=string.split('.')
        E = 1 #得到list的第一个元素
        while E < len(list):
            #print "1111",list[E]
            if not data.find("."+list[E])==-1:
                return 0
            E = E + 1
        return 1
    except:
        print u"域名排除异常"
        return 1

if __name__=='__main__':
    if not CS_YM("www.126.cn"):  #域名排除异常
        print "此域名在不添加后辍名内"

#    sStr1 = 'abcdefg'
#    sStr2 = 'aaa'
#    print sStr1.find(sStr2)

