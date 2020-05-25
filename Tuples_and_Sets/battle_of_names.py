n = int(input())

even = set()
odd = set()

for i in range(1, n + 1):
    name = input()
    sum_name = 0
    for letter in name:
        sum_name += ord(letter)
    sum_name = sum_name // i
    if sum_name % 2 == 0:
        even.add(sum_name)
    else:
        odd.add(sum_name)

sum_even = sum(even)
sum_odd = sum(odd)

result = None

if sum_even == sum_odd:
    result = odd.union(even)
elif sum_odd > sum_even:
    result = odd.difference(even)
elif sum_even>sum_odd:
    result = odd.symmetric_difference(even)

print(', '.join([str(x) for x in result]))