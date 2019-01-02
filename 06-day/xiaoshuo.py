import requests
from lxml import etree
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
}


def gettxt(url):
    req = requests.get(url, headers=headers)
    html = req.text
    html2 = etree.HTML(html)
    finction_name = html2.xpath('//a[@data-eid="qd_C40"]')
    finction_author = html2.xpath('//a[@data-eid="qd_C41"]')
    finction_type = html2.xpath('//a[@data-eid="qd_C42"]')
    finction_context = html2.xpath('//p[@class="intro"]')
    finction_update = html2.xpath('//a[@data-eid="qd_C43"]')
    finction_image = html2.xpath('//a[@data-eid="qd_C39"]/img/@src')
    for i in range(len(finction_name)):
        tofile(finction_name, finction_author, finction_type, finction_context, finction_update, finction_image, i)




def tofile(finction_name, finction_author, finction_type, finction_context, finction_update, finction_image, i):
    filename = finction_name[i].text
    os.makedirs('小说阅读/' + filename)
    context = '名字:' + finction_name[i].text + '\n作者:' + finction_author[i].text + '\n分类:' + finction_type[
        i].text + '\n简介:' + finction_context[i].text + '\n更新状态:' + finction_update[i].text
    with open('小说阅读/' + filename + '/' + filename + '.txt', 'w') as file:
        file.write(context)
    img_url = 'https:' + finction_image[i]
    img = requests.get(img_url, headers=headers)
    with open('小说阅读/' + filename + '/' + filename + '.jpeg', 'wb') as image:
        image.write(img.content)


def run():
    for page in range(34):
        url = 'https://www.readnovel.com/rank/hotsales?pageNum={}'.format(page + 1)
        gettxt(url)
        print(page)


run()
