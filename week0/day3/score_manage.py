students = dict()

# 添加学生
def add_stu():
    name = input("请输入要添加的学生姓名：").strip()
    #空姓名判断
    if len(name) == 0:
        print("错误：姓名不能为空！")
        return

    #判断姓名存在
    if name in students:
        print(f"添加失败，学生{name}已存在")
        return

    #成绩输入
    try:
        score = int(input("请输入学生成绩："))
    except ValueError:
        print("成绩必须为整数，添加失败")
        return
    students[name] = score
    print(f"学生{name}添加成功！，成绩：{score}")
    return 

#删除学生
def delete_stu():
    name = input("请输入要删除的学生姓名：").strip()
    #空姓名判断
    if len(name) == 0:
        print("错误：姓名不能为空！")
        return
    
    #判断姓名存在
    if name in students:
        del students[name]
        print(f"学生{name}删除成功！")
    else:
        print(f"学生{name}不存在，删除失败！")
    return

#查询学生
def query_stu():
    name = input("请输入要查询的学生姓名：").strip()
    #空姓名判断
    if len(name) == 0:
        print("错误：姓名不能为空！")
        return
    
    #判断姓名存在
    if name in students:
        print(f"学生{name},成绩{students[name]}")
    else:
        print(f"查询失败！学生{name}不存在")
    return

#修改成绩
def update_stu():
    name = input("请输入要修改成绩的学生姓名：").strip()
    #空姓名判断
    if len(name) == 0:
        print("错误：姓名不能为空！")
        return
        
    #判断姓名存在
    if name in students:
        try:
            new_score = int(input("请输入新的成绩："))
            students[name] = new_score
            print(f"学生{name}的成绩已修改，修改后的成绩为：{new_score}")
        except ValueError:
            print("修改失败，成绩必须是整数！")
    else:
        print(f"学生{name}不存在，修改失败！")
    return

def avg_stu():
    if len(students) == 0:
        print("暂无学生数据，无法计算平均分！")
        return
    total = sum(students.values())
    count = len(students)
    avg_score = total/count
    print(f"全班平均分：{avg_score:.1f}")

def sort_by_score():
    if len(students) == 0:
        print("暂无学生数据！")
        return
    # items拿到(姓名,成绩)，key取成绩，reverse=True降序
    sorted_list = sorted(students.items(), key=lambda x:x[1], reverse=True)
    print("=====学生成绩（从高到低）=====")
    for name, score in sorted_list:
        print(f"{name} : {score}")


def main():
    while True:
        print("\n===== 学生成绩管理系统 =====")
        print("a 添加学生")
        print("b 删除学生")
        print("c 查询学生")
        print("d 修改成绩")
        print("e 计算全班平均分")
        print("f 按成绩降序输出")
        print("g 退出系统")
        choice = input("请选择功能(a-g)：").strip()

        match choice:
            case "a":
                add_stu()
            case "b":
                delete_stu()
            case "c":
                query_stu()
            case "d":
                update_stu()
            case "e":
                avg_stu()
            case "f":
                sort_by_score()
            case "g":
                print("系统退出，再见！")
                break
            case _:   # _ 代表默认分支，其他所有情况
                print("输入无效，请选择a~g！")



# 1. `__name__`：是 Python 内置的**特殊变量**

# - 当**直接运行这个 py 文件**（例如 `python score_manage.py`，VS Code 点运行）：
# Python 自动把这个文件的 `__name__` 赋值为字符串 `"__main__"`
# - 当这个文件**被别的 py 文件 import 导入**当作模块使用时：
# `__name__` 就等于**文件名**（比如 `score_manage`），不再是`"__main__"`

# 2. `if __name__ == "__main__":`
# 翻译：**如果当前是直接运行本文件，才执行冒号后面的代码**
if __name__ == "__main__":
    main()
