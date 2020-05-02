names = input().split(' ')

valid_names = filter(lambda x: x.istitle(),names)

total_len = [len(x) for x in valid_names]
total_sum = sum(total_len)

print(total_sum)