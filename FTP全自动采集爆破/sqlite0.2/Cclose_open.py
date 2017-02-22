#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##################################################
#结束进程  在从新开启进程
import time
import threading
import ConfigParser  #INI读取数据
import os

class CS_close_open(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        config = ConfigParser.ConfigParser()
        config.readfp(open("gost.ini"))
        self.close_open = int(config.get("DATA","close_open"))
        #self.data=__file__  #完整路径
        #self.run()

    def run(self):
        try:
            print u"结束进程  在从新开启进程----线程启动\r\n"
            for i in range(self.close_open):
                time.sleep(60)
                delete=u"#################程序已经启动%d分钟#################"%(i)
                print delete
                if i>=self.close_open-1:
                    print u"重启程序本身"
                    data2=os.getcwd() #当前目录
                    data2="%s\\main.exe"%(data2)
                    print data2
                    #data=__file__  #完整路径
#                    nPos = self.data.rfind('/') #查找字符
#                    L_1=len(self.data)
#                    sStr1 = self.data[nPos+1:L_1] #复制指定长度的字符
#                    print sStr1
#                    print self.data
                    os.system('close_open.exe main.exe %s'%(data2))
                    #os.system('close_open.exe VStart.exe C:\Users\Administrator.PC-20130126ZMFE\Desktop\cs1111111111111\close_open\Debug')
                    break     #在需要时终止for循环
        except:
            time.sleep(60)
            self.run()



if __name__=='__main__':
    threads = []  #线程
    nthreads=1
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(CS_linkftp())

    for thread in threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程



