import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

print('初始化浏览器')
USERNAME   = os.environ['20S105159']
PASSWORD   = os.environ['cao19920922']
LOCATION   = os.environ['哈尔滨市南岗区']
driver = None
ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 MicroMessenger/6.3.27 NetType/WIFI Language/zh_CN'
option = webdriver.ChromeOptions()
option.headless = True
option.add_argument('user-agent='+ua)
driver = webdriver.Chrome(executable_path= '/usr/bin/chromedriver', options = option)

print('正在上报')
driver.get('https://ids.hit.edu.cn/authserver/')
driver.find_element_by_id('mobileUsername').send_keys(USERNAME)
driver.find_element_by_id('mobilePassword').send_keys(PASSWORD)
driver.find_element_by_id('load').click()
driver.get('https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xs/yqxx')
driver.find_element_by_class_name('right_btn').click()
sleep(1)
alert = EC.alert_is_present()(driver)
if alert:
	alert.accept()
	driver.find_element_by_id('center').find_elements_by_tag_name('div')[5].click()
loc = driver.find_element_by_id('gnxxdz')
driver.execute_script('arguments[0].value="'+LOCATION+'"', loc)
driver.find_element_by_id('checkbox').click()
driver.execute_script('save()')
driver.execute_script('document.getElementsByClassName("weui-dialog__btn primary")[0].click()')
driver.quit()

print('上报完成')
