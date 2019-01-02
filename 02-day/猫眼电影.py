import urllib.request as request
import re
with open('yingyuan.txt','w') as q:
    q.write(' ')

a = 0
while True:
    page = a*12
    url = 'http://maoyan.com/cinemas?brandId=-1&offset={}'.format(page)
    a+=1

    r = request.urlopen(url)
    pattern=re.compile('<div\sclass="cinema-info".*?<a\shref=(.*?)\sclass="cinema-name"\sdata-act=.*?\sdata-bid=.*?\sdata-val=.*?>(.*?)</a>.*?<p\sclass="cinema-address">(.*?)</p>.*?</div>',re.S)
    result = re.findall(pattern,r.read().decode())
    if result == []:
        break
    for i in result:
        dic = {}
        dic['名称']=i[1]
        dic['连接']='http://maoyan.com'+i[0][1:-2]
        dic['地址']=i[2]
        with open('yingyuan.txt','a') as q:
            q.write('名称:{}\t连接:{}\t{}\n\n'.format(dic['名称'],dic['连接'],dic['地址']))
