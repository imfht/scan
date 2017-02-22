#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##################################################
#qq:316118740
#BLOG:http://hi.baidu.com/alalmn
# 正则  获取网页中的链接地址  并判断是否不是HTTP地址
#  刚学写的不好请大家见谅
##################################################
"""
*****读取网页源码=====遍历URL提取网址=====添加到数据库*****
"""

def URL_STR(data):#判断是否是HTTP字符
    try:
        sStr2 = 'http://'
        sStr3 = 'https://'
        #print sStr1.find(sStr2)
        if data.find(sStr2) and data.find(sStr3):
            return 1 #print "没有找到"
        else:
            return 0 #print "查找到了"
    except:
        return 1
##################################################
def URL_TQURL(data): #URL提取URL
    try:
        data +="/"
        #data ="https://www.baidu.com/cache/sethelp/index.html"
        if ~data.find("http://"):  #~取反
            data=data[7:] #字符串删除
            nPos = data.index('/') #查找字符
            #print nPos
            sStr1 = data[0:nPos] #复制指定长度的字符
            return sStr1

        if ~data.find("https://"):  #~取反
            data=data[8:] #字符串删除
            nPos = data.index('/') #查找字符
            #print nPos
            sStr1 = data[0:nPos] #复制指定长度的字符
            return sStr1
    except:
        print u"URL提取URL错误"
##################################################
import urllib2, re, time
import mysql #数据库操作文件
def URL_DZ(URL):  #遍历页里的地址
    try:
        s = urllib2.urlopen(URL,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        ss = s.read()
        p = re.compile( r'<a.+?href=.+?>.+?</a>' )
        pname = re.compile( r'(?<=>).*?(?=</a>)' )
        phref = re.compile( r'(?<=href\=\").*?(?=\")')
        #构造及编译正则表达式
        sarr = p.findall(ss)
        #找出一条一条的<a></a>标签
        i=0
        for every in sarr:
            if i>1000:
                print u"超过1000个URL地址！！！！！！\n"
                break
            else:
                i+=1
            sname = pname.findall( every )
            if sname:
                sname = sname[0]
                shref = phref.findall( every )
            if shref:
                shref = shref[0]
                #print sname.decode( 'gbk' ), "\n" #获取连接名字
                #print shref #获取URL
                if URL_STR(shref):
                    print shref,u"没有找到非法HTTP地址"
                else:
                    #print shref   #"查找到了正确URL地址"
                    a1=URL_TQURL(shref) #URL提取URL
                    mysql_add(a1)  #添加到数据库
        mysql.mysql_S()  #保存数据
        open_mysql()  #读取URL
                    # 上面是将每条<a></a>里面的内容和地址给匹配出来
    except:
        print u"这个URL地址无效！！！！！！！！！！！！！！"
        mysql.mysql_S()  #保存数据
        open_mysql()  #读取URL
#        print u"3秒后,程序将结束重启..."
#        mysql.mysql_close()  #关闭数据库
#        time.sleep(3)  #3秒
#        close()  #自动重启本程序
##################################################

def mysql_add(data1):  #添加到数据库
    try:
    #    print "++++++++++++++++++++",data   #添加数据
        sql="select * from url where url='%s'"%(data1)
        data = mysql.mysql_select(sql)
        if data.find('null123456'):
            print u"已经有了这个URL",data1
            return 0
        else:  #没有可以添加
            print data1
            if ~(data1.find("/") and data1.find("http") and data1.find("?") and data1.find("%")):
                print u"非法URL"
                return 0
            else:
                insert="insert into url(url) VALUES('%s')"%(data1)
                #print insert
                if mysql.mysql_insert(insert): #添加数据
                #mysql.mysql_S()   #提交
                    print u"添加成功",data1
                else:
                    print u"添加失败",data1
    except:
        return 0
##################################################
import sys
import os
import atexit
def close():  #自动重启本程序
    try:
    #    python = sys.executable
    #    os.execl(python, python, * sys.argv)
    #    mysql.mysql_close()  #关闭数据库
        time.sleep(3)
    #    os.system('python txt.py')
        python = sys.executable
        os.execl(python, python, * sys.argv)
        #########
    except:
        sys.exit(0)  #结束进程

def open_mysql():  #读取URL
#    sql="select * from url where httpsend is NULL limit 1"
#    data = mysql.mysql_select(sql)
#    if ~data.find("null123456"):
#        while True:  #进入死循环不读取
#            print "可能无读取的数据请查看数据库！！！！！"
#            time.sleep(3)  #3秒
##############
#    else:
#        update = "update url set time='%s',httpsend='send' where url='%s'"%(time.strftime('%Y.%m.%d-%H.%M.%S'),data)
#        mysql.mysql_update(update)
#        mysql.mysql_S()  #保存数据
#        url_data = "http://"+data
#        print "读取URL：",url_data
#        URL_DZ(url_data)  #遍历页里的地址
##############
    try:
        sql="select * from url where httpsend is NULL limit 1"
        data = mysql.mysql_select(sql)
        print U"数据库URL",data
        if ~data.find("null123456"):
                print u"可能无读取的数据请查看数据库！！！！！"
                mysql.mysql_S()  #保存数据
                time.sleep(1)  #3秒
                #open_mysql()  #读取URL
                atexit.register(close)#自动重启本程序
        update = "update url set time='%s',httpsend='send' where url='%s'"%(time.strftime('%Y.%m.%d-%H.%M.%S'),data)
        mysql.mysql_update(update)
        mysql.mysql_S()  #保存数据
        url_data = "http://"+data
        print u"读取URL：",url_data
        URL_DZ(url_data)  #遍历页里的地址
    except:
        print u"读取URL异常！！！！！"
        print u"3秒后,程序将结束重启..."
        mysql.mysql_S()  #保存数据
        mysql.mysql_close()  #关闭数据库
        #close()  #自动重启本程序
        atexit.register(close)#自动重启本程序
##################################################
#from ctypes import *
if __name__=='__main__':
    try:
        print __doc__
        mysql.mysql_open()  #连接数据库
        open_mysql()     #读取URL
    except:
    #    user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
    #    user32.MessageBoxA(0, u'内容', u'标题', 0)   # 调用MessageBoxA函数
        atexit.register(close)
#        time.sleep(6)
#        sys.exit(0)  #结束进程
##################################################


