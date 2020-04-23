def is_valid(number):
    min_value = 2
    max_value = 10

    for i in range(min_value, max_value + 1):
        if number % i == 0:
            return True


n = int(input())
m = int(input())

result = [x for x in range(n, m + 1) if is_valid(x)]

print(result)
