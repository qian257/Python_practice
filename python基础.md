## **Git简单使用**

```bash
# ========== 基础配置（仅首次执行）==========
git config --global user.name "你的名字"          # 设置全局用户名
git config --global user.email "你的邮箱"        # 设置全局邮箱
git config --list                                # 查看git配置

# ========== 仓库创建/克隆 ==========
git init                                         # 当前文件夹初始化为Git仓库
git clone 仓库地址                               # 克隆远程仓库到本地

# ========== 日常提交流程 ==========
git status                                       # 查看文件状态
git add 文件名                                   # 添加单个文件到暂存区
git add .                                        # 添加所有修改文件到暂存区
git commit -m "提交备注"                         # 暂存区提交到本地仓库
git log                                          # 查看提交历史记录

# ========== 远程仓库操作 ==========
git remote -v                                    # 查看远程仓库信息
git remote add origin 远程仓库地址               # 关联本地仓库到远程
git pull origin 分支名                           # 拉取远程代码并合并
git push origin 分支名                           # 推送本地分支到远程

# ========== 分支操作（核心）==========
git branch                                       # 查看本地分支，*为当前分支
git branch dev                                   # 创建dev分支，不切换
git switch -c dev                                # 创建并切换到dev分支（新版推荐）
git switch master                                # 切换到master分支
git merge dev                                    # 在当前分支合并dev分支
git branch -d dev                                # 删除已合并的本地分支
git branch -D dev                                # 强制删除未合并本地分支（谨慎）

# ========== 撤销/回退（救急）==========
git checkout -- 文件名                           # 丢弃未add的文件本地修改
git reset --hard commit_id                       # 强制回退到指定提交，丢弃后续改动（谨慎）

# ========== 危险命令！慎用 ==========
git pull origin master:master -f                 # 强制拉取，覆盖本地分支
git push -f origin 分支名                        # 强制推送，改写远程历史，多人协作严禁
```



## 基础内容

### 强制类型转换

```
str()	int()	float() ...
```



### 输出

```
print(f"字符串{变量名}")   //f 可以将变量名变成其值
```

print语句自带换行效果，即默认print("字符串", end="\n")

不想换行可以print("字符串", end="")

```
print("交换前：a = ",a,"b = ",b,"c = ",c)
print("交换后：a = " + str(a) + "b = ",b,"c = ",c)
print("交换后（占位符）：a = %d, b = %d"%(a,b))
# 推荐
print(f"交换后ffff：a = {a}, b = {b}")
```



### 转义字符

```
# 转义字符 \'  \"  \n  \t
```

```
s3 = 'It\'s a good thing'
s3 = "It's a good thing"
s4 = '\thello的意思\n\t是“你好”'
```



### 输入

```
# 获取键盘上的输入数据 ---input(...)  所有的数据都是字符串类型
```

```
# 案例：银行卡ATM取款
# 总金额
total = 10000

# 1. 输入密码
password = input("请输入您的银行卡密码：")
print(f"密码正确，{password}")

# 2. 请输入取款金额
num = input("请输入您的取款金额：")

# 3. 计算余额并输出 --> num 转为 int 类型 --> int()
print(f"取款后银行卡余额为：{total - int(num)}")

# 计算从键盘输入的两个数的和
num1 = input("相加的第一个数：")
num2 = input("相加的第二个数：")
print(f"{num1} + {num2} = {int(num1) + int(num2)}")
```



### 算术运算符

```
# 算术运算符： + - * / // % **    加减乘除（小数）、整除（结果为整数）、取余/求模、幂指数
# 算术运算符的优先级 --> ** --> * / // % --> + -
```



### if基础

注意冒号，还有相同的缩进，嵌套if缩进，python通过缩进来表示层级关系

```
if 要判断的条件：
	条件成立，要做的事
elif 要判断的条件：
	....
else:
	....
```



### match...case

```
#工作日安排

day = input("请输入今天星期几（1-7）：")

match day:
	case "1":
		print("周一：工作日会议")  #自带break，匹配到后面的会自动跳过
	case "2":
		print("周二：学习培训日")
	case "3"：
		print("周三：项目开发日")
	case "4"|"5":  #4或5都行
		...
	...
	case _:   #不满足上述条件的所有其他情况，可以没有这个
		print("输入错误")
```



