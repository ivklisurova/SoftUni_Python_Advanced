text = input().split(' ')

numbers = map(int, [x for x in text if x.isdigit()])

filtered_list = list(filter(lambda x: x > len(text), numbers))
sorted_numbers = sorted(filtered_list)

print(*sorted_numbers)
