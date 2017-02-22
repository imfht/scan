#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import time
import socket
from ftplib import FTP
socket.setdefaulttimeout(10)
import sys
def open_ftp(host):  #查看FTP是否开放
    ftp=FTP()
    try:
        ftp.connect(host,21) #连接
        #ftp.quit() #退出ftp服务器
        return 1
    except:
        try:
            ftp.quit() #退出ftp服务器
        except:
            ftp.close()
        return 0

def TXT_file(data):  #写入文本
    try:
        #file_nem=time.strftime('%Y.%m.%d')   #file_nem+".txt"
        file_object = open("open_ftp.txt",'a+')
        #file_object.write(list_passwed[E])
        file_object.writelines(data)
        file_object.writelines("\n")
        file_object.close()
    except Exception,e:
        print "ftp.txt except",e
        return 0

def add_Queue(name_file):  #添加到消息队列
    try:
        list=[]
        list_2=[]
        xxx = file(name_file,'r')
        for xxx_line in xxx.readlines():  #读取数据
            #如果输入的内容读取有回车符号，可以用strip来消除，可得到完美的输出
            list.append(xxx_line.strip())  #添加数据

        for i in list:  #去重重复数据
            if i not in list_2:
                list_2.append(i)

        for i in list_2:  #添加到数组
            try:
                if "http" in i:
                    print u"请不要带上 http://-----%s"%(i)
                    time.sleep(0.5)
                    continue  #跳过
                if  open_ftp(i):
                    print "ftp==ok==%s"%(i)
                    TXT_file(i)  #写入文本
                    #ftp_url.put(i,0.3)   #插入队列
                else:
                    print "ftp==no==%s"%(i)
            except Exception,e:
                pass
    except Exception,e:
        print e
        return 0

##############################################################################################
if __name__ == "__main__":
#    if len(sys.argv) < 1:
#        print u"无参数传入   \r\n软件使用bat方法   main.exe url.txt 20   "
#        time.sleep(300)
#        sys.exit()
    argv1=sys.argv[1]
    print argv1
    add_Queue(str(argv1))  #添加到消息队列