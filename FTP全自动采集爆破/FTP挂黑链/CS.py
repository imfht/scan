#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import re

data_write="333333"
#向文本中写入数据
def txt_write(ftp_download):  #向文本中写入数据
    try:
        item=ftp_download
        nPos = str(item).rfind('/') #查找字符
        L_1=len(item)
        sStr1 = item[nPos+1:L_1] #复制指定长度的字符
        f = open(sStr1, 'r')
        data=f.read()
        f.close()  #关闭文本
        if (re.compile(data_write,re.I|re.S).search(data) != None):  #正则查询
            print u"已经有要写入的数据了不在写入" #消息提示
            return 0
        else:
            file_object = open(sStr1,'w')  #追加写文件
            file_object.write(data_write)
            file_object.write("\n")
            file_object.writelines(data)  #写入多行
            file_object.close()
            return 1
    except:
        print u"写入数据%s失败"%(ftp_download) #消息提示
        return 0


if __name__=='__main__':
    txt_write("wwwroot.txt")  #向文本中写入数据


