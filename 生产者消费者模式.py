__author__ = 'Administrator'

import time,queue,threading
q = queue.Queue(maxsize=10)
def Product(name):
    count = 1
    while True:
           q.put("骨头%s" % count)
           print("生产了骨头",count)
           count+=1
           time.sleep(2)
           print(threading.active_count())

def Consumer(name):
    while q.qsize()>0:
        print("[%s] 取到[%s] 并且吃了它" %(name,q.get()))


p = threading.Thread(target=Product,args=("xxx",))

c = threading.Thread(target=Consumer,args=("crh",))

p.start()
c.start()