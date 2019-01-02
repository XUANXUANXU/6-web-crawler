import threading
import time

def run(args):
    print(args)
    time.sleep(1)
    print(threading.currentThread().name+'执行完毕')


if __name__ == '__main__':
    print(threading.currentThread().name+'开始')
    startTime = time.time()
    # 创建线程
    threads = []
    for i in range(0,5):
        # target=None,
        # name=None,
        # args=(), 
        # kwargs=None,
        thread = threading.Thread(target=run,name='thread'+str(i),args=(i,))
        #setDaemon设置线程守护，默认是False
        # thread.setDaemon(True)
        #启动
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    
    endTime = time.time()
    print(endTime-startTime)
    print(threading.currentThread().name+'结束')
