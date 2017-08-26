__author__ = 'Administrator'
'''
  队列::---解耦,是程序直接实现松耦合,提高处理效率
  python的多线程不适合cpu密集型的任务,适合io密集型的任务
  什么是io密集型的呢,例如socketServer就是io密集型的
  在python里面怎么做???
  可以使用多进程,python的进程也是用的原生操作系统的进程
  两个进程之间的顺序不能相互访问 所以不需要锁 (gil) 的概念
  每个进程下面至少有一个线程

'''
import multiprocessing,time,threading

def thread_run():
    print(threading.get_ident())

def run(name):
    time.sleep(2)
    print("hello world",name)
    t = threading.Thread(target=thread_run)
    t.start()
if __name__ == "__main__":
   for i in range(10):
       p = multiprocessing.Process(target=run,args=("bob %s" % i,))
       p.start()
