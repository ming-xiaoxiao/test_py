# I/O操作

path = 'C:/Users/Wang/PycharmProjects/book_learn/test.txt'
with open(path) as file_obj:
    # 1.
    # contents = file_obj.read()
    # print(contents.strip())
    # 2.
    # for line in file_obj:
    #     print(line.rstrip())
    # 3.
    lines = file_obj.readlines()

for line in lines:
    print(line.rstrip())

# 写入————覆盖写入模式
with open(path, 'w') as file_obj:
    file_obj.write('this is a test1\n')

# 写入————增加append写入模式
with open(path, 'a') as file_obj:
    file_obj.write('this is a test2')

################# 异常
try:
    print(5/0)
except ZeroDivisionError:
    print("zero_error")
except FileExistsError:
    print('file_error')


