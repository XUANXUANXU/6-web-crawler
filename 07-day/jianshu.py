import requests
from lxml import etree
import os
# https://www.jianshu.com/c/7b2be866f564?order_by=added_at&page=11
page = int(input('输入想要的页数:'))
for i in range(page):
    j_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }

    j_url = 'https://www.jianshu.com/c/7b2be866f564?order_by=added_at&page={}'.format(i+1)
    respone = requests.get(j_url,headers=j_headers)
    # print(respone.status_code)
    html = respone.text
    html2 = etree.HTML(html)
    j_title = html2.xpath('//a[@class="title"]/text()')
    # print(j_title)
    j_author = html2.xpath('//a[@class="nickname"]/text()')
    # print(j_author)
   

    j_herf = html2.xpath('//a[@class="wrap-img"]/@href')
    # print(j_herf)
    k = 0
    for j in j_herf:

        t_lianjie = 'https://www.jianshu.com'+j
        rep = requests.get(t_lianjie,headers=j_headers)
        html3 = rep.text
        html4 = etree.HTML(html3)
        j_time = html4.xpath('//span[@class="publish-time"]/text()')
        # print(j_time)
        j_content = html4.xpath('//div[@class="show-content-free"]/*/text()')
        j_image = html4.xpath('//div[@class="image-view"]/img/@data-original-src')
        # print(j_content)
        # print(j_image)

        filename = j_title[k]
        k+=1
        os.makedirs('简书摄影/'+filename)
        content = ''
        for a in j_content:
            content+=a
        with open('简书摄影/'+filename+'/'+filename+'.txt','w') as file:
            file.write('标题:'+j_title[0]+'\n作者:'+j_author[0]+'\n发布时间:'+j_time[0]+'\n文字内容:'+content)
        num = 0
        for j in j_image:
            num+=1
            imgs_url = 'https:'+j
            img_req = requests.get(imgs_url,headers=j_headers)
            with open('简书摄影/'+filename+'/img{}'.format(num)+'.jpg','wb') as imgs:
                imgs.write(img_req.content)

    




