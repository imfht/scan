﻿#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#百度权重   PR查询
import re
import urllib
import threading
import time
import Cmysql #数据库操作文件
from struct import *
import urllib2
import string
import re
import sys
import socket
#####################################################
#QQWry.dat
def ip2string( ip ):
    a = (ip & 0xff000000) >> 24
    b = (ip & 0x00ff0000) >> 16
    c = (ip & 0x0000ff00) >> 8
    d = ip & 0x000000ff
    return "%d.%d.%d.%d" % (a,b,c,d)

def string2ip( str ):
    ss = string.split(str, '.')
    ip = 0L
    for s in ss: ip = (ip << 8) + string.atoi(s)
    return ip

class IPSearch:
    def __init__(self,ip_file):
        self.ipdb=open(ip_file,'rb')
        str=self.ipdb.read(8)
        self.first_index ,self.last_index =unpack("II",str)

    def getIPLocation(self,ip):
        IP=string2ip(ip)
        #print IP
        count=(self.last_index-self.first_index)/7+1
        left=0
        right=count
        middle=(right-left)/2+left
        while True:
            if right-left==1:
                #print 'result:%s'%left
                return left
            offset=self.first_index+middle*7
            self.ipdb.seek(offset)
            temp=unpack("I",self.ipdb.read(4))[0]
            #print 'left:%s right:%s middle:%s value:%d' %( left,right,middle,temp  )
            if IP<temp:
                right=middle
            elif IP>temp:
                left=middle
            else:
                return middle
            middle=(right-left)/2+left
    def readpos(self,seek):
        self.ipdb.seek(seek)
        num=self.ipdb.read(3)
        (h,l)=unpack("HB",num)
        return (l<<16)+h

    def find(self,ip):
        ipIndex=self.getIPLocation(ip)
        offset=self.first_index+ipIndex*7+4
        pos_num=self.readpos(offset)
        #print pos_num
        return self.getArea(pos_num+4,True)


    def getString(self,offset):
        self.ipdb.seek(offset)
        result=''
        i=0
        word=unpack("B",self.ipdb.read(1))[0]
        while word!=0:
            i+=1
            word=unpack("B",self.ipdb.read(1))[0]
        self.ipdb.seek(offset)
        result=self.ipdb.read(i)
        #print result
        return result
    def getArea(self,offset,deep):
        self.ipdb.seek(offset)
        area1=''
        area2=''
        str=self.ipdb.read(1)
        firstw=unpack("B",str)[0]
        if firstw==1 and deep:
            return self.getArea(self.readpos(self.ipdb.tell()),True)
        elif firstw==2  and deep:
            area1=self.getArea(self.readpos(self.ipdb.tell()),False)
            area2=self.getArea(offset+4,False)
            return (area1,area2)
        elif firstw==2 and  not deep:
            return self.getArea(self.readpos(offset+1),False)
        else:
            if deep:
                area1=self.getString(self.ipdb.tell()-1)
                area2=self.getString(self.ipdb.tell())
                return (area1,area2)
            else:
                area1=self.getString(self.ipdb.tell()-1)
                return area1
#####################################################
class CS_QZ_RP(threading.Thread):   #测试权重和RP
    def __init__(self,htint):
        threading.Thread.__init__(self)
        self.Ht=htint
        self.tt=IPSearch('QQWry.dat')
        self.sql=Cmysql.mysql_handle()
        self.sql.mysql_open()


    def run(self):
        try:
            print u"----百度权重   PR查询CS_QZ_RP线程%d启动----"%(self.Ht)
            self.SQL_slect("select * from hostIP where baiduQZ is NULL")  #获取数量
            self.SQL_slect("select * from ftppassword3 where baiduQZ is NULL")  #获取数量
            self.SQL_slect("select * from ftppassword3 where PR is NULL")  #获取数量
            #self.SQL_slect("select * from ftppassword3")  #获取数量

            #print self.baidu_qz("www.ws8.org")  #百度权重查询
            #print self.getPr("www.ws8.org")  #rp查询
            #print self.www_IP_QQWry_title("127.0.0.1")   #'IP/地理位置/网站标题
        except:
            print u"----线程%d--百度权重   PR查询CS_QZ_RP---run异常！！！！！----"%(self.Ht)
            time.sleep(60)
            self.run()

    def SQL_slect(self,sql):  #获取数量
        self.i=0
        try:
            print u"测试网站权重--PR开始"
            #sql="select * from ftppassword3"
            self.cursor=self.sql.conn.cursor()
            n = self.cursor.execute(sql)
            self.cursor.scroll(0)
            for row in self.cursor.fetchall():
                data_qz=self.baidu_qz(row[0])  #百度权重查询
                data_pr=self.getPr(row[0])  #rp查询
                www_IP=self.www_IP_QQWry_title(row[0])   #'IP/地理位置/网站标题  #中文无法添加到数据库  #只能只获取IP
                print u"%s网站权重%s网站PR%s---网站信息%s"%(row[0],str(data_qz),str(data_pr),str(www_IP))
                if str(data_qz)=="NO":
                    update="update ftppassword3 set hostIP='%s',PR='%s' where IP='%s'"%(str(www_IP),str(data_pr),row[0])
                    #print update
                else:
                    update="update ftppassword3 set hostIP='%s',baiduQZ='%s',PR='%s' where IP='%s'"%(str(www_IP),str(data_qz),str(data_pr),row[0])
                    #print update
                self.sql.mysql_update(update)
                self.sql.mysql_S()  #保存数据
                time.sleep(20)
            self.cursor.close()
        except:
            time.sleep(4)
            self.sql.mysql_S()  #保存数据
            #self.SQL_slect()     #读取URL
