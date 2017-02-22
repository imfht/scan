# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys
import time
from PyQt4.QtGui  import *
from PyQt4.QtCore import *


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class CheckBoxDelegate(QItemDelegate):

    def __init__(self, parent=None):
        QItemDelegate.__init__(self, parent)
        self.chkboxSize = 19 #?!

    def createEditor(self, parent, option, index):
        chkbox = QCheckBox(parent)
        chkbox.setText('')
        chkbox.setTristate(False) #只用两个状态
        left = option.rect.x() + (option.rect.width() - self.chkboxSize) / 2
        top  = option.rect.y() + (option.rect.height() - self.chkboxSize) / 2
        chkbox.setGeometry(left, top, self.chkboxSize, self.chkboxSize)
        return chkbox

    def paint(self, painter, option, index):
        value = index.data().toBool()
        opt = QStyleOptionButton()
        opt.state |= QStyle.State_Enabled | (QStyle.State_On if value else QStyle.State_Off)
        opt.text = ''
        left = option.rect.x() + (option.rect.width() - self.chkboxSize) / 2
        top  = option.rect.y() + (option.rect.height() - self.chkboxSize) / 2
        opt.rect = QRect(left, top, self.chkboxSize, self.chkboxSize)
        QApplication.style().drawControl(QStyle.CE_CheckBox, opt, painter)

    def updateEditorGeometry(self, editor, option, index):
        pass

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(696, 518)
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(7, 0, 351, 441))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(370, 10, 321, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.textEdit = QtGui.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 301, 91))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 480, 75, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 480, 75, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 450, 141, 30))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 450, 171, 61))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(370, 140, 321, 371))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.textEdit_2 = QtGui.QTextEdit(self.groupBox_2)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 20, 301, 341))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "FTP黑链挂载器    谢谢 灰帽程序员论坛 hmhacker.org  技术帮助", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "挂马地址：", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "全选", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "反选", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "选择了0个要上传的FTP", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "处理了0个页面\n"
"更新成功0个页面\n"
"页面已有现在的连接0个", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "MsessageBox消息提示：", None, QtGui.QApplication.UnicodeUTF8))

    def ini_Dialog(self):
        #########################
#        self.tableView.setRowCount(10)  #创建行
#        self.tableView.setColumnCount(6)  #创建列
        model = QStandardItemModel(300, 7, self.tableView)   #行 列
        model.setHorizontalHeaderLabels([u'选择',u'IP',u'用户名',u'密码',u'root权限',u'title网页标题',u'time时间'])
        self.tableView.setModel(model)
        self.tableView.setItemDelegateForColumn(0, CheckBoxDelegate(self.tableView))

        #########################
        self.textEdit_2.setEnabled(0)  #给改成禁用
        self.textEdit_2.append(u"欢迎使用FTP黑链挂在器---"+time.strftime('%Y.%m.%d-%H.%M.%S'))
        self.textEdit_2.append(u"root 列表解释")
        self.textEdit_2.append(u"0  连接不上FTP")
        self.textEdit_2.append(u"1  连接成功什么权限都没给")
        self.textEdit_2.append(u"2  仅有上传权限")
        self.textEdit_2.append(u"3  有上传和删除权限")
        #########################

class Start(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Dialog()#这儿跟上面那个class一样
        self.ui.setupUi(self)
        self.ui.ini_Dialog()

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=Start()
    myapp.show()
    sys.exit(app.exec_())