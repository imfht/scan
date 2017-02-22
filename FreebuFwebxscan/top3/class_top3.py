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
class top3(object):
#    def __init__(self,tab3_tableView_1,tab3_textEdit_1,tab3_textEdit_2,tab3_textEdit_3,tab3_textEdit_4,tab3_textEdit_5):
#        self.tab3_tableView_1=tab3_tableView_1
#        self.tab3_textEdit_1=tab3_textEdit_1
#        self.tab3_textEdit_2=tab3_textEdit_2
#
#        self.tab3_textEdit_3=tab3_textEdit_3
#        self.tab3_textEdit_4=tab3_textEdit_4
#
#        self.tab3_textEdit_5=tab3_textEdit_5
    def __init__(self,ui):
        self.ui=ui
        self.LS =[]  #初始化类
        self.list_2=[]
        self.NO_url ="msn.com|microsoft.com"
        self.NO_url_list=self.NO_url.split('|')
        ######################
    def initdlalig(self):
        ###################
        self.tab3_tableView_count(0) #设置tableView属性  行数
        self.ui.tab3_checkBox_1.setChecked(True)    #设置复选框为选择状态
        ###################
    def tab3_tableView_count(self,h):  #设置tableView属性  行数
        try:
            self.model = QStandardItemModel()
            self.model.setColumnCount(3)     #列
            self.model.setRowCount(h)  #行  len(node)

            self.model.setHorizontalHeaderLabels([u'IP/域名',u'扫描到的域名',u'IP/物理位置/title网站标题'])
            self.ui.tab3_tableView_1.setModel(self.model)

            #self.tableView.resizeColumnsToContents()   #由内容调整列
            self.ui.tab3_tableView_1.setColumnWidth(0,150)  #设置表格的各列的宽度值
            self.ui.tab3_tableView_1.setColumnWidth(1,250)  #设置表格的各列的宽度值
            self.ui.tab3_tableView_1.setColumnWidth(2,340)  #设置表格的各列的宽度值
            for i in range(h):  #调整行高度  len(node)
                self.ui.tab3_tableView_1.setRowHeight(i, 20)

            self.ui.tab3_tableView_1.setEditTriggers(QTableWidget.NoEditTriggers)  #设置表格的单元为只读属性，即不能编辑
            self.ui.tab3_tableView_1.setSelectionBehavior(QTableWidget.SelectRows) #点击选择是选择行//设置选中时为整行选中
            self.ui.tab3_tableView_1.setSelectionMode(QTableWidget.SingleSelection)  #禁止多行选择
            self.ui.tab3_tableView_1.setAlternatingRowColors(True)  #还是只可以选择单行（单列）
            #self.tableView.verticalHeader().hide() #隐藏行头
        except BaseException, e:
            print(str(e))
            pass
    ###############################
    def url_www(self,url): #URL地址中提取网址  http://www.bizschool.cn/plus/90sec.php        www.bizschool.cn
        proto, rest = urllib.splittype(url)
        host, rest = urllib.splithost(rest)
        return host
    def www_ping_ip(self,WWW):  #域名转IP
        try:
            result = socket.getaddrinfo(WWW, None)
            return result[0][4][0]
        except:
            return 0

    def open_url_data(self,url):  #读取网页内容
        try:
            req = urllib2.Request(url)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            return s.read()
        except:
            return 0
    def URL_STR(self,data):#判断是否是HTTP字符
        try:
            sStr2 = 'http://'
            sStr3 = 'https://'
            if data.find(sStr2) and data.find(sStr3):
                return 1
            else:
                return 0 #print "查找到了"
        except:
            return 1
    def URL_TQURL(self,data): #URL提取URL
        try:
            data +="/"      #data ="https://www.baidu.com/cache/sethelp/index.html"
            if ~data.find("http://"):  #~取反
                data=data[7:] #字符串删除
                nPos = data.index('/') #查找字符        #print nPos
                sStr1 = data[0:nPos] #复制指定长度的字符
                return sStr1

            if ~data.find("https://"):  #~取反
                data=data[8:] #字符串删除
                nPos = data.index('/') #查找字符
                #print nPos
                sStr1 = data[0:nPos] #复制指定长度的字符
                return sStr1
        except:
            pass
    def CS_YM(self,data):  #域名排除异常
        try:
            self.AE = 0 #得到list的第一个元素
            while self.AE < len(self.NO_url_list):
                #print "1111",list[E]
                if not data.find("."+self.NO_url_list[self.AE])==-1:
                    return 0
                self.AE +=1
            return 1
        except:
            #print u"域名排除异常"
            return 1
    def bing_ip_www(self,ip):
        try:
            bing_data="http://cn.bing.com/search?q=IP:%s&rn=50&go=&first=0"%(ip)
            #print bing_data
            ss=self.open_url_data(bing_data)
            if ss==0:
                return
                ##################################
            p = re.compile( r'<li class="sa_wr"><div class="sa_cc".*?<div Class="sa_mc"><div class="sb_tlst sbt_ad"><h3><a href="(.*?)" target=' )
            sarr = p.findall(ss)
            self.statusBar(u'正在测试IP:%s 绑定的域名'%ip)  #数据显示在状态栏里
            for every in sarr:
                #print every
                if ~self.URL_STR(every):
                    a1=self.URL_TQURL(every) #URL提取URL
                    if (a1 is not None) or (a1==""):  #判断是否为 None
                        if not self.CS_YM(a1):  #域名排除异常
                            continue #进入下一次环
                        string=str(ip)+"|"+a1
                        self.LS.append(string)  #添加数据
                        self.liet_lsqc() #列表去重复
                        self.liet_CX()  #查询数据是否存在
        except BaseException, e:
            print(str(e))
            pass
    def liet_lsqc(self): #列表去重复
        try:
        #列表去重复
            for i in self.LS:
                if i not in self.list_2:
                    self.list_2.append(i)
        except:
            pass
    def liet_CX(self):  #查询数据是否存在
        try:
            E = 0 #得到list的第一个元素
            while E < len(self.list_2):
                ls=self.list_2[E].split('|')
                time.sleep(0.01)
                if "http" in ls[1]:
                    self.tab3_tableView1_add(E,ls[0],ls[1],None)  #添加数据
                else:
                    self.tab3_tableView1_add(E,ls[0],"http://"+ls[1],None)  #添加数据
                E = E + 1
            return 0
        except:
            pass
    def c_bing_IP(self,IP):
        try:
            #self.bing_ip_www(str(s1))  #192.157.211.40
            #IP=str(s1)
            if IP==0:
                return
            id=IP.rfind('.')
            sStr1 = IP[0:id+1] #复制指定长度的字符
            for IP4 in range(254,0,-1):
                IP_data=sStr1+str(IP4)
                #print IP_data
                self.bing_ip_www(IP_data)
                time.sleep(0.05) #确保先运行Seeker中的方法
            self.statusBar(u'C段域名枚举完成')  #数据显示在状态栏里
            self.ui.tab3_Button_2.setEnabled(1)  #给改成禁用
        except BaseException, e:
            self.ui.tab3_Button_2.setEnabled(1)  #给改成禁用
            print(str(e))
            pass

    def statusBar(self,data): #数据显示在状态栏里
        try:
            #self.ui.statusBar().showMessage(data)  #设置状态栏
            self.ui.messagebox.append(data)
        except BaseException, e:
            print(str(e))
            pass

    #添加数据
    def tab3_tableView1_add(self,ints,s0,s1,s2):  #添加数据
        try:
            if not s0==None:
                self.model.setItem(ints, 0, QStandardItem(s0))
            if not s1==None:
                self.model.setItem(ints, 1, QStandardItem(s1))
            if not s2==None:
                self.model.setItem(ints, 2, QStandardItem(s2))
            self.ui.tab3_tableView_1.setModel(self.model)
        except BaseException, e:
            print(str(e))
            pass

    def bing_IP(self,ip):
        try:
            self.bing_ip_www(ip)
            time.sleep(0.05) #确保先运行Seeker中的方法
            self.statusBar(u'%s域名枚举完成'%ip)  #数据显示在状态栏里
            self.ui.tab3_Button_4.setEnabled(1)  #给改成禁用
        except BaseException, e:
            self.ui.tab3_Button_4.setEnabled(1)  #给改成禁用
            print(str(e))
            pass

    def list_del(self):  #清空list列表
        try:
            i = 0 #得到list的第一个元素
            while i < len(self.LS):
                del self.LS[i]

            i2 = 0 #得到list的第一个元素
            while i2 < len(self.list_2):
                del self.list_2[i2]
        except BaseException, e:
            print(str(e))
            pass

    def url_post(self,URL):
        try:
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s=urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            #urllib2.urlopen(URL,timeout=20)  # 后门POST提交   超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            return s.read()
            #time.sleep(1)
        except:
            return 0
    def ej_url(self,url): #采集二级域名
        try:
            data=self.url_post("http://i.links.cn/subdomain/%s.html"%url)
            if data==0:
                self.statusBar(u'获取URL:%s数据失败'%url)  #数据显示在状态栏里
                self.ui.tab3_Button_5.setEnabled(1)  #给改成禁用
                return 0
                #.<a href="http://club.freebuf.com" rel=nofollow target=_blank>http://club.freebuf.com</a>
            #.<a.*?href=\"(?<url>.*?)\".*?>(?<content>.*?)</a>
            s= re.compile(r'.<a.+?href="(.*?)" rel=nofollow target=_blank>.+?</a>')

            sarr = s.findall(data)
            #E = 0 #得到list的第一个元素
            for every in sarr:
                #self.tab3_tableView1_add(E,"http://"+url,every,None)  #添加数据
                string="http://"+url+"|"+every
                self.LS.append(string)  #添加数据
                #E = E + 1

            self.liet_lsqc() #列表去重复
            self.liet_CX()  #查询数据是否存在
            self.ui.tab3_Button_5.setEnabled(1)  #给改成禁用
            self.statusBar(u'获取URL:%s数据完成'%url)  #数据显示在状态栏里
        except:
            self.ui.tab3_Button_5.setEnabled(1)  #给改成禁用
            pass
    ###############################
    def tab3_Button_1(self): #域名转换成IP
        try:
            s1=self.ui.tab3_textEdit_1.toPlainText() #获取内容
            self.ui.tab3_textEdit_2.setPlainText(self.www_ping_ip(self.url_www(str(s1))))  #写入内容
            self.statusBar(u'C段扫描 域名转换成IP完成%s'%str(s1))  #数据显示在状态栏里
        except:
            pass

    def tab3_Button_2(self): #开始扫描 C段
        try:
            self.xh_tableView() #循环读取数据
            if not self.ui.tab3_checkBox_1.isChecked():
                self.list_del()  #清空list列表
                self.tab3_tableView_count(0) #设置tableView属性  行数
            s1=self.ui.tab3_textEdit_2.toPlainText() #获取内容
            thread.start_new_thread(self.c_bing_IP,(str(s1),))  ##开启线程
            self.ui.tab3_Button_2.setEnabled(0)  #给改成禁用
            self.statusBar(u'C段扫描 开始扫描 C段%s'%str(s1))  #数据显示在状态栏里
        except:
            self.ui.tab3_Button_2.setEnabled(1)  #给改成禁用
            pass

    def tab3_Button_3(self): #域名转换成IP
        try:
            s1=self.ui.tab3_textEdit_3.toPlainText() #获取内容
            self.ui.tab3_textEdit_4.setPlainText(self.www_ping_ip(self.url_www(str(s1))))  #写入内容
            self.statusBar(u'域名转换成IP完成%s'%str(s1))  #数据显示在状态栏里
        except:
            pass

    def tab3_Button_4(self): #开始扫描
        try:
            self.xh_tableView() #循环读取数据
            if not self.ui.tab3_checkBox_1.isChecked():
                self.list_del()  #清空list列表
                self.tab3_tableView_count(0) #设置tableView属性  行数
            s1=self.ui.tab3_textEdit_4.toPlainText() #获取内容
            thread.start_new_thread(self.bing_IP,(str(s1),))  ##开启线程
            self.ui.tab3_Button_4.setEnabled(0)  #给改成禁用
            self.statusBar(u'开始旁站扫描完成%s'%str(s1))  #数据显示在状态栏里
        except:
            self.ui.tab3_Button_4.setEnabled(1)  #给改成禁用
            pass

    def tab3_Button_5(self): #开始扫描 域名
        try:
            self.xh_tableView() #循环读取数据
            if not self.ui.tab3_checkBox_1.isChecked():
                self.list_del()  #清空list列表
                self.tab3_tableView_count(0) #设置tableView属性  行数
            s1=self.ui.tab3_textEdit_5.toPlainText() #获取内容
            url=self.url_www(str(s1))
            thread.start_new_thread(self.ej_url,(str(url),))  #开启线程
            self.ui.tab3_Button_5.setEnabled(0)  #给改成禁用
            self.statusBar(u'开始扫描二级域名%s'%str(s1))  #数据显示在状态栏里
        except:
            self.ui.tab3_Button_5.setEnabled(1)  #给改成禁用
            pass

    #############################导出数据和 显示IP和位置网站名称
    def tab3_Button_7(self):#导出数据
        try:
            # 1表示打开文件对话框   0表示保存
            dlg = win32ui.CreateFileDialog(0, "*.txt", None, 0, u"txt 文本 (*.txt)|*.txt|All files|*.*")
            #dlg.SetOFNInitialDir('E:/Python') # 设置打开文件对话框中的初始显示目录
            dlg.DoModal()
            filename = dlg.GetPathName() # 获取选择的文件名称
            data=""
            int_View=self.ui.tab3_tableView_1.model().rowCount()   #获取共多少行
            model = self.ui.tab3_tableView_1.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
            for index in range(int_View):
                s0= model.data(model.index(index,1)).toString()
                data +=s0+"\n"

            file_object = open(filename,'a')
            #file_object.write(list_passwed[E])
            file_object.writelines(data)
            file_object.close()
            #查看PYQT保存文件如何做
            #user32.MessageBoxW(0,c_wchar_p(data), c_wchar_p("QQ:23456789"), 0)   # 调用MessageBoxA函数
        except:
            pass

    def IP_WLWZ_title(self): #'IP/地理位置/网站标题'
        try:
            h=qqwry.C_hoset()
            int_View=self.ui.tab3_tableView_1.model().rowCount()   #获取共多少行
            model = self.ui.tab3_tableView_1.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
            for index in range(int_View):
                s0= model.data(model.index(index,1)).toString()
                data=h.www_data(qqwry.url_www(str(s0)))   #'IP/地理位置/网站标题'
                self.tab3_tableView1_add(index,None,None,data)  #添加数据
            self.ui.tab3_Button_6.setEnabled(1)  #给改成禁用
        except:
            pass

    def tab3_Button_6(self):
        try:
            thread.start_new_thread(self.IP_WLWZ_title,())  #开启线程
            self.ui.tab3_Button_6.setEnabled(0)  #给改成禁用
        except:
            self.ui.tab3_Button_6.setEnabled(1)  #给改成禁用
            pass


    def xh_tableView(self): #循环读取数据
        try:
            int_View=self.ui.tab3_tableView_1.model().rowCount()   #获取共多少行
            model = self.ui.tab3_tableView_1.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
            for index in range(int_View):
                s0= model.data(model.index(index,0)).toString()
                s1= model.data(model.index(index,1)).toString()
                string=str(s0)+"|"+str(s1)
                self.LS.append(string)  #添加数据
        except:
            pass

    def SJIndex(self, index):  #双击事件
        try:
            #print self.ui.tab3_tableView_1.currentIndex().row()  可以使用这个获取当前选择行
            model = self.ui.tab3_tableView_1.model()
            url=model.data(model.index(index.row(),1)).toString()
            os.startfile(str(url))
        except BaseException, e:
            print(str(e))


#user32.MessageBoxW(0,c_wchar_p("1111111"), c_wchar_p("QQ:23456789"), 0)   # 调用MessageBoxA函数\
import os
import thread
import qqwry
import win32ui
if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=Start()
    myapp.show()
    sys.exit(app.exec_())