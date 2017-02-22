#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
"""
*****读取网页源码=====遍历URL提取网址=====添加到数据库*****
"""

################################################
################################################
################################################
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

import urllib2, re, time
import list
import mysql #数据库操作文件
def URL_DZ(URL):  #遍历页里的地址
    try:
        LS = list.Clist()  #初始化类
        LS.list_del()  #清空list列表
        s = urllib2.urlopen(URL,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        ss = s.read()
        p = re.compile( r'<a.+?href=.+?>.+?</a>' )
        pname = re.compile( r'(?<=>).*?(?=</a>)' )
        phref = re.compile( r'(?<=href\=\").*?(?=\")')
        #构造及编译正则表达式
        sarr = p.findall(ss)
        #找出一条一条的<a></a>标签
        #这添加到数组在过滤重复值减少mysql压力
        i=0
        for every in sarr:
            if i>=3000:
                print u"超过3000个URL地址！！！！！！\n"
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
                    print shref,u"非法HTTP地址"
                else:
                    #print shref   #"查找到了正确URL地址"
                    a1=URL_TQURL(shref) #URL提取URL
                    LS.liet_add(a1)  #添加到数组

        LS.liet_lsqc() #数组列表去重复
        print u"原URL数据量：",len(LS.list)
        print u"去掉重复URL剩下数据量：",len(LS.list_2)
        time.sleep(1)
        E = 0 #得到list的第一个元素
        while E < len(LS.list_2):
              #添加到数据库
            if mysql_add(LS.list_2[E]):
                print "_-_"  #添加成功
            else:
                print "-_-"  #添加失败
            #print "\n",LS.list_2[E],
            E = E + 1
        mysql.mysql_S()  #保存数据
        print u"-----------------------URL列表添加完成-----------------------"
        open_mysql()  #读取URL

        # 上面是将每条<a></a>里面的内容和地址给匹配出来
    except:
        print u"这个URL地址无效！！！！！！！！！！！！！！"
        mysql.mysql_S()  #保存数据
        open_mysql()  #读取URL
##################################################
def get_sdomain(domain):  #域名拆解www.baidu.com->baidu.com
    suffixes = 'ac', 'ad', 'ae', 'aero', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'arpa', 'as', 'asia', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'biz', 'bj', 'bm', 'bn', 'bo', 'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cat', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'com', 'coop', 'cr', 'cu', 'cv', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'edu', 'ee', 'eg', 'er', 'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gov', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'info', 'int', 'io', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jobs', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mg', 'mh', 'mil', 'mk', 'ml', 'mm', 'mn', 'mo', 'mobi', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'name', 'nc', 'ne', 'net', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'org', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'pro', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'st', 'su', 'sv', 'sy', 'sz', 'tc', 'td', 'tel', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'xn', 'ye', 'yt', 'za', 'zm', 'zw'
    sdomain = []
    bdomain = False
    for section in domain.split('.'):
        if section in suffixes:
            sdomain.append(section)
            bdomain = True
        else:
            sdomain = [section]
    return '.'.join(sdomain) if bdomain  else ''

def mysql_select2(data):  #模糊查询
    try:
        i=0
        n = mysql.cursor.execute(data)
        mysql.cursor.scroll(0)
        for row in mysql.cursor.fetchall():
            #print '%s-%s-%s'%(row[0],row[1],row[2])
            #return row[0]
            if i>=10:
                return i
            i=i+1
        return 0
    except:
        return 0

def mysql_add(data1):  #添加到数据库
    try:   #查看这个数据是否值得添加
        dURL=get_sdomain(data1)  #拆解域名1234.163.com=》163.com
        #在模糊查询看看有多少个  》=10个  这个就不进行添加
        #print dURL
        sql="select * from url where url like '%%%s'"%(dURL)
        #print sql
        if mysql_select2(sql):  #模糊查询
            print dURL,u"域名下已经有10个二级域名了不进行添加",
            return 0
        else:
            #print "没有可以添加"
        #    print "++++++++++++++++++++",data   #添加数据
            sql="select * from url where url='%s'"%(data1)
            data = mysql.mysql_select(sql)
            if data.find('null123456'):
                print u"已经有了这个URL",data1,
                return 0
            else:  #没有可以添加
                #print data1
                if ~(data1.find("/") and data1.find("http") and data1.find("?") and data1.find("%")):
                    print data1,u"非法URL",
                    return 0
                else:
                    insert="insert into url(url,time) VALUES('%s','%s')"%(data1,time.strftime('%Y.%m.%d-%H.%M.%S'))
                    #print insert
                    if mysql.mysql_insert(insert): #添加数据
                    #mysql.mysql_S()   #提交
                        print data1,u"添加成功",
                        return 1
                    else:
                        print data1,u"添加失败",
                        return 0
        return 0
    except:
        return 0
#    try:
#    #    print "++++++++++++++++++++",data   #添加数据
#        sql="select * from url where url='%s'"%(data1)
#        data = mysql.mysql_select(sql)
#        if data.find('null123456'):
#            print u"已经有了这个URL",data1
#            return 0
#        else:  #没有可以添加
#            #print data1
#            if ~(data1.find("/") and data1.find("http") and data1.find("?") and data1.find("%")):
#                print data1,u"非法URL"
#                return 0
#            else:
#                insert="insert into url(url,time) VALUES('%s','%s')"%(data1,time.strftime('%Y.%m.%d-%H.%M.%S'))
#                #print insert
#                if mysql.mysql_insert(insert): #添加数据
#                #mysql.mysql_S()   #提交
#                    print data1,u"添加成功"
#                else:
#                    print data1,u"添加失败"
#        return 1
#    except:
#        return 0
################################################
def open_mysql():  #读取URL
    try:
        sql="select * from url where httpsend is NULL limit 1"
        data = mysql.mysql_select(sql)
        #print U"数据库URL",data
        if ~data.find("null123456"):
            print u"可能无读取的数据请查看数据库！！！！！"
            mysql.mysql_S()  #保存数据
            time.sleep(1)  #3秒
            atexit.register(close)#自动重启本程序
        update = "update url set httpsend='send' where url='%s'"%(data)
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
################################################
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


if __name__=='__main__':
    try:
        #print __doc__
        print u"*****读取网站首页源码=====遍历URL提取网址=====添加到数据库*****"
        mysql.mysql_open()  #连接数据库
        open_mysql()     #读取URL

#        url_data = "http://"+"163.com"
#        print u"读取URL：",url_data
#        URL_DZ(url_data)  #遍历页里的地址
    except:
        atexit.register(close)











