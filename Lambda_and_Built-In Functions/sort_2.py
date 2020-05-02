numbers = map(int, input().split(' '))

negative_numbers = list(filter(lambda x: x<0, numbers))
abs_value = [abs(x) for x in negative_numbers]

sum_numbers = sum(abs_value)
print(sum_numbers)