### while循环

```
while 条件表达式:
	循环语句1
	循环语句2
	...
else:  #可有可无
	条件为false时，执行该语句
```



### for循环

while循环是通过条件表达式来控制是否要进行下一次循环的。而for循环，本质是一种轮询遍历机制，对一批内容进行逐个处理

```
for 元素 in 待处理数据集:
	循环体代码（对元素进行处理）
else:	#可有可无
	循环结束时，执行的代码
```

```
for i in range(10)
	total += i;
#i会自动更新，不需要手动i++
```



### while和for的使用场景

- while循环：用于在某个条件满足时一直循环，循环的次数通常是未知的，只知道循环开始/结束的条件。（关注的是循环的条件）
- for循环：用于对一个已知的数据集进行遍历或者已知次数的循环（关注的是每一个元素）



### range语句

- **作用**：生成指定规则的数字序列
- **用法1**：range(end) ->获取一个从0开始，到end结束的数字序列（不包含end本身）
  - range(5)获取的数据就是0，1，2，3，4
- **用法2**：range(start,end) -> 获取一个从start开始，到end结束的数字序列（不包含end本身）
  - range(2,8) 获取的数据就是：2，3，4，5，6，7
- **用法3**：range(start,end,step) -> 获取一个从start开始，到end结束的数字序列，step步长（不包含end本身）
  - range(0,10,2)获取的数据就是0，2，4，6，8



### random随机数

```
import random
random_number = random.randint(1,100) 
#随机数是1到100之间的随机数，包含1也包含100
```



## 核心语法--容器

### 列表（list）

- 一次性可以存储多个数据（元素）的数据容器 -----和数组类似
- 定义： **列表名称 = [元素1，元素2，元素3...]**   s = [54, 15, 75, 425, 45]
- 特点：
  - 可以存储不同类型的元素
  - 元素有序、可以重复、元素可以修改
  - 支持反向索引 如:s[0], s[1], s[2]就是s[-3], s[-2]. s[-1]
  - 删除：del s[2],后面会自动补齐



#### 列表——切片

- 介绍：切片是指对操作的数据截取其中一部分的操作。列表、字符串、元组都支持切片操作。
- 语法： **序列数据[开始索引：结束索引：步长]** 
  - 不包含结束索引位置对应的元素（开始索引未指定默认为0；结束索引未指定默认为列表长度（直到列表末尾）；步长未指定默认为1）
  - 索引采用正向、反向索引都可以
  - 步长是选取间隔，默认步长为1，**正数是从前往后截取；负数是从后往前截取**

- 举例： s = ["a", "b", "c", "d", "e", "f", "g"]
  - s[0 : 5 : 1] 切片后的结果为["a", "b", "c", "d", "e"]
  - s[0 : 5 : 2]切片后的结果为["a", "c", "e"]
  - s[::-1]切片后的结果为["g", "f", "e", "d", "c", "b", "a"]



#### 列表常用方法

|   方法    |                             作用                             |        样例        |
| :-------: | :----------------------------------------------------------: | :----------------: |
| append()  |                     在列表的尾部追加元素                     |  s.append(10086)   |
| insert()  |                  在指定索引之前，插入该元素                  |   s.insert(0,92)   |
| remove()  |                  移除列表中第一个匹配到的值                  |    s.remove(75)    |
|   pop()   | 删除列表中指定索引位置的元素（如果未指定索引，默认删除最后一个） | s.pop(2) / s.pop() |
|  sort()   |   对列表进行排序（列表元素的数据类型一致，才可以进行排序）   |      s.sort()      |
| reverse() |                         反转列表元素                         |    s.reverse()     |



#### python中常用于数据统计的常见语句

- min()：获取最小值
- max()：获取最大值
- sum()：求和
- len()：获取元素的个数



#### 解包和组包

- **解包**：将列表这一类容器解开成一个一个独立的元素
- **组包**：将多个值合并到一个容器

- 举例：
  - 解包：  *num_list1 ，将num_list1中的元素一个个解包出来
  - 组包：num_list = [*num_list1, *num_list2]     ==     num_list =  num_list1 + num_list2



#### in判断一个元素是否存在于列表中

- 可以使用 in 运算符，语法为：元素 in 列表
- 返回结果可以为布尔值，True表示存在，False表示不存在



