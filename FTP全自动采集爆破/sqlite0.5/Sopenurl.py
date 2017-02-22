#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#采集URL地址
################################################
import urllib2, re, time
import Csqlite3
import socket
import threading
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import thread
import list
import ConfigParser  #INI读取数据

class CS_openurl(threading.Thread):
    def __init__(self,htint):
        threading.Thread.__init__(self)
        self.Ht=htint
        self.INI_data1=0  #扫描过URL个
        self.INI_data2=0  #URL获取失败
        self.INI_data3=0  #添加到数据库个
        self.Internet=200  #控制到300次检测一次网络状态
        self.printf=10  #控制显示
        self.no_openurl=0  #获取失败
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
            print u"INI读取异常try_openurl"

    def run(self):
        try:

            print u"----CS_openurl线程%d启动----"%(self.Ht)
            self.open_mysql()     #读取URL
            #self.URL_DZ("http://www.163.com") #遍历页里的地址
        except:
            print u"----线程%d--CS_openurl---run异常！！！！！----"%(self.Ht)
            time.sleep(60)
            self.run()

    def open_mysql(self):  #读取URL
        try:
            sql="select * from openurl where openurl is NULL limit 1"
            data = self.sql3.mysqlite3_select(sql)
            #print U"数据库URL",data
            if ~data.find("null123456"):
                print u"----线程%d--可能无读取openurl表的数据请查看数据库！！！！！----"%(self.Ht)
                #mysql.mysql_S()  #保存数据
                time.sleep(10)
                self.open_mysql()
            update = "update openurl set openurl='send' where url='%s'"%(data)
            self.sql3.mysqlite3_update(update)

            url_data = "http://"+data
            print u"----线程%d--读取URL：%s"%(self.Ht,url_data)
            self.INI_data1=self.INI_data1+1
            self.no_openurl=0  #获取失败
            self.URL_DZ(url_data)  #遍历页里的地址
        except:
            #print u"----线程%d--读取openurl表URL异常！！！！！----"%(self.Ht)
            time.sleep(3)
            self.no_openurl+=1  #获取失败
            if self.no_openurl>=10:
                self.no_openurl=0  #获取失败
                print u"----线程%d--读取openurl表URL异常！！！！！----"%(self.Ht)
                self.URL_DZ(self.try_openurl)  #遍历页里的地址
            self.open_mysql()

    ####################################################################
    def URL_STR(self,data):#判断是否是HTTP字符
        try:
            sStr2 = 'http://'
            sStr3 = 'https://'
            if data.find(sStr2) and data.find(sStr3):
                return 1 #print "没有找到"
            else:
                return 0 #print "查找到了"
        except:
            return 1

    def URL_TQURL(self,data): #URL提取URL
        try:
            data +="/"      #data ="https://www.baidu.com/cache/sethelp/index.html"
            if ~data.find("http://"):  #~取反
                data=data[7:] #字符串删除
                nPos = data.index('/') #查找字符        #print nPos
                sStr1 = data[0:nPos] #复制指定长度的字符
                return sStr1

            if ~data.find("https://"):  #~取反
                data=data[8:] #字符串删除
                nPos = data.index('/') #查找字符
                #print nPos
                sStr1 = data[0:nPos] #复制指定长度的字符
                return sStr1
        except:
            print u"----URL提取URL错误----"
    ####################################################################

    def URL_DZ(self,URL):  #遍历页里的地址
        try:
            LS = list.Clist()  #初始化类
            LS.list_del()  #清空list列表
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            ss = s.read()
            p = re.compile( r'<a.+?href=.+?>.+?</a>' )
            pname = re.compile( r'(?<=>).*?(?=</a>)' )
            phref = re.compile( r'(?<=href\=\").*?(?=\")')
            #构造及编译正则表达式
            sarr = p.findall(ss)#找出一条一条的<a></a>标签   #这添加到数组在过滤重复值减少mysql压力
            i=0
            for every in sarr:
                if i>=3000:
                    print u"----超过3000个URL地址！！！！！！----\n"
                    break
                else:
                    i+=1
                sname = pname.findall( every )
                if sname:
                    sname = sname[0]
                    shref = phref.findall( every )
                if shref:
                    shref = shref[0]
                    #print shref #获取URL
                    if ~self.URL_STR(shref):
                        a1=self.URL_TQURL(shref) #URL提取URL
                        LS.liet_add(a1)  #添加到数组

            LS.liet_lsqc() #数组列表去重复
            time.sleep(0.5)
            E = 0 #得到list的第一个元素
            while E < len(LS.list_2):
                self.mysql_add(LS.list_2[E])   #添加到数据库
                E = E + 1
                #print u"\n-----------------------URL列表添加完成-----------------------"
            if self.printf>=10:#  #控制显示
                print u"----线程%d--采集URL:%s原URL:%d去掉重复URL:%d---扫描过URL:%s个/URL读取失败%s个/成功添加到数据库URL:%s个--%s----"%(self.Ht,URL,len(LS.list),len(LS.list_2),self.INI_data1,self.INI_data2,self.INI_data3,time.strftime('%Y.%m.%d-%H.%M.%S'))
                self.printf=0
            self.printf=self.printf+1
            if self.INI_data1>=3000 and self.INI_data3>=100000:
                self.INI_data1=0
                self.INI_data2=0
                self.INI_data3=0
            self.open_mysql()  #读取URL
            # 上面是将每条<a></a>里面的内容和地址给匹配出来
        except:
            print u"----线程%d--%s这个URL地址无效！！！！！！！！！！！----"%(self.Ht,URL)
            self.INI_data2=self.INI_data2+1  #URL获取失败
            #self.sql.mysql_S()  #保存数据
            time.sleep(5)
            self.open_mysql()

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

    def mysql_select2(self,data):  #模糊查询
        try:
            i=0

            self.sql3.conn.commit()# 获取到游标对象
            cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
            cur.execute(data)# 获取所有结果
            res = cur.fetchall()  #从结果中取出所有记录
            for line in res:
                if i>=10:
                    return i
                i=i+1
            cur.close()  #关闭游标
            return 0
        except:
            return 0

    def CS_YM(self,data):  #域名排除异常
        try:
            self.AE = 1 #得到list的第一个元素
            while self.AE < len(self.NO_url_list):
                #print "1111",list[E]
                if not data.find("."+self.NO_url_list[self.AE])==-1:
                    return 0
                self.AE +=1
            return 1
        except:
            #print u"域名排除异常"
            return 1

    def mysql_add(self,data1):  #添加到数据库
        try:   #查看这个数据是否值得添加
            if data1=="":
                return 0

            if not self.CS_YM(data1):  #域名排除异常
                print u"----线程%d--%s此域名在不添加后辍名内"%(self.Ht,data1)
                return 0

            dURL=self.get_sdomain(data1)  #拆解域名1234.163.com=》163.com
            #在模糊查询看看有多少个  》=10个  这个就不进行添加
            #print dURL

            sql="select * from openurl where url like '%%%s'"%(dURL)
            #print sql
            if self.mysql_select2(sql):  #模糊查询
                #print dURL,u"域名下已经有10个二级域名了不进行添加",
                #print "1",
                return 0
            else:
                #print "没有可以添加"
                if ~(data1.find("/") and data1.find("http") and data1.find("?") and data1.find("%")and data1.find(" ")and data1.find("�")):
                    print data1,u"非法URL",
                    return 0
                else:
                    insert="insert into openurl(url,time) VALUES('%s','%s')"%(data1,time.strftime('%Y.%m.%d-%H.%M.%S'))
                    #print insert
                    if self.sql3.mysqlite3_insert(insert): #添加数据
                    #mysql.mysql_S()   #提交
                        #print "\n",data1,u"添加成功",
                        self.INI_data3=self.INI_data3+1
                        return 1
                    else:
                        #print "\n",data1,u"添加失败",
                        return 0
                ##############
