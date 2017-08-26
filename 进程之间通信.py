__author__ = 'Administrator'

import multiprocessing,time,threading,queue
import os

def f(q):
    q.put([4,None,"hello"])
'''
  不同进程间内存是不共享的,要想实现两个进程间的数据交换,可以使用以下方法:
'''
if __name__ == "__main__":
  q = queue.Queue()
  p = multiprocessing.Process(target=f,args=(q,))
  p.start()