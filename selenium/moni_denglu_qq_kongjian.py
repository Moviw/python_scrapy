from selenium import webdriver
import time
from lxml import etree
from time import sleep

'''
功能：
    
'''

'''
当出现“连到系统上的设备没有发挥作用。 (0x1F)”
时写下面三行代码
并将它们用于创建对象的传入的参数中
'''
option = webdriver.ChromeOptions()
# 防止打印一些无用的日志
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])


driver=webdriver.Chrome(options=option,executable_path='C:/Users/19735/anaconda3/pkgs/python-3.8.3-he1778fa_2/chromedriver') # 将chromedriver放在该目录下
driver.get(url='https://qzone.qq.com/')

driver.switch_to.frame("login_frame")
a=driver.find_element_by_id("switcher_plogin")
a.click()
driver.find_element_by_class_name('inputstyle').send_keys('2295871753')
driver.find_element_by_id('p').send_keys('qpmz2002')
driver.find_element_by_class_name('btn').click()