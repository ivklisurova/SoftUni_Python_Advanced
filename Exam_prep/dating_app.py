from collections import deque

males = list(map(int, input().split(' ')))
females = deque(map(int, input().split(' ')))

matches = 0

while males and females:
    male = males[-1]
    female = females[0]
    if male <= 0 or female <= 0:
        if male <= 0:
            males.pop()
        if female <= 0:
            females.popleft()
        continue
    if male % 25 == 0 or female % 25 == 0:
        if male % 25 == 0:
            males.pop()
            if males:
                males.pop()
        if female % 25 == 0:
            females.popleft()
            if females:
                females.popleft()
        continue
    if male == female:
        matches += 1
        males.pop()
        females.popleft()
    elif male != female:
        females.popleft()
        males[-1] = male - 2

print(f'Matches: {matches}')

if males:
    print(f'Males left: {", ".join([str(i) for i in males[::-1]])}')
else:
    print('Males left: none')


if females:
    print(f'Females left: {", ".join([str(i) for i in females])}')
else:
    print('Females left: none')
