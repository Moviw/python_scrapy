from selenium import webdriver
import time
from lxml import etree
from time import sleep

'''
功能：
    模拟浏览器搜索，返回，前进，退出等操作
        1.标签定位：使用find()一系列的方法定位标签位置
        2.标签交互:使用send_key('xxx')传入参数
        3.后退：back(),前进：forward(),退出：quit()
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
driver.get(url='https://www.taobao.com/')

driver.find_element_by_id('q').send_keys('Ipad')  #这里使用了匿名简化代码  “find_element_by_id('q')”用来确定搜索框的位置   “send_keys('Ipad')”用来向搜索框内输入  

driver.find_element_by_class_name('tb-bg').click()  
#!!这里按钮的class标签是“btn-search tb-bg”不能全部复制 只能选btn-search或tb-bg  但不知道为什么  视频里说要从空格左右两个中任选其一
driver.back()
driver.forward()
sleep(5)
driver.quit()

