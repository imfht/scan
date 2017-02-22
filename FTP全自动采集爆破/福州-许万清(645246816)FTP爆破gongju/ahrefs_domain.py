#-*coding:utf8*-
import urllib2,urllib
import simplejson
import re
import urllib
import os
import socket
import cookielib
import urllib
import urllib2
import threading as thread  # 导入线程模块
import math
from time import time 
import time as timer
import socket
from collections import defaultdict, deque

socket.setdefaulttimeout(300)

save_lock = thread.RLock()
list_lock = thread.RLock()
result_lock = thread.RLock()

def Save(content):
    fail_file = open("content.html", "w")
    fail_file.write(content+"\r\n")
    fail_file.close()

def result_save(content):
    result_file = open("result.txt", "a")
    for item in content:
        result_file.write(item)
	result_file.write("\r\n")
    result_file.close()

# 多线程任务
class ahrefs_thread(thread.Thread):
    def __init__(self, i):
	thread.Thread.__init__(self)    # 默认初始化
	self.thread_id = i
	self.url_content = ""
	pass
    def run(self):
	ahrefs_link = Ahrefs()
	ahrefs_link.begin_ahrefs()
	print u"线程", str(self.thread_id)+u"退出\n"
        pass

class  Ahrefs:
    def __init__(self):
	self.href_list = []
	pass
    def begin_ahrefs(self):
	global ahrefs_set
	# 第一步登录
	post_url = "https://ahrefs.com/users/login.php"
	data = {'email':'barbuzdb@hotmail.com', 'password':'fery1950'}
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
	    list_lock.acquire()
	    try:
	        url = ahrefs_set.popleft()
		trytimes = 0
		list_lock.release()
	    except:
		list_lock.release()
		timer.sleep(2)
		try_times = try_times + 1
		if(try_times == 10):
		    result_lock.acquire()
		    result_save(self.href_list)
		    result_lock.release()
		    return
		else:
		    continue
	    print url
	    try:
	        response = opener.open(url)
	        content = response.read()
	    except Exception,e:
		print e
		continue
	    target_str = "(?<=title=\"Open in a new tab:\s).*?(?=\")"
	    target_re = re.compile(target_str, re.I|re.S)
	    find_text = target_re.findall(content)
	    if(find_text == []):
		continue
	    for node in find_text:
		self.href_list.append(node)
	    if(len(self.href_list) > 100):
		result_lock.acquire()
		result_save(self.href_list)            # 保存起来
		result_lock.release()
		self.href_list = []
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
		        list_lock.acquire()
		        ahrefs_set.append(new_insert)
			list_lock.release()
ahrefs_file = open("url.txt", "r")
ahrefs = [line.strip() for line in ahrefs_file.readlines()]
ahrefs_file.close()
start = time()
ahrefs_set = deque()   #list数组
# 前面全部补齐为ahrefs语句
for i in range(0, len(ahrefs)):
    if(ahrefs[i].find("http://") != -1):
	print u"查询域名不能带http://, 请删除.\r\n"
	timer.sleep(5)
	import sys
	sys.exit(-1)
    ahrefs_set.append("https://ahrefs.com/site-explorer/refdomains/subdomains/"+ahrefs[i]+"/")    
thread_cnt = int(raw_input("input the thread count"))
start = time()
cap_set = []
for i in range(0,thread_cnt):
    print  u"线程", i,"\n"
    cap_thread = ahrefs_thread(i)
    cap_set.append(cap_thread)
    cap_thread.start()
for cap_thread in cap_set:
    cap_thread.join()
print  u"查询结束\n"
end = time()
print str(end-start)+"second\n"