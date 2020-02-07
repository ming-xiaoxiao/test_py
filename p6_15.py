# 元组不能修改元素
print(12 > 11 and 11 > 13)

# 字典
dic = {1:'a',2:'b'}
print(dic)
del dic[1]
print(dic)
print(dic.items())
for k,v in dic.items():
    print('key is : '+str(k)+'\nvalue is: '+str(v))
print(dic.keys())
print(dic.values())
# 同理可以用for循环遍历所有键

# set 集合————自动去重

# input
msg = input('tell me sth:')
print('you tell ————' + msg)