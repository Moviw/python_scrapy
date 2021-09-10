'''************************************************ 
 * @Author: Movix
 * @Date: 2021-07-26 22:42:12
 * @LastEditTime: 2021-07-26 23:09:58
 * @Github: https://github.com/Moviw
 * @FilePath: \数据分析\数据获取初试.py
 * @Description: 通过向网站发送请求、解析数据、存储数据三步骤完成数据获取
 ************************************************'''
import requests
import pandas as pd
from lxml import etree
import os

#!向指定url发送请求 并获取网页源码
def get_data():
    url='https://book.douban.com/latest'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
    }
    response=requests.get(url=url,headers=headers)
    return response.text


#!解析页面源码数据，并将数据储存在列表中
def parse(data,img_urls,titles,ratings,authors,details):
    tree=etree.HTML(data)
    list1=tree.xpath('//*[@class="cover-col-4 clearfix"]/li')
    list2=tree.xpath('//*[@class="cover-col-4 pl20 clearfix"]/li')
    list=list1+list2
    for li in list:
        img_url=li.xpath('./a/img/@src')[0]
        img_urls.append(img_url)
        title=li.xpath('./div/h2/a/text()')
        titles.append(title)
        rating=li.xpath('./div/p[@class="rating"]/span[2]/text()')
        ratings.append(rating)
        author=li.xpath('./div/p[@class="color-gray"]/text()')
        authors.append(author)
        detail=li.xpath('./div/p[3]/text()')
        details.append(detail)


#!以.csv的文件格式保存数据
def save(img_urls,titles,ratings,authors,details):
    result=pd.DataFrame()
    result['img_urls']=img_urls
    result['titles']=titles
    result['ratings']=ratings
    result['authors']=authors
    result['details']=details
    result.to_csv('result.csv',index=None)


#!总流程
def run():
    img_urls=[]
    titles=[]
    ratings=[]
    authors=[]
    details=[]
    print('--get_data-- ongoing')
    data=get_data()
    print('--parse-- ongoing')
    data=parse(data,img_urls,titles,ratings,authors,details)
    print('--save-- ongoing')
    save(img_urls,titles,ratings,authors,details)
if __name__=='__main__':
    run()