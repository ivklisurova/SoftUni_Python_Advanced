from collections import deque

food = int(input())

queue = deque([int(x) for x in input().split(' ')])

print(max(queue))

while queue:
    a = queue.popleft()
    if food >= a:
        food -= a
    else:
        queue.appendleft(a)
        break

if queue:
    print(f'Orders left: {" ".join([str(y) for y in list(queue)])}')
else:
    print('Orders complete')
