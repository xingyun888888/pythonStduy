__author__ = 'Administrator'
'''
 全局解释器锁: 无论你有4核8核,同一时间执行线程就是只有一个;
 线程之间数据共享的问题
 不断地进行上下文的切换 是调用操作系统的原生线程
 调用线程执行任务,必须要把这个上下文关系传给它,python为了避免
 变成了我这里有一个number等于1,我要对这个number进行加1
 要想让cpu执行任务 必须把上下文交给cpu,在线程1把上下文给cpu1的时候,在真正计算的时候变成串行;
 我们直接控制 让线程1先执行，然后让线程2再执行 只是把上下文传给了线程,
 python的解释器就是把number拷贝给了cpu线程  在这种情况下没有办法说让哪一个线程先执行
 这时候就变成了让4个线程独自执行
 所以当时设计的最简单的办法就是 同一时间只有一个线程能够工作
 pypy是加入了一个jit的技术
 即时编译就是提前预编译一部分 相当于提前把一部分代码预编译
 但这只是一个人的事情 到现在为止在cpython去掉全局锁是没办法了
 怎么办?既然不能改变那么便有这种的办法
 这个东西跟我们程序员完全没有关系
 执行线程python3和python2没有区别 centos ubuntu debian window linux macOs
 为什么加不准了 但是只有一个线程执行 但是实际的情况下就是有的时候加的不对
 先说为什么加的不准 申请gil lock 申请全局解释器锁 调用系统的原生线程  执行时间到了
 每100条指令切换一次锁 你要把锁释放出来让其他线程开始执行 释放完成之后就不执行了
 第6步在哪里 但是问题是这个线程执行完毕了吗

 保证统一时间只有一个线程执行
 递归锁
 logs = {"door1":key1,"door2":key2}连续锁好几次的时候 就会用到递归锁
 互斥锁(Mutex)一个进程可以启动多个线程
 信号量(Semaphone) 同时只有一个线程更改数据,
'''

import threading
import time

num = 0
lock = threading.Lock()
def run(n):
    lock.acquire()
    global num
    num += 1
    time.sleep(2)
    lock.release()


t1 = threading.Thread(target=run,args=("t1",))
t2 = threading.Thread(target=run,args=("t2",))

t1.start()
t2.start()

time.sleep(3)
print(num)
