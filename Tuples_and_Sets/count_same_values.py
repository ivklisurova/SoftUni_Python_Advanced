numbers = map(float, input().split(' '))

t = tuple(numbers)

unique_grades = []

[unique_grades.append(i) for i in t if i not in unique_grades]

[print(f'{x} - {t.count(x)} times')for x in unique_grades]
