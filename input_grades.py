from operations import save_grades, load_grades
from globals import grades

def input_grades():
    while True:
        try:
            name = input("请输入姓名：")
            if name == "":
                print("姓名不能为空")
                continue

            grade = int(input("请输入成绩："))
            grades[name] = grade
            print("录入成功")
        except ValueError:
            print("输入格式错误，请重新输入！")
            continue

        while True:
            try:
                cont = int(input("是否继续输入？(1.是 2.否)"))
                if cont in (1, 2):
                    break
                else:
                    print("请输入1或2")
            except ValueError:
                print("请输入数字格式！")

        if cont == 2:
            break
    
    #是否保存
    while True:
        try:
            save_opt = int(input("是否保存？(1.是 2.否)"))
            if save_opt == 1:
                save_grades()
                break
            elif save_opt == 2:
                load_grades()
                break
            else:
                print("请输入1或2")
        except ValueError:
            print("请输入数字格式！")