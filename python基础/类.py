#创建一个类
class Dog():
    #1.类名一般大写 类名后面要加括号,括号里面写的是该类的父类，若没写则父类是Object
    #2.所有的方法都要加上self参数
    #3.init左右是两个_下划线
    #4.python里面属性就定义在构造器里
    def __init__(self,name,age):   #构造器
        self.name=name
        self.age=age
    def sit(self):
        print(self.name,'is sitting')
    def roll_over(self):
        print(self.name,'is rollingover!')

dog=Dog('asd',2)
dog.sit()
dog.roll_over()

#子类调用父类
class BigDog(Dog):

    def __init__(self, name, age,size):
        super().__init__(name, age)  #调用父类方法
        self.size=size
    
    #子类重写父类方法
    def sit(self):
        super().sit()  #super().fuleifangfa(param)的格式调用父类方法
        print('but it cannot sit')

bd=BigDog('zxc',3,'large')
bd.sit()