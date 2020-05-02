numbers = list(map(lambda x: round(float(x)), input().split(' ')))

print(min(numbers))
print(max(numbers))

multiplied = map(lambda x: x * 3, numbers)
uniques = sorted(set(multiplied))

print(*uniques)