#### 列表推导式

按照一定的规则快速生成一个列表的方法

|                语法格式                |                             举例                             |
| :------------------------------------: | :----------------------------------------------------------: |
|    [要插入的值 for i in 序列/列表]     | num_list = [i**2 for i in range(1,21)]     生成1-20的平方列表 |
| [要插入的值 of i in 序列/列表 if 条件] | nums_list = [i**2 for i in num_list if i % 2 == 0]从一个数字列表中提取所有的偶数，计算其平方组成新的列表 |



### 字符串（string）

- 介绍：字符串是字符的容器，一个字符串中可以存放任意数量的字符
- 特点：不可变性（无法修改）、有序性、可迭代性
- 字符串中的每一个字符元素都有其对应的下标（索引），通过元素对应的索引，就可以获取对应的元素



#### 字符串——切片

和列表一样



#### 字符串常用方法

|     方法     |                             作用                             |          样例          |
| :----------: | :----------------------------------------------------------: | :--------------------: |
|    find()    |  在字符串中查找子串，返回第一次出现的索引位置，找不到返回-1  |    s.find('Python')    |
|   count()    |                 统计子串在字符串中出现的次数                 |      s.count('H')      |
|   upper()    |     将字符串中所有字母转换为大写返回，不会修改字符串本身     |       s.upper()        |
|   lower()    |    将字符串中的所有字母转换为小写返回，不会修改字符串本身    |       s.lower()        |
|   split()    |      将字符串按指定分隔符分割成列表(会把切割的字符拿掉)      |      s.split(' ')      |
|   strip()    | 去除字符串两端的空白字符或者指定字符（“12”会视作分开的两个字符） | s.strip()/s.strip('*') |
|  replace()   |          将字符串中的指定字串替换为新的子串(H-->C)           |   s.replace('H','C')   |
| startswith() |           检查字符串是否以指定子串开头，返回布尔值           |   s.startswitch('p')   |



#### in判断一个子串是否存在字符串中

同列表



#### re模块（正则表达式模块）

`re` 是python内置模块，不需要pip安装，`import re ` 直接导入

作用： 用正则表达式，最字符串做匹配、查找、替换、分割，适合处理文本



### 元组（tuple）

- 介绍：元组是不可变的序列，类似于列表，但创建后不能修改
- 特点：
  - 可以存储不同类型的元素
  - 元素可以重复、有序、不可以修改（支持索引访问、切片）
  - 可以修改嵌套的list的元素内容
  
- 定义：

![definition of set](D:\Leo7\plan\media\python基础\definition of set.png)

- 方法：
  - 元组.count() ：统计某元素在元组中出现的次数
  - 元组.index()：查找某个元素在元组中的索引位置（第一次出现的位置），不存在会报错
  - len(元组)：统计元组里内的元素的个数



#### 注意

如果定义单元素的元组，单个元素之后需要加上逗号，比如（100，）



#### 组包和解包

- 组包（packing）：将多个值合并到一个容器（元组、列表）中，变量数量与容器元素个数一致，不然会报错
- 解包（unpacking）：将容器（元组、列表）解开成独立的元素、分别赋值给多个变量

![packing & unpacking](D:\Leo7\plan\media\python基础\packing & unpacking.png)

**说明**：在元组解包时，* 表示收集剩余的所有元素（列表），允许我们处理不确定数量的元素（生成列表，以便于可以进行进一步的处理）



### 集合（set)

- 介绍：集合是一种无序的、不可重复、可修改的数据容器
- 特点：
  - 可以存储可哈希（不可变类型）的不同类型元素、不能放可变对象（列表、字典、集合本身，不能作为集合元素）
  - 元素无序、唯一、自动去重
  - 因为集合是无序的，所以集合不支持下标索引访问
- 定义：

![definition of set](D:\Leo7\plan\media\python基础\definition of set.png)



#### 集合常用方法：

