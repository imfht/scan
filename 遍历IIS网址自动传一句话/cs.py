#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import urllib2
def post(URL):   #提交数据
    try:
        req = urllib2.Request(URL)
        req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
        s = urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        #ss = s.read()
    except Exception,e:
        print e
        return 0


if __name__ == "__main__":
    a1="http://127.0.0.1:8888/webshell.php"
    data="2222222222222222222222222"
    url="%s?shell=%s"%(a1,data)
    post(url)


