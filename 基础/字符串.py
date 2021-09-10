#删除空白
i=' asd asd '
print(i.strip())    #asd asd 去除两边空白
print(i.lstrip())   #asd asd  去除左空白
print(i.rstrip())   # asd asd 去除右空白



#len函数
a='asd'
print(len(a))  #3



#使用[]提取字符串中的字符
a = 'abcdefghijklmnopqrstuvwxyz'
print(a[0])#a
print(a[25])#z
print(a[-1])#z



# split()可以基于指定分隔符将字符串分隔成多个子字符串(存储到列表中)。
# 如果不指定分隔符,则默认使用空白字符(换行符/空格/制表符)。
b = "to be or not to be"
print(b.split())    #['to', 'be', 'or', 'not', 'to', 'be']
print(b.split('be'))#['to', ' or not to', '']


#join()用于将一系列子字符串连接起来
c=['qwe','asd','zxc']
print('8'.join(c))   #qwe8asd8zxc

#!推荐使用 join函数,因为 join函数在拼接字符串之前会计算所有字符串的长度,然后逐一拷贝,仅新建一次对象。
import time
time01 = time.time() #起始时刻
r = ""
for i in range(10000000):
    r += "sxt"
time02 = time.time() #终止时刻
print("运算时间："+str(time02-time01))   #运算时间：19.844109535217285
time03 = time.time() #起始时刻
li = []
for i in range(10000000):
    li.append("sxt")
r = "".join(li)
time04 = time.time() #终止时刻
print("运算时间："+str(time04-time03))   #运算时间：1.0002288818359375

#常用''.join('被连接字符串')连接字符串