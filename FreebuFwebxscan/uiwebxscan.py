# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FreebuFwebxscan.ui'
#
# Created: Wed Oct 02 11:49:04 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(1150, 579)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 811, 531))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self._2 = QtGui.QGridLayout(self.layoutWidget)
        self._2.setMargin(0)
        self._2.setSpacing(6)
        self._2.setObjectName(_fromUtf8("_2"))
        self.tabWidget = QtGui.QTabWidget(self.layoutWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_A1 = QtGui.QWidget()
        self.tab_A1.setObjectName(_fromUtf8("tab_A1"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_A1)
        self.groupBox_7.setGeometry(QtCore.QRect(120, 10, 681, 491))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.tab1_treeWidget_1 = QtGui.QTreeWidget(self.groupBox_7)
        self.tab1_treeWidget_1.setGeometry(QtCore.QRect(10, 20, 661, 461))
        self.tab1_treeWidget_1.setObjectName(_fromUtf8("tab1_treeWidget_1"))
        self.tab1_treeWidget_1.headerItem().setText(0, _fromUtf8("1"))
        self.tab1_Button_2 = QtGui.QPushButton(self.tab_A1)
        self.tab1_Button_2.setGeometry(QtCore.QRect(10, 110, 101, 41))
        self.tab1_Button_2.setObjectName(_fromUtf8("tab1_Button_2"))
        self.tab1_Button_1 = QtGui.QPushButton(self.tab_A1)
        self.tab1_Button_1.setGeometry(QtCore.QRect(10, 10, 101, 41))
        self.tab1_Button_1.setObjectName(_fromUtf8("tab1_Button_1"))
        self.groupBox_8 = QtGui.QGroupBox(self.tab_A1)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 160, 101, 71))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.label_8 = QtGui.QLabel(self.groupBox_8)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 41, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.tab1_Box_1 = QtGui.QSpinBox(self.groupBox_8)
        self.tab1_Box_1.setGeometry(QtCore.QRect(10, 40, 81, 22))
        self.tab1_Box_1.setMinimum(1)
        self.tab1_Box_1.setMaximum(100)
        self.tab1_Box_1.setObjectName(_fromUtf8("tab1_Box_1"))
        self.tab1_Button_3 = QtGui.QPushButton(self.tab_A1)
        self.tab1_Button_3.setGeometry(QtCore.QRect(10, 240, 101, 41))
        self.tab1_Button_3.setObjectName(_fromUtf8("tab1_Button_3"))
        self.tab1_Button_4 = QtGui.QPushButton(self.tab_A1)
        self.tab1_Button_4.setGeometry(QtCore.QRect(10, 60, 101, 41))
        self.tab1_Button_4.setObjectName(_fromUtf8("tab1_Button_4"))
        self.label_7 = QtGui.QLabel(self.tab_A1)
        self.label_7.setGeometry(QtCore.QRect(10, 300, 101, 191))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tabWidget.addTab(self.tab_A1, _fromUtf8(""))
        self.tab_A2 = QtGui.QWidget()
        self.tab_A2.setObjectName(_fromUtf8("tab_A2"))
        self.tab2_Button_1 = QtGui.QPushButton(self.tab_A2)
        self.tab2_Button_1.setGeometry(QtCore.QRect(10, 10, 101, 41))
        self.tab2_Button_1.setObjectName(_fromUtf8("tab2_Button_1"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_A2)
        self.groupBox_5.setGeometry(QtCore.QRect(120, 10, 681, 491))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.tab2_tableView_1 = QtGui.QTableView(self.groupBox_5)
        self.tab2_tableView_1.setGeometry(QtCore.QRect(10, 20, 661, 461))
        self.tab2_tableView_1.setObjectName(_fromUtf8("tab2_tableView_1"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_A2)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 160, 101, 71))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.label_6 = QtGui.QLabel(self.groupBox_6)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tab2_spinBox_1 = QtGui.QSpinBox(self.groupBox_6)
        self.tab2_spinBox_1.setGeometry(QtCore.QRect(10, 40, 81, 22))
        self.tab2_spinBox_1.setMinimum(1)
        self.tab2_spinBox_1.setMaximum(100)
        self.tab2_spinBox_1.setObjectName(_fromUtf8("tab2_spinBox_1"))
        self.tab2_Button_3 = QtGui.QPushButton(self.tab_A2)
        self.tab2_Button_3.setGeometry(QtCore.QRect(10, 240, 101, 41))
        self.tab2_Button_3.setObjectName(_fromUtf8("tab2_Button_3"))
        self.tab2_Button_2 = QtGui.QPushButton(self.tab_A2)
        self.tab2_Button_2.setGeometry(QtCore.QRect(10, 110, 101, 41))
        self.tab2_Button_2.setObjectName(_fromUtf8("tab2_Button_2"))
        self.tab2_Button_4 = QtGui.QPushButton(self.tab_A2)
        self.tab2_Button_4.setGeometry(QtCore.QRect(10, 290, 101, 41))
        self.tab2_Button_4.setObjectName(_fromUtf8("tab2_Button_4"))
        self.tab2_Button_5 = QtGui.QPushButton(self.tab_A2)
        self.tab2_Button_5.setGeometry(QtCore.QRect(10, 60, 101, 41))
        self.tab2_Button_5.setObjectName(_fromUtf8("tab2_Button_5"))
        self.tabWidget.addTab(self.tab_A2, _fromUtf8(""))
        self.tab_A3 = QtGui.QWidget()
        self.tab_A3.setObjectName(_fromUtf8("tab_A3"))
        self.groupBox = QtGui.QGroupBox(self.tab_A3)
        self.groupBox.setGeometry(QtCore.QRect(0, 130, 801, 371))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tab3_tableView_1 = QtGui.QTableView(self.groupBox)
        self.tab3_tableView_1.setGeometry(QtCore.QRect(10, 20, 781, 341))
        self.tab3_tableView_1.setObjectName(_fromUtf8("tab3_tableView_1"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_A3)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 10, 261, 111))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.tab3_textEdit_1 = QtGui.QTextEdit(self.groupBox_2)
        self.tab3_textEdit_1.setGeometry(QtCore.QRect(40, 20, 151, 31))
        self.tab3_textEdit_1.setObjectName(_fromUtf8("tab3_textEdit_1"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 30, 31, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.tab3_Button_1 = QtGui.QPushButton(self.groupBox_2)
        self.tab3_Button_1.setGeometry(QtCore.QRect(200, 10, 51, 41))
        self.tab3_Button_1.setObjectName(_fromUtf8("tab3_Button_1"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 21, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tab3_textEdit_2 = QtGui.QTextEdit(self.groupBox_2)
        self.tab3_textEdit_2.setGeometry(QtCore.QRect(40, 60, 151, 31))
        self.tab3_textEdit_2.setObjectName(_fromUtf8("tab3_textEdit_2"))
        self.tab3_Button_2 = QtGui.QPushButton(self.groupBox_2)
        self.tab3_Button_2.setGeometry(QtCore.QRect(200, 60, 51, 41))
        self.tab3_Button_2.setObjectName(_fromUtf8("tab3_Button_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_A3)
        self.groupBox_3.setGeometry(QtCore.QRect(270, 10, 261, 111))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.tab3_Button_3 = QtGui.QPushButton(self.groupBox_3)
        self.tab3_Button_3.setGeometry(QtCore.QRect(200, 10, 51, 41))
        self.tab3_Button_3.setObjectName(_fromUtf8("tab3_Button_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 31, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tab3_textEdit_3 = QtGui.QTextEdit(self.groupBox_3)
        self.tab3_textEdit_3.setGeometry(QtCore.QRect(40, 20, 151, 31))
        self.tab3_textEdit_3.setObjectName(_fromUtf8("tab3_textEdit_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 21, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tab3_textEdit_4 = QtGui.QTextEdit(self.groupBox_3)
        self.tab3_textEdit_4.setGeometry(QtCore.QRect(40, 60, 151, 31))
        self.tab3_textEdit_4.setObjectName(_fromUtf8("tab3_textEdit_4"))
        self.tab3_Button_4 = QtGui.QPushButton(self.groupBox_3)
        self.tab3_Button_4.setGeometry(QtCore.QRect(200, 60, 51, 41))
        self.tab3_Button_4.setObjectName(_fromUtf8("tab3_Button_4"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_A3)
        self.groupBox_4.setGeometry(QtCore.QRect(540, 10, 261, 61))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 31, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tab3_Button_5 = QtGui.QPushButton(self.groupBox_4)
        self.tab3_Button_5.setGeometry(QtCore.QRect(200, 10, 51, 41))
        self.tab3_Button_5.setObjectName(_fromUtf8("tab3_Button_5"))
        self.tab3_textEdit_5 = QtGui.QTextEdit(self.groupBox_4)
        self.tab3_textEdit_5.setGeometry(QtCore.QRect(40, 20, 151, 31))
        self.tab3_textEdit_5.setObjectName(_fromUtf8("tab3_textEdit_5"))
        self.tab3_Button_7 = QtGui.QPushButton(self.tab_A3)
        self.tab3_Button_7.setGeometry(QtCore.QRect(720, 80, 81, 41))
        self.tab3_Button_7.setObjectName(_fromUtf8("tab3_Button_7"))
        self.tab3_Button_6 = QtGui.QPushButton(self.tab_A3)
        self.tab3_Button_6.setGeometry(QtCore.QRect(630, 80, 81, 41))
        self.tab3_Button_6.setObjectName(_fromUtf8("tab3_Button_6"))
        self.tab3_checkBox_1 = QtGui.QCheckBox(self.tab_A3)
        self.tab3_checkBox_1.setGeometry(QtCore.QRect(550, 80, 71, 41))
        self.tab3_checkBox_1.setObjectName(_fromUtf8("tab3_checkBox_1"))
        self.tabWidget.addTab(self.tab_A3, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.label_9 = QtGui.QLabel(self.tab_6)
        self.label_9.setGeometry(QtCore.QRect(110, 20, 351, 81))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tab5_textEdit_1 = QtGui.QTextEdit(self.tab_2)
        self.tab5_textEdit_1.setGeometry(QtCore.QRect(10, 0, 791, 71))
        self.tab5_textEdit_1.setObjectName(_fromUtf8("tab5_textEdit_1"))
        self.webView = QtWebKit.QWebView(self.tab_2)
        self.webView.setGeometry(QtCore.QRect(10, 80, 791, 411))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.tabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.tabWidget.addTab(self.tab_8, _fromUtf8(""))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        self.tabWidget.addTab(self.tab_9, _fromUtf8(""))
        self.tab_10 = QtGui.QWidget()
        self.tab_10.setObjectName(_fromUtf8("tab_10"))
        self.tabWidget.addTab(self.tab_10, _fromUtf8(""))
        self._2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.groupBox_9 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(820, 0, 321, 531))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.messagebox = QtGui.QTextEdit(self.groupBox_9)
        self.messagebox.setGeometry(QtCore.QRect(10, 20, 301, 501))
        self.messagebox.setObjectName(_fromUtf8("messagebox"))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(mainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(mainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "FreebuF webxscan  安全扫描器  内部自用   FreebuF-BY:小薛   0.1测试版本", None))
        self.groupBox_7.setTitle(_translate("mainWindow", "域名列表", None))
        self.tab1_Button_2.setText(_translate("mainWindow", "导出扫描结果", None))
        self.tab1_Button_1.setText(_translate("mainWindow", "导入URL列表", None))
        self.groupBox_8.setTitle(_translate("mainWindow", "参数设置", None))
        self.label_8.setText(_translate("mainWindow", "线程数：", None))
        self.tab1_Button_3.setText(_translate("mainWindow", "开始测试", None))
        self.tab1_Button_4.setText(_translate("mainWindow", "导入C段/旁站/\n"
"二级/域名结果", None))
        self.label_7.setText(_translate("mainWindow", "请自己根据文件大\n"
"小判断是否是404\n"
"(网站下多个文件大\n"
"小相同的说明是\n"
"这个文件不是我们\n"
"想要的)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_A1), _translate("mainWindow", "危险文件/后台/扫描", None))
        self.tab2_Button_1.setText(_translate("mainWindow", "导入URL列表", None))
        self.groupBox_5.setTitle(_translate("mainWindow", "域名列表", None))
        self.groupBox_6.setTitle(_translate("mainWindow", "参数设置", None))
        self.label_6.setText(_translate("mainWindow", "线程数：", None))
        self.tab2_Button_3.setText(_translate("mainWindow", "开始CMS识别", None))
        self.tab2_Button_2.setText(_translate("mainWindow", "导出扫描结果", None))
        self.tab2_Button_4.setText(_translate("mainWindow", "显示IP和标题", None))
        self.tab2_Button_5.setText(_translate("mainWindow", "导入C段/旁站/\n"
"二级/域名结果", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_A2), _translate("mainWindow", "CMS指纹识别", None))
        self.groupBox.setTitle(_translate("mainWindow", "域名列表", None))
        self.groupBox_2.setTitle(_translate("mainWindow", "C段-域名", None))
        self.tab3_textEdit_1.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">http://www.freebuf.com</p></body></html>", None))
        self.label.setText(_translate("mainWindow", "域名：", None))
        self.tab3_Button_1.setText(_translate("mainWindow", "域名\n"
"转IP", None))
        self.label_2.setText(_translate("mainWindow", "IP：", None))
        self.tab3_textEdit_2.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">127.0.0.1</p></body></html>", None))
        self.tab3_Button_2.setText(_translate("mainWindow", "开始\n"
"扫描", None))
        self.groupBox_3.setTitle(_translate("mainWindow", "旁站-域名", None))
        self.tab3_Button_3.setText(_translate("mainWindow", "域名\n"
"转IP", None))
        self.label_3.setText(_translate("mainWindow", "域名：", None))
        self.tab3_textEdit_3.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">http://www.freebuf.com</p></body></html>", None))
        self.label_4.setText(_translate("mainWindow", "IP：", None))
        self.tab3_textEdit_4.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">127.0.0.1</p></body></html>", None))
        self.tab3_Button_4.setText(_translate("mainWindow", "开始\n"
"扫描", None))
        self.groupBox_4.setTitle(_translate("mainWindow", "二级-域名", None))
        self.label_5.setText(_translate("mainWindow", "域名：", None))
        self.tab3_Button_5.setText(_translate("mainWindow", "开始\n"
"扫描", None))
        self.tab3_textEdit_5.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">http://www.freebuf.com</p></body></html>", None))
        self.tab3_Button_7.setText(_translate("mainWindow", "导出\n"
"扫描结果", None))
        self.tab3_Button_6.setText(_translate("mainWindow", "显示IP\n"
"和标题", None))
        self.tab3_checkBox_1.setText(_translate("mainWindow", "不删除\n"
"原有数据", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_A3), _translate("mainWindow", "C段/旁站/二级/-域名", None))
        self.label_9.setText(_translate("mainWindow", "Cookie提交数据等会在写     学校的事情太多了", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("mainWindow", "Cookie提交", None))
        self.tab5_textEdit_1.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">FreebuF-BY:薛薛  (本软件使用PYQT开发python2.7.3+pyqt4 开发   等开发的差不多的时候会开源)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">希望大家能提供宝贵意见  好让我改进  大家的支持是我开发的动力(超级宅女)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">声明：本软件只是测试网站使用请勿做任何违法行为(如果做了 与本人无关 请遵守所在国的相关法律)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">网络安全交流QQ群220695354   </p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "关于webxscan", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("mainWindow", "等待1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("mainWindow", "等待2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("mainWindow", "等待3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("mainWindow", "等待4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("mainWindow", "等待5", None))
        self.groupBox_9.setTitle(_translate("mainWindow", "messagebox消息提示", None))
        self.menu.setTitle(_translate("mainWindow", "帮助", None))
        self.action.setText(_translate("mainWindow", "软件声明", None))
        self.action_2.setText(_translate("mainWindow", "关注作者", None))

from PyQt4 import QtWebKit
