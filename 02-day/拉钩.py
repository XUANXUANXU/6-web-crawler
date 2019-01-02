#发送请求
import urllib.request as request
#url的编码解码
import urllib.parse as parse
#转换成Python对象
import json
#清空
with open('job.txt','w') as file:
    file.write(' ')
#
wd=input("请输入关键字:")
address = '北京'
ur='https://www.lagou.com/jobs/list_'+parse.quote(wd)+'?city='+parse.quote(address)

header = {
    'Referer': ur,
    'Cookie':'JSESSIONID=ABAAABAAADEAAFI510DC7338C30D8500734C49DED326D63; _ga=GA1.2.1933729234.1536490407; _gat=1; _gid=GA1.2.339630705.1536490407; index_location_city=%E5%85%A8%E5%9B%BD; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536490410; TG-TRACK-CODE=index_search; LGSID=20180909185327-94a7587e-b41e-11e8-b62b-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20180909185327-94a759ec-b41e-11e8-b62b-5254005c3644; user_trace_token=20180909185337-b37b7c6a-5d4e-4c2e-8a1c-300feb73c07d; LGRID=20180909185351-a2f31d4c-b41e-11e8-8ce9-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536490431; SEARCH_ID=4055709701bc40708e3738f222465e5b',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

a = 0
while True:
    form_data={
        'first': 'false',
        'pn': str(a+1),
        'kd': wd,
    }
    new_form_data=parse.urlencode(form_data).encode('utf-8')
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
    req = request.Request(url, headers=header,data=new_form_data)
    response = request.urlopen(req)
    html = response.read().decode('utf8')
    try:
        json_data=json.loads(html)
        print(json_data)
    except:
        break
    new_json_data=json_data['content']['positionResult']['result']
    li = []
    for pos in new_json_data:
        dt={}
        dt['公司名称']=pos['companyFullName']
        dt['职位']=pos['positionName']
        dt['薪资']=pos['salary']
        dt['工作经验']=pos['workYear']
        li.append(dt)
    with open('job.txt', 'a') as file:
        for i in li:
            i = str(i)
            b = i + '\n'
            file.write(b)
    a+=1


