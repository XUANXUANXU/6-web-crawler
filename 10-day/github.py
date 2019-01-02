from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='/home/xuan/下载/chromedriver')
driver.get('https://github.com/login')
driver.find_element_by_name('login').send_keys('302738630@qq.com')
driver.find_element_by_name('password').send_keys('xuan1121')
time.sleep(2)
driver.find_element_by_name('commit').click()
cookies_dict = {}
for cook in driver.get_cookies():
    cookies_dict[cook['name']] = cook['value']
print(cookies_dict)
driver.get('https://github.com/XUANXUANXU')
with open('xuan.html','w') as x:
    x.write(driver.page_source)