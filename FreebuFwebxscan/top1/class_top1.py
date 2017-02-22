#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import urllib
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import urllib2, re, time
import urllib
import socket
import threading
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
from ctypes import *
user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
#user32.MessageBoxW(0,c_wchar_p("1111111"), c_wchar_p("QQ:23456789"), 0)   # 调用MessageBoxA函数
class top1(object):
    def __init__(self,ui):
        self.ui=ui

    def initdlalig(self):
        ###################
        self.tab1_treeWidget_1_count() #设置tableView属性  行数
        ###################
    def tab1_treeWidget_1_count(self):  #设置tableView属性  行数
        try:
            self.ui.tab1_treeWidget_1.setColumnCount(0) #设置TreeWidget的列数
            self.ui.tab1_treeWidget_1.setHeaderLabels([u'URL/域名',u'可疑/路径/文件',u'文件大小'])
            self.ui.tab1_treeWidget_1.setColumnWidth(0,200) #第一列宽设为200
            self.ui.tab1_treeWidget_1.setColumnWidth(1,370) #第一列宽设为200
            self.ui.tab1_treeWidget_1.setColumnWidth(2,60) #第一列宽设为200
        except BaseException, e:
            print(str(e))
            pass

#    #添加数据
#    def tab1_treeWidget_1_add(self,Aroot,s0,s1,s2):  #添加数据
#        try:
#            #self.tab1_treeWidget_1_add(root,"1111","2222","33333")  #添加数据
#            if not s0==None:
#                child1 = QTreeWidgetItem(Aroot)
#                child1.setText(0,s0)
#                child1.setText(1,s1)
#                child1.setText(2,s2)
#            #self.ui.tab1_treeWidget_1.addTopLevelItem(Aroot)
#            #self.ui.setCentralWidget(Aroot)
#            Aroot.addChild(Aroot) #添加子节点
#            Aroot.setExpanded(1) #展开子项
#        except BaseException, e:
#            print(str(e))
#            pass
    ###################################################
    def tab1_Button_1(self):  #导入URL
        try:
#            root= QTreeWidgetItem(self.ui.tab1_treeWidget_1)
#            root.setText(0,"HTTP://WWW.126.COM")
#            self.tab1_treeWidget_1_add(root,"NULL",None,None)  #添加数据
#            #self.tab1_treeWidget_1_add(root,"HTTP://WWW.126.COM",None,None)  #添加数据
#            #self.tab1_treeWidget_1_add(root,"HTTP://WWW.163.COM",None,None)  #添加数据

            #self.ui.tab1_Box_1.text()  #获取线程数
            self.tab1_treeWidget_1_count() #设置tableView属性  行数
            # 1表示打开文件对话框   0表示保存
            dlg = win32ui.CreateFileDialog(1, "*.txt", None, 0, u"txt 文本 (*.txt)|*.txt|All files|*.*")
            #dlg.SetOFNInitialDir('E:/Python') # 设置打开文件对话框中的初始显示目录
            dlg.DoModal()
            filename = dlg.GetPathName() # 获取选择的文件名称

            TX=len(open(filename,'rU').readlines())/5
            if TX==0:
                TX=1
            if TX>=30:
                TX=30
            self.ui.tab1_Box_1.setValue(TX) #设置线程值

            xxx = file(filename, 'r')

            for xxx_line in xxx.readlines():
                try:
                    root= QTreeWidgetItem(self.ui.tab1_treeWidget_1)
                    data=xxx_line.strip().lstrip().rstrip('\n')
                    if len(data)>=3:
                        if "http" in data:
                            root.setText(0,data)
                        else:
                            root.setText(0,"http://"+data)

                        #self.tab1_treeWidget_1_add(root,None,None,None)  #添加数据
                        root.addChild(root) #添加子节点
                except BaseException, e:
                    print(str(e))
        except:
            pass
#QTreeWidgetItem *pChildNode = new QTreeWidgetItem(QStringList(QString("ChildNext"))); //添加子节点
#this->currentItem()->parent()->insertChild(this->currentItem()->parent()->indexOfChild(this->currentItem())+1, pChildNode);

    def tab3_Button_2(self): #导出扫描结果 tab1_Button_2
        try: #data=[self.URL,"http_download",i]
            # 1表示打开文件对话框   0表示保存
            dlg = win32ui.CreateFileDialog(0, "*.txt", None, 0, u"txt 文本 (*.txt)|*.txt|All files|*.*")
            #dlg.SetOFNInitialDir('E:/Python') # 设置打开文件对话框中的初始显示目录
            dlg.DoModal()
            filename = dlg.GetPathName() # 获取选择的文件名称
            it = QTreeWidgetItemIterator(self.ui.tab1_treeWidget_1)
            data=""
            while it.value():
                v = it.value()
                s0=v.text(0)
                if not s0=="":
                    data+=s0
                s1=v.text(1)
                if not s1=="":
                    data+="|"+s1
                s2=v.text(2)
                if not s2=="":
                    data+="|"+s2
                data+="\n"
                it += 1
            #print data
            file_object = open(filename,'a')
            #file_object.write(list_passwed[E])
            file_object.writelines(data)
            file_object.close()
        except:
            pass


    def tab3_Button_3(self): #开始测试 tab3_Button_3
