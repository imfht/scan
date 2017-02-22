#!/usr/local/bin/python
#  QQ316118740  BLOG http://hi.baidu.com/alalmn
class Clist:
    def __init__(self):
        #self.list
        self.list=[]
        #self.list_2
        self.list_2=[]

    def list_del(self):
        try:
            i = 0
            while i < len(self.list):
                del self.list[i]

            i2 = 0
            while i2 < len(self.list_2):
                del self.list_2[i2]
        #########################################
        except:
            return 0

    def liet_lsqc(self):
        try:
            for i in self.list:
                if i not in self.list_2:
                    self.list_2.append(i)
        except:
            return 0

    def liet_add(self,data):
        try:
            if len(self.list)>=4100:
                return 0

            self.list.append(data)

        except:
            return 0
    def liet_CX(self,data):
        try:
                    E = 0
                    while E < len(self.list_2):
                        #print self.list_2[E]
                        if self.list_2[E]==data:
                            return 1
                        E = E + 1
                    return 0
        except:
            return 0

