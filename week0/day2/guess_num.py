import random
#猜数字，1到100
def game():
    num = random.randint(1,100)
    count = 0
    while True:
        keyboard_input = input("请输入您的数字(按q退出)：")
        #判断输入q退出
        if keyboard_input.lower() == 'q':
            print("程序已退出！")
            return
        #尝试转数字
        try:
            guess = int(keyboard_input)
        except ValueError:
            print("输入的不是数字，程序已退出！")
            return
        
        count += 1
        if guess == num:
            print(f"恭喜你猜对了！！,你猜了{count}次")
            again = input("是否再玩一次（y/n)")
            if again.lower() == 'y':
                count = 0
                num = random.randint(1,100)
                continue
            else:
                return
        elif guess < num:
            print("小了")
        else:
            print("大了")


game()