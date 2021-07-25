import requests
import json
from lxml import etree
import os
import time
#需求解析：用xpath下载网站
# https://www.quanjing.com/search/%E6%98%9F%E7%A9%BA#%E6%98%9F%E7%A9%BA||1|100|1|2||||||
# 到
# https://www.quanjing.com/search/%E6%98%9F%E7%A9%BA#%E6%98%9F%E7%A9%BA||1|100|3333|2||||||
# 中的所有图片
# for i in range(1,30):
i=1
# url='https://www.quanjing.com/search/%E6%98%9F%E7%A9%BA#%E6%98%9F%E7%A9%BA||1|100|'+str(i)+'|2||||||'
url='https://www.quanjing.com/search/星空#星空||1|100|1|2||||||'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59'
}
j=1
#获取响应数据
response=requests.get(url=url,headers=headers, timeout=5)


page_text=response.text
with open ("1.html",'w',encoding='utf-8') as fp:
    fp.write(page_text)
tree=etree.HTML(page_text)           #!!!用HTML传递网址参数时不用加双引号，直接传文本时需要
li_list=tree.xpath('//ul[@class="gallery_list"]/li')
print(li_list)
    # #创建保存图片的文件夹
    # if not os.path.exists('./picLibs('+str(i)+')'):
    #     os.mkdir('./picLibs('+str(i)+')')
    # for li in li_list:
    #     #要注意获取图片地址时是否前面还有前缀
    #     #./用来表示“在当前层级下”
    #     #用@取得属性值
    #     src="https://pic.netbian.com"+li.xpath("./a/img/@src")[0]  #因为返回的是一个列表所以在最后要用[0]取到第一个元素  

    #     alt=li.xpath("./a/img/@alt")[0]+'.jpg'                      #要在最后加上.jpg，要不然没有后缀名
    
    #     # print(alt)
    #     # print(src)
    #     #如果在有中文时出现乱码 最通用的解决方案是:alt=alt.encode('iso-8859-1').decode('gbk')可以解决大多数乱码问题


    #     #持久化存储

    #     #用content来保存图片
    #     data=requests.get(url=src,headers=headers).content
    #     #前面加上文件夹piclibs
    #     img_path='picLibs('+str(i)+')/'+alt
    #     with open(img_path,'wb') as fp:
    #         fp.write(data)
    #         print(alt,'下载成功!')
    # print('-'*50)

