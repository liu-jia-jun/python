# 函数

'''
函数定义
def 函数名(形参):
    函数体


函数调用
函数名(实参)
'''

def sayhello(str):
    print("hello" + " " + str)
    return str


return_value = sayhello("world")

print(return_value)



# 全局变量和局部变量

# global 全局变量  在函数内部使用局部变量