- 集合.add(元素) ：将指定元素，添加到集合内（修改集合本身）
- 集合.remove(元素) ：将指定元素，从集合内移除（修改集合本身）
- 集合.pop() ：从集合中随机取出一个元素，返回一个元素的结果，同时修改集合本身
- 集合.clear() ：清空集合
- 集合1.difference(集合2) ：取出集合1和集合2的差集（集合1有但是集合2没有的），**返回一个新的集合**，**集合1和集合2都不变**
- 集合1.difference_update(集合2) ：在集合1内删除和集合2相同的元素，**集合1被修改，集合2不变**	
- 集合1.union(集合2) ：将集合1和集合2合成新集合，**返回新集合，集合1和集合2不变**



#### 注意：

- 空集合的定义不可以使用{ },{ }表示的是空字典；
- 由于集合是无序的，因此集合不支持下标索引访问的，所以不能使用while循环遍历、但是可以使用for循环（for element in my_set : ) 



### 字典（dict）

- 介绍：字典里面存储的是键值对（key: value) 类型的数据，可以根据键（key）找到对应的值（value)
- 特点：键值对（key: value）存储、键（key）不能重复、可修改（重复会发生后面的value值覆盖前面的值）
- 定义：

![definition of dict](D:\Leo7\plan\media\python基础\definition of dict.png)

 

#### 常用操作

![Common Op of dict](D:\Leo7\plan\media\python基础\Common Op of dict.png)



#### 字典的遍历

- 字典支持for循环遍历
- 通过keys(), value(), items() 进行循环遍历



```python
if word in dic:
    dic[word] += 1
else:
    dic[word] = 1


#可以替换成
dic[word] = dic.get(word, 0) + 1

```

原理：`dict.get(key,默认值)`，key 不存在返回 0



#### 注意

- 字典（dict）中的value可以是任何类型的数据源，而key不能为可变类型（如：不能为 列表list、集合set、字典dict）
- 字典内的key不允许重复，如果重复定义，后面的覆盖前面的
- 字典是没有索引下标的，不能根据索引获取值，只能根据key获取value



## 函数

### 匿名函数

没有名称的函数，需要通过lambda表达式来声明函数，可以简化简单函数的编写（单行表达式）

```python
#定义匿名函数
lambda 参数列表 : 函数体

lambda : print('---------------------------')
lambda x, y : x + y
```

注意：

- 函数逻辑比较简单（单行表达式）且只在一个地方使用时，可以考虑使用匿名函数，简化书写（通常作为高阶函数的参数使用）
- 匿名函数中可以返回结果，也可以不返回结果。返回结果时，不需要写return，表达式的运行结果就是要返回的结果



### sort()和sorted()

- `list.sort()`：原地排序，直接修改原列表，返回值时`None`
- `sorted(可迭代对象)`：生成新列表，原数据不变；可以给所有可迭代对象排序（列表、元组、字典items等）



#### `list.sort()`方法

特点：

1. 只列表list能用，元组、字典不能调用`.sort()`
2. 原地修改，不产生新内存
3. 参数：`key` 、`reverse=True/False`



```python
data_list = ["c++", "c", "python", "jack", "php", "java", "go"]

#按字符串排序
data_list.sort()

#按元素个数进行排序
data_list.sort(key=lambda item : len(item))
```



#### `sorted()`方法

sorted(可迭代对象、key=函数、reverse=布尔值)，作用：排序、返回一个新列表，不会改动原来的数据

第一个参数：要排的数据。

第二个参数：key=排序规则（接收一个函数）

第三个参数：是否倒序

```python
#对学生成绩进行排序
sorted_list = sorted (students.items (), key=lambda x:x [1], reverse=True)

"""
流程：
sorted会循环把students里面每一个元素传给key的规则，元素叫x
这里的每一个x时（”名字“， 分数）的元组
x[1]就是取第二个值-->成绩
sorted拿着这个返回值（成绩）去比较大小、排序
"""

```

**三种写法对比：**

1. `sorted(students)` → 遍历**keys**，排序【姓名】，返回姓名 list
2. `sorted(students.values())` → 遍历**values**，只排序【成绩】，返回成绩 list
3. `sorted(students.items())` → 遍历**(key,value) 元组**，排序【姓名 + 成绩整套数据】，返回元组列表



## 文件

文件的基本操作，大概可以分成三个步骤：

1. ​	打开文件
2. ​	读写文件
3. ​	关闭文件

### 打开文件（open()打开函数）

​	使用open()函数，可以打开一个已经存在的文件，或者创建一个新文件，语法如下：

