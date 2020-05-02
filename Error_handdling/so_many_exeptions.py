numbers_list = list(map(int, input().split(", ")))
result = 1

for i in range(len(numbers_list)):
    try:
        number = numbers_list[i]
        if number <= 5:
            result *= number
        elif 5 < number <= 10:
            result /= number
    except IndexError:
        break

print(round(result))
