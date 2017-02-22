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
class top2(object):
    def __init__(self,ui):
        self.ui=ui

    def initdlalig(self):
        ###################
        self.tab2_tableView_count(0) #设置tableView属性  行数
        ###################
    def tab2_tableView_count(self,h):  #设置tableView属性  行数
        try:
            self.model = QStandardItemModel()
            self.model.setColumnCount(3)     #列
            self.model.setRowCount(h)  #行  len(node)

            self.model.setHorizontalHeaderLabels([u'域名',u'CMS指纹',u'指纹详细地址',u'IP/物理位置/title网站标题'])
            self.ui.tab2_tableView_1.setModel(self.model)

            #self.tableView.resizeColumnsToContents()   #由内容调整列
            self.ui.tab2_tableView_1.setColumnWidth(0,180)  #设置表格的各列的宽度值
            self.ui.tab2_tableView_1.setColumnWidth(1,70)  #设置表格的各列的宽度值
            self.ui.tab2_tableView_1.setColumnWidth(2,150)  #设置表格的各列的宽度值
            self.ui.tab2_tableView_1.setColumnWidth(3,290)  #设置表格的各列的宽度值
            for i in range(h):  #调整行高度  len(node)
                self.ui.tab2_tableView_1.setRowHeight(i, 20)

            self.ui.tab2_tableView_1.setEditTriggers(QTableWidget.NoEditTriggers)  #设置表格的单元为只读属性，即不能编辑
            self.ui.tab2_tableView_1.setSelectionBehavior(QTableWidget.SelectRows) #点击选择是选择行//设置选中时为整行选中
            self.ui.tab2_tableView_1.setSelectionMode(QTableWidget.SingleSelection)  #禁止多行选择
            self.ui.tab2_tableView_1.setAlternatingRowColors(True)  #还是只可以选择单行（单列）
            #self.tableView.verticalHeader().hide() #隐藏行头
        except BaseException, e:
            print(str(e))
            pass

    #添加数据
    def tab2_tableView1_add(self,ints,s0,s1,s2,s3):  #添加数据
        try:
            if not s0==None:
                self.model.setItem(ints, 0, QStandardItem(s0))
            if not s1==None:
                self.model.setItem(ints, 1, QStandardItem(s1))
            if not s2==None:
                self.model.setItem(ints, 2, QStandardItem(s2))
            if not s3==None:
                self.model.setItem(ints, 3, QStandardItem(s3))
            self.ui.tab2_tableView_1.setModel(self.model)
        except BaseException, e:
            print(str(e))
            pass
    ###################################################
    def tab2_Button_1(self):  #导入URL
        try:
            self.tab2_tableView_count(0) #设置tableView属性  行数
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
            self.ui.tab2_spinBox_1.setValue(TX) #设置线程值

            xxx = file(filename, 'r')
            i=0
            for xxx_line in xxx.readlines():
                try:
                    data=xxx_line.strip().lstrip().rstrip('\n')
                    if len(data)>=3:
                        if "http" in data:
                            self.tab2_tableView1_add(i,data,None,None,None)  #添加数据
                        else:
                            self.tab2_tableView1_add(i,"http://"+data,None,None,None)  #添加数据
                except BaseException, e:
                    print(str(e))
                i+=1
        except:
            pass

    def cms(self): #CMS指纹识别
        try:
            T_X=self.ui.tab2_spinBox_1.text()  #获取线程数
            int_View=self.ui.tab2_tableView_1.model().rowCount()   #获取共多少行
            model = self.ui.tab2_tableView_1.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
            for index in range(int_View):
                s0= model.data(model.index(index,0)).toString()
                Class_cms.openurl.put(str(s0),0.5)   #插入队列

            threads = []  #线程
            for i in range(int(T_X)):  #nthreads=10  创建10个线程 int(T_X)
                threads.append(Class_cms.Class_cms(i))

            for t in threads:   #不理解这是什么意思    是结束线程吗
                t.start()  #start就是开始线程

            while 1:
                time.sleep(0.5)
                if Class_cms.openurl.empty():   #判断队列是否为空
                    self.ui.tab2_Button_3.setEnabled(1)  #给改成禁用
                    self.ui.tab2_spinBox_1.setEnabled(1)  #给改成禁用
                    #return 0

                h=Class_cms.messagebox.qsize()
                if int(h)>=1:
                    for i in range(h):
                        msg = Class_cms.messagebox.get(0.5)  #get()方法从队头删除并返回一个项目
                        if not msg=="":
                            self.ui.messagebox.append(msg)
                            time.sleep(0.01)

                if Class_cms.url_exp.empty():   #判断队列是否为空
                    continue #跳过
                URL = Class_cms.url_exp.get(0.5)  #get()方法从队头删除并返回一个项目
                if not URL=="":
                    #域名--CMS指纹--指纹详细地址
                    #data=[self.URL,i[1],i[0]]
                    int_View=self.ui.tab2_tableView_1.model().rowCount()   #获取共多少行
                    model = self.ui.tab2_tableView_1.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
                    for index in range(int_View):
                        s0= model.data(model.index(index,0)).toString()
                        if URL[1]=="t":  #垃圾数据
                            continue  #跳过   这一次
                        if URL[0] in s0:
                            self.tab2_tableView1_add(index,None,URL[1],URL[2],None)  #添加数据
                            self.ui.messagebox.append(u"域名%s--CMS指纹%s--指纹详细地址%s"%(URL[0],URL[1],URL[2]))
                            URL="http://webxscan.com/cms.php?url=%s&cms=%s"%(URL[0],URL[1])
                            self.url_post(URL)   #后门

        except:
            pass

    def url_post(self,URL):  #收集CMS
        try:
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            #urllib2.urlopen(URL,timeout=20)  # 后门POST提交   超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            #time.sleep(1)
        except:
            #print "Thread:%d--C_ftppassword--http-POST-Failure"%(self.Ht)
            return 0

    def tab2_Button_3(self): #开始CMS识别
        try:
            thread.start_new_thread(self.cms,())  #开启线程

            self.ui.tab2_Button_3.setEnabled(0)  #给改成禁用
            self.ui.tab2_spinBox_1.setEnabled(0)  #给改成禁用
        except:
            self.ui.tab2_Button_3.setEnabled(1)  #给改成禁用
            self.ui.tab2_spinBox_1.setEnabled(1)  #给改成禁用
            pass

    def IP_WLWZ_title(self): #'IP/地理位置/网站标题'
        try:
            h=qqwry.C_hoset()
            int_View=self.ui.tab2_tableView_1.model().rowCount()   #获取共多少行
            model = self.ui.tab2_tableView_1.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
            for index in range(int_View):
                s0= model.data(model.index(index,0)).toString()
                data=h.www_data(qqwry.url_www(str(s0)))   #'IP/地理位置/网站标题'
                self.tab2_tableView1_add(index,None,None,None,data)  #添加数据
            self.ui.tab2_Button_4.setEnabled(1)  #给改成禁用
        except:
            pass

    def tab2_Button_4(self): #显示IP和标题 tab2_Button_4
        try:
            thread.start_new_thread(self.IP_WLWZ_title,())  #开启线程
            self.ui.tab2_Button_4.setEnabled(0)  #给改成禁用
        except:
            self.ui.tab2_Button_4.setEnabled(1)  #给改成禁用
            pass

    def tab2_Button_2(self): #导出URL列表 tab2_Button_2
        try:
            # 1表示打开文件对话框   0表示保存
            dlg = win32ui.CreateFileDialog(0, "*.txt", None, 0, u"txt 文本 (*.txt)|*.txt|All files|*.*")
            #dlg.SetOFNInitialDir('E:/Python') # 设置打开文件对话框中的初始显示目录
            dlg.DoModal()
            filename = dlg.GetPathName() # 获取选择的文件名称
            data=""
            int_View=self.ui.tab2_tableView_1.model().rowCount()   #获取共多少行
            model = self.ui.tab2_tableView_1.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
            for index in range(int_View):
                s0= model.data(model.index(index,0)).toString()
                data +=s0
                s1= model.data(model.index(index,1)).toString()
                if not s1=="":
                    data +="|"+s1
                data +="\n"
            file_object = open(filename,'a')
            #file_object.write(list_passwed[E])
            file_object.writelines(data)
            file_object.close()
            #查看PYQT保存文件如何做
            #user32.MessageBoxW(0,c_wchar_p(data), c_wchar_p("QQ:23456789"), 0)   # 调用MessageBoxA函数
        except:
            pass

    def tab2_Button_5(self): #导入C段/旁站/\n二级/域名结果   tab2_Button_5
        try:
            self.tab2_tableView_count(0) #设置tableView属性  行数
            int_View=self.ui.tab3_tableView_1.model().rowCount()   #获取共多少行
            model = self.ui.tab3_tableView_1.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()

            TX=int(int_View)/5
            if TX==0:
                TX=1
            if TX>=30:
                TX=30
            self.ui.tab2_spinBox_1.setValue(TX) #设置线程值

            for index in range(int_View):
                s1= model.data(model.index(index,1)).toString()
                self.tab2_tableView1_add(index,s1,None,None,None)  #添加数据
            self.ui.messagebox.append(u"导入C段/旁站/二级/域名结果%d条"%len(range(int_View)))
        except:
            pass

    def SJIndex(self, index):  #双击事件
        try:
            #print self.ui.tab3_tableView_1.currentIndex().row()  可以使用这个获取当前选择行
            model = self.ui.tab2_tableView_1.model()
            url=model.data(model.index(index.row(),0)).toString()
            os.startfile(str(url))
        except BaseException, e:
            print(str(e))

import os
import Class_cms
import thread
import qqwry


import win32ui
