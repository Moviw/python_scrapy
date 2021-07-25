from selenium import webdriver
import time
from lxml import etree
from time import sleep


option = webdriver.ChromeOptions()
# 防止打印一些无用的日志
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

driver=webdriver.Chrome(options=option,executable_path='C:/Users/19735/anaconda3/pkgs/python-3.8.3-he1778fa_2/chromedriver') # 将chromedriver放在该目录下
driver.get(url='http://www.kfc.com.cn/kfccda/storelist/index.aspx')
driver.find_element_by_id('keyword').send_keys('北京')
driver.find_element_by_class_name('btn_search').click()
sleep(5)