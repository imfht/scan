#!/usr/local/bin/python

import SlinkFTP
import Sopenftp
import Sopenurl
import Sthread
import Ssqlite_delete
import SpasswordFTP

import Cclose_open
import time
import ctypes
import thread


def Crun():
    thrint=1
    t_h=Sthread.CS_Cthread()
    Copenurl_nthreads=t_h.openurl()
    Copenftp_nthreads=t_h.openftp()
    ClinkFTP_nthreads=t_h.linkftp()
    print "-"*60
    #time.sleep(10)
    ###########################
    Cclose_open_threads = []
    Cclose_open_nthreads=1
    for i in range(Cclose_open_nthreads):
        Cclose_open_threads.append(Cclose_open.CS_close_open())

    for thread in Cclose_open_threads:
        thread.start()
    ###########################
    t_delete=Ssqlite_delete.CS_mysql_delete()
    t_delete.open_mysql()
    print "-"*60

    Cmysql_delete_threads = []
    Cmysql_delete_nthreads=1
    for i in range(Cmysql_delete_nthreads):
        Cmysql_delete_threads.append(Ssqlite_delete.CS_mysql_delete())

    for thread in Cmysql_delete_threads:
        thread.start()

    ###########################
    CpasswordFTP_threads = []
    CpasswordFTP_nthreads=1
    for i in range(CpasswordFTP_nthreads):
        CpasswordFTP_threads.append(SpasswordFTP.CS_passwordFTP())

    for thread in CpasswordFTP_threads:
        thread.start()
    ###########################
    Copenurl_threads = []
    for i in range(Copenurl_nthreads):
        Copenurl_threads.append(Sopenurl.CS_openurl(thrint))
        thrint=thrint+1

    for thread in Copenurl_threads:
        time.sleep(1)
        thread.start()
    ###########################
    Copenftp_threads = []
    for i in range(Copenftp_nthreads):
        Copenftp_threads.append(Sopenftp.CS_openftp(thrint))
        thrint=thrint+1

    for thread in Copenftp_threads:
        time.sleep(1)
        thread.start()
    ###########################
    ClinkFTP_threads = []
    for i in range(ClinkFTP_nthreads):
        ClinkFTP_threads.append(SlinkFTP.CS_linkftp(thrint))
        thrint=thrint+1

    for thread in ClinkFTP_threads:
        time.sleep(1)
        thread.start()
    ###########################

    ###########################
    ###########################
    ###########################
    ###########################


##################################################
import sys
import os
import atexit
def close():
    try:
        time.sleep(10)
        python = sys.executable
        os.execl(python, python, * sys.argv)
        #########
    except:
        sys.exit(0)

def intet_close():
    dll=ctypes.CDLL("internet_close.dll")
    add=dll.Fun_Internet
    add.restypes=ctypes.c_int
    INIclose=0
    while 1:
        INIclose=INIclose+1
        if INIclose>=100:
            INIclose=0
            time.sleep(10)
            atexit.register(close)
        try:
            Ainternet=add()
            if str(Ainternet)=="0":
                time.sleep(1)
                atexit.register(close)
            else:
                result = {
                    "1" : "1",
                    "2" : "2",
                    "3" : "3",
                    "4" : "4",
                    "5" : "5"
                }
                print "----",INIclose,"----",result.get(str(Ainternet)),time.strftime('%Y.%m.%d-%H.%M.%S')

        except:
            print "--------NOInternet ---time.sleep--------"
            time.sleep(3)
            atexit.register(close)
        time.sleep(20)

def Aintet_close():
    dll=ctypes.CDLL("internet_close.dll")
    add=dll.Fun_Internet
    add.restypes=ctypes.c_int

    try:
        Ainternet=add()
        if str(Ainternet)=="0":
            time.sleep(1)
            atexit.register(close)
            return 0
        else:
            result = {
                "1" : "1",
                "2" : "2",
                "3" : "3",
                "4" : "4",
                "5" : "5"
            }
            print "----",result.get(str(Ainternet)),time.strftime('%Y.%m.%d-%H.%M.%S')
            return 1
    except:
        print "--------NOInternet ---time.sleep--------"
        return 0

if __name__=='__main__':
    print "---------------------------------------------------------------------"
    print "      FTP--webshell--sqlite--0.4            "
    print "      BLOG--http://hmhacker.org/            "
    print "----------------------time 2013.4.24--------------------------"
    print "----------------------------------------------------------------------"
    #time.sleep(10)
    try:
        if Aintet_close():
            Crun()
            thread.start_new_thread(intet_close())
        else:
            print "NOInternet ---time.sleep10S"
            time.sleep(5)
            atexit.register(close)
    except:
        time.sleep(10)
        atexit.register(close)










