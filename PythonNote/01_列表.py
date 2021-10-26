# 列表

# 定义一个空的列表  list = []

list = [1,"2",3.0] # 列表中可以混合存储数据，也就是说什么类型的数据都能存储在同一个列表中

# 列表操作

# 增
list.append("小刘")  # 在列表末尾追加一个元素

list.extend([4,5]) # list.extend（列表），将该列表的数据单个的加入到列表的最后，扩容到列表中

list.insert(len(list),"米娜") # list.insert(下标,元素) 将元素插入到列表中指定的位置

# 删

del list[0] # 删除指定元素，del list 删除整个列表

list.pop() # 弹出最后一个元素,list.pop(index) 添加index 参数，指定弹出该位置的元素

list.remove("2") # 删除value 元素，如果重复的话，只会删除第一个


# 改

list[0] ="被修改的元素"  # 通过下标访问并直接赋值即可修改

# 查 【in，not in】,

print("判断这个值是否存在该列表中","米娜" not in list)

print("index方法测试，返回该元素的下表",list.index(4)) # 如果列表中没有这个元素的话会报错

print("查找元素在列表中的个数",list.count(3))

# 列表反转,列表排序
list.reverse() # 反转

list.sort() # 排序


print(list)

# 循环打印列表
for  item in list:
    print(item)