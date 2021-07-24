import requests
import json

from requests.api import post
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
for page in range(43,60):  #从1到3-1=2
    home_page_url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    
    home_page_param={
        'on': 'True',  #这里必须要写小写的t么?  答：没必要大小写都可以
        'page': page,   #所有数字都要以字符串形式传输么   答:不用
        'pageSize': 13,
        'productName': '',
        'conditionType': 1,
        'applyname': '',
        'applysn': '',
    }


    home_page_info=requests.post(home_page_url,params=home_page_param,headers=headers).json()
   
    list=home_page_info['list']
  
    for num in range(0,len(list)):
        ID=list[num]['ID']
        info_page_url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
        data={
             'id':ID
        }
        info_json=response=requests.post(url=info_page_url,params=data,headers=headers).json()
        fp=open('info('+str(page)+').json','a',encoding='utf-8')
        json.dump(info_json,fp=fp,ensure_ascii=False)
        fp.close()
    print('第'+str(page)+'页数据已捕捉成功!!')