#                sql="select * from openurl where url='%s'"%(data1)
#                data = self.sql3.mysqlite3_insert(sql)
#                if data.find('null123456'):
#                    print u"已经有了这个URL",data1,
#                    #print "N",
#                    return 0
#                else:  #没有可以添加
#                    #print data1
#                    if ~(data1.find("/") and data1.find("http") and data1.find("?") and data1.find("%")):
#                        print data1,u"非法URL",
#                        return 0
#                    else:
#                        insert="insert into openurl(url,time) VALUES('%s','%s')"%(data1,time.strftime('%Y.%m.%d-%H.%M.%S'))
#                        #print insert
#                        if self.sql3.mysqlite3_insert(insert): #添加数据
#                        #mysql.mysql_S()   #提交
#                            print "\n",data1,u"添加成功",
#                            self.INI_data3=self.INI_data3+1
#                            return 1
#                        else:
#                            print "\n",data1,u"添加失败",
#                            return 0
        except:
            return 0





################################################
if __name__=='__main__':
#    mysql_handle.__init__('localhost','root','316118740','urldata')
#    mysql.mysql_open()  #连接数据库
#    TH_OPURL=CS_openurl()
#    TH_OPURL.start()
    threads = []  #线程
    nthreads=10
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(CS_openurl(i))

    for thread in threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程

