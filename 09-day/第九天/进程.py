#进程：资源是有CPU分配，是CPU资源分配的最小单元
#进程包含线程

# 如何创建进程？
from multiprocessing import Process
import os

def run():
    print('子进程开启'+str(os.getpid()))
    for i in range(1,300):
        print(i)

    print('子进程结束'+str(os.getpid()))
    
if __name__ == '__main__':
    
    print('主进程开启'+str(os.getpid()))

    #创建一个进程：
    sub_process = Process(target=run)

    #启动子进程
    sub_process.start()

    #查看子进程是否处于存活状态
    print(sub_process.is_alive())

    #让主进程度等待子进程执行完毕
    sub_process.join()
    print('主进程结束'+str(os.getpid()))
    print(sub_process.is_alive())
    