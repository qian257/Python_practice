while True:
    User_input = input("请输入式子（如：3+5，按'q'退出）：")
    if User_input == 'q':
        print("程序退出")
        break

    #按空格分割
    parts = User_input.strip().split()
    #格式必须是三个部分
    if len(parts) != 3:
        print("格式错误")
        continue

    a_str, op, b_str = parts
    #尝试转数字
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        print("格式错误")
        continue

    #判断符号
    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a * b
    elif op == '/':
        try:
            res = a / b
        except ZeroDivisionError:
            print("除数不能为0")
            continue
    else:
        print("格式错误")
        continue

    print(f"结果：{res}")