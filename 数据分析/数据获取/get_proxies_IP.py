'''************************************************ 
 * @Author: Movix
 * @Date: 2021-07-26 23:51:33
 * @LastEditTime: 2021-07-27 00:09:32
 * @Github: https://github.com/Moviw
 * @FilePath: \数据分析\代理IP.py
 * @Description: 
 ************************************************'''
import requests
#!这些代理IP无法使用,需要找代理商购买IP
def get_proxies():
    proxies = {
        "http": "125.88.74.122:84",
        "http": "123.84.13.240:8118",
        "https": "94.240.33.242:3128"
    }

    return proxies