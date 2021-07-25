# with open的好处:不用再写close
# with open自动关闭文件
# 写入方式 w,a,wb,r

#用json来存储数据

import json
num=[1,2,3,4]
with open('python基础/num.json','w')as fp:
    json.dump(fp=fp,obj=num) #obj就是需要存储的数据

#用json来取出数据
num=[]
with open('python基础/num.json','r') as fp:
    num=json.load(fp=fp) #注意这里没有obj了 转而使用返回值的形式传递
print(num)