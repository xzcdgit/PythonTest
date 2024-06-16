import time
import random
import os
from multiprocessing import Process, Queue

def count(que:Queue):
    i = 0
    while True:
        if que.full():
            que.get()
        que.put(i)
        i += 1
        time.sleep(0.1)
        

def down(text):
    print(f"{text}开始下载...子进程id：{os.getpid()}")
    down_time = random.randint(2,5)
    time.sleep(down_time)
    print(f"{text}下载成功，耗时{down_time}秒")

def main():
    print(f'主线程id：{os.getpid()}')
    start_time = time.time()
    
    que = Queue(maxsize=5)
    
    #下载任务1
    t1 = Process(target=down, args=('中国历史', ))    
    #下载任务2
    t2 = Process(target=down, args=('世界历史', ))    
    
    #计数任务3
    t3 = Process(target=count, args=(que,))
    
    #守护线程
    t1.daemon = True
    t2.daemon = True
    t3.daemon = True
    
    #开始下载
    t1.start()
    t2.start()
    t3.start()
    j = 0
    while True:
        if not que.empty():
            res = que.get()
        else:
            res = None
        time.sleep(0.5)
        print(j, res)
        print(que.qsize())
        j += 1
        
        if time.time()-start_time > 8000:
            break
    
    end_time = time.time()
    print(f"全部下载完成，耗时：{end_time-start_time}秒")

if __name__ == "__main__":
    main()