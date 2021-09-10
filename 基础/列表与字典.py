service = ['http','ssh','ftp']
#列表切片

print(service[1:])   ##打印第一个元素之后的内容     ['ssh', 'ftp']
print(service[:-1])  ##打印最后一个元素之前的内容   ['http', 'ssh']
print(service[::-1])  ##倒序输出                  ['ftp', 'ssh', 'http']


#成员操作
print('nfs' in service)   ##判断是否存在   False


#复制列表service[::]即可


#列表解析
#每一个列表推导式包括在一个 for 语句之后的表达式，零或多个 for 或 if 语句。
# 返回值是由 for 或 if 子句之后的表达式得到的元素组成的列表。

#基本列表解析
li=[x for x in range(1,10)]
print(li)  #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print([x*2 for x in li])  #[2, 4, 6, 8, 10, 12, 14, 16, 18]
#!第一个表达式x or x*2是列表中元素的表达式  后面是x的范围

#条件列表解析
b=[ x for x in range(10) if x%2 ==0 ]
print(b)   #[0, 2, 4, 6, 8]
#!与基本列表解析前面一样，在后面加上限制条件