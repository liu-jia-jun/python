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

print("============================================================")

# 搜索文档内容

import re

# find_all() 方法搜索文档内容
# 字符串过滤：会查找与字符串完全匹配的所有内容
list = bs.find_all("a") # 找出所有的a标签，返回一个列表


# 使用正则表达式搜索，使用search() 方法来匹配内容
list = bs.find_all(re.compile("a"))# 找出所有包含a的标签，eg: a,head,meta 标签等

# keyword 关键字参数，类似与属性与属性值匹配
list = bs.find_all(id="head")
list = bs.find_all(href="https://www.baidu.com")# 匹配属性和属性值，返回列表


# 方法：传入一个函数，根据函数的要求来搜索
def name_is_exists(tag):
    return tag.has_attr("name")

list = bs.find_all(name_is_exists)


# limit 限制返回的记录条数

list = bs.find_all("a",limit=3) # 最多返回三条数据


# text 参数，一般和正则表达式配合使用
list = bs.find_all(text = "新闻")
list = bs.find_all(text = ["新闻","美食"])
list = bs.find_all(text= re.compile("\d")) # 应用正则表达式来查找包含特定文本的内容（标签里的字符串）

# 通过css选择器来匹配内容

list = bs.select("title")

list = bs.select("#head")

list = bs.select("a[class='bri']")# 通过属性来查找

list = bs.select("head > title") # 通过子标签来查找


for item in list:
    print(item)