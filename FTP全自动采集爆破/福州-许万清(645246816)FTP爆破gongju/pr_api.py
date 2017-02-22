#-*- coding:utf-8 -*-
import urllib2
import re
class pr_api:
    def getpr(self,domain, proxy=""):
        null_proxy_handler = urllib2.ProxyHandler({})
        if proxy != "":
            proxy_handler = urllib2.ProxyHandler({"http":proxy})
            opener = urllib2.build_opener(proxy_handler)
        else:
            opener = urllib2.build_opener(null_proxy_handler)
        domain = domain.replace('http://','').strip()
        url = "http://toolbarqueries.google.com/tbr?client=navclient-auto&features=Rank&ch=%s&q=info:%s"%(self.google_hash(domain),domain)
        try:
            result = opener.open(url).read()[9:]
        except:
            opener = urllib2.build_opener(null_proxy_handler)
            try:
                result = opener.open(url).read()[9:]
            except:
                result = -1
        return result
    def google_hash(self,value):
        GPR_HASH_SEED = "Mining PageRank is AGAINST GOOGLE’S TERMS OF SERVICE.Yes,I’m talking to you,scammer."
        magic = 0x1020345
        for i in xrange(len(value)):
            magic ^= ord(GPR_HASH_SEED[i % len(GPR_HASH_SEED)]) ^ ord(value[i])
            magic = (magic >> 23 | magic << 9) & 0xFFFFFFFF
        return "8%08x" % (magic)

if __name__ == "__main__":
    pr = pr_api()
    print pr.getpr('www.baidu.com', "85.10.202.142:3128")
    print pr.getpr('www.customnfljerseyssus.com', "95.80.92.52:3128")
    print pr.getpr('www.baidu.com', "190.248.67.146:8080")
    print pr.getpr('www.customnfljerseyssus.com', "41.75.201.146:3128")
    print pr.getpr('www.baidu.com', "117.218.37.18:3128")
    print pr.getpr('www.customnfljerseyssus.com', "116.213.49.171:8080")
