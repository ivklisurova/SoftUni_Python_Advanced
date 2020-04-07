from collections import deque

text = input().split(' ')
circle = deque(text)

toss = int(input())

counter = 0

while len(circle) > 1:
    counter += 1
    player = circle.popleft()
    if counter == toss:
        print(f'Removed {player}')
        counter = 0
    else:
        circle.append(player)

print(f'Last is {circle.popleft()}')
