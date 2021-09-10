'''************************************************ 
 * @Author: Movix
 * @Date: 2021-07-26 23:13:34
 * @LastEditTime: 2021-07-27 01:46:27
 * @Github: https://github.com/Moviw
 * @FilePath: \数据分析\exceptions.py
 * @Description: 在向url发送请求时，可能遇到错误的网址，这时用try-expect语句可以避免程序直接终止
                 plus!!:由于从状态码为5xx的服务器无法得到网页内容，所以还要将其考虑在内
                 在这种情况下 我们只需模拟等待和刷新的过程即可
 ************************************************'''
import time
import requests
from get_Dynamic_UA import get_headers
urls=['http://www.baidussss.com','http://www.news.baidu.com','http://datahonor.com/404','http://httpstat.us/500']

def get_data(url,num_retries=3):  #num_retries:重新请求的次数,默认为3
        #! try即尝试执行try代码块中的代码,
        #! 若出现异常则执行expect代码块
        #! 否则执行else代码块  else代码块只能有一个
        #! 无论如何finally代码块都会执行,所以finally代码块一般用于释放文件或网络等资源
        try:
            data=requests.get(url=url,headers=get_headers())
        except requests.exceptions.ConnectionError as e:
            print('请求错误,url:',url)
            print('错误详情:',e)
            data=None
        except:  #未知的错误
            print("未知的错误,url:",url)
            data=None
        else:
            print('请求',url,'成功!')

        finally:
            print('请求完毕,进行下一个！')
            print()
        

        if(data!=None and (500<=data.status_code<600)):  #data.status_code请求状态码 若大于500则需要等待、再次刷新即可
            if(num_retries>0):
                print('服务器错误,正在重试...')
                time.sleep(1)
                num_retries-=1
                get_data(url,num_retries)       #递归
    
        return data

       
if __name__=='__main__':
    for url in urls:
        get_data(url)