#####################################################
    def www_IP_QQWry_title(self,www):   #'IP/地理位置/网站标题
        data=u""
        try:   #中文无法添加到数据库
            ip=self.www_ping_ip(www)  #ping域名转IP
            data+=str(ip)
#            data+=str(ip)+u"/"
#            dlwz=self.www_ip(ip)  #显示IP地理位置
#            data+=dlwz.decode('utf-8')+u"/"
#            title=self.open_title(www)
#            data+=title.decode('utf-8')
#            #data+=u"%s/%s/%s" % (ip, dlwz.decode('utf-8'),title.decode('utf-8'))
            return data
        except:
            return data

#    def www_ip(self,IP):   #显示IP地理位置
#        try:
#            (area1,area2)=self.tt.find(IP)
#            return "%s-%s"%(area1.decode('gb2312').encode('utf-8'),area2.decode('gb2312').encode('utf-8'))
#        except:
#            return "NO"

    def www_ping_ip(self,WWW):  #域名转IP
        try:
            result = socket.getaddrinfo(WWW, None)
            return result[0][4][0]
        except:
            return "NO"

#    def open_title(self,data):   #获取网站名称
#        try:
#            url="http://"+data
#            sys.getdefaultencoding()
#            #url='http://www.163.com'
#            #s = urllib2.urlopen(url,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
#            req = urllib2.Request(url)
#            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
#            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
#            ss = s.read()
#            #p = re.compile(r'<title>[\s\S]*?</title>')   ##p = re.compile( r'<a>[\s\S]*?</a>' )
#            p = re.compile(r'<\s*/?title\s*>[\s\S]*?<\s*/?title\s*>')
#            sarr = p.findall(ss)#找出一条一条的<a></a>标签
#
#            As=sarr[0]
#            if isinstance(As, unicode):  #判断字符编码
#                #print u"1111中文"
#                return As.decode('utf-8').encode('gb2312')
#            else:
#                #print u"22222中文"
#                return As.decode('gb2312').encode('utf-8')
#
#        except:
#            return u"获取不到网站名称"
#####################################################
    def sockPage(self,url):
        try:
            sockPage = urllib.urlopen(url)
            data = sockPage.read()
            utf8data = data.decode("utf-8")
            return utf8data
        except:
            print u"URL读取失败"
            return "NO4"
##############################################
    def getPr(self,url):
        try:
            self.chinaz = "http://pr.chinaz.com"
            #提交一次，http://pr.chinaz.com/?PRAddress=
            #取得enkey
            data = self.sockPage("%s/?PRAddress=%s"%(self.chinaz,url))
            enkey = self.getEnkey(data)
            #访问查询Pr页
            prHostUrl = "%s/ajaxsync.aspx?at=pr&enkey=%s&url=%s"\
                        % (self.chinaz,enkey,url)
            pageHtml = self.sockPage(prHostUrl)
            #print pageHtml
            #匹配出Pr数值
            patten = re.compile(r'[0-9]')
            pr =  patten.search(pageHtml).group(0)
            return pr
        except:
            print u"=======%sRP查询失败"%(url)
            return "NO3"

    def getEnkey(self,data):
        try:
            enkeyPoit = data.find('enkey')
            enkey =  data[enkeyPoit+6:enkeyPoit+38]
            return enkey
        except:
            return "NO2"
##############################################
    def baidu_qz(self,url):  #百度权重查询
        try:
            dataurl="http://mytool.chinaz.com/baidusort.aspx?host=%s+&sortType=0"%(url)
            pageHtml=self.sockPage(dataurl)
            aadata=u"百度权重为 <font color=\"\">(.*?)</font>"
            patten = re.compile(aadata)
            data=patten.search(pageHtml).group(1)
            return data
        except:
            #print u"=======%s百度权重查询失败"%(url)
            return "NO"
##############################################
if __name__ == "__main__":
    threads = []  #线程
    nthreads=1
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(CS_QZ_RP(i))

    for thread in threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程
