# # 进程之间的数据不共享
# from queue import Queue
# from multiprocessing import Process
# import os

# def read1(data_queue):
#     print(data_queue)
#     while not data_queue.empty():
#         print(os.getpid(),data_queue.get())

# def read2(data_queue):
#     print(data_queue)
    
#     while not data_queue.empty():
#         print(os.getpid(),data_queue.get())


# if __name__ == '__main__':

#     data_queue = Queue(40)
#     for i in range(0,40):
#         data_queue.put(i)

#     print(data_queue.full())

#     #创建　两个进程分别读取我们的对列数据
#     r1_process = Process(target=read1,args=(data_queue,))
#     r1_process.start()

#     r2_process = Process(target=read2,args=(data_queue,))
#     r2_process.start()

#     #通过打印结果可以看出资源不共享

# 实现进程之间的数据共享,可以使用multiprocessing下的Queue
from multiprocessing import Process,Queue
import os

def read1(data_queue):
    print(data_queue)
    while not data_queue.empty():
        print(os.getpid(),data_queue.get())

def read2(data_queue):
    print(data_queue)
    
    while not data_queue.empty():
        print(os.getpid(),data_queue.get())


if __name__ == '__main__':

    data_queue = Queue(40)
    for i in range(0,40):
        data_queue.put(i)

    print(data_queue.full())

    #创建　两个进程分别读取我们的对列数据
    r1_process = Process(target=read1,args=(data_queue,))
    r1_process.start()

    r2_process = Process(target=read2,args=(data_queue,))
    r2_process.start()

    #通过打印结果可以看出资源发生了共享
    
