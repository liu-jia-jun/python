# 字典 (dict)

# 字典是无序的对象集合，使用键值对的形式进行存储，具有极快的查找速度

# 字典中的键 必须是使用不可变类型，同一个字典中的key 值必须是唯一的

# 创建一个空字典 info = {}

info = {"name":"小刘"}

print(info["name"]) # 通过键值来访问 ，如果访问一个不存在的键值会直接报错

print(info.get("age","默认值")) # 通过get 方法来访问字典，如果该没有找到该键值会返回一个默认值为None 可以设定默认值 info.get("键名","默认值")

# 增加

info["sex"]="man"

# 删

del info["sex"] # 删除指定的键值对，如果再次访问会直接报错

info.clear() # 清空该字典中的所有值

# 改 直接赋值即可

info["name"] = "米娜"

# 查

print(info.keys())  # 得到所有的键，（得到一个列表）
print(info.values()) # 得到所有的值，（得到一个列表）


print(info)


# 遍历，info.items() 得到字典中一组一组的键值对
for key,value in info.items():
    print(key,value)


