#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

if __name__ == '__main__':
    import sys
    import socket
    socket.setdefaulttimeout(10)

    if len(sys.argv)!=4:
        print '传入参数不对python c1.py %s %s %s\n'
    else:
        print sys.argv[1].strip()
        print sys.argv[2].strip()
        print sys.argv[3].strip()


