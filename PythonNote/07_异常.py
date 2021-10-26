# 异常

'''
try:
    代码块
except (异常类型1,异常类型2) as result: # Exception 可以承接所有的异常类型，是所有异常的父类
    异常处理
    print("异常信息",result)**

'''


try:
 print(1/0)
except Exception as result:
 print(result)
finally:
 print("最后的操作")