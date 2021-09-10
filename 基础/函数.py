'''
Author: Movix
Date: 2021-07-26 03:36:18
LastEditTime: 2021-07-26 16:01:24
FilePath: \python_scrapy\python基础\函数.py
Description: 
'''

#采用关键字实参时就不能使用位置实参
def f(a,b):
    print(a,b)
#f(a=1,2)  #!positional argument follows keyword argument 
#!错误：关键字参数必须跟随在位置参数后面! 
#!因为python函数在解析参数时, 是按照顺序来的, 位置参数是必须先满足, 才能考虑其他可变参数.
f(a=1,b=2)  #*正确



#传参可以带有默认值
#!但是要先列出没有默认值的形参，在列出有默认值的形参
def f(b,a=1):
    print(a+b)
f(2)

'''def f(a=1,b):
    print(a+b)'''
#*错误 必须让没默认值的形参在前



#传递列表备份
def f(a):
    print(a)
a=[1,2,3]
f(a[::]) #!使用name_of_list[::]可以将列表备份作为参数传递，从而不改变原列表本身的属性
#*tips:[::]中可以任意选择原数组的切片大小，步长

#传递任意数量的实参
def f(*a):
    print(a)  
f(1,2,3,4) ##(1, 2, 3, 4)
#*得到的是一个元组


#导入特定的函数并为其起一个别名
# from mouduleName import function_name as fn



#导入模块中的所有函数
#from maduleName import *