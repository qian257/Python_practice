
#循环斐波那契
def fib_loop(n):
    a, b = 0, 1
    res = []
    #代码里从头到尾**没有使用 i 这个变量**，按照规范就写成`_`
    for _ in range(n):
        res.append(a)
        a, b = b, a + b
    return res

#递归斐波那契，n大了存在大量的重复计算，所以速度慢
def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n - 1) +fib_rec(n - 2)


num = input("请输入：")

try:
    n = int(num)
except ValueError:
    print("请输入数字!!")
else:
    #res1记录递归的斐波那契数列
    res1 = []
    for i in range(n):
        res1.append(fib_rec(i)) 
    #res2记录循环的斐波那契数列
    res2 = fib_loop(n)

    print(f"递归的斐波那契：{res1}")
    print(f"循环的斐波那契：{res2}")
    print("两组结果是否一致：", res1 == res2)