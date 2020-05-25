def average(value):
    return sum(value)/len(value)

n = int(input())

grades = {}

for i in range(n):
    (name, grade) = input().split(' ')
    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

for (k, v) in grades.items():
    average_mark = average([float(mark) for mark in v])
    print(f'{k} -> {" ".join(v)} (avg: {average_mark:.2f})')
