#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

from uiwebxscan import *

import socket
socket.setdefaulttimeout(10)

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Start(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        #http://www.cnblogs.com/caomingongli/archive/2011/09/19/2181842.html    这个不错   PyQt之自定义无边框窗口遮盖任务栏显示问题
        flags = 0  #设置禁止最大化
        flags|= Qt.WindowMinimizeButtonHint  #设置禁止最大化
        self.setWindowFlags(flags)  #设置禁止最大化
        self.setWindowTitle(u'FreebuF webxscan  安全扫描器  内部自用   FreebuF-BY:薛薛')  #设置标题
        self.statusBar().showMessage(u'FreebuF webxscan  安全扫描器  内部自用   FreebuF-BY:薛薛   0.1测试版本  版本时间TIME:2013.10.1')  #设置状态栏
        self.ui.webView.setUrl(QtCore.QUrl("http://www.freebuf.com"))
        self.ui.messagebox.append(u'欢迎使用 FreebuF webxscan  安全扫描器  0.1版本')

        #self.ui.tab1_Box_1.setSuffix(u"线程")       #设置输出显示前缀
        ############taop1 事件处理
        from top1.class_top1 import top1
        self.top1=top1(self.ui)
        self.top1.initdlalig()  #初始化
#        导入URL列表 tab1_Button_1
#        导入C段/旁站/\n二级/域名结果   tab1_Button_4
        #        导出扫描结果 tab1_Button_2
#        开始测试 tab3_Button_3
#
#        线程 tab1_spinBox_1
        #                      控件                                                       响应函数
        QtCore.QObject.connect(self.ui.tab1_Button_1, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top1.tab1_Button_1) #导入URL列表 tab1_Button_1
        QtCore.QObject.connect(self.ui.tab1_Button_2, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top1.tab3_Button_2) #导出扫描结果 tab1_Button_2
        QtCore.QObject.connect(self.ui.tab1_Button_3, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top1.tab3_Button_3) #开始测试 tab3_Button_3
        QtCore.QObject.connect(self.ui.tab1_Button_4, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top1.tab1_Button_4) #导入C段/旁站/\n二级/域名结果   tab1_Button_4

        #connect(ui.treeWidget,SIGNAL(itemDoubleClicked(QTreeWidgetItem*,int)),this,SLOT(showSelectedImg(QTreeWidgetItem*,int)))
        #QtCore.QObject.connect(self.CTree,QtCore.SIGNAL("itemDoubleClicked(QTreeWidgetItem*,int)"),self.data_query)
        QtCore.QObject.connect(self.ui.tab1_treeWidget_1,QtCore.SIGNAL("itemDoubleClicked(QTreeWidgetItem*,int)"),self.msg)
        #tab1_treeWidget_1
        ############taop2 事件处理
#        导入URL列表 tab2_Button_1
#        导入C段/旁站/\n二级/域名结果   tab2_Button_5
#        导出URL列表 tab2_Button_2
#        开始CMS识别 tab2_Button_3
#        显示IP和标题 tab2_Button_4
#
#        线程数 tab2_spinBox_1
        from top2.class_top2 import top2
        self.top2=top2(self.ui)
        self.top2.initdlalig()  #初始化
        #                      控件                                                       响应函数
        QtCore.QObject.connect(self.ui.tab2_Button_1, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top2.tab2_Button_1) #导入URL列表 tab2_Button_1
        QtCore.QObject.connect(self.ui.tab2_Button_2, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top2.tab2_Button_2) #导出URL列表 tab2_Button_2
        QtCore.QObject.connect(self.ui.tab2_Button_3, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top2.tab2_Button_3) #开始CMS识别 tab2_Button_3
        QtCore.QObject.connect(self.ui.tab2_Button_4, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top2.tab2_Button_4) #显示IP和标题 tab2_Button_4
        QtCore.QObject.connect(self.ui.tab2_Button_5, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top2.tab2_Button_5) #导入C段/旁站/\n二级/域名结果   tab2_Button_5

        QtCore.QObject.connect(self.ui.tab2_tableView_1, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.top2.SJIndex)   #双击事件
        #tab2_tableView_1
#        self.tab2_
        ############taop3 事件处理
        #        C段 域名 tab3_textEdit_1
        #        C段 IP tab3_textEdit_2
        #        域名转IP tab3_Button_1
        #        开始扫描 tab3_Button_2
        #
        #        旁站 域名 tab3_textEdit_3
        #        旁站 IP tab3_textEdit_4
        #        域名转IP tab3_Button_3
        #        开始扫描 tab3_Button_4
        #
        #        二级域名 tab3_textEdit_5
        #        开始扫描 tab3_Button_5
        #        显示IP和标题 tab3_Button_6
        #        导出扫描结果 tab3_Button_7
        from top3.class_top3 import top3
        self.top3=top3(self.ui)
        self.top3.initdlalig()  #初始化
        #                      控件                                                       响应函数
        QtCore.QObject.connect(self.ui.tab3_Button_1, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top3.tab3_Button_1) #域名转IP tab3_Button_1
        QtCore.QObject.connect(self.ui.tab3_Button_2, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top3.tab3_Button_2) #开始扫描 tab3_Button_2
        QtCore.QObject.connect(self.ui.tab3_Button_3, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top3.tab3_Button_3) #域名转IP tab3_Button_3
        QtCore.QObject.connect(self.ui.tab3_Button_4, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top3.tab3_Button_4) #开始扫描 tab3_Button_4
        QtCore.QObject.connect(self.ui.tab3_Button_5, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top3.tab3_Button_5) #开始扫描 tab3_Button_5
        QtCore.QObject.connect(self.ui.tab3_Button_6, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top3.tab3_Button_6) #显示IP和标题 tab3_Button_6
        QtCore.QObject.connect(self.ui.tab3_Button_7, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top3.tab3_Button_7) #导出扫描结果 tab3_Button_7

        QtCore.QObject.connect(self.ui.tab3_tableView_1, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.top3.SJIndex)   #双击事件
        #tab3_tableView_1
        ############
    #########################################################################################
    #http://www.cxybl.com/html/bcyy/c/qt/20130717/39146.html
    def msg(self, item, column):#currentRow()
        user32.MessageBoxW(0,c_wchar_p(u"这个地方还没想到什么好方法获取内容  技术问题呵呵"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
        #print self.ui.tab1_treeWidget_1.currentIndex()
        #print self.ui.tab1_treeWidget_1.currentItem()
#        pCurrSelItem=self.ui.tab1_treeWidget_1.selectAll()  #获取选择行数
#        print pCurrSelItem
#        print pCurrSelItem.count()
#        pCurrSelItem.setText(0,"1212121212121212")  #修改内容
#        print pCurrSelItem.text(0)
#        print pCurrSelItem.text(1)

#import class_top3
#from class_top3 import Taop3
from PyQt4 import QtCore, QtGui ,QtNetwork
from PyQt4.QtCore import *
from ctypes import *
#import QtNetwork
user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
#user32.MessageBoxW(0,c_wchar_p("1111111"), c_wchar_p("QQ:23456789"), 0)   # 调用MessageBoxA函数
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #lang = QtCore.QTranslator()
    #lang.load("qt_zh_CN.qm")
    #app.installTranslator(lang)#载入中文字体需要从qt安装目录里复制PyQt4\translations\qt_zh_CN.qm
    myapp = Start()
    myapp.show()
    sys.exit(app.exec_())













