import scrapy
from simple.items import SimpleItem
import requests
import json
from lxml import etree
import os
import time
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
class ImageCapSpider(scrapy.Spider):
   
    name = 'image_cap'
    # allowed_domains = ['http://simpledesktops.com/browse/']
    # start_urls = ['https://freenaturestock.com/category/clouds/']

    start_urls = ['https://freenaturestock.com/videos/']
    def parse(self, response):
        fig_list=response.xpath('//main/div[1]/figure')
        # print(fig_list)
        i=0
        for fig in fig_list:
            nm=fig.xpath('./a/@title')[0].extract()

            print('正在下载',nm)

            pic=nm+'.jpg'

            # print(pic)

            url=fig.xpath('./a/@href')[0].extract()
            page_text=requests.get(url=url,headers=headers).text
            src=etree.HTML(page_text).xpath('//div[@class="media-actions"]/a/@href')[0]
            #用content来保存图片
            data=requests.get(url=src,headers=headers).content

            item=SimpleItem()
            item['pic']=pic
            item['data']=data
            yield item 
            print(nm,'下载完成!')
            i+=1
            print(i)
            time.sleep(3)
