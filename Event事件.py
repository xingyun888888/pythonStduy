__author__ = 'Administrator'

'''
  An event is a simple sysnchronization object;
  the event represents an internal flag,and threads
  can wait for the flag to be set,or set or clear the flag themselves.

  event = threading.Event()

  如果标志位设定了,代表绿灯,直接通行
  如果标志位被清空,代表红灯,wait等待变绿灯
'''
import threading,time
event = threading.Event()
def lighter():
    count = 0
    event.set()
    while True:
        if count>20 and count<30:#如果count大于20就改成红灯
           event.clear() #将标志位清空
           print("\033[41;1mred light is on ....\033[0m")
        elif count>30:
           event.set() #变绿灯
           count = 0
        else:
           print("\033[42;1mgreen light is on ....\033[0m")
        time.sleep(1)
        count+=1
def car(name):
    while True:
        if event.is_set():#代表设置了绿灯
           print("[%s] running...." % name)
           time.sleep(1)
        else:
           print("[%s] sees red light, waiting....",name)
           event.wait()
           print("[$s] green light is on,start going",name)

light = threading.Thread(target=lighter)
light.start()
car1 = threading.Thread(target=car,args=("tesla",))
car1.start()
