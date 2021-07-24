import requests
import json
from requests.api import post

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

post_url='https://fanyi.baidu.com/sug'
kw=input("输入单词")
data={
    'kw':kw
}
response =requests.post(url=post_url,data=data,headers=headers)

dic=response.json()
filename=kw+'.json'
fp=open(filename,'w',encoding='utf-8')
json.dump(dic,fp=fp,ensure_ascii=False)
print('单词%s的json格式文件已生成!'%kw)