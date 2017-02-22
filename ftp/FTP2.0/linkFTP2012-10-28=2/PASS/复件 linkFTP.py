#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
####################################################################
#qq:316118740
#BLOG:http://hi.baidu.com/alalmn
from ftplib import FTP
import time
####################################################################
#密码组合
def str_index(data1,data2):  #查找字符
    try:
        data1.index(data2)
        return 0
    except:
        return 1

def www_cj(sStr1):  #域名拆解
    passlist.append(sStr1+sStr1)
    sStr2 = "."
    passlist.append(sStr1)
    d1 = sStr1[0:sStr1.find(sStr2)]
    #print "11111",d1
    passlist.append(d1)
    passlist.append(d1+d1)
    sStr1 = sStr1[sStr1.find(sStr2)+1:]
    #print "2222",sStr1
    passlist.append(sStr1)
    passlist.append(sStr1+sStr1)
    if str_index(sStr1,sStr2):
        return 0
        #print "1111111111没有"
    else:
        #print "2222222222有了"
        d2 = sStr1[0:sStr1.find(sStr2)]
        #print d2
        passlist.append(d2)
        passlist.append(d2+d2)
        sStr1 = sStr1[sStr1.find(sStr2)+1:]
        #print sStr1
        passlist.append(sStr1)
        passlist.append(sStr1+sStr1)
        if str_index(sStr1,sStr2):
            return 0
            #print "222222没有"
        else:
            #print "2222222222有了"
            d3 = sStr1[0:sStr1.find(sStr2)]
            #print d3
            passlist.append(d3)
            passlist.append(d3+d3)
            sStr1 = sStr1[sStr1.find(sStr2)+1:]
            #print sStr1
            passlist.append(sStr1)
            passlist.append(sStr1+sStr1)
            if str_index(sStr1,sStr2):
                return 0
                #print "33333没有"
            else:
                #print "2222222222有了"
                d4 = sStr1[0:sStr1.find(sStr2)]
                #print d4
                passlist.append(d4)
                passlist.append(d4+d4)
                sStr1 = sStr1[sStr1.find(sStr2)+1:]
                #print sStr1
                passlist.append(sStr1)
                passlist.append(sStr1+sStr1)
                if str_index(sStr1,sStr2):
                    return 0
                    #print "44444没有"
                else:
                    #print "2222222222有了"
                    d5 = sStr1[0:sStr1.find(sStr2)]
                    #print d5
                    passlist.append(d5)
                    passlist.append(d5+d5)
                    sStr1 = sStr1[sStr1.find(sStr2)+1:]
                    #print sStr1
                    passlist.append(sStr1)
                    passlist.append(sStr1+sStr1)
                    if str_index(sStr1,sStr2):
                        return 0
                        #print "55555没有"
####################################################################
def www_port(host,port=21):  #查看21端口是否开放
    try:
        if host == '':  #传入值等于空   返回
            print u"地址不能为空"
            time.sleep(3) #确保先运行Seeker中的方法
            #linkftp.sql_sel()   #SQL查询
            return 0
        ###############查看21端口是否开放
        ftpA = FTP()  #初始化FTP类
        ftpA.connect(host,port)  #连接 服务器名  端口号
        ################开放了在组合密码最后开始爆破
        www_cj(host)  #域名拆解
    except Exception, e:
        print u"服务器FTP21端口可能没有开放"
        #linkftp.sql_sel()   #SQL查询
        return 0
####################################################################
####################################################################
####################################################################
if __name__=='__main__':
    global  passlist  #声明全局变量
    passlist = []    #用户名：anonymous 密码为空
    global  list_passwed  #列表去重，不打乱原来的顺序
    list_passwed=[]
    www= "ftp.hificat.com"
    www_cj(www)  #域名拆解
    #www= "127.0.0.1"
    #www_port(www)  #www转换IP在查看端口

    print len(passlist)
    #print len(list_passwed)
    #passlist = list(set(passlist))   #python 列表去重
#    for i in passlist:
#        if i not in list_passwed:
#            list_passwed.append(i)
#
    E = 0 #得到list的第一个元素
    while E < len(passlist):
        print passlist[E]
        E = E + 1