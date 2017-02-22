
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