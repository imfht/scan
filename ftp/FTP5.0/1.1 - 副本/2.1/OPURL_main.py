#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
################################################
import sys
#from mysql_handle import mysql_handle
import urllib2, re, time
#import mysql #数据库操作文件
import socket
import threading,time
from threading import Thread
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import thread
import time #获取时间和延时
import urllib2, re, time
import list
import mysql_connector #数据库操作文件

class CS_openurl(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print "开始采集URL地址"
        self.INI_data1=0  #扫描过URL个
        self.INI_data2=0  #URL获取失败
        self.INI_data3=0  #添加到数据库个
        self.Internet=300  #控制到300次检测一次网络状态
        self.conn=mysql_connector.mysql_handle()
        self.conn.mysql_open()


    def run(self):
        try:
            self.open_mysql()     #读取URL
        except:
            print u"CS_openurl---run异常！！！！！"
            time.sleep(10)
            self.run()


    def open_mysql(self):  #读取URL
        try:
            try:   #检测网络连接状态
                if self.Internet>=300:
                    print "11111111111111111111111111111111"
                    urllib2.urlopen(r"http://www.163.com",timeout=10)
                    self.Internet=0
                self.Internet=self.Internet+1
                #print u"网络连接成功"
                #return 1
            except:
                print u"网络无连接 重启程序自身"
                #mysql.mysql_S()  #保存数据
                time.sleep(60)
                self.conn.mysql_S()  #保存数据
                self.open_mysql()
            sql="select * from openurl where openurl is NULL limit 1"
            data = self.conn.mysql_select(sql)
            print U"数据库URL",data
            if ~data.find("null123456"):
                print u"可能无读取的数据请查看数据库！！！！！"
                #mysql.mysql_S()  #保存数据
                data=""
                time.sleep(4)
                self.conn.mysql_S()  #保存数据
                self.open_mysql()
            update = "update openurl set openurl='send' where url='%s'"%(data)
            self.conn.mysql_update(update)
            self.conn.mysql_S()  #保存数据

            url_data = "http://"+data
            #print u"读取URL：",url_data
            self.INI_data1=self.INI_data1+1
            self.URL_DZ(url_data)  #遍历页里的地址
        except:
            print u"读取URL异常！！！！！"
            #mysql.mysql_S()  #保存数据
            time.sleep(10)
            self.conn.mysql_S()  #保存数据
            self.open_mysql()

    def URL_DZ(self,URL):  #遍历页里的地址
        try:
            LS = list.Clist()  #初始化类
            LS.list_del()  #清空list列表
            s = urllib2.urlopen(URL,timeout=5)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            ss = s.read()
            p = re.compile( r'<a.+?href=.+?>.+?</a>' )
            pname = re.compile( r'(?<=>).*?(?=</a>)' )
            phref = re.compile( r'(?<=href\=\").*?(?=\")')
            #构造及编译正则表达式
            sarr = p.findall(ss)#找出一条一条的<a></a>标签   #这添加到数组在过滤重复值减少mysql压力
            i=0
            for every in sarr:
                if i>=3000:
                    print u"超过3000个URL地址！！！！！！\n"
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
            self.conn.mysql_S()  #保存数据
            #print u"\n-----------------------URL列表添加完成-----------------------"
            #print u"-------扫描过URL:%s个/URL读取失败%s个/成功添加到数据库URL:%s个-------"%(self.INI_data1,self.INI_data2,self.INI_data3)
            #采集URL:www.baidu.com原URL:34去掉重复URL:16---扫描过URL:1个/URL读取失败0个/成功添加到数据库URL:0个
            #print "采集URL:%s原URL:%d去掉重复URL:%d---扫描过URL:%s个/URL读取失败%s个/成功添加到数据库URL:%s个--%s"%\
            print (URL,len(LS.list),len(LS.list_2),self.INI_data1,self.INI_data2,self.INI_data3,time.strftime('%Y.%m.%d-%H.%M.%S'))
            if self.INI_data1>=3000 and self.INI_data3>=100000:
                self.INI_data1=0
                self.INI_data2=0
                self.INI_data3=0
            self.open_mysql()  #读取URL
            # 上面是将每条<a></a>里面的内容和地址给匹配出来
        except:
            print u"%s这个URL地址无效！！！！！！！！！！！"%(URL)
            self.INI_data2=self.INI_data2+1  #URL获取失败
            #mysql.mysql_S()  #保存数据
            self.open_mysql()
    ################################
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
            self.conn.cursor.execute(data)
            #self.conn.cursor.scroll(0)
            for row in self.conn.cursor:
                #print '%s-%s-%s'%(row[0],row[1],row[2])
                #return row[0]
                if i>=10:
                    return i
                i=i+1
            return 0
        except:
            return 0

    def mysql_add(self,data1):  #添加到数据库
        try:   #查看这个数据是否值得添加
            dURL=self.get_sdomain(data1)  #拆解域名1234.163.com=》163.com  #在模糊查询看看有多少个  》=10个  这个就不进行添加
            #print dURL
            sql="select * from openurl where url like '%%%s'"%(dURL)
            #print sql
            if self.mysql_select2(sql):  #模糊查询
                #print dURL,u"域名下已经有10个二级域名了不进行添加",
                #print "1",
                return 0
            else:
#                print u"没有可以添加111111111111111"
#                sql="select * from openurl where url='%s'"%(data1)
#                data = self.conn.mysql_select(sql)
#                if data.find('null123456'):
#                    print u"已经有了这个URL",data1,
#                    #print "N",
#                    return 0
#                else:  #没有可以添加
                #print "没有可以添加",data1
                if ~(data1.find("/") and data1.find("http") and data1.find("?") and data1.find("%")):
                    print data1,u"非法URL",
                    return 0
                else:
                    insert="insert into openurl(url,time) VALUES('%s','%s')"%(str(data1),time.strftime('%Y.%m.%d-%H.%M.%S'))
                    #print insert
                    if self.conn.mysql_insert(insert): #添加数据
                        #print "\n",insert,u"添加成功",
                        self.INI_data3=self.INI_data3+1
                        return 1
                    else:
                        #print "\n",insert,u"添加失败",
                        return 0
            return 0
        except:
            return 0
    ################################
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
            print u"URL提取URL错误"
################################################
if __name__=='__main__':
#    mysql_handle.__init__('localhost','root','316118740','urldata')
    #mysql.mysql_open()  #连接数据库
    TH_OPURL=CS_openurl()
    TH_OPURL.start()
#    threads = []  #线程
#    nthreads=1
#    for i in range(nthreads):  #nthreads=10  创建10个线程
#        threads.append(CS_openurl())
#
#    for thread in threads:   #不理解这是什么意思    是结束线程吗
#        thread.start()  #start就是开始线程




