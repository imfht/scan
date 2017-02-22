#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import sys, os, time, httplib
import re
import threading
import gzip,StringIO
from class_Queue import url_exp
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
class class_download(threading.Thread):
    def __init__(self,penurl):
        threading.Thread.__init__(self)
        self.penurl=penurl
        self.url=self.penurl[1].split('//')[1]
        self.past=[]
        self.list_download=[]
        self.open_file(self.url)  #打开TXT文本写入数组
        ###############
        self.pst_download(self.url)
        if len(self.list_download)<=10:
            self.rfid_list() #读取储存
        self.del_list()  #删除数组

    def rfid_list(self):  #读取数组
        try:
            for i in self.list_download:
                #print i
#                EXP_list=[1,self.penurl,"http_download","http_download",i,"","http+download"]
#                #["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","漏洞地址","密码","备注"]7个
#                url_exp.put(EXP_list,0.5)   #插入队列
                EXP_list=[1,self.penurl[0],self.penurl[1],"http_download",i,"",""]
                #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                #print EXP_list
                url_exp.put(EXP_list,0.5)   #插入队列
        except Exception,e:
            print e
            return 0

    def del_list(self):  #删除数组
        try:
            i = 0 #得到list的第一个元素
            while i < len(self.list_download):
                del self.list_download[i]
        except Exception,e:
            print e
            return 0

    def pst_download(self,host):
        try:
            for admin in self.past:
                admin = admin.replace("\n","")
                #print admin
                #admin = "/" + admin
                connection = httplib.HTTPConnection(host,80,timeout=10)
                connection.request("GET",admin)
                response = connection.getresponse()#返回处理后的数据
                #print "%s %s %s" % (admin, response.status, response.reason)
                #/admin-login.php   ,错误404  ，Not Found   /moderator/ 404 File Not Found
                data=response.reason
                #                result=response.getresponse()
                #                print data
                #                print result
                if "OK" in data or "Forbidden" in data:  #302
                    if ('content-encoding', 'gzip') in response.getheaders():
                        compressedstream = StringIO.StringIO(response.read())
                        gzipper = gzip.GzipFile(fileobj=compressedstream)
                        data = gzipper.read()
                    else:
                        data = response.read()

                    if (len(data)>=100):
                        #SQLdata="http://"+host+admin+"---%s %s"%(response.status, response.reason)
                        #print "http://"+host+admin+len(data)+"KB"
                        data="http://%s%s---%dKB"%(host,admin,len(data))
                        #print data
                        self.list_download.append(data)
                else:
                    continue  #跳过
                    #print "H",
                connection.close()
            return 1
        except Exception,e:
            #print e
            return 0

    #生成字典下面
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

    def open_file(self,host):  #遍历文件
        try:
            domain = host   #不明白未什么还要赋值  直接使用host变量不就可以了吗
            sdomain = self.get_sdomain(domain)  #域名拆解www.baidu.com->baidu.com
            ssdomain = self.get_ssdomain(domain)  #域名拆解www.baidu.com->baidu
            p = re.compile( r'25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))' )   #正则是否是IP地址
            passlist = []
            list_passlist=[]
            #合并字典
            doclist = os.listdir(os.getcwd()+r'\download')
            doclist.sort()
            for i in doclist:
                for url in open('download/'+i,'r'):
                    data=url.strip().decode("gbk")
                    passlist.append(data)
                    #print self.list
                    #print len(self.list)

            for i in passlist:  #python 列表去重
                if i not in list_passlist:
                    list_passlist.append(i)

            E = 0 #得到list的第一个元素
            while E < len(list_passlist):
                username=list_passlist[E]
                #%domain%  完整域名 www.baidu.com
                #%sdomain% 域名拆解 baidu.com
                #%ssdomain% 域名拆解 baidu
                if  '%domain%' in username or '%sdomain%' in username or '%ssdomain%' in username:
                    if sdomain=='' in p.findall(domain):
                        continue  #跳过
                    else:
                        username = username.replace('%domain%',domain)  #返回根据正则表达式进行文字替换后的字符串的复制
                        username = username.replace('%sdomain%',sdomain)
                        username = username.replace('%ssdomain%',ssdomain)

                self.past.append(username)  #添加到数组里
                E = E + 1

                #print len(self.past)
        except Exception,e:
            #print e
            return 0

################################################
if __name__=='__main__':
#启动线程控制漏洞扫描
    threads = []  #线程
    list=["http://www.baidu.com","http://127.0.0.1"]
    for i in range(1):
        threads.append(class_download(list))
    for t in threads:
        t.start()



