import os
import time
from multiprocessing import Pool

import requests


def run(agrs):
    url = 'http://www.baidu.com/'
    response = requests.get(url)
    print('进程号'+str(os.getpid()),response.status_code)
    return response.status_code

#进程执行完毕之后的回调函数
def done(future):
    print(future)

if __name__ == '__main__':
    #创建进程池
    pool = Pool(4)

    for i in range(1,400):
        pool.apply_async(run,(i,),callback=done)
    
    #关闭进程池，不载接收新的任务
    pool.close()
    pool.join()

#方式二
# from concurrent.futures import ProcessPoolExecutor
# import requests,os
# def run(agrs):
#     print(agrs)
#     url = 'http://www.baidu.com/'
#     response = requests.get(url)
#     print('进程号'+str(os.getpid()),response.status_code)

#     return response.status_code
   
# def done(future):
#     print(future.result)

# if __name__ == '__main__':
#     #创建一个进程池
#     pool = ProcessPoolExecutor(4)

#     for i in range(1,400):
#         hanlder = pool.submit(run,(i,))
#         hanlder.add_done_callback(done)
    
#     pool.shutdown()
