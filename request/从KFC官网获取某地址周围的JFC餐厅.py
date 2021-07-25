import requests
import json
from requests.api import head, post

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
post_url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

data={
    'cname': "",
    'pid': "",
    'keyword': "北京" ,
    'pageIndex': '1',
    'pageSize': '1000',
}

response=requests.post(url=post_url,data=data)

s=response.text
filename=data.get("keyword")+'.json'
#fp=open(filename,'w',encoding='utf-8')
with open(filename,'w',encoding='utf-8') as fp:
    fp.write(s)
print("over")
