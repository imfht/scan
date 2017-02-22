# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Fri Feb 22 04:53:30 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "FTP黑链挂载器 1.1   谢谢 灰帽程序员论坛 hmhacker.org  技术帮助      BY:落雪QQ2602159946", None, QtGui.QApplication.UnicodeUTF8))
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

