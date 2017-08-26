__author__ = 'Administrator'
import queue,time
'''
  queue is expecially useful in threaded programming when information must be exchanged safely
  between multiple threads.

  class queue.Queue(maxsize = 0) #先入先出
  class queue.LifoQueue(maxsize = 0) #last in first out
  class queue.PriorityQueue(maxsize = 0) #存储数据时可设置优先级的队列

  contructor for a priority queue. maxsize is an iteger that sets the upperbound limit on the
  number of items that can be placed in the queue.Intertion will block once this size has been
  reached, until queue items are consumed. If maxsize is less than or eqals to zero, the queue
  size is infinite.
  The lowest valued entires are retrieved first(the lowest valued entry is the one retured)
  by sorted(list(entries))[0]. A typical pattern for entries is a tuple in the form: (priority_number,data)

  为什么还要队列 列表有顺序 元组有顺序
  list = [] 列表只是从列表里面取出来 但是数据还在列表里
  tuple=()
  dist={"key":"value"}

'''
# s = {1,3,4,4,2,3}
# l = [1,3,4,3,45,5,3423]
# d = {"key":"value"}
# print(type(d))
# print(type(l))
# print(s)
# print(l)
# print(type(s))

q = queue.Queue() #生成一个队列
q.put("d1")
q.put("d2")
q.put("d3")

print(q.qsize())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
q.put("d4")
print("324234")