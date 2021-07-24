import requests
import json

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
url="http://scxk.nmpa.gov.cn:81/xk/"
response=requests.get(url=url,headers=headers)

url_text=response.text
with open("info.html",'w',encoding='utf-8') as fp:
    fp.write(url_text)
print('over!!')
