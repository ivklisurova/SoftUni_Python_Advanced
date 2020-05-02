numbers = list(map(int, input().split(' ')))

negative_num = list(filter(lambda x: x < 0, numbers))
positive_num = list(filter(lambda y: y >= 0, numbers))

total_positive_sum = sum(positive_num)
total_negative_sum = sum(negative_num)

print(total_negative_sum)
print(total_positive_sum)

if abs(total_negative_sum) > total_positive_sum:
    print(f'The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')
