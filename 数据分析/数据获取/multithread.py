'''************************************************ 
 * @Author: Movix
 * @Date: 2021-07-27 01:09:10
 * @LastEditTime: 2021-07-27 01:17:12
 * @Github: https://github.com/Moviw
 * @FilePath: \数据分析\multithread.py
 * @Description: 通过运用进程池或线程池缩短获取页面源码的时间
 ************************************************
'''
import time
import requests
import concurrent
from concurrent import futures
import pandas as pd
import threading
from multiprocessing import Pool


# 请求并解析网页获取数据（这里简单把要获取的数据设为网页源码）
def getdata(url, retries=3):
    # print("正在下载:", url)
    headers = {}
    try:
        html = requests.get(url, headers=headers,allow_redirects=False)
        # print(html)

    except requests.exceptions.ConnectionError as e:
        # print('下载出错[ConnectionError]:', e)
        html = None

        # 5xx 错误为服务器错误,我们可以进行重新请求
    if (html != None and 500 <= html.status_code < 600 and retries):
        retries -= 1
        # print('服务器错误正在重试...')
        getdata(url, retries)
        data = html.text
    else:
        data = None

    return data


# 进程池
def MyprocessPool(urls,num=10):
    pool = Pool(num)
    results = pool.map(getdata, urls)

    pool.close()
    pool.join()
    return results


# 线程池
def Myfutures(urls,num_of_max_works=10):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_of_max_works) as executor:
        executor.map(getdata, urls)


if __name__ == '__main__':
    # 　取100个网页做测试
    urls =[]
    MyprocessPool(urls,10)  # 进程池
    Myfutures(urls,10)  # 线程池