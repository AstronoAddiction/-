from globals import grades

def load_grades():
    grades.clear()
    with open('grades.txt', 'r', encoding="utf-8") as f:
        f.seek(0)
        for line in f:
            line = line.strip()
            name, grade = line.split()
            grades[name] = int(grade)

def save_grades():
    with open('grades.txt', 'w', encoding="utf-8") as f:
        for n, g in grades.items():
            f.write(n + ' ' + str(g) + '\n')

def print_grades():
    print("成绩列表如下：")
    for n, g in grades.items():
        print(f'{n}的成绩为：{g}')
