# bs4
# https://www.readnovel.com/rank/hotsales?pageNum=1
import requests
from bs4 import BeautifulSoup

x_url = 'https://www.readnovel.com/rank/hotsales?'

parmas ={
    'pageNum' : 1
}


header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

}
response = requests.get(x_url,headers=header,params=parmas)
print(response.status_code)
# with open('page.html','w') as file:
#     file.write(response.text)
if response.status_code == 200:
    soup = BeautifulSoup(response.text)
    print(soup.prettify())