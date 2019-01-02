import urllib.request as request
import re
import pymysql

sss = pymysql.Connect('localhost', 'root', 'zxcvbnm000', 'tengxun',charset='utf8')
ssss = sss.cursor()
page = int(input('输入页数:'))
for i in range(page):
    a = i*10
    url = 'https://hr.tencent.com/position.php?keywords=%E8%AF%B7%E8%BE%93%E5%85%A5%E5%85%B3%E9%94%AE%E8%AF%8D&lid=0&tid=0&start={}'.format(a)
    header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Referer':'https://hr.tencent.com/social.php',
        'Cookie':'_ga=GA1.2.877289435.1535589852; pgv_pvi=5272499200; PHPSESSID=5at28cs3jr3v9ubm3mnbprgk64; pgv_si=s3683072000'
    }
    req = request.Request(url,headers=header)
    req = request.urlopen(req)
    html = req.read().decode('utf-8')
    p = re.compile('<tr\sclass=".*?">.*?<td\sclass="l\ssquare"><a\starget="_blank"\shref="(.*?)">(.*?)</a>.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?</tr>',re.S)
    res = p.findall(html)
    for cc in res:
        dic = {
            'name':cc[1],
            'type':cc[2],
            'count':cc[3],
            'address':cc[4],
            'date':cc[5],
            'href':'https://hr.tencent.com/'+cc[0]
        }
        sql = """insert into tenginfo(%s) values(%s)"""%(','.join([key for key,values in dic.items()]),','.join(['%s' for key,values in dic.items()]))
        # try:
        ssss.execute(sql,[value for key,value in dic.items()])
        sss.commit()
        # except:
        #     sss.rollback()
        #     print('插入失败')
        print('\r%s'%dic)
        