#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import time
import webbrowser #访问URL
def show_url(url): #正常打开RUL
    try:
        webbrowser.open_new_tab(url)
        return 1
    except BaseException, e:
        print(str(e))
        return 0

if __name__ == "__main__":
    xxx = file("123.txt", 'r')
    for xxx_line in xxx.readlines():
        data=xxx_line.strip().lstrip().rstrip('\n')
        print data
        time.sleep(5)
        show_url(str(data)) #正常打开RUL
    print u"遍历完成"

