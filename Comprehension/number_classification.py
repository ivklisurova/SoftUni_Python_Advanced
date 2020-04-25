numbers = list(map(int, input().split(', ')))

positive = [i for i in numbers if i >= 0]
negative = [i for i in numbers if i < 0]
even = [i for i in numbers if i % 2 == 0]
odd = [i for i in numbers if i % 2 != 0]

print(f'Positive: {", ".join([str(x) for x in positive])}')
print(f'Negative: {", ".join([str(x) for x in negative])}')
print(f'Even: {", ".join([str(x) for x in even])}')
print(f'Odd: {", ".join([str(x) for x in odd])}')
