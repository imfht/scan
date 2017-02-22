# -*- coding: cp936 -*-

import logging
import traceback
import multiprocessing
import os
import argparse

'''多进程模块，给任何单任务提供多进程接口,可根据类似思路编写自动生成代码的代码'''

class multi_process(multiprocessing.Process):
    '''设置函数名及函数参数列表---第一个元素为元组列表，第二个元素为关键词字典列表'''
    def __init__(self,func_name,func_arg):
        multiprocessing.Process.__init__(self)
        self.func_name=func_name
        self.func_arg=func_arg
    def set_func_name(self):
        self.func_name=''
    def run(self):
        try:
            apply(self.func_name,self.func_arg)
        except:
            pass

def process_job(process_num,func_name,arg_list):
    process_list=[]
    for i in range(process_num):
        print arg_list[i]
        p=multi_process(func_name,arg_list[i])
        process_list.append(p)
    for i in range(process_num):
        process_list[i].daemon=True
        process_list[i].start()
    for i in range(process_num):
        process_list[i].join()

def test(fn):
    print fn

if __name__=="__main__":
    process_job(3,test,[1,2,3])