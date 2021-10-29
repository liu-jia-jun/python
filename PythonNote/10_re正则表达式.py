# 正则表达式

# 先引入re库
import re

# 创建模式对象

pat = re.compile("A") # 此处的AA是正则表达式的模板用于验证其他的字符串
# 这里的search 方法中的字符串是被验证的字符串,这里返回的是模板字符串在被检验的字符串中第一次出现的位置
m = pat.search("CBA")


# 不创建模式对象时

m = re.search("A","CBA") # 这里没有创建模板对象，而是传入两个参数，那么前面的字符串作为模板对象，后面的字符串是被检验的对象

m = re.findall("[A-Z]","Abcdfjei")

m = re.findall("[A-Z]+","asdfjiAAAaa")


# sub

m = re.sub("a","A",r"abcdefaaa") # 在abcdefaaa中找到a并用A替换掉a,并返回替换的字符串

# 建议在正则表达式中，被比较的字符串前面加上r，这样可以不用担心字符串转义问题





print(m)