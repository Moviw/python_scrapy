'''************************************************ 
 * @Author: Movix
 * @Date: 2021-07-28 22:03:02
 * @LastEditTime: 2021-07-29 20:10:14
 * @Github: https://github.com/Moviw
 * @FilePath: /数据可视化/tempCodeRunnerFile.py
 * @Description: 
 ************************************************'''
import re
pattern = re.compile(r"[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)")

strs = '今天是2020/12/20，去年的今天是2019.12.20，明年的今天是2021-12-20'
result = re.findall("\d{4}.?\d{1,2}.?\d{1,2}",strs)
wew=re.Match
print(result)
['zhuwjwh@outlook.com', '123456@qq.org']