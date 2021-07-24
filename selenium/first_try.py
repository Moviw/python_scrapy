"""
selenium模块的基本使用

问题：selenium模块与爬虫之间具有什么关联
    --便捷的获取网站中动态加载出来的数据
    --便捷实现模拟登录
什么是selenium模块?
    --基于浏览器自动化的一个模块

"""
from selenium import webdriver
import time
from lxml import etree
#操作流程：

# 1.实例化一个浏览器对象
'''
当出现“连到系统上的设备没有发挥作用。 (0x1F)”
时写下面三行代码
并将它们用于创建对象的传入的参数中
'''
option = webdriver.ChromeOptions()
# 防止打印一些无用的日志
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

driver=webdriver.Chrome(chrome_options=option,executable_path='C:/Users/19735/anaconda3/pkgs/python-3.8.3-he1778fa_2/chromedriver') # 将chromedriver放在该目录下
#2.编写基于浏览器自动化的操作代码
driver.get(url='http://scxk.nmpa.gov.cn:81/xk/')#向药监总局页面发请求

page_text=driver.page_source # 获取浏览器当前页面的源码数据

#解析企业名称
tree=etree.HTML(page_text)
li_list=tree.xpath("//ul[@id='gzlist']/li")
print(li_list)
for li in li_list:
    name=li.xpath("./dl/@title")[0]
    print(name)
time.sleep(2)
driver.quit()