#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##################################################################
#from ftplib import FTP
#import time
#import time
#import thread

#def close():  #自动重启本程序
#    print u"3秒后,程序将结束重启..."
#    print u"自动重启本程序"
#    time.sleep(5)
#
#
#if __name__=='__main__':
#    thread.start_new_thread(close)

#import threading
#import time
#class timer(threading.Thread): #The timer class is derived from the class threading.Thread
#    def __init__(self, num, interval):
#        threading.Thread.__init__(self)
#        self.thread_num = num
#        self.interval = interval
#        self.thread_stop = False
#
#    def run(self): #Overwrite run() method, put what you want the thread do here
#        while not self.thread_stop:
#            print 'Thread Object(%d), Time:%s\n' %(self.thread_num, time.ctime())
#            time.sleep(self.interval)
#    def stop(self):
#        self.thread_stop = True
#
#
#def test():
#    thread1 = timer(1, 1)
#    thread2 = timer(2, 2)
#    thread1.start()
#    thread2.start()
#    time.sleep(10)
#    thread1.stop()
#    thread2.stop()
#    return
#
#if __name__ == '__main__':
#    test()

#import time
#import thread
#def timer(no, interval):
#    print u"3秒后,程序将结束重启..."
#    time.sleep(5)
#    thread.exit_thread()
#
#
#def test(): #Use thread.start_new_thread() to create 2 new threads
#    thread.start_new_thread(timer, (1,1))
#    thread.start_new_thread(timer, (2,2))
#
#if __name__=='__main__':
#    test()
Python高级编程
上海-做梦的傻(114660483)  17:41:30
import timeimport threaddef timer(no,interval):
print u"retstar %d"%no
time.sleep(5)
thread.exit_thread()

def test():
Use thread.start_new_thread() to create 2 new threads
thread.start_new_thread(timer, (1,1))
thread.start_new_thread(timer, (2,2))

if __name__=='__main__':
test()