'''************************************************ 
 * @Author: Movix
 * @Date: 2021-07-26 23:25:27
 * @LastEditTime: 2021-07-27 00:11:25
 * @Github: https://github.com/Moviw
 * @FilePath: \数据分析\get_Dynamic_UA.py
 * @Description: 通过fake_useragent获取动态UA(字典)
 ************************************************'''
from fake_useragent import UserAgent
def get_headers():
    ua = UserAgent()
    user_agent = ua.random
    headers = {'User-Agent': user_agent}

    return headers