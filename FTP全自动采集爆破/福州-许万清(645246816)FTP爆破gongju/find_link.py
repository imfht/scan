#-*-coding:utf-8-*-
'''
    find_link.py. 文件负责接收从FTP破解程序破解后得到的结果文件中进行筛选和获取网页链接。
    流程上:   1> FTP 破解软件在破解完一份数据以后。把success.txt 文件重命名为find_url.txt. 这份文件的格式是:
    0000:0000@www.0000.com/#   内容。
                 2> 我们打开这个文件，首先跟all.txt 文件进行筛选，筛选出没有破解过的FTP信息。然后自身去重下，去除掉
		      带www和不带www的影响。
		 3> 进入到多线程里面去获取他们的链接。每个网页如果失败可以重复尝试打开3次。获取首页链接。并且判断
		      是否是互相交换友链。如果是友链不要，我们只要单向链接。带有.gov.cn 和 .edu.cn 的站不要，这些站不至于去
		      挂链接，不浪费时间。
		 4> 获取到结果先要跟been_ahrefs.txt 文件进行筛选下。然后存入到result.txt文件。result.txt 回由下一级程序。ahrefs_domain.py 接收走
		 
'''
import urllib
import re
import time
import socket
import threading as thread  # 导入线程模块
import sys
import os

socket.setdefaulttimeout(300)
msg_list_lock = thread.RLock()
save_result_lock = thread.RLock()


def  shaixuan_url(been_ahrefs_list, url_list):
    shaixuan_result = []
    for message in url_list:
	message = message.strip()
	new_msg = message
	add = 1
	if(new_msg.find("www") != -1):
	    new_msg = new_msg[4:]
	for source in been_ahrefs_list:
	    if(source.find(new_msg) >= 0):
		add = 0
	if(add == 1):
	    chongfu = 0
	    for item in shaixuan_result:
		if item == message:
		    chongfu = 1
		    break
	    if (chongfu == 0):
	        shaixuan_result.append(message)
    return shaixuan_result

def links_quchong(links_list):
    unique_list = []
    chongfu = 0
    for item in links_list:
	for unique_item in unique_list:
	    if(item == unique_item):
		chongfu = 1
		break
	if(chongfu == 0):
	    unique_list.append(item)
    return unique_list

def result_save(content):
    result_file = open("been_ahrefs.txt", "r")
    result_url_contents = result_file.readlines()
    result_file.close()
    unique_list = shaixuan_url(result_url_contents,content)
    result_file = open("result.txt", "a")
    for item in unique_list:
        result_file.write(item)
	result_file.write("\r\n")
    result_file.close()

def ftp_shaixuan_url(content):
    url_content_list = []
    for message in content:
	i = i + 1
	source_file = open("all.txt", "r+")
	source_content = source_file.readlines()
	message = message.strip()
	message_re = re.compile(r"(?<=@).*?(?=\s|$|/)", re.I|re.S)
	msg = message_re.findall(message)
	new_msg = msg[0]
	add = 1
	if(new_msg[:4] == "www."):
	    new_msg = new_msg[4:]
	for source in source_content:
	    if(source.find(new_msg) >= 0):
		add = 0
	if(add == 1):
	    url_content_list.append(message)
	    source_file.write(message)
	    source_file.write("\n")
	source_file.close()
    return url_content_list

