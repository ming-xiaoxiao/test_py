# 介绍一些常用函数
msg = "this is a massage"
print('\ttitle函数：' + msg.title())
print('\tupper函数：' + msg.upper())
print('lower函数：' + msg.lower())
print((msg+'   ').rstrip())
print(('    ' + msg).strip())

string = 'this is a test'
# split函数返回的是列表
print(string.split())


# 列表
li = []
li.append("a")
li.append("b")
li.append("c")
print(li)
li.insert(0,"z")
print(li)
del li[0]
print(li)
li.pop()    # 删除末尾元素
print(li)
print(li.pop(1))    # 弹出指定元素
li.append(1)
li.append(2)
print(li)
li.remove('a')  # 删除指定值
print(li)
li = ['c','a','b']
print(sorted(li))   # 临时排序
li.sort()   # 永久性排序
print(li)
li.sort(reverse=True)
print(li)
li.reverse()
print(li)

# 创建列表
li = list(range(1,6))
print(li)
li = list(range(1,6,2))
print(li)

li = [value**2 for value in range(1,11)]
print(li)

# 切片
print(li[-3:])

# 复制问题
list1 = ['a','b']
list2 = list1[:]
list1.append('c')
list2.append(2)
print(list1)
print(list2)

list2 = list1
list1.append(1)
list2.append(2)
print(list1)
print(list2)

list2.append(1)
print(list2)
list2.remove(1)
print(list2)


