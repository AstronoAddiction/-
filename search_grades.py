from globals import grades
from search import max_grade, min_grade, avg_grade
from operations import print_grades

def search_grades():
    opt = 0 # 1.查询成绩 2.查询最高分 3.查询最低分 4.查询平均分 5.输出成绩表 6.退出
    while opt != 6:
        while opt != 1 and opt != 2 and opt != 3 and opt != 4 and opt != 5 and opt != 6:
            try:
                opt = int(input("请选择编号:1.查询成绩 2.查询最高分 3.查询最低分 4.查询平均分 5.输出成绩表 6.退出\n"))
                while opt != 1 and opt != 2 and opt != 3 and opt != 4 and opt != 5 and opt != 6:
                    opt = int(input("输入格式错误，请重新输入！"))
            except:
                print("请输入正确格式！")
                opt = 0
        if opt == 1:
            try:
                name = input("请输入姓名：")
                print(f'{name}的成绩是{grades[name]}分')
                opt = 0
            except:
                print("请输入正确格式！")
                opt = 0
        elif opt == 2:
            g, ns = max_grade()
            print(f'最高分是{g}分,得该分的有:', end = '')
            for i in ns:
                print(i, end = ' ')
            print()
            opt = 0
        elif opt == 3:
            g, ns = min_grade()
            print(f'最低分是{g}分,得该分的有:', end = '')
            for i in ns:
                print(i, end = ' ')
            print()
            opt = 0
        elif opt == 4:
            print(f'平均分是{avg_grade()}')
            opt = 0
        elif opt == 5:
            print_grades()
            opt = 0