def get_root_link(url):
    try_times = 0
    while(try_times < 3):
        try:
            web_content = urllib.urlopen(url).read()
            href_re = re.compile(r'(?<=href="http://).*?(?=")', re.I|re.S)
            target = href_re.findall(web_content)   # 只要首页链接，其他一概不要
            break
        except:
            try_times = try_times + 1
            continue
    result = []
    for item in target:
        if(item.find("/") != -1):
            if(item.count("/") > 1):
                continue
            elif(item[len(item) - 1] != "/"):
                continue
            else:
                if(item.find("www") != -1):
                    new_msg = item[4:]
                else:
                    new_msg = item
		if(len(new_msg) == 0):
		    continue
                if(new_msg[len(new_msg) - 1] == "/"):
                    new_msg = new_msg[:len(new_msg) - 1]
                if(url.find(new_msg) != -1):
                    continue
                else:
		    # 首先去除掉我们不想要的部分
		    if(item.find(".gov.cn") != -1 or item.find(".edu.cn") != -1):
			continue
		    # 取出掉IP 加端口号的类型
		    ip_re = re.compile(r"^[\d.:]+$", re.I|re.S)
		    if(ip_re.match(item) != None):
			continue
		    # 这里需要做筛选和去除首页友情链接
		    if(item.find("http://") == -1):
		        item = "http://"+ item
		    try_url_times = 0
		    while(try_url_times < 3):
		        try:
			    url_fp = urllib.urlopen(item)
			    url_content = url_fp.read()
			    url_fp.close()
			    break
		        except:
			    try_url_times = try_url_times + 1
                            url_content = ""
			    continue
		    if(url_content != ""):
		        url_re = re.compile(url, re.I|re.S)
		        if(url_re.match(url_content) != None):
			    print item + u"友情链接\r\n"
			    continue
                        result.append(new_msg)
    return result

# 多线程任务
class find_link_thread(thread.Thread):
    def __init__(self, i):
	thread.Thread.__init__(self)    # 默认初始化
	self.thread_id = i
	self.msg_content = ""
	pass
    def run(self):
	global url_content_list
	self.msg_content = ""
	while(1):
	    msg_list_lock.acquire()
	    try:
	        self.msg_content = url_content_list.pop()
	    except:
	        msg_list_lock.release()
	        break	
	    msg_list_lock.release()
	    result = get_root_link(self.msg_content)
	    save_result_lock.acquire()
	    result_save(result)
	    save_result_lock.release()
	print u"线程", str(self.thread_id)+u"退出\n"
        pass

# 读取配置文件
import ConfigParser
config = ConfigParser.ConfigParser()
while(1):
    config.readfp(open("config.ini"))
    thread_cnt = int(config.get("GET_LINK","thread"))
    stop = int(config.get("STOP", "stop"))
    if(stop != 0):
	print u"程序开关关闭,5秒后程序退出"
	time.sleep(5)
	sys.exit(-1)
    # 第一步。先接收success.txt.
    try:
	os.rename("success.txt", "find_url.txt")
    except:
        print u"没有找到接收对象. 继续没做完的工作"
    try:
        url_file = open("find_url.txt", "r")
        url_content = url_file.readlines()
	url_file.close()
    except:
	print u"流水线暂停工作, 20分钟后再启动"
	time.sleep(1200)
	print u"重新启动流水线"
	continue
    print u"接收完成"
    url_content_list = []
    os.remove("find_url.txt")
    # 打开all.txt 文件来进行筛选
    url_content_list = ftp_shaixuan_url(url_content_list)       
    for url in url_content:
        try:
            url = (url.split("@")[1]).split("/")[0]
        except:
	    continue
        if(url.find("http://") == -1):
	    url = "http://" + url
        url_content_list.append(url)
    url_content_list = links_quchong(url_content_list)  
    find_link_set = []
    print u"去重结束,开始获取链接"
    for i in range(0,thread_cnt):
	link_thread = find_link_thread(i)
	find_link_set.append(link_thread)
	link_thread.start()
    for link_thread in find_link_set:
	link_thread.join()
    print  u"获取链接结束. 进入下一轮"
    # 把结果文件交给下一轮
    url_link_fp = open("url.txt", "a")
    result_fp = open("result.txt", "r")
    url_result_content = [line.strip() for line in result_fp.readlines()]
    result_fp.close()
    # 自我去重
    url_result_content = links_quchong(url_result_content)
    for url in url_result_content:
	url_link_fp.write(url)
	url_link_fp.write("\r\n")
    url_link_fp.close()
    os.remove("result.txt")
    
    

    

