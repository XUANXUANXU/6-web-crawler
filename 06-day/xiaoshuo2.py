import requests
from lxml import etree
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
}

for page in range(34):
    url = 'https://www.readnovel.com/rank/hotsales?pageNum={}'.format(page+1)
    req = requests.get(url,headers=headers)
    html = req.text
    html2 = etree.HTML(html)
    txt_name = html2.xpath('//a[@data-eid="qd_C40"]')
    txt_author = html2.xpath('//a[@data-eid="qd_C41"]')
    txt_type = html2.xpath('//a[@data-eid="qd_C42"]')
    txt_context = html2.xpath('//p[@class="intro"]')
    txt_update = html2.xpath('//a[@data-eid="qd_C43"]')
    txt_image = html2.xpath('//a[@data-eid="qd_C39"]/img/@src')
    for i in range(len(txt_name)):
        os.makedirs('小说阅读/'+txt_name[i].text)
        filename = txt_name[i].text
        context = '名字:'+txt_name[i].text+'\n作者:'+txt_author[i].text+'\n分类:'+txt_type[i].text+'\n简介:'+txt_context[i].text+'\n更新状态:'+txt_update[i].text
        with open('小说阅读/'+txt_name[i].text+'/'+filename+'.txt','w') as file:
            file.write(context)
        img_url = 'https:'+txt_image[i]
        img = requests.get(img_url,headers=headers)
        with open('小说阅读/'+txt_name[i].text+'/'+filename+'.jpeg','wb') as image:
            image.write(img.content)
