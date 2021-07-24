import requests
from lxml import etree
   
url='https://bj.58.com/ershoufang/?PGTID=0d100000-0000-16a0-42ce-253b5b24008f&ClickID=4'
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
 #1.爬取页面源码数据
text=requests.get(url=url,headers=headers).text
#2.用xpath进行数据解析
tree=etree.HTML(text)
