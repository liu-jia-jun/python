# BeautifulSoup 用于数据解析

'''
BeautifulSoup4 将复杂HTML文档转换成一个复杂的树形结构，每个节点都是Python对象，所有对象可以归为4种

- Tag
- NavigableString
- BeautifulSoup
- comment

注意: 这里的对象类型是读取的类型，是指将读取中的内容进行分类，总体都是通过BeautifulSoup对象进行文档的读取操作
'''
# 引入BeautifulSoup包
from bs4 import BeautifulSoup

# 打开文件，并读取到html，并将html传递到BeautifulSoup对象中，并返回一个BeautifulSoup对象
# 将文件中的内容读取出来，以字符串的形式放到BeautifulSoup对象中形成一个Dom树，之后在BeautifulSoup对象中读取内容即可
file = open("./static/test2.html","rb")

html = file.read()

bs = BeautifulSoup(html,"html.parser")

# Tag形式 读取识别的第一个标签及其内容,根据标签进行读取，返回识别的第一个标签及其内容

print(bs.title)
print(bs.div)
print(bs.a)

# NavigableString 标签中的内容（字符串）

print(bs.title.string)


# attrs, 读取识别到的第一个标签中的所有属性及其属性值并以字典的形式返回


print(bs.a.attrs)

# BeautifulSoup 表示整个html文档

print(bs.name)
print(bs)

# comment 输出的内容不包含注释符号

print(bs.a.string)

# 文档的遍历
print(bs.head.contents)
print(bs.head.contents[1])

# 搜索文档内容

