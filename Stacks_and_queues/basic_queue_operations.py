from collections import deque

n = input().split(' ')
element = input().split(' ')

add = int(n[0])
remove = int(n[1])
x = n[2]

queue = deque()

for i in range(add):
    queue.append(element[i])

for j in range(remove):
    queue.popleft()

if len(queue) > 0:
    if x in queue:
        print('True')
    else:
        print(min(queue))
else:
    print('0')