```python
open(name,mode,encoding)

#name：是要打开的目标文件名的字符串（可以包含文件所在的具体路径）
#mode：设置打开文件的模式（访问模式）：只读、写入、追加等
#encoding：编码格式（推荐使用UTF-8）
```

```python
#示例代码：
f = open('python.txt','r',encoding = "UTF-8")
#encoding的顺序不是第三位，所以不能用位置参数，用关键字参数直接指定
```

mode常用的三种基础访问模式

| 模式 |                             描述                             |
| :--: | :----------------------------------------------------------: |
|  r   | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。如果文件**不存在，报错。** |
|  w   | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，原有内容会被删除。如果文件**不存在，创建新文件。** |
|  a   | 打开一个文件用于追加，新的内容将会被写入到已有内容之后。如果该**文件不存在，创建新文件**进行写入。 |

### 读操作相关方法

```python
read():
文件对象.read(num)
#num表示要从文件中读取的数据的长度（单位是字节），如果没有传入num，那么就表示读取文件中的所有的数据。

readline():
#readline一次读取一行内容
readlines():
#readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素。

f = open('python.txt')
content = f.readlines()

#['hello world\n', 'abcdefg\n', 'aaa\n', 'ccc']
print(content)

#for循环读取文件行
#for line in f:
#	print(f"每一行的数据是:{line}")

#关闭文件
f.close()
```

当对一个文件进行操作的时候，每次都是接着上次读取的位置后继续读取的



### 写和追加操作相关方法

```python
#1.打开文件
f = open('python.txt', 'w')    #写
f1 = open('python.txt', 'a')   #追加

#2.文件写入
f.write('hello world')    #写权限会把文件删除重新写
f1.write('nihaoya!')	  #追加只会在已有内容后面加上新的内容

#3.内容刷新
f.flush()
```

**注意：**

- 直接调用write，内容并未真正写入文件，而是会积攒在程序的内存中，称之为缓冲区
- 当调用flush的时候，内容会真正写入文件（close()方法内置了flush()功能）
- 这样做是避免频繁的操作硬盘，导致效率下降（攒一堆，一次性写磁盘）



### 关闭文件 （close()关闭文件）

close() 关闭文件对象

```python
f = open("oython.txt", "r")
f.close()
#最后通过close，关闭文件对象，也就是关闭对文件的占用
#如果不调用close，同时程序没有停止运行，那么这个文件将一直被python程序占用
```



### with open()语法

```python
with open("python.txt", "r") as f:
    f.readlinse()

#通过在with open的语句块中对文件进行操作
#可以在操作完成后自动关闭close文件，避免遗忘掉close方法
```



### 汇总

![image-20261022162332274](D:\Leo7\plan\media\python基础\image-20261022162332274.png)





## 异常

### 捕获异常

#### 捕获常规异常

语法：

```python
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
    
#尝试以'r'模式打开文件，如果文件不存在，则以'w'方式打开 
try:
    f = open('linux.txt','r')
except:
    f = open('linux.txt', 'w')
```



#### 捕获指定异常

语法：如果尝试执行的代码异常类型和要捕获的异常类型不一致，则无法捕获异常。

一般try下方只放一行尝试执行的代码。

```python
try: 
    print(name)
except NameError as e:
    prin("出现了变量定义的异常")
    print(e) #异常的名称
```



#### 捕获多个异常

当捕获多个异常时，可以把要捕获的异常类型的名字，放到except后，并使用元组的方式进行书写。

```python
try:
	print(1/0)
except(NameError,ZeroDivisionError):
	print('ZeroDivision错误...')
```



#### 捕获所有异常

等同于捕获常规异常

```python
try:
	尝试语句
except Exception as e:
	print("出现异常了")
else:
    print('没有出现异常')
finally:  #无论是否有异常，finally后的语句是一定要执行的
    f.close()
```



### 异常的传递

异常是具有传递性的

```python
def func01():
    print("这是func01开始")
    num = 1 / 0
    print("这是func01结束")
   
def func02():
    print("这是func02开始")
    func01()
    print("这是func02结束")
    
def main():
	try:
        func02()
    except Exception as e:
        print(e)
```

当**函数func01**中发生异常，并且没有捕获处理这个异常的时候，异常会传递到**函数func02**，当func02也没有捕获处理这个异常的时候，**main函数**会捕获这个异常，这就是**异常的传递性**

