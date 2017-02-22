#!/usr/local/bin/python

################################################
import urllib2, re, time
import Csqlite3
import socket
import threading
socket.setdefaulttimeout(10)
import thread
import list
import ConfigParser

class CS_openurl(threading.Thread):
    def __init__(self,htint):
        threading.Thread.__init__(self)
        self.Ht=htint
        self.INI_data1=0
        self.INI_data2=0
        self.INI_data3=0
        self.Internet=200
        self.printf=10
        self.no_openurl=0
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()

        self.try_openurl="http://www.msn.com"
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("gost.ini"))
            self.try_openurl = config.get("DATA","try_openurl")
            self.NO_url = config.get("DATA","NO_url")
            self.NO_url_list=self.NO_url.split('.')
        except:
            print "INI--try: except: try_openurl"

    def run(self):
        try:

            print "----CS_openurl%drun----"%(self.Ht)
            self.open_mysql()
        except:
            print "----%d--CS_openurl---run try: except:----"%(self.Ht)
            time.sleep(60)
            self.run()

    def open_mysql(self):
        try:
            sql="select * from openurl where openurl is NULL limit 1"
            data = self.sql3.mysqlite3_select(sql)
            if ~data.find("null123456"):
                print "----%d--openurltry: except:----"%(self.Ht)
                time.sleep(10)
                self.open_mysql()
            update = "update openurl set openurl='send' where url='%s'"%(data)
            self.sql3.mysqlite3_update(update)

            url_data = "http://"+data
            print "----%d--open URL:%s"%(self.Ht,url_data)
            self.INI_data1=self.INI_data1+1
            self.no_openurl=0
            self.URL_DZ(url_data)
        except:
            time.sleep(3)
            self.no_openurl+=1
            if self.no_openurl>=10:
                self.no_openurl=0
                print "----%d--openurl URLtry: except:----"%(self.Ht)
                self.URL_DZ(self.try_openurl)
            self.open_mysql()

    ####################################################################
    def URL_STR(self,data):
        try:
            sStr2 = 'http://'
            sStr3 = 'https://'
            if data.find(sStr2) and data.find(sStr3):
                return 1
            else:
                return 0
        except:
            return 1

    def URL_TQURL(self,data):
        try:
            data +="/"      #data ="https://www.baidu.com/cache/sethelp/index.html"
            if ~data.find("http://"):
                data=data[7:]
                nPos = data.index('/')
                sStr1 = data[0:nPos]
                return sStr1

            if ~data.find("https://"):
                data=data[8:]
                nPos = data.index('/')
                #print nPos
                sStr1 = data[0:nPos]
                return sStr1
        except:
            print "----URL----"
    ####################################################################

    def URL_DZ(self,URL):
        try:
            LS = list.Clist()
            LS.list_del()
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=10)
            ss = s.read()
            p = re.compile( r'<a.+?href=.+?>.+?</a>' )
            pname = re.compile( r'(?<=>).*?(?=</a>)' )
            phref = re.compile( r'(?<=href\=\").*?(?=\")')
            sarr = p.findall(ss)
            i=0
            for every in sarr:
                if i>=4000:
                    print "---->4000 URL----\n"
                    break
                else:
                    i+=1
                sname = pname.findall( every )
                if sname:
                    sname = sname[0]
                    shref = phref.findall( every )
                if shref:
                    shref = shref[0]
                    if ~self.URL_STR(shref):
                        a1=self.URL_TQURL(shref)
                        LS.liet_add(a1)

            LS.liet_lsqc()
            time.sleep(0.5)
            E = 0
            while E < len(LS.list_2):
                self.mysql_add(LS.list_2[E])
                E = E + 1
            if self.printf>=10:
                print "----%d--URL:%sURL:%dURL%d---URL:%s/URL%s/URL:%s--%s----"%(self.Ht,URL,len(LS.list),len(LS.list_2),self.INI_data1,self.INI_data2,self.INI_data3,time.strftime('%Y.%m.%d-%H.%M.%S'))
                self.printf=0
            self.printf=self.printf+1
            if self.INI_data1>=3000 and self.INI_data3>=100000:
                self.INI_data1=0
                self.INI_data2=0
                self.INI_data3=0
            self.open_mysql()
        except:
            print "----%d--%sURL NO----"%(self.Ht,URL)
            self.INI_data2=self.INI_data2+1
            time.sleep(5)
            self.open_mysql()

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

    def mysql_select2(self,data):
        try:
            i=0

            self.sql3.conn.commit()
            cur = self.sql3.conn.cursor()
            cur.execute(data)
            res = cur.fetchall()
            for line in res:
                if i>=10:
                    return i
                i=i+1
            cur.close()
            return 0
        except:
            return 0

    def CS_YM(self,data):
        try:
            self.AE = 1
            while self.AE < len(self.NO_url_list):
                #print "1111",list[E]
                if not data.find("."+self.NO_url_list[self.AE])==-1:
                    return 0
                self.AE +=1
            return 1
        except:
            return 1

    def mysql_add(self,data1):
        try:
            if data1=="":
                return 0

            if not self.CS_YM(data1):
                print "----%d--%s no"%(self.Ht,data1)
                return 0

            dURL=self.get_sdomain(data1)
            #print dURL

            sql="select * from openurl where url like '%%%s'"%(dURL)
            #print sql
            if self.mysql_select2(sql):
                #print "1",
                return 0
            else:
                if ~(data1.find("/") and data1.find("http") and data1.find("?") and data1.find("%")and data1.find(" ")and data1.find("�")):
                    print data1,"NO URL",
                    return 0
                else:
                    insert="insert into openurl(url,time) VALUES('%s','%s')"%(data1,time.strftime('%Y.%m.%d-%H.%M.%S'))
                    #print insert
                    if self.sql3.mysqlite3_insert(insert):
                        self.INI_data3=self.INI_data3+1
                        return 1
                    else:
                        return 0
                ##############
        except:
            return 0





################################################
if __name__=='__main__':
    threads = []
    nthreads=10
    for i in range(nthreads):
        threads.append(CS_openurl(i))

    for thread in threads:
        thread.start()

