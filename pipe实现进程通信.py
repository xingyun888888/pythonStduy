__author__ = 'Administrator'
import multiprocessing,threading,time
def f(conn):
    conn.send([42,None,"hello from child"])
    print("from parent:",conn.recv())
    conn.close()

if __name__ == "main":
    parent_conn,child_conn =multiprocessing.Pipe()
    p = multiprocessing.Process(target=f,args=(child_conn,))
    print(parent_conn.recv())
    p.start()
    p.join()