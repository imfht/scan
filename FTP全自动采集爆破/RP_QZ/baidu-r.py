#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import re
import urllib
import threading
import time
import Cmysql #数据库操作文件
class CS_QZ_RP(threading.Thread):   #测试权重和RP
    def __init__(self,htint):
        threading.Thread.__init__(self)
        self.Ht=htint
        self.sql=Cmysql.mysql_handle()
        self.sql.mysql_open()


    def run(self):
        try:
            print u"----CS_QZ_RP线程%d启动----"%(self.Ht)
            self.SQL_slect("select * from ftppassword3")  #获取数量
            #print self.baidu_qz("www.ws8.org")  #百度权重查询
            #print self.getPr("www.ws8.org")  #rp查询
        except:
            print u"----线程%d--CS_QZ_RP---run异常！！！！！----"%(self.Ht)
            time.sleep(60)
            self.run()

    def SQL_slect(self,sql):  #获取数量
        self.i=0
        try:
            print u"测试网站权重--PR开始"
            #sql="select * from ftppassword3"
            self.cursor=self.sql.conn.cursor()
            n = self.cursor.execute(sql)
            self.cursor.scroll(0)
            for row in self.cursor.fetchall():
                data_qz=self.baidu_qz(row[0])  #百度权重查询
                data_pr=self.getPr(row[0])  #rp查询
                print u"%s网站权重%s网站PR%s"%(row[0],str(data_qz),str(data_pr))
                if str(data_qz)=="NO":
                    update="update ftppassword3 set PR='%s' where IP='%s'"%(str(data_pr),row[0])
                else:
                    update="update ftppassword3 set baiduQZ='%s',PR='%s' where IP='%s'"%(str(data_qz),str(data_pr),row[0])
                #print update
                self.sql.mysql_update(update)
                self.sql.mysql_S()  #保存数据
                time.sleep(20)
            self.cursor.close()
        except:
            time.sleep(4)
            self.sql.mysql_S()  #保存数据
            #self.SQL_slect()     #读取URL
#####################################################
    def sockPage(self,url):
        try:
            sockPage = urllib.urlopen(url)
            data = sockPage.read()
            utf8data = data.decode("utf-8")
            return utf8data
        except:
            print u"URL读取失败"
            return "NO4"
##############################################
    def getPr(self,url):
        try:
            self.chinaz = "http://pr.chinaz.com"
            #提交一次，http://pr.chinaz.com/?PRAddress=
            #取得enkey
            data = self.sockPage("%s/?PRAddress=%s"%(self.chinaz,url))
            enkey = self.getEnkey(data)
            #访问查询Pr页
            prHostUrl = "%s/ajaxsync.aspx?at=pr&enkey=%s&url=%s"\
                        % (self.chinaz,enkey,url)
            pageHtml = self.sockPage(prHostUrl)
            #print pageHtml
            #匹配出Pr数值
            patten = re.compile(r'[0-9]')
            pr =  patten.search(pageHtml).group(0)
            return pr
        except:
            print u"=======%sRP查询失败"%(url)
            return "NO3"

    def getEnkey(self,data):
        try:
            enkeyPoit = data.find('enkey')
            enkey =  data[enkeyPoit+6:enkeyPoit+38]
            return enkey
        except:
            return "NO2"
##############################################
    def baidu_qz(self,url):  #百度权重查询
        try:
            dataurl="http://mytool.chinaz.com/baidusort.aspx?host=%s+&sortType=0"%(url)
            pageHtml=self.sockPage(dataurl)
            aadata=u"百度权重为 <font color=\"\">(.*?)</font>"
            patten = re.compile(aadata)
            data=patten.search(pageHtml).group(1)
            return data
        except:
            #print u"=======%s百度权重查询失败"%(url)
            return "NO"
##############################################
if __name__ == "__main__":
    threads = []  #线程
    nthreads=1
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(CS_QZ_RP(i))

    for thread in threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程
