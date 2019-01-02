# 1.任务队列
# 2.模拟一个线程池（下载任务）
# 3.数据队列（存储下载任务得到的数据结果）
# 4.模拟一个线程池（解析数据）

# 5.处理数据（线程锁）
import threading
import queue,time
import requests
from lxml import etree
import json

def crawl_data(test_queue,data_queue):
    print(test_queue,data_queue)
    #下载任务

    while not test_queue.empty():
        #从任务队列中取出要爬取的页码
        page = test_queue.get()
        print(threading.currentThread().name+'正在下载'+str(page)+'页')
        #目标url
        full_url = 'https://www.qiushibaike.com/8hr/page/%s/' % str(page)
        #请求头
        header = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }

        response = requests.get(full_url,headers=header)
        #如果获取数据成功，将结果存放在数据队列里面
        if response.status_code == requests.codes.ok:
            data_queue.put(response.text)
            print(str(page)+'页'+'下载完毕')
            
    
def parser_data(data_queue,lock):
    print(data_queue)
    while not data_queue.empty():
        data = data_queue.get()
        html_data = etree.HTML(data)
        print(threading.currentThread().name+'正在解析')
        data_list = html_data.xpath('//div[@id="content-left"]/div')
        print(len(data_list))
        for item in data_list:
            name = item.xpath('./div[@class="author clearfix"]//h2/text()')[0]
            age = item.xpath('.//div[@class="articleGender manIcon"]/text()')
            if len(age) ==0:
                age = 0
            else:
                age = age[0]
            content = ''.join(item.xpath('.//div[@class="content"]/span//text()'))
            # print(name,age,content)

            dict = {
                'name':name,
                'age':age,
                'content':content,
            }
            with open('qiushidata.txt','a+') as file:
                #在写入数据之前先加锁
                lock.acquire()
                file.write(json.dumps(dict,ensure_ascii=False)+'\n')
                #写完数据之后解锁
                lock.release()

def main():
    startTime = time.time()
    #1.任务队列(FIFO)
    test_queue = queue.Queue(40)
    # https://www.qiushibaike.com/8hr/page/2/
    #把下载任务放在任务队列里面
    for i in range(1,14):
        test_queue.put(i)

    #2.创建一个数据对列
    data_queue = queue.Queue()

    #创建多个线程，执行下载任务
    threadName = ['crawl-1号','crawl-2号','crawl-3号','crawl-4号']
    threads = []
    for name in threadName:
        thread = threading.Thread(target=crawl_data,name=name,args=(test_queue,data_queue))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()


    #创建一个互斥锁
    lock = threading.Lock()
    
    #创建解析线程，解析数据
    parserThreadName = ['parser-1号','parser-2号','parser-3号']
    parserThreads = []

    for name in parserThreadName:
        thread = threading.Thread(target=parser_data,name=name,args=(data_queue,lock))
        thread.start()
        parserThreads.append(thread)
    
    for thread in parserThreads:
        thread.join()

    endTime = time.time()
    print(endTime-startTime)
    
    # print(test_queue.empty(),test_queue.full())

    # for _ in range(0,40):
    #     print(test_queue.get())

    # print(test_queue.empty(),test_queue.full())
    
if __name__ == '__main__':
    main()