#        ==data== ['http://www.anzhuo.com', 'http_200', u'http://www.anzhuo.com/admin/admin.php|861KB']
#        data=[u"http://goldhao.com",u"http_200",u"http://goldhao.com/123123.rar|1234KB"]
#        self.treeWidget_add(data)    #添加子项
        try:
            it = QTreeWidgetItemIterator(self.ui.tab1_treeWidget_1)
            while it.value():
                v = it.value().text(0)
                Class_download.openurl.put(str(v),0.5)   #插入队列
                Class_http_200.openurl.put(str(v),0.5)   #插入队列
                it += 1

            T_X=self.ui.tab1_Box_1.text()  #获取线程数
            thread.start_new_thread(self.download,(T_X,))  #开启线程
            thread.start_new_thread(self.http_200,(T_X,))  #开启线程
            self.ui.tab1_Button_3.setEnabled(0)  #给改成禁用
            self.ui.tab1_Box_1.setEnabled(0)  #给改成禁用
        except:
            pass

    def messagebox(self,data):
        try:
            self.ui.messagebox.append(data)
        except:
            pass

    def treeWidget_add(self,data):    #添加子项  多线程向这个里面添加会出问题
#        Abool=1
        try: #data=[self.URL,"http_download",i]
            #['http://goldhao.com', 'http_download', u'http://goldhao.com/www.rar|611KB']
#            while Abool:
#                Abool=0
            it = QTreeWidgetItemIterator(self.ui.tab1_treeWidget_1)
            while it.value():
                v = it.value()
                if data[0] in v.text(0):
                    child1 = QTreeWidgetItem(v)
                    child1.setText(0,data[1])
                    Adata=data[2].split("|")
                    child1.setText(1,Adata[0])
                    child1.setText(2,Adata[1])

                    child1.addChild(child1) #添加子节点
                    child1.setExpanded(1) #展开子项
                it += 1
        except:
            pass

    def http_200(self,T_X):
        try:
            #后台测试
            threadsA = []  #线程  下载测试
            for i in range(int(T_X)):  #nthreads=10  创建10个线程 int(T_X)
                threadsA.append(Class_http_200.class_http_200(i))
            for t in threadsA:   #不理解这是什么意思    是结束线程吗
                t.start()  #start就是开始线程

            while 1:
                time.sleep(random.randint(1, 8))
                h1=Class_http_200.messagebox.qsize()
                if int(h1)>=1:
                    #消息提示
                    for i in range(h1):
                        msg = Class_http_200.messagebox.get(0.5)  #get()方法从队头删除并返回一个项目
                        if not msg=="":
                            self.messagebox(msg)
                            time.sleep(0.1)

                #添加数据
                if Class_http_200.url_exp.empty():   #判断队列是否为空
                    continue #跳过
                M2=Class_http_200.url_exp.qsize()
                if int(M2)>=1:
                    for i in range(M2):
                        URL2 = Class_http_200.url_exp.get(0.5)  #get()方法从队头删除并返回一个项目
                        if not URL2=="":
                            print "http_200",URL2
                            self.treeWidget_add(URL2)    #添加子项
                            time.sleep(0.1)
        except:
            pass

    def download(self,T_X):
        try:
            threads = []  #线程  下载测试
            for i in range(int(T_X)):  #nthreads=10  创建10个线程 int(T_X)
                threads.append(Class_download.class_download(i))
            for t in threads:   #不理解这是什么意思    是结束线程吗
                t.start()  #start就是开始线程

            while 1:
                time.sleep(random.randint(1, 8))
                if Class_download.openurl.empty() and Class_http_200.openurl.empty():   #判断队列是否为空
                    self.ui.tab1_Button_3.setEnabled(1)  #给改成禁用
                    self.ui.tab1_Box_1.setEnabled(1)  #给改成禁用
                    #return 0
                #消息提示
                h=Class_download.messagebox.qsize()
                if int(h)>=1:
                    for i in range(h):
                        msg = Class_download.messagebox.get(0.5)  #get()方法从队头删除并返回一个项目
                        if not msg=="":
                            self.messagebox(msg)
                            time.sleep(0.01)

                #添加数据
                if Class_download.url_exp.empty():   #判断队列是否为空
                    continue #跳过
                M1=Class_download.url_exp.qsize()
                if int(M1)>=1:
                    for i in range(M1):
                        URL = Class_download.url_exp.get(0.5)  #get()方法从队头删除并返回一个项目
                        if not URL=="":
                            print "download",URL
                            self.treeWidget_add(URL)    #添加子项
                            time.sleep(0.01)
        except:
            pass

    def tab1_Button_4(self): #导入C段/旁站/\n二级/域名结果   tab1_Button_4
        try:
            self.tab1_treeWidget_1_count() #设置tableView属性  行数
            int_View=self.ui.tab3_tableView_1.model().rowCount()   #获取共多少行

            TX=int(int_View)/5
            if TX==0:
                TX=1
            if TX>=30:
                TX=30
            self.ui.tab1_Box_1.setValue(TX) #设置线程值

            model = self.ui.tab3_tableView_1.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
            for index in range(int_View):
                s1= model.data(model.index(index,1)).toString()
                root= QTreeWidgetItem(self.ui.tab1_treeWidget_1)
                if len(s1)>=3:
                    if "http" in s1:
                        root.setText(0,s1)
                    else:
                        root.setText(0,"http://"+s1)
                root.addChild(root) #添加子节点
            self.ui.messagebox.append(u"导入C段/旁站/二级/域名结果%d条"%len(range(int_View)))
        except:
            pass

import random   #抽取随机数
import thread
import win32ui
import Class_download  #下载测试
import Class_http_200 #文件测试
#//改变文本背景的颜色也是一样的效果
#ui->treeWidget->currentItem()->setBackgroundColor(0, Qt::green);
#ui->treeWidget->currentItem()->setBackgroundColor(1, Qt::red);