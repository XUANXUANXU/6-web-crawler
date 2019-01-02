#如何使用线程池
from concurrent.futures import ThreadPoolExecutor
import threading,requests
from lxml import etree
import json

#线程要执行的任务
def crawl_data(full_url):
    print(full_url[0])
    print(threading.currentThread().name+'正在下载'+full_url[0])
    #目标url
    url = full_url[0]
    #请求头
    header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    response = requests.get(url,headers=header)
    #如果获取数据成功，将结果存放在数据队列里面
    if response.status_code == requests.codes.ok:
        print(full_url[0]+'下载完毕')
        return response.text

#线程池中的线程，执行完毕之后的回调函数
def download_done(future):
    #获取下载结果，可以在这里进行解析
    # print(future.result())
    html_data = etree.HTML(future.result())
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
        dict = {
            'name':name,
            'age':age,
            'content':content,
        }
        with open('qiushidata.txt','a+') as file:
            file.write(json.dumps(dict,ensure_ascii=False)+'\n')


if __name__ == '__main__':
    # 创建一个线程池，内部的线程不需要你手动管理
    print(threading.currentThread().name)
    pool = ThreadPoolExecutor(10)

    for page in range(1,14):
        #目标url
        full_url = 'https://www.qiushibaike.com/8hr/page/%s/' % str(page)
        handler = pool.submit(crawl_data,(full_url,))
        handler.add_done_callback(download_done)

    pool.shutdown()
    
    print(threading.currentThread().name)


