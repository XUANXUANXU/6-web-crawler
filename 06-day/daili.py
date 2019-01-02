import urllib.request as request
import re
import pymysql

db = pymysql.connect('localhost', 'root', 'zxcvbnm000', 'daili')
cursor = db.cursor()

xi_header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Referer': 'http://www.xicidaili.com/',
}
proxy_handler = request.ProxyHandler(
    {'http': '121.31.101.184:8123'}
)
for i in range(1,500):
    opener = request.build_opener(proxy_handler)

    req = request.Request('http://www.xicidaili.com/nn/' + str(i), headers=xi_header)
    response = opener.open(req)
    html = response.read().decode()
    reg = re.compile(
        '<tr class=".*?">.*?<td class="country"><img src=".*?" alt=".*?" /></td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>.*?<a href=".*?">(.*?)</a>.*?</td>.*?<td class=".*?">(.*?)</td>.*?<td>(.*?)</td>.*?<td class=".*?">.*?<div title=".*?" class=".*?">.*?<div class=".*?" style=".*?">.*?</div>.*?</div>.*?</td>.*?<td class=".*?">.*?<div title=".*?" class=".*?">.*?<div class=".*?" style=".*?">.*?</div>.*?</div>.*?</td>.*?<td>(\d+).*?</td>.*?<td>(.*?)</td>.*?</tr>',
        re.S)
    r = re.findall(reg, html)
    for j in r:
        dt = {}
        dt['ip'] = j[0]
        dt['port'] = j[1]
        dt['address'] = j[2]
        dt['proxy_type'] = j[3]
        dt['protocol_type'] = j[4]
        dt['exp_time'] = int(j[5])
        dt['pub_date'] = j[6]
        if dt['exp_time'] >= 300:
            sql='''INSERT INTO all_daili(%s) VALUES (%s)'''%(','.join([keys for keys in dt.keys()]),','.join(['%s' for values in dt.values()]))
            try:
                cursor.execute(sql,[values for values in dt.values()])
                db.commit()
            except:
                db.rollback()

        proxy_handle = request.ProxyHandler(
            {dt['protocol_type'].lower(): dt['ip'] + ':' + dt['port']})
        opener = request.build_opener(proxy_handle)
        if dt['protocol_type'] == 'http':
            url = request.Request("http://httpbin.org/get", headers=xi_header)
        else:
            url = request.Request("https://httpbin.org/get", headers=xi_header)
        try:
            response = opener.open(url, timeout=10)
            text = response.read().decode()
            reg = re.compile('"origin".*?"(.*?)",', re.S)
            r = re.findall(reg, text)
            print(r[0])
            if r[0] == dt['ip']:
                try:
                    ok_sql = '''INSERT INTO keyong(ip,port,protocol_type) VALUES (%s,%s,%s)'''
                    cursor.execute(ok_sql, (dt['ip'], dt['port'], dt['protocol_type']))
                    db.commit()
                    print('insert......ok......')
                except:
                    print('insert...error')
                    db.rollback()
        except:
            print('error')
