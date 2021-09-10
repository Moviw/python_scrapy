'''************************************************ 
 * @Author: Movix
 * @Date: 2021-07-27 01:33:06
 * @LastEditTime: 2021-07-27 02:04:44
 * @Github: https://github.com/Moviw
 * @FilePath: \数据分析\ajax.py
 * @Description: 
 ************************************************'''
import requests
import exceptions 
import json
import re
from fake_useragent import UserAgent
def get_headers():
    ua = UserAgent()
    user_agent = ua.random
    headers = {'User-Agent': user_agent}

    return headers
url='https://api.m.jd.com/api?appid=o2_channels&functionId=pcMiaoShaAreaList&client=pc&clientVersion=1.0.0&callback=pcMiaoShaAreaList&jsonp=pcMiaoShaAreaList&body=%7B%7D&_=1627320519513'
response=requests.get(url=url,headers=get_headers())
data=response.text
# data=data[17:]
with open('asdsd.txt','w') as fp:
    fp.write(data)
#     # 转化为json格式，方便处理
# json_data = json.loads(data)
# goods=[]
# for item in json_data['brandList']:

#     name=item['shortWname']
#     price=item['miaoShaPrice']
#     good={
#         'name':name,
#         'price':price
#     }
#     goods.append(good)
# with open('p.json','w') as fp:
#     json.dump(goods,fp,ensure_ascii=False)


