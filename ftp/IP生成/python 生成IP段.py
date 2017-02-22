#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
####################################################################
#qq:316118740
#BLOG:http://hi.baidu.com/alalmn
# python 生成IP段
#  刚学写的不好请大家见谅
####################################################################
if __name__ == '__main__':
    xxx=file('test.txt','w')
    for IP1 in range(254,0,-1):
        for IP2 in range(254,0,-1):
            #for IP3 in range(254,0,-1):
                #for IP4 in range(254,0,-1):
                    #print IP1,IP2
                abc= '%s.%s.%s-%s.%s.%s\n' % (IP1,IP2,"1.1",
                                       IP1,IP2,"255.255")
                xxx.write(abc)
    xxx.close()