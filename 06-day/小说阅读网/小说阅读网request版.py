# https://www.readnovel.com/rank/hotsales?pageNum=2
# https://www.readnovel.com/rank/hotsales?pageNum=1

import urllib.parse as parse
import urllib.error as error
import ssl, os, re
import requests
from lxml import etree
from requests.exceptions import ConnectionError,ConnectTimeout,Timeout,ProxyError,HTTPError

ISFINISHED = False

def get_data_from_url(url):
    print(url)
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    try:
        response = requests.get(url,headers=headers)
    except error.HTTPError as err:
        print(err)
    except error.URLError as err:
        print(err)
    else:
        if response.status_code == 200:
            print('请求完成')
            html = etree.HTML(response.text)
            print(type(html))

            novel_list = html.xpath('//div[@class="book-img-text"]/ul/li')
            # print(len(novel_list))

            if len(novel_list) == 0:
                print('全部下载完成')
                global ISFINISHED
                ISFINISHED = True
            
            for novel in novel_list:
                print(novel)
                #图片链接
                image_url = novel.xpath('./div[@class="book-img-box"]//img/@src')[0]
                #小说的地址
                noval_url = novel.xpath('./div[@class="book-mid-info"]/h4/a/@href')[0]
                #小说的标题
                title = novel.xpath('./div[@class="book-mid-info"]/h4/a/text()')[0]
                #作者名称
                author = novel.xpath('.//p[@class="author"]/a[@class="name default"]/text()')[0]
                #标签
                tags = ','.join(novel.xpath('//p[@class="author"]/a[2]/text()'))
                #是否连载
                finished = novel.xpath('.//p[@class="author"]/span/text()')[0]
                #描述
                desc = novel.xpath('.//p[@class="intro"]/text()')[0]
                # print(image_url,title,author,tags,desc)
                #更新章节
                update_noval = novel.xpath('.//p[@class="update"]/a/text()')[0]
                #更新时间
                update_time = novel.xpath('.//p[@class="update"]/span/text()')[0]

                novel_data = [image_url,noval_url,title,author,tags,finished,desc,update_noval,update_time]
                # print(dict)
                # ''.join():把列表拼接成字符串
                content = '\n'.join(novel_data).replace(' ','').replace('\r','')
                print(novel[2])
                if not os.path.exists('小说阅读二/'+title):
                    print('正在创建文件夹：' + title)
                    os.mkdir('小说阅读二/'+title)
                write_txt_to_file(content,title)
                get_image_from_url('https:'+image_url,title)


                #思考，如果下载免费章节详情并保存本地，怎么办？？
                # https://www.readnovel.com/book/9553264004296703#Catalog

                # novel_deatil_url = parse.urljoin('https://www.readnovel.com/book/9553264004296703#Catalog',novel[1])+'#Catalog'
                # print(novel_deatil_url)
                # get_novel_datail_from_url(novel_deatil_url)

def get_novel_datail_from_url(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    try:
        response = requests.get(url,headers=headers)
    except error.HTTPError as err:
        print(err)
    except error.URLError as err:
        print(err)
    else:
        if response.status_code == 200:
           print(response.status_code)
           html = response.content.decode('utf-8')
           #通过分析页面，我们发现每一个详情中的免费的章节列表，在第一div的ul下
           pattern = re.compile('<div\sclass="volume".*?<ul\sclass="cf">(.*?)</ul>',re.S)
           result = re.search(pattern,html)
           #这个时候我们取到了所有的免费章节的li标签
           html = result.group(1)
           #为了匹配章节详情的连接和标题
           pattern = re.compile('<a\shref="(.*?)".*?>(.*?)</a>',re.S)
           chapter_list = re.findall(pattern,html)
           for chapter in chapter_list:
               print(chapter) 


def write_txt_to_file(content,filename):
    print('正在写入小说信息：'+filename)
    with open('小说阅读二/'+filename+'/'+filename+'.txt','w') as f:
        f.write(content)

def get_image_from_url(url,filename):
    print('正在下载图片：'+filename+'jpg')
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    try:
        response = requests.get(url,headers=headers)
    except error.HTTPError as err:
        print(err)
    except error.URLError as err:
        print(err)
    else:
        if response.status_code == 200:
            print(filename+'.jpg'+'下载完成')
            write_image_to_file(response.content,filename)


def write_image_to_file(data,filename):
    print('正在写入图片信息：'+filename)
    with open('小说阅读二/'+filename+'/'+filename+'.jpg','wb') as f:
        f.write(data)


def main():
    for i in range(1,2):
        if ISFINISHED == False:
            full_url = 'https://www.readnovel.com/rank/hotsales?pageNum='+str(i)
            get_data_from_url(full_url)
        else:
            print('跳出循环，下载完毕')
            break

if __name__ == '__main__':
    main()