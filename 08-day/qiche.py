# https://www.autohome.com.cn/all/1/
import requests
from bs4 import BeautifulSoup
import re
import pymysql
from ftplib import FTP
# import urllib.error
c = pymysql.Connect('localhost','root','zxcvbnm000','test_zxx',charset='utf8')
d = c.cursor()

page = int(input('输入想要的页数:'))
for i in range(page):
    
    q_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    q_url = 'https://www.autohome.com.cn/all/{}/'.format(i+1)
    reponse = requests.get(q_url,headers=q_headers)
    print(reponse.status_code)
    html = reponse.text
    # print(html)
    soup = BeautifulSoup(html, features='html.parser')
    li_list = soup.select('ul.article li')
    for j in li_list:
        try:
            title = j.select('h3')[0].text
            time = j.select('span.fn-left')[0].text
            content = j.select('p')[0].text
            read_num = j.select('em')[0].text
            # print(read_num)

            img_lian = 'https:' + j.select('img')[0].get('src')
            content_href = 'https:' + j.select('a')[0].get('href')

            comment_num = j.select('em')[1].get('data-articleid')
            print(comment_num)
            comment_url = 'https://reply.autohome.com.cn/api/getData_ReplyCounts.ashx?appid=1&dateType=jsonp&objids={}&callback=jQuery172022293431050373824_1537037454377&_=1537037454582'.format(
                    comment_num)
            reponse2 = requests.get(comment_url, headers=q_headers)
            html2 = reponse2.text
            print(html2)
            comment_re = re.compile('"replycountall":(.*?),')
        
            comment = re.findall(comment_re, html2)[0]
            print(re.findall(comment_re, html2))
                

            sql = '''INSERT INTO qiche VALUES (null ,"%s","%s","%s","%s","%s","%s","%s")'''%(title,time,content,read_num,img_lian,content_href,comment)
            d.execute(sql)
            c.commit()
        except:

            pass
     