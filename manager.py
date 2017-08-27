__author__ = 'Administrator'

import multiprocessing,os

def f(d,l):
    d[1]="1"
    d["2"] =2
    d[0.24]=None
    d[os.getpid()]=os.getppid()
    l.append(os.getpid())
    print(l)
if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        d = manager.dict() #生成一个字典，可在多个进程间共享和传递

        l = manager.list(range(5)) #生成一个列表，可在多个进程间共享和传递
        p_list = []
        for i in range(10):
            p = multiprocessing.Process(target = f,args=(d,l,))
            p.start()  #一定记得启动进程
            p_list.append(p)
        for res in p_list:#等待结果
            res.join()
        print(os.getpid())
        print(l)
        print(d)