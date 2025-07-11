from operations import load_grades
from input_grades import input_grades
from search_grades import search_grades

# 1.录入成绩 2.查询成绩 3.退出
load_grades()

while True:
    while True:
        try:
            opt = int(input("请选择编号:1.录入成绩 2.查询成绩 3.退出\n"))
            break
        except:
            print("请输入正确格式！")
    if opt not in (1, 2, 3):
        print("请输入1或2或3")
        continue
    elif opt == 1:
        input_grades()
        opt = 0
    elif opt == 2:
        search_grades()
        opt = 0
    elif opt == 3:
        break