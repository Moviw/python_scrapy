import requests
# 谷歌浏览器的UI伪装
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
kw=input("enter what you wanna search for:")
asd={
    "query":kw
}
response=requests.get("https://www.sogou.com/web?",params=asd,headers=headers)

page_text=response.text

filename=kw+".html"
with open(filename,'w',encoding='utf-8') as fp:
    fp.write(page_text)
print(filename+"保存成功")