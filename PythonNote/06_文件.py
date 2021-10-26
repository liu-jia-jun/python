# 文件操作

# 打开文件  open("文件路径",打开模式) 方法打开一个已经存在的文件或者创建一个新文件再打开，创建文件必须要有一个可写模式，并返回该文件的对象，默认为r 只读模式
# 引入操作文件的库
import os
os.rename("./static/test.txt","./static/test1.txt")
f = open("./static/test1.txt","r") # 打开文件，w模式（可读可写模式），文件不存在就新建文件



# f.write("hello world") # 将字符串写入到文件中

print(f.read(2)) # 读单个字符，可以指定个数，如果不指定个数就是读取全部
print(f.read(3))


print(f.readline()) # 读取整行

f.readlines(2) # 读取多行以列表的形式返回每一行

f.close()# 关闭文件

