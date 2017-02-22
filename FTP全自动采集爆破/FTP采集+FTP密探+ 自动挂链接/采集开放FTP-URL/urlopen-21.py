#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#qq 29295842
import urllib2, re, time
import sys
import thread
import threading
import list
import Queue
Aopenurl = Queue.Queue(6000) #要采集的URL
openftp = Queue.Queue(4000)
from ftplib import FTP

class CS_openurl(threading.Thread):
    def __init__(self,htint,Aopenurl,openftp):
        threading.Thread.__init__(self)
        self.Ht=htint
        self.Aopenurl=Aopenurl  #要采集的URL
        self.openftp=openftp
        self.NO_url =".cn.gov"
        self.NO_url_list=self.NO_url.split('.')

    def TXT_file(self,data):  #写入文本
        try:
            file_nem=time.strftime('%Y.%m.%d')
            file_object = open(file_nem+".txt",'a')
            #file_object.write(list_passwed[E])
            file_object.writelines("\n")
            file_object.writelines(data)
            file_object.close()
        except:
            print u"Thread:%d---TXT_file  %s写入异常-try--except!!!!!"%(self.Ht,data)
            return 0

    def run(self):
        try:
            print "----------------------------------------------------------"
            print "Aopenurl---------6000--------%s"%(self.Aopenurl.qsize())
            print "openftp----------200---------%s"%(self.openftp.qsize())
            int_FTP=self.openftp.qsize()
            if int_FTP>=200:
                for i in range(int_FTP):
                    url=self.openftp.get(0.1)  #get()方法从队头删除并返回一个项目
                    if str(url)=="":
                        break
                    self.TXT_file(str(url))  #写入文本
                    time.sleep(0.1)

            if self.Aopenurl.qsize()>=5000:
                print u"Thread:%d--CS_openurl- Aopenurl 消息队列大于>=5000"%(self.Ht)
                for i in range(50):  #如果消息队列满了 采集会停止    取出来一点让采集还能继续   只是减慢速度而已
                    self.Aopenurl.get(0.2)
                    time.sleep(0.1)
                time.sleep(5)
                self.run()

            if self.Aopenurl.full(): #如果队列满了   就停止下
                print u"Thread:%d--CS_openurl-data Aopenurl 队列为空"%(self.Ht)
                for i in range(50):  #如果消息队列满了 采集会停止    取出来一点让采集还能继续   只是减慢速度而已
                    self.Aopenurl.get(0.2)
                    time.sleep(1)
                time.sleep(10)
                self.run()
            if self.Aopenurl.empty():   #判断队列是否为空
                print u"Thread:%d--CS_openurl-data Aopenurl 队列为空"%(self.Ht)
                time.sleep(20)
                self.run()
            self.Chost = self.Aopenurl.get(0.5)  #get()方法从队头删除并返回一个项目
            if self.Chost=="":
                time.sleep(20)
                self.run()
                #self.Chost="127.0.0.1"
            #print "Thread:%d-CS_openurl-CS-url:http://%s-run"%(self.Ht,self.Chost)
            self.URL_DZ("http://"+self.Chost) #遍历页里的地址

            self.run()
        except:
            print u"Thread:%d--CS_openurl---run-异常-try--except!!!!!"%(self.Ht)
            time.sleep(10)
            self.run()

    ####################################################################
    def URL_STR(self,data):#判断是否是HTTP字符
        try:
            sStr2 = 'http://'
            sStr3 = 'https://'
            if data.find(sStr2) and data.find(sStr3):
                return 1 #print "没有找到"
            else:
                return 0 #print "查找到了"
        except:
            return 1

    def URL_TQURL(self,data): #URL提取URL
        try:
            data +="/"      #data ="https://www.baidu.com/cache/sethelp/index.html"
            if ~data.find("http://"):  #~取反
                data=data[7:] #字符串删除
                nPos = data.index('/') #查找字符        #print nPos
                sStr1 = data[0:nPos] #复制指定长度的字符
                return sStr1

            if ~data.find("https://"):  #~取反
                data=data[8:] #字符串删除
                nPos = data.index('/') #查找字符
                #print nPos
                sStr1 = data[0:nPos] #复制指定长度的字符
                return sStr1
        except:
            print "Thread:%d-CS_openurl-Extract URL:%s URL error"%\
                  (self.Ht,data)

    def URL_DZ(self,URL):  #遍历页里的地址
        try:
            LS = list.Clist()  #初始化类
            LS.list_del()  #清空list列表
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            ss = s.read()
            p = re.compile( r'<a.+?href=.+?>.+?</a>' )
            pname = re.compile( r'(?<=>).*?(?=</a>)' )
            phref = re.compile( r'(?<=href\=\").*?(?=\")')
            #构造及编译正则表达式
            sarr = p.findall(ss)#找出一条一条的<a></a>标签   #这添加到数组在过滤重复值减少mysql压力

            i=0
            for every in sarr:
                if i>=3000:
                    print u"Thread:%d-CS_openurl-URL:%s-提取URL>=3000 URL\n"%\
                          (self.Ht,URL)
                    break
                else:
                    i+=1
                sname = pname.findall( every )
                if sname:
                    #sname = sname[0]
                    shref = phref.findall( every )
                    if shref:
                        shref = shref[0]
                        #print shref #获取URL
                        if ~self.URL_STR(shref):
                            a1=self.URL_TQURL(shref) #URL提取URL
                            LS.liet_add(a1)  #添加到数组

            LS.liet_lsqc() #数组列表去重复
            time.sleep(0.3)
            E = 0 #得到list的第一个元素
            while E < len(LS.list_2):
                #print LS.list_2[E]
                E = E + 1
                if not self.CS_YM(LS.list_2[E]):  #域名排除异常
                    #print "Thread:%d--CS_openurl--%s  no add"%(self.Ht,LS.list_2[E])
                    continue #进入下一次环
                if ~self.Aopenurl.full(): #如果队列满了  取反
                    self.Aopenurl.put(LS.list_2[E],0.1)
                try:
                    thread.start_new_thread(self.host_ftp,(LS.list_2[E],))
                    time.sleep(0.1) #确保先运行Seeker中的方法
                except BaseException, e:
                    print(str(e))
                    return 0

           # print "Thread:%d-CS_openurl-cjURL:%s-yURL:%d-qdcfURL:%d-time:%s"%\
           #       (self.Ht,URL,len(LS.list),len(LS.list_2),time.strftime('%Y.%m.%d-%H.%M.%S'))
            self.run()  #读取URL
            # 上面是将每条<a></a>里面的内容和地址给匹配出来
        except:
            #print "--Thread:%d--CS_openurl-url:%s--try--except!!--"%(self.Ht,URL)
            time.sleep(2)
            self.run()

    def CS_YM(self,data):  #域名排除异常
        try:
            self.AE = 1 #得到list的第一个元素
            while self.AE < len(self.NO_url_list):
                #print "1111",list[E]
                if not data.find("."+self.NO_url_list[self.AE])==-1:
                    return 0
                self.AE +=1
            return 1
        except:
            #print u"域名排除异常"
            return 1

