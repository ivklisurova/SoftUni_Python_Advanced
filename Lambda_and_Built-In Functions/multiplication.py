number = int(input())
list_numbers = list(map(int, input().split(' ')))

result = [x* number for x in list_numbers]

print(*result)