#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import urllib2
#http://www.hack1990.com/cat_2/1235.html
import re,threading,Queue,os,httplib
import msvcrt
import urllib

def open_url_data(url):  #读取网页内容
    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
        #req.add_header('User-Agent','userAgentIE9')
        #req.add_header('User-Agent', "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)")
        s = urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        return s.read()
    except:
        return 0

if __name__ == "__main__":
    #http://www.syfc.com.cn/fqzj/index.action
    data="cat /etc/passwd"
    print urllib.quote(data.strip())
#cat\40\u002fetc\u002fpasswd


#    html = urllib2.urlopen("http://wifiportal.newbridgenet.com",timeout=10).info()['Server']
#    if 'pache' in html:  #判断是否安装了apache
#        #self.dir(arg)
#        print "安装了apache"
#    else:
#        print '此网站不是apache的网站!'
#    index=["index.action","商城.achtion","shangcheng.achtion",".action","redirect.action"]
#    for i in range(len(index)):
#        print index[i]

################################################





