#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import urllib2
def URL_TQURL(data): #URL提取URL
        data +="/"      #data ="https://www.baidu.com/cache/sethelp/index.html"
        if ~data.find("http://"):  #~取反
            data=data[7:] #字符串删除
            nPos = data.index('/') #查找字符        #print nPos
            sStr1 = data[0:nPos] #复制指定长度的字符
            return sStr1



print URL_TQURL("http://cache.baiducontent.com/c?m=9f65cb4a8c8507ed4fece7631053843a4c15da30608286522f898448e42f0b0b102ef4bb50734d5bced1393a41f9464b9b8621063d1421c78cb9835daccf85295f9f5730676d805662d30edcc0&p=9a3dc54ad6c34ab90be296381e4a8f&newp=882a9545dd9e18b90dfed52d02149e231610db2151d0db4826c2c65bd2&user=baidu&fm=sc&query=D:\PyCharm%202.6.1\binF8%C9%CF%B6%C4%B2%A9&qid=&p1=10")