#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import Queue
import time
import socket
from ftplib import FTP
socket.setdefaulttimeout(10)
import sys
ftp_url = Queue.Queue()  #开放FTP的URL
import SlinkFTP  #开始破解FTP
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

def add_Queue(TXT_file):  #添加到消息队列
    try:
        list=[]
        list_2=[]
        xxx = file(TXT_file,'r')
        for xxx_line in xxx.readlines():  #读取数据
            #如果输入的内容读取有回车符号，可以用strip来消除，可得到完美的输出
            data=xxx_line.strip()
            list.append(data)  #添加数据

        for i in list:  #去重重复数据
            if i not in list_2:
                list_2.append(i)

        for i in list_2:  #添加到数组
            if "http" in i:
                print u"请不要带上 http://-----%s"%(i)
                time.sleep(0.5)
                continue  #跳过
            if  open_ftp(i):
                print "ftp==ok==%s"%(i)
                ftp_url.put(i,0.3)   #插入队列
            else:
                print "ftp==no==%s"%(i)

        print u"共%s条开放FTP的"%(ftp_url.qsize())
    except Exception,e:
        print e
        return 0

##############################################################################################
if __name__ == "__main__":
    print u"       落雪QQ:2602159946"
    print u"结果保存在目录下   ftp.txt"
    print u"\r\n参数   主程序名 URL列表 线程数   "
    print u"参数   main.exe url.txt 20   "
    if len(sys.argv) < 2:
        print u"无参数传入   \r\n软件使用bat方法   main.exe url.txt 20   "
        time.sleep(300)
        sys.exit()
    argv1=sys.argv[1]
    add_Queue(str(argv1))  #添加到消息队列
    time.sleep(1)  #把数据都读取出来
    #开始破解FTP
    ClinkFTP_threads = []  #线程
    argv2=sys.argv[2]
    for i in range(int(argv2)):  #nthreads=10  创建10个线程
        ClinkFTP_threads.append(SlinkFTP.CS_linkftp(i,ftp_url))
    for t2 in ClinkFTP_threads:   #不理解这是什么意思    是结束线程吗
        time.sleep(1)  #把数据都读取出来
        t2.start()  #start就是开始线程





