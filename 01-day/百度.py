from urllib import parse,request
# import ssl
kw = input('输入关键字:')
key = parse.quote(kw)
url = 'https://www.baidu.com/s?'
for i in range(1,11):
    pn = (i-1)*10
    filename = str(i)+'页.html'
    fulurl = 'http://www.baidu.com/s?wd={}&pn={}'.format(key,pn)
    # context = ssl.create_default_context()
    requests = request.Request(fulurl)
    response = request.urlopen(requests)
    html = response.read().decode()
    with open(filename,'w') as f:
        f.write(html)