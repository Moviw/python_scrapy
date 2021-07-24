from selenium import webdriver
from time import sleep
#实现·无可视化界面
from selenium.webdriver.chrome.options import Options
#实现·规避检测
from selenium.webdriver import ChromeOptions


chrome_option=ChromeOptions()
#实现·规避检测
chrome_option.add_experimental_option('excludeSwitches',['enable-automation'])
#实现·无可视化界面的操作
chrome_option.add_argument('--headless')
chrome_option.add_argument('disable-gpu')
# 防止打印一些无用的日志
chrome_option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

#如何实现让selenium规避被检测的风险
driver=webdriver.Chrome(executable_path='C:/Users/19735/anaconda3/pkgs/python-3.8.3-he1778fa_2/chromedriver',options=chrome_option)

driver.get('https://www.baidu.com/')
print(driver.page_source)
sleep(4)
driver.quit()