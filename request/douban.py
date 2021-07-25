import requests
import json
import os
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
#!这里要用基于ajax返回的response包里面的‘请求url’作为url不是浏览器中的url
post_url='https://movie.douban.com/j/search_subjects?'
param={
    'type':'movie',
    'tag':'豆瓣高分',
    'sort':'recommend',
    'page_limit':500,
    'page_start':0
}

#!下面的两种只能解析出字符串 这一版可以生成一系列以“名字+评分”形式为名字的图片
response=requests.get(url=post_url,headers=headers,params=param)
data=response.json()
list=data['subjects']
if not os.path.exists('./dianying'):
    os.mkdir('./dianying')
    print('创建文件夹"dianying成功"')
else:
    print('文件夹"dianying"已存在')
i=1
#!这一版就可以把网上的json串解析出来
for li in list:
    name=li["title"]
    rate=li['rate']
    src=li['cover']
    img=requests.get(url=src,headers=headers).content

    nm='dianying/'+name+rate+'分.jpg'
    with open(file=nm,mode='wb') as fp: 
        fp.write(img)
    print('第%d个爬取成功！'%i)
    i+=1
print('共',len(list),'个!\nover!')




















# response=requests.get(url=post_url,headers=headers,params=param)
# data=response.json()
# list=data['subjects']
# #!这一版就可以把网上的json串解析出来
# with open('dianying1.txt','a',encoding='utf-8') as fp:
#     for li in list:
#         name=li["title"]
#         rate=float(li['rate'])
#         # if(rate<9.0):
#         #     continue
#         # else:
#         fp.write(name+':'+str(rate)+'分\n')
#     fp.write('--------------\n')
# print('共',len(list),'个!\nover!')
















#这一版可以将本地的json数据串进行解析

# data={}
# with open('douban.json','r',encoding='utf-8')as fp:
#     data=json.load(fp=fp)
# list=data['subjects']
# with open('dianying.txt','a',encoding='utf-8') as fp:
#     for li in list:
#         name=li["title"]
#         rate=float(li['rate'])
#         # if(rate<9.0):
#         #     continue
#         # else:
#         fp.write(name+':'+str(rate)+'分\n')
#     fp.write('--------------\n')
# print('over')
    
