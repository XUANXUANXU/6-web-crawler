# 使用selenium来加载动态网页
from selenium import webdriver


driver = webdriver.Chrome(executable_path='/home/xuan/下载/chromedriver')
driver.get('http://www.baidu.com')