**当所有的函数都没有捕获异常的时候，程序就会报错**





## 模块

python模块（Module），是一个python文件，以 .py 结尾。模块能定义函数，类和变量，模块里也能包含可执行的代码。



**模块的作用**：python 中有很多各种不同的模块，每一个每块都可以帮助我们快速的实验一些功能，比如实现和时间相关的功能就可以使用time模块，我们可以惹味一个模块就是一个工具包，每一个工具包都有各种不同的工具供我们使用进而实现各种不同的功能。

总结：模块就是一个python 文件，里面偶类、函数、变量等，我们可以拿过来使用（导入模块去使用）



### 模块的导入方式

模块在使用前需要先导入 导入的语法如下：

```python
[from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]

#常用的组合形式如：
import 模块名
from 模块名 import 类、变量、方法等
from 模块名 import *
import 模块名 as 别名
from 模块名 import 功能名 as 别名
```



通过使用 import 导入 time 模块使用 sleep 功能

```python
import time
time.sleep(5)
```



通过使用 from 导入 time 的 sleep 功能

```python
from time import sleep
sleep(5)
```



使用 * 导入 time 模块的全部功能

```python
form time import *  # * 表示全部的意思
sleep(5)
```



as 定义别名

```python
import time as t
t.sleep(5)

from time import time as sl
sl(5)
```



**注意**：当导入不同模块的同名功能时，后导入的模块会把前一个覆盖掉



### 自定义模块

就是一个普通的python文件



### `__main__` 变量

当导入的模块有直接的函数调用时，在导入的时候，会自动进行函数的调用执行，所以要使用`__main__`变量。

```python
#my_module.py

def test(a, b):
	print(a + b)
	
if __name__ == '__main__':
	test(1, 2)
```

```python
#test_my_module.py

from my_module import test
#此时不会调用执行test
```



### `__all__` 变量

如果一个模块文件中有`__all__` 变量，当使用`from xxx import * ` 导入时，只能导入这个列表中的元素

```python
#my_module.py

__all__ = ['test_a']

def test_a(a, b):
    print(a + b)

def test_b(a, b):
    print(a - b)

```

```python
#test_my_module.py

from my_module import * #当my_module.py文件中有了__all__变量，此时 * 只能导入test_a
test_a(1, 2)
test_b(2, 1) #报错

#但是可以单独导入test_b
#from my_module import test_b
#test_b(2, 1)  #可以
```





## 包

### 什么是 python 包

从物理上看，包就是一个文件夹，在该文件夹下包含了一个`__init.py__` 文件，该文件夹可用于包含多个模块文件

从逻辑上看，包的本质依然是模块

![image-20261026170354658](D:\Leo7\plan\media\python基础\image-20261026170354658.png)

有`__init.py__` 文件就是包，没有就是普通文件夹



### 导入包

```python
#方式一：
import 包名.模块名
包名.模块名.目标

#方式二
from 包名 import 模块名
模块名.目标

#方式三
from 包名.模块名 import 方法目标
目标

```



#### `__all__` 变量

注意：

必须在`__init__.py` 文件中添加`__all__` =[]，控制允许导入的模块列表

`__all__` 针对的是 ` from ... import * ` 这种方式，对` import xxx` 这种方式是无效的



### 安装第三方包

```
pip 第三方包  #默认国外网站
```





## numpy

导入数据包`import numpy as np`

```python
import numpy as np

a = np.array([1,2,3],
             [2,3,4])
#需要定义类型
a = np.array([2,23,4],dtype=int)

#定义全部为0的矩阵,三行四列
a = np.zeros((3,4),dtype=int64)
a = np.ones((3,4),dtype=float64)

#定义有序的矩阵
a = np.arange(10,20,2)  #a = [10 12 14 16 18]
"""
a = [[0 1 2 3]
	 [4 5 6 7]
	 [8 9 10 11]]
"""
a = np.arange(12).reshape((3,4))

"""
np.linspace(start, stop, num)
作用：在 start 到 stop 之间，均匀生成 num 个等间距的数，默认返回浮点数数组
"""
a = np.linespace(1,10,5) #a = [1. 3.25 5.5 7.75 10.] 
```

  