#    def TXT_file(self,data):  #写入文本
#        try:
#            file_nem=time.strftime('%Y.%m.%d')
#            file_object = open(file_nem+".txt",'a')
#            #file_object.write(list_passwed[E])
#            file_object.writelines("\n")
#            file_object.writelines(data)
#            file_object.close()
#        except:
#            print "Thread:%d--C_ftppassword---TXT_file-try--except!!!!!"%(self.Ht)
#            return 0

    def host_ftp(self,host):  #测试URL FTP是否开放
        try:

            if host =="":  #传入值等于空   返回
                #print u"传入地址不能为空"
                return 0

            ftpB = FTP()  #初始化FTP类
            ftpB.connect(host,21)  #连接 服务器名  端口号
            ftpB.quit() #退出ftp服务器
            #print host
            self.openftp.put(host,0.1)
            print "open FTP---%s"%(host)

        except:
            return 0
###############################################################
if __name__=="__main__":
    url=sys.argv[1]
    #url= "www.hao123.com"
    print "----BY:www.hmhacker.org----"
    print "QQ:1045985095"
    print "urlopen-21.exe www.xxxxxxx.com"
    if url=="":
        url= "51.la"
        time.sleep(200)

    threads = []  #线程
    nthreads=10
    Aopenurl.put(url,1)   #插入队列
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(CS_openurl(i,Aopenurl,openftp))

    for t in threads:   #不理解这是什么意思    是结束线程吗
        time.sleep(4)
        t.start()  #start就是开始线程




