# 函数参数
# 5种参数类型

# 1.位置参数
def fun(name,age,country = 'China'):
    return '\n'+'hello!!'+str(name)+'\n'+str(age)+' years old' +'\ncome from ' + country


print(fun('wells',12,'USA'))
print(fun(age=12,name='wells'))
# 2.默认参数
# 见上//需要注意的是，默认参数必须放在最右，否则会产生二义性

# 3.可变参数————是一个元组
def getsum(*num):
    sum = 0
    for n in num:
        sum += n
    return sum

list = [2, 3, 4]

print(getsum(1, 2, 3))
print(getsum(*list))    # 将list变成可变参数

# 4.关键字参数————是一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('wells',12)
person('wells',12,gender = 'M')
person('wells',12,gender = 'M',address = 'China')

# 5.命名关键字参数
# 关键字参数 和 命名关键字参数 的 区别在于
# 前者可以传递任何名字的参数，而后者只能传递*后面名字的参数。
def personinfo(name, age, *, gender, city):
    #只能传递gender和city参数
    print(name, age, gender, city)

personinfo('Steve', 22, gender = 'male', city = 'shanghai')
# personinfo('Steve', 22,gender='M')    #wrong
# personinfo('Steve', 22) #wrong

# 如果函数定义中已经有了一个可变参数
# 后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def personinfo(name, age, *args, gender, city):
    #args可以传递一个list 其后只能传递gedner和city参数
    print(name, age, gender, city)
