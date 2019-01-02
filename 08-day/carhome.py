import requests
from bs4 import BeautifulSoup
import re
import pymysql

sss = pymysql.Connect('localhost', 'root', '199888', 'pachong')
ssss = sss.cursor()

starpage = int(input('起始页:'))
endpage = int(input('终止页:'))
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
for page in range(starpage, endpage + 1):
    url = 'https://www.autohome.com.cn/all/{}/'.format(page)
    req = requests.get(url, headers=header)
    html = req.text
    soup = BeautifulSoup(html, features='html.parser')
    li_list = soup.select('ul.article li')
    for info in li_list:
        try:
            title = info.select('h3')[0].text
            print(title)
            time = info.select('span.fn-left')[0].text
            view = info.select('em')[0].text
            comment_id = info.select('em')[1].get('data-articleid')
            comment_url = 'https://reply.autohome.com.cn/api/getData_ReplyCounts.ashx?appid=1&dateType=jsonp&objids={}&callback=jQuery172022293431050373824_1537037454377&_=1537037454582'.format(
                comment_id)
            comment_req = requests.get(comment_url, headers=header)
            comment_html = comment_req.text
            comment_re = re.compile('"replycountall":(.*?),')
            comment = re.findall(comment_re, comment_html)[0]
            content = info.select('p')[0].text
            img_src = 'https:' + info.select('img')[0].get('src')
            href = 'https:' + info.select('a')[0].get('href')
            sql = '''INSERT INTO carhome VALUES (null ,"%s","%s","%s","%s","%s","%s","%s")'''%(title,time,view,comment,content,img_src,href)
            ssss.execute(sql)
            sss.commit()
        except:
            pass

