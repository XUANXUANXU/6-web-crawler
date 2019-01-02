# 1.分析目标网站
# 头条
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=-1

# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=20298065&count=15&category=-1

#直播
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=6

# #沪深
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=105

# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=178343&count=15&category=105

#房产
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=111

#港股
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=102

#基金
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=104

#美股
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=101

# 私募
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=113

#保险
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=110
#多进程来实现
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import requests
import json,os
import threading
pool = ProcessPoolExecutor(8)
threadPool = ThreadPoolExecutor(10)

def get_data_from_parmas(parmas):
    # parmas:参数,get请求后面拼接的参数，是一个字典类型
    # requests.get(url,parmas)
    print('开启下载进程'+str(os.getpid()))
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Referer':'https://xueqiu.com/',
        'Cookie':'aliyungf_tc=AQAAAHGN9QUUIAoA3Berc9RK7IaYfw4b; xq_a_token=9c75d6bfbd0112c72b385fd95305e36563da53fb; xq_a_token.sig=-6-bcHntQlhRjsyrvsY2IGwh-B4; xq_r_token=9ad364aac7522791166c59720025e1f8f11bf9eb; xq_r_token.sig=usx1_hrblByw-9h0cXk1yLIUlL4; _ga=GA1.2.2007234704.1537273099; _gid=GA1.2.1901963480.1537273099; u=661537273098973; Hm_lvt_1db88642e346389874251b5a1eded6e3=1537273099; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1537273099; device_id=a118f672b464105016a05eb75e12e7c1',
    }
    response = requests.get('https://xueqiu.com/v4/statuses/public_timeline_by_category.json',params=parmas,headers=headers)
    # print('1')
    print(response.status_code) #打印结果状态
    # response.json() = > json.loads(response.text)
    # print(response.json())
    # print(next_max_id)
    parmas['count'] = 15
    parmas['max_id'] = response.json()['next_max_id']
    #将要获取的下一页的链接的参数，和响应结果返回
    print('结束下载进程'+str(os.getpid()))
    return parmas,response.json(),response.url

def download_done(future):
    # print(future.result()[0])
    # print(future.result()[2])
    #添加下一页的下载啊任务，
    handler = pool.submit(get_data_from_parmas,future.result()[0])
    handler.add_done_callback(download_done)

    #将下载的任务给线程池做解析操作，
    jsonData = future.result()[1]
    threadhandler = threadPool.submit(parse_data,args=(jsonData,))
    threadhandler.add_done_callback(done)
    
    # parse_data(jsonData)

def done(future):
    print(future.result())
    

# def parse_data(jsonData):
    # print(type(jsonData))
    # article_list = jsonData['list']

def parse_data(args):
    print('-------'+threading.currentThread().name+'正在解析数据')
    #解析数据
    print(type(args[0]))
    article_list = args[0]['list']
    for article in article_list:
        #分类名称
        column = article['column']
        contentJson = json.loads(article['data'])
        articleid = contentJson['id']
        url = contentJson['target']

        title = '未发现标题'
        if 'title' in contentJson:
            title = contentJson['title']
        
        # desc = '未发现简介'
        # if 'description' in contentJson:
        #     desc = contentJson['description']
            
        username = '未知'
        profile_image_url = '未知'
        if 'user' in contentJson:
            username = contentJson['user']['screen_name']
            profile_image_url = contentJson['user']['profile_image_url']

        print(column,articleid,url,title,username,profile_image_url)

    return 'done'

if __name__ == '__main__':
    #进程池
    print('开启主进程'+str(os.getpid))
    # since_id=-1&max_id=-1&count=10&category=113
    list = [
        {'since_id':-1,'max_id':-1,'count':10,'category':-1},#头条
        {'since_id':-1,'max_id':-1,'count':10,'category':6},#直播
        {'since_id':-1,'max_id':-1,'count':10,'category':105},#沪深
        {'since_id':-1,'max_id':-1,'count':10,'category':111},#房产
        {'since_id':-1,'max_id':-1,'count':10,'category':102},#港股
        {'since_id':-1,'max_id':-1,'count':10,'category':104},#基金
        {'since_id':-1,'max_id':-1,'count':10,'category':101},#美股
        {'since_id':-1,'max_id':-1,'count':10,'category':113},#私募
        {'since_id':-1,'max_id':-1,'count':10,'category':110},#保险
    ]

    for parmas in list:
        handler = pool.submit(get_data_from_parmas,parmas)
        handler.add_done_callback(download_done)

    # pool.shutdown(wait=True)

    print('主进程结束'+str(os.getpid))



