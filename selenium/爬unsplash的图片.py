from selenium import webdriver
import time
from lxml import etree
from time import sleep
import requests
#实现·无可视化界面
from selenium.webdriver.chrome.options import Options
#实现·规避检测
from selenium.webdriver import ChromeOptions
'''
功能：
    实现无验证码前提下的登陆网站功能
        步骤：找到对应的搜索栏与登陆按键即可
'''

'''
当出现“连到系统上的设备没有发挥作用。 (0x1F)”
时写下面三行代码
并将它们用于创建对象的传入的参数中
'''
chrome_option=ChromeOptions()
#实现·规避检测
chrome_option.add_experimental_option('excludeSwitches',['enable-automation'])
#实现·无可视化界面的操作
chrome_option.add_argument('--headless')
chrome_option.add_argument('disable-gpu')
# 防止打印一些无用的日志
chrome_option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])


driver=webdriver.Chrome(options=chrome_option,executable_path='C:/Users/19735/anaconda3/pkgs/python-3.8.3-he1778fa_2/chromedriver') # 将chromedriver放在该目录下
driver.get(url='https://unsplash.com/t/experimental')

tree=etree.HTML(driver.page_source)
li_list=tree.xpath('//div[@id="app"]/div/div[3]/div[2]/div[1]/div/div/div') 
print(li_list)
i=1

# //*[@id="app"]/div/div[3]/div[2]/div[1]/div/div/div[1]/figure[1]/div/div/div/div/div[2]/div[2]/div[2]/a
# //*[@id="app"]/div/div[3]/div[2]/div[1]/div/div/div[2]/figure[1]/div/div/div/div/div[2]/div[2]/div[2]/a
# //*[@id="app"]/div/div[3]/div[2]/div[1]/div/div/div[3]/figure[1]/div/div/div/div/div[2]/div[2]/div[2]/a

# //*[@id="app"]/div/div[3]/div[2]/div[1]/div/div/div[1]/figure[2]/div/div/div/div/div[2]/div[2]/div[2]/a
# //*[@id="app"]/div/div[3]/div[2]/div[1]/div/div/div[2]/figure[2]/div/div/div/div/div[2]/div[2]/div[2]/a
# //*[@id="app"]/div/div[3]/div[2]/div[1]/div/div/div[3]/figure[2]/div/div/div/div/div[2]/div[2]/div[2]/a

# //*[@id="app"]/div/div[3]/div[2]/div[1]/div/div/div[1]/figure[3]/div/div/div/div/div[2]/div[2]/div[2]/a
# //*[@id="app"]/div/div[3]/div[2]/div[1]/div/div/div[2]/figure[3]/div/div/div/div/div[2]/div[2]/div[2]/a
# //*[@id="app"]/div/div[3]/div[2]/div[1]/div/div/div[3]/figure[3]/div/div/div/div/div[2]/div[2]/div[2]/a

# //*[@id="app"]/div/div[3]/div[2]/div[1]/div/div/div[1]/figure[1]/div/div/div/div/div[2]/div[2]/div[2]/a
for div in li_list:
    image_list=div.xpath("./figure")
    for image in image_list: 
        print("正在爬取第"+str(i)+"张")
        print(image)
        image_src=image.xpath("./div/div/div/div/div[2]/div[2]/div[2]/a/@href")[0]
        # 用content来保存图片
        data=requests.get(url=image_src).content
        name=image.xpath('./div/div/a/@title')[0]+'.jpg'
        with open(name,'wb') as fp:
            fp.write(data)   
        print("第"+str(i)+"张爬取完成")
        i+=1
        sleep(4)
        

# 还没有彻底完成
# 问题：停在第四张就不爬了
#      爬取顺序也是随机的
#      并且会报错：Traceback (most recent call last):
#   File "c:\Users\19735\Desktop\python_vscode\爬unsplash的图片.py", line 56, in <module>
#     image_src=image.xpath("./div/div/div/div/div[2]/div[2]/div[2]/a/@href")[0]
# IndexError: list index out of range
