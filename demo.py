from collections import deque

males = list(map(int, input().split(' ')))
females = deque([int(x) for x in input().split() if int(x) > 0])

finish = False

matches = 0
while males and females:
    if males[-1] == females[0]:
        males.pop()
        females.popleft()
        matches += 1
        continue
    if males[-1] % 25 != 0 and females[0] % 25 != 0:
        males[-1] -= 2
        if males[-1] <= 0:
            males.pop()
        females.popleft()
    else:
        if males[-1] % 25 == 0:
            while True:
                try:
                    if males[-1] % 25 != 0:
                        males.pop()
                        break
                    else:
                        males.pop()
                except:
                    break
        if females[0] % 25 == 0:
            while True:
                try:
                    if females[0] % 25 != 0:
                        females.popleft()
                        break
                    else:
                        females.popleft()
                except:
                    break

print(f'Matches: {matches}')
if males:
    print(f'Males left: {", ".join(str(x) for x in males)}')
else:
    print('Males left: none')
if females:
    print(f'Females left: {", ".join(str(x) for x in females)}')
else:
    print('Females left: none')