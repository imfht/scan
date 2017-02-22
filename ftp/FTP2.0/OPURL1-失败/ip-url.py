#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#飞龙  QQ316118740  BLOG http://hi.baidu.com/alalmn
"""
*****读取网页源码=====遍历URL提取网址=====添加到数据库*****
"""
import list #数组类
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
                    #print shref,u"没有找到非法HTTP地址"
                    print "#",
                else:
                    #print shref   #"查找到了正确URL地址"
                    a1=URL_TQURL(shref) #URL提取URL
#                    print ""
#                    print a1
                    mysql_add(a1)  #添加到数据库
#        mysql.mysql_S()  #保存数据
#        open_mysql()  #读取URL
        # 上面是将每条<a></a>里面的内容和地址给匹配出来
    except:
        #print u"这个URL地址无效！！！！！！！！！！！！！！"
        mysql.mysql_S()  #保存数据
#        open_mysql()  #读取URL
##################################################

def mysql_add(data1):  #添加到数据库
    try:
    #    print "++++++++++++++++++++",data   #添加数据
        sql="select * from url where url='%s'"%(data1)
        data = mysql.mysql_select(sql)
        if data.find('null123456'):
            #print u"已经有了这个URL",data1
            return 0
        else:  #没有可以添加
            #print data1
            if ~(data1.find("/") and data1.find("http") and data1.find("?") and data1.find("%")):
                #print u"非法URL"
                return 0
            else:
                LS.liet_add(data1)   #添加到数组
                if LS.liet_CX("AAAAA"):  #查询数据是否存在
                    print u"\n数组里以有这个域名不添加",data1
                    return 0
                else:
                    #print u"无"
                    insert="insert into url(url,time) VALUES('%s','%s')"%(data1,time.strftime('%Y.%m.%d-%H.%M.%S'))
                    #print insert
                    if mysql.mysql_insert(insert): #添加数据
                        mysql.mysql_S()   #提交
                        print u"\n添加成功",data1
                    else:
                        print u"\n添加失败",data1
    except:
        return 0
##################################################
##################################################
import socket
import threading,time
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
#查看IP端口是否开放
class socket_port(threading.Thread):
    def __init__(self,cond, name):
        super(socket_port, self).__init__()
        self.cond = cond
        self.cond.set()#将标识位设为Ture
        self.HOST = name
    def run(self):
        #time.sleep(1) #确保先运行Seeker中的方法
        try:
            PORT=80
            #PORT2=21
            #2端口都要开放
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.HOST,PORT))
            #print u"\n",self.HOST,u":",PORT,u"端口开放"
            #s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #s2.connect((self.HOST,PORT2))
            print u"\n",self.HOST,u":",PORT,u"端口开放"
            #print self.HOST,u":",PORT,u":",PORT2,u"端口开放",
            bing_url=('http://cn.bing.com/search?q=ip:%s&go=&form=QBLH&filt=all&qs=n')%(self.HOST)
            URL_DZ(bing_url)  #遍历页里的地址
#            sql_desc = "insert into port21(IP,TIME) VALUES('%s','%s')"%(self.HOST,time.strftime('%Y.%m.%d-%H.%M.%S'))
#            if mysql.mysql_insert(sql_desc): #添加
#                print u"添加成功"
#            else:
#                print u"添加失败"
#            mysql.mysql_S()  #保存数据
            #self.cond.wait()#堵塞线程，直到Event对象内部标识位被设为True或超时（如果提供了参数timeout）。
            self.cond.set()#将标识位设为Ture
            return 1
        except:
            print ".",
            #print self.HOST,u":",PORT,u"端口未开放"
            #self.cond.wait()#堵塞线程，直到Event对象内部标识位被设为True或超时（如果提供了参数timeout）。
            self.cond.set()#将标识位设为Ture
        return 0
    ##
#socket_port("192.168.2.1")
#if socket_port("192.168.2.100"):
#    print "开放"
#else:
#    print "未开放"

def ip2num(ip):
    ip = [int(x) for x in ip.split('.')]
    return ip[0]<<24 | ip[1]<<16 | ip[2]<<8 | ip[3]

def num2ip(num):
#time.sleep(0.05) #50ms
#time.sleep(0.1) #s
#    data='%s.%s.%s.%s' % (  (num & 0xff000000) >> 24,
#                                 (num & 0x00ff0000) >> 16,
#                                 (num & 0x0000ff00) >> 8,
#                                  num & 0x000000ff  )
#    #socket_port(data)  #查看IP端口是否开放
    if num>=IPend:
        print u"IP导入数组完成"
    return '%s.%s.%s.%s' % (  (num & 0xff000000) >> 24,
                              (num & 0x00ff0000) >> 16,
                              (num & 0x0000ff00) >> 8,
                              num & 0x000000ff  )

def gen_ip(ip1,ip2):  #返回数组
#    ip
#    global IPend
#    start, IPend = [ip2num(x) for x in ip.split('-')]
    global IPend
    IPend=ip2
    return [num2ip(num) for num in range(ip1,ip2+1) if num & 0xff]
##################################################
import ini
if __name__=='__main__':
    global LS
    LS = list.Clist()  #初始化类
    #http://ip.chinaz.com/?IP=www.163.com
#    URL="http://cn.bing.com/search?q=ip:61.153.56.166&go=&form=QBLH&filt=all&qs=n"
#    URL_DZ(URL)  #遍历页里的地址
    mysql.mysql_open()  #连接数据库
    ini.ini_get()  #读取INI
    print u"开始IP:",ini.IP1,u"-------",u"结束IP:",ini.IP2
    if ini.IP1>=ini.IP2:
        print u"IP以扫描完成"

    print u"IP还没扫描完"
    list_ip=gen_ip(ip2num(ini.IP1),ip2num(ini.IP2))
    I1 = 0 #得到list的第一个元素
    print u"开始扫描IP"
    ip=0
    while I1 < len(list_ip):
        if ip>=255:
            ini.ini_write(int(ini.ID),list_ip[I1],ini.IP2)  #修改INI
            ip=0
            print list_ip[I1]
        ip = ip + 1
        time.sleep(0.3) #确保先运行Seeker中的方法
        cond = threading.Event()
        hider = socket_port(cond,list_ip[I1])
        hider.start()

        I1 = I1 + 1   #一层

    print u"IP扫描完成将从新导入"