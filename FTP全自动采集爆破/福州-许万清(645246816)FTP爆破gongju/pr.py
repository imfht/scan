#coding=utf-8
import re
import urllib

class Prer:
    """查询网站的PR值"""
    def __init__(self):
        self.chinaz = "http://pr.chinaz.com"
       
    def getPr(self,url):
        #提交一次，http://pr.chinaz.com/?PRAddress=
        #取得enkey
        try:
            data = self.sockPage("%s/?PRAddress=%s"%(self.chinaz,url))
            enkey = self.getEnkey(data)
            #访问查询Pr页
            prHostUrl = "%s/ajaxsync.aspx?at=pr&enkey=%s&url=%s"\
            % (self.chinaz,enkey,url)
            pageHtml = self.sockPage(prHostUrl)
            #print pageHtml
            #匹配出Pr数值
            patten = re.compile(r'[0-9]')
            pr =  patten.search(pageHtml).group(0)
            return pr
        except:
            return 0

    def sockPage(self,url):
        sockPage = urllib.urlopen(url)
        data = sockPage.read()
        utf8data = data.decode("utf-8")
        return utf8data

    def getEnkey(self,data):
        enkeyPoit = data.find('enkey')
        enkey =  data[enkeyPoit+6:enkeyPoit+38]
        return enkey

if __name__ == "__main__":
    pr = Prer()
    while True:
        #url = raw_input("Enter Domain:")
        url = "http://www.customnfljerseyssus.com"
        url = url.strip()
        try:
            print "PR:", pr.getPr(url)
        except Exception,e:
            print "Get pr false:",e
