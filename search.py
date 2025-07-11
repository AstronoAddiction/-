from globals import grades

def search_grade(name):
    try:
        print(f'{name}的成绩为：{grades[name]}')
    except:
        print('未找到')

def max_grade():
    max_g = max(grades.values())
    names = [n for n, g in grades.items() if g == max_g]
    return max_g, names

def min_grade():
    min_g = min(grades.values())
    names = [n for n, g in grades.items() if g == min_g]
    return min_g, names

def avg_grade():
    return sum(grades.values()) / len(grades)