__author__ = 'Administrator'
import threading,time

def run(n):
    semaphore.acquire()
    time.sleep(3)
    print("run the thead%s" % n)
    semaphore.release()

if  __name__ == "__main__":
    num = 0
    semaphore = threading.BoundedSemaphore(5) #最多允许5个线程同时执行
    for i in range(23):
        t = threading.Thread(target=run,args=(i,))
        t.start()

while threading.activeCount() != 1:
    pass
else:
    print("all theads is done")
