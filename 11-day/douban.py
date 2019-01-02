# https://movie.douban.com/subject_search?search_text=%E9%99%88%E5%B0%8F%E6%98%A5&cat=1002
# import requests


# url = 'https://movie.douban.com/subject_search?search_text=%E9%99%88%E5%B0%8F%E6%98%A5&cat=1002'
# reponse = requests.get(url)
from selenium import webdriver
driver = webdriver.Chrome(executable_path='/home/xuan/下载/chromedriver')
driver.get('https://movie.douban.com/subject_search?search_text=%E9%99%88%E5%B0%8F%E6%98%A5&cat=1002')
with open('./douban.html','w') as x:
    x.write(driver.page_source)