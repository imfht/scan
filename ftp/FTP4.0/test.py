# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Fri Nov 16 21:06:52 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

# -*- coding: cp936 -*-
from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 200, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.plainTextEdit = QtGui.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 40, 104, 64))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.TextEdit = QtGui.QPlainTextEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 180, 64, 14))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setText("aaaaadddaaa")

        self.retranslateUi(Form)#zenm bu怎么不能测试了
        
        #QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        #这儿是刚刚加的那个信号槽。标示单击那个按钮就关闭窗口，你也可以自定义信号
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.set)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def set(self):
        self.plainTextEdit.setPlainText("aaaaaaaa")#这个就是自定义刚刚那个按钮的功能为想那个文本框里设置文本

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
class Start(QtGui.QMainWindow):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui=Ui_Form()#这儿跟上面那个class一样
		self.ui.setupUi(self)

if __name__=="__main__":
 	app=QtGui.QApplication(sys.argv)
	myapp=Start()
	myapp.show()
	sys.exit(app.exec_())
