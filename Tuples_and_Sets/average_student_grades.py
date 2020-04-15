n = int(input())

grades = {}

for i in range(n):
    args = input().split(' ')
    name, grade = args[0], args[1]
    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

for k, v in grades.items():
    print(f'{k} -> {" ".join(v)} (avg: {sum(map(float,v)) / len(v):.2f})')
