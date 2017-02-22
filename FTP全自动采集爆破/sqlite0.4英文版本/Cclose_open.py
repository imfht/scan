#!/usr/local/bin/python
##################################################
import time
import threading
import ConfigParser
import os

class CS_close_open(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.close_open=100
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("gost.ini"))
            self.close_open = int(config.get("DATA","close_open"))
        except:
            print "INI--try: except:close_open"
        #self.run()

    def run(self):
        try:
            for i in range(self.close_open):
                time.sleep(60)
                delete="#################run%d  time#################"%(i)
                print delete
                if i>=self.close_open-1:
                    data2=os.getcwd()
                    data2="%s\\main.exe"%(data2)
                    print data2
                    os.system('close_open.exe main.exe %s'%(data2))
                    #os.system('close_open.exe VStart.exe C:\Users\Administrator.PC-20130126ZMFE\Desktop\cs1111111111111\close_open\Debug')
                    break
        except:
            time.sleep(60)
            self.run()



if __name__=='__main__':
    threads = []
    nthreads=1
    for i in range(nthreads):
        threads.append(CS_close_open())

    for thread in threads:
        thread.start()



