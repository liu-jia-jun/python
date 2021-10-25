# Python
## 变量，常量,字符串与操作符

### 变量 

在 python 中变量无需声明，直接赋值使用即可，**使用的变量必须是已经赋值了的**

在 python 中与其他语言不同，python更像是为一个值贴上名字，所以说python中没有变量只有名字

### 字符串 

字符串的拼接：在字符串中使用 + 来对多个字符串进行拼接

转义字符：在字符串中 \ 为转义字符，可以将字母转义成不同意义

原生字符串：只要在字符串前添加字母 r ，此时该字符串就不会发生转义，\ 就会正常输出

```python
# 此时是原生字符串，原生字符串是不能以 \ 结尾的
str  = r"C:\now"   
               
```

#### 关于字符串的方法 

|               capitalize()               | 把字符串的第一个字符改为大写                                 |
| :--------------------------------------: | ------------------------------------------------------------ |
|                casefold()                | 把整个字符串的所有字符改为小写                               |
|              center(width)               | 将字符串居中，并使用空格填充至长度width 的新字符串           |
|         count(sub[,start][,end])         | 返回sub 在字符串中出现的次数，start和end参数范围，可选       |
| encode(encoding="utf-8",errors="strict") | 以encoding指定的编码格式对字符串进行编码                     |
|       endswith(sub[,start][,end])        | 检查字符串是否以sub子字符串结束，如果返回为True，否则返回False start和end 参数表示范围可选 |
|        expandtabs（[tabsize=8]）         | 把字符串中的tab 符号（\t） 转换为空格，如果不指定参数，那么默认的空格数为tabsize=8 |
|         find(sub[,start][,end])          | 检测sub 是否包含在字符串中，如果有则返回索引值，否则返回-1，start 和 end 参数表示范围，可选 |
|         index(sub[,start][,end])         | 与find方法一样，不过如果sub不在String中会返回一个异常        |
|               isalnum（）                | 如果字符串至少有一个字符且所有字符串都是字母或者数数组则返回True ，否则返回False |
|                islnha（）                | 如果字符串至少有一个字符并且所有字符都是字母则返回True，否则返回False |
|              isdecimal（）               | 如果字符串只包含十进制数字则返回True否则返回False            |
|               isdigit（）                | 如果字符串只包含数字则返回True，否则发回False                |
|               islower（）                | 如果字符串至少包含一个区分大小写的字符，并且这些字符都是小写则返回True否则返回False |
|              isnumeric（）               | 如果字符串中只包含数字字符，则返回True，否则返回False        |
|               isspace（）                | 如果字符串中只包含空格，则返回True，否则返回False            |
|               istitle（）                | 如果字符串是标题化（所有单词都已大写开始，并且其余字符都是小写）则返回True，否则返回False |
|               isupper（）                | 如果字符串中至少包含一个区分大小写的字符，并且这些字符都是大写的，则返回True,否则返回False |

### 常量

True：python中，True的T必须大写

False：python中，False的必须大写

![](E:\code\python\PythonNote\imgs\变量与赋值.jpg)

### 操作运算符

### 比较运算符

- \>	大于
- \>=	大于等于
- <	小于等于
- <=	小于等于
- ==	等于
- !=	不等于

### 逻辑操作符

- and	与
- or	或
- not	非

### 数学运算符

- +：	加
- -：	减
- *：	乘
- /：	除 得到一个 float 类型的数据    
- %：	取余
- **：	幂运算，指数乘法，eg：a ** b  相当于 a 的 b 次方
- //：	整除 等到一个整数，向下取整

![](E:\code\python\PythonNote\imgs\操作符优先级.jpg)

## 数据类型



**类型**

整形，浮点型，布尔型，字符型

布尔型数值为 True 和 False ,布尔型可以作为整数型进行计算，True 为1，False 为0

![](E:\code\python\PythonNote\imgs\编程中的数字.jpg)

**确定数值类型**

**type（值）**：返回该值的数据类型

**isinstance（值，数据类型）**：判断值的类型是否与输入的数据类型相匹配，如果匹配则返回 true ，不匹配则返回 false

![](E:\code\python\PythonNote\imgs\类型转换.jpg)

## 分支语句与循环语句

### 条件分支语句（if）

             ```py
             if 判断条件 :
             	print(1)
             elif 判断条件 :
             	print(2)
             else:
             	print(3)
             # eg：
             if 1<2 :
             	print(1)
             elif 1==1:
             	print(2)
             else:
             	print("错误") 
             ```

​                         

### 循环语句

#### while循环

```py
while 判断条件 :
    循环体
    
eg:
while True:
    temp = input("猜数字")
    guess = int(temp)
    if guess == randomNumber:
        print("猜对了")
        break;
    else:
        if guess > randomNumber:
            print("大了")
        else:
            print("小了")  
```

#### for循环

        ```py
        语法：
        for 目标 in 表达式:
            循环体
            
            
        eg：
        
        1.
        for i in [10,20,30]:
            print(i)
            
        2.
        for temp in "abcdefg":
            print(temp)
        ```



#### 三元运算符

            ```py
            big = x if 条件判断 else y
            如果条件判断为真，则将 x 的值赋给big，
            如果条件判断为假，则将 y 的值赋给big
            
            eg:
                
             big = 3 if 3>2 else 2
             此时 big 的值为3 
            ```

  

## 列表



### 初始化列表



 ```py
 初始化列表：
     python中的列表可以存储任意类型的数据
 temp = [1,'abc',[1,2] ]
 
 print(temp)
 
 
 初始化一个空列表
 temp = []
 
 print(temp)
 ```
 
