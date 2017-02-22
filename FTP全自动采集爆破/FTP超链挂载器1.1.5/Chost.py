#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##################################################
from struct import *
import urllib2
import string
import re
import sys
import socket
#reload(sys)
#sys.setdefaultencoding('utf-8')
#bg2312
#gb2312
#utf8
#gbk
def ip2string( ip ):
    a = (ip & 0xff000000) >> 24
    b = (ip & 0x00ff0000) >> 16
    c = (ip & 0x0000ff00) >> 8
    d = ip & 0x000000ff
    return "%d.%d.%d.%d" % (a,b,c,d)

def string2ip( str ):
    ss = string.split(str, '.');
    ip = 0L
    for s in ss: ip = (ip << 8) + string.atoi(s)
    return ip;

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

class C_hoset():
    def __init__(self):
        self.tt=IPSearch('QQWry.dat')

    def www_data(self,www):   #'IP/地理位置/网站标题'
        data=u""
        try:
            ip=self.www_ping_ip(www)  #ping域名转IP
            data+=str(ip)+u"/"
            dlwz=self.www_ip(ip)  #显示IP地理位置
            data+=dlwz.decode('utf-8')+u"/"
            title=self.open_title(www)
            data+=title.decode('utf-8')
            #data+=u"%s/%s/%s" % (ip, dlwz.decode('utf-8'),title.decode('utf-8'))
            return data
        except:
            return data

    def www_ip(self,IP):   #显示IP地理位置
        try:
            (area1,area2)=self.tt.find(IP)
            return "%s-%s"%(area1.decode('gb2312').encode('utf-8'),area2.decode('gb2312').encode('utf-8'))
        except:
            return 0

    def www_ping_ip(self,WWW):  #域名转IP
        try:
            result = socket.getaddrinfo(WWW, None)
            return result[0][4][0]
        except:
            return 0

#    def www_ping_ip(self,www):  #ping域名转IP
#        try:
#            #patt = re.compile('\d+.\d+.\d+.\d+')
#            return re.findall("\[(.+?)\]",os.popen('ping '+www+' -l 1 -n 1').read())
#        except:
#            #return 0
#            return u"转换IP失败"

    def open_title(self,data):   #获取网站名称
        try:
            url="http://"+data
            sys.getdefaultencoding()
            #url='http://www.163.com'
            s = urllib2.urlopen(url,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            ss = s.read()
            #p = re.compile(r'<title>[\s\S]*?</title>')   ##p = re.compile( r'<a>[\s\S]*?</a>' )
            p = re.compile(r'<\s*/?title\s*>[\s\S]*?<\s*/?title\s*>')
            sarr = p.findall(ss)#找出一条一条的<a></a>标签

            As=sarr[0]
            if isinstance(As, unicode):  #判断字符编码
                #print u"1111中文"
                return As.decode('utf-8').encode('gb2312')
            else:
                #print u"22222中文"
                return As.decode('gb2312').encode('utf-8')

        except:
            return u"获取不到网站名称"

if __name__=='__main__':
    h=C_hoset()
    data=h.www_data('www.baidu.com')   #'IP/地理位置/网站标题'
    print data   #'IP/地理位置/网站标题'


