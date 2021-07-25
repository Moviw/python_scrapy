from selenium import webdriver
import time
from lxml import etree
from time import sleep


option = webdriver.ChromeOptions()
# 防止打印一些无用的日志
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

driver=webdriver.Chrome(options=option,executable_path='C:/Users/19735/anaconda3/pkgs/python-3.8.3-he1778fa_2/chromedriver') # 将chromedriver放在该目录下
# driver.get(url='http://scxk.nmpa.gov.cn:81/xk/')
# sleep(1)
# driver.find_element_by_id('qymc').click()
# sleep(1)
# driver.find_element_by_id('searchtext').send_keys('广州八面喜生物科技有限公司')  #这里使用了匿名简化代码  “find_element_by_id('q')”用来确定搜索框的位置   “send_keys('Ipad')”用来向搜索框内输入  
# sleep(1)
# driver.find_element_by_class_name('hzbbtn').click()  
# sleep(5)

driver.get(url='https://www.jd.com/')
driver.find_element_by_class_name('link-login').click()
# driver.back()
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
driver.find_element_by_class_name('itxt').send_keys('15510704642')
driver.find_element_by_id('nloginpwd').send_keys('qpmz2002')
driver.find_element_by_id('loginsubmit').click()
# driver.find_element_by_id('searchtext').send_keys('广州八面喜生物科技有限公司')  #这里使用了匿名简化代码  “find_element_by_id('q')”用来确定搜索框的位置   “send_keys('Ipad')”用来向搜索框内输入  
# sleep(1)
# driver.find_element_by_class_name('hzbbtn').click()  
# sleep(5)