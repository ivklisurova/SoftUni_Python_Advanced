numbers = list(map(lambda x: round(float(x)), input().split(' ')))

total_sum = sum([x * len(numbers) for x in numbers])

print(total_sum)