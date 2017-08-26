__author__ = 'Administrator'

import threading,time

def run(n):
    print("task %s" % n,threading.current_thread(),threading.activeCount())
    time.sleep(2)
    print("task done",n)

start_time = time.time()
join_arr = []
for i in range(50):
   t = threading.Thread(target=run,args=("t%s"% i,))
   t.setDaemon(True)
   t.start()
   join_arr.append(t)

# for t in join_arr:
#     t.join()

print("cost:",time.time()-start_time,threading.current_thread(),threading.activeCount())
# t1.start()
# t2.start()