### 列表插入

- append（任意类型数据），将任意类型的数据作为一个整体放在列表的最后一个
- extend（列表），将该列表的数据单个的加入到列表的最后，扩容到列表中
- insert（下标，任意类型数据），将该数据放在指定的下标位置，如果下标越界就会默认放在最后一位

       ```py
       temp = [1,2,3]
       
       print(temp)
       
       1.
       temp.append(4)
       
       print(temp)
       
       2.
       temp.extend([5,6])
       
       print(temp)
       
       3.
       temp.insert(0,0)
       
       print(temp)
       
       ```
           

### 列表删除

- del  +  列表[下标]：	属于一种指令，释放该位置的内存
- pop（[下标]）：	删除指定下标位置的数据，如果没有值，默认删除最后一个
- remove（值）：	删除列表中与参数相匹配的值

           ```py
           temp = [1,2,3]
           
           print(temp)
           
           del temp[0]
           
           print(temp)
           
           
           temp.pop(0)
           
           temp.remove(3)
           
           print(temp)
           ```

 

### 列表操作符

+ 比较操作符：	大于小于等于，用于比较两个列表从第一个数据顺序比较过去，一个数据大就整个列表大

- 逻辑操作符：	与或非，用于连接列表比较结果，返回布尔型的值
- 连接操作符：	+，将一个列表追加到一个列表的后面
- 重复操作符：	*，将该列表复制 n 次
- 成员关系操作符	in，判断某个数据是否在该列表中，只能单层次的比较，not in  判断某个数据是否不在该列表中
- 
- 操作符：	list[start：end]，将list列表从开始到结束复制一份，start 和 end 都是可选值，不填则默认为0 或者最后一位

![](E:\code\python\PythonNote\imgs\列表操作符.jpg)

### 列表内置函数

- list.count(数据)：返回数据在该列表中出现的次数
- list.index（数据[，start][，end]）：返回从指定下标范围内**（可选）**返回该数据在整个列表中的下标
- list.sort（[reverse=True]）：将 list 列表按从小到大循序排序，添加可选内容可以改变排序方式

![](E:\code\python\PythonNote\imgs\列表内置函数.jpg)

    ``` py
        
    >>> [1,2,3]>[1,2,1]
    True
    >>> [1,2,3]<[1,2,1]
    False
    >>> [1,2,3]>[1,2,1] and [1,2,3]<[1,2,1]
    False
    >>> list=[1,2,3]+[1,2,1]
    >>> list
    [1, 2, 3, 1, 2, 1]
    >>> list *=2
    >>> list
    [1, 2, 3, 1, 2, 1, 1, 2, 3, 1, 2, 1]
    >>> 1 in list
    True
    >>> list.index(1)
    0
    >>> list.index(1,1)
    3
    >>> list.index(1,1,2)
    Traceback (most recent call last):
      File "<pyshell#10>", line 1, in <module>
        list.index(1,1,2)
    ValueError: 1 is not in list
    >>> list.count(1)
    6
    >>> list.sort()
    >>> list
    [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3]
    
    
    
    切片
    >>> temp = [1,2,3,4]
    >>> temp[1:3]
    [2, 3]
     
    ```

​          

## 元组：列表的一种



**区别**：列表中的值可以随意更改，但是元组中的值一旦确定不能更改

             ```py
             判断该数据是否为元组：看该数据中是否有逗号列表除外
             
             元组的初始化
             >>> temp = (1,2,3,4)
             >>> temp
             (1, 2, 3, 4)
             >>> temp = 1,2,3
             >>> temp
             (1, 2, 3)
             >>> 
             >>> temp = 1,
             >>> temp
             (1,)
             
             元组的读取
             >>> temp[1]
             2
             
             列表中的操作，原子大部分也能使用
             >>> temp *=2
             >>> temp
             (1, 2, 3, 4, 1, 2, 3, 4)
             ```

​        

## 内置函数



**len（对象）**

得到该对象的长度，例如字符串的长度，数组的长度等等

**print（）|  print（a,b,c[,end=""]）| print（f："文本{变量名}"）**

输出括号内的值  |  以此输出abc的值

默认以回车结束，end=""  可选，以任意字符结束

插入

​                name = "刘佳俊" print(f"My name is {name}")              

**dir（__builtins__）**

查看python中的内置函数等其他的用法吧

**help（内置函数名或者其他）**

查看该内置函数或者其他例如int等等的用法

**int(值)**    

将值转换为 int 型的数值，如果是 float 类型的值转换为 int 型会直接截取整数部分，而不会四舍五入

**str(值)**

将值转换为串类型的值

**float（ 值）**

将值转换为浮点型的值

**range（[start]，stop[，step]）**

range（）函数有三个函数，**strat开始默认为0，stop结束，step步长：默认为1**  

生成一个从start开始到stop结束的数字序列

               ```py
               与for循环搭配使用
               
               
               for i in range(5):
                   print(i)
               
               
               
               for temp in range(1,10,3):
                   print(temp)
               
               
               ```

​         

## 关键字



**断言关键字（assert）**

```py
assert 3>2  正常运行

assert 3<2  直接报错
```

​       

**break;**

退出当前循环

**continue;**

退出本次循环并接着进行下面的循环

##  模块

**import + 模块名：导入相应模块**

**random模块，用于产生随机数**

**random.ranint(a,b)**

随机产生[a,b]之间的整数，闭区间hon 中与其他语言不同，python更像是为一个值贴上名字，所以说python中没有变量只有名字

```py

[,end]: 

```

