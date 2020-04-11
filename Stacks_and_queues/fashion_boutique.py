stack = list(input().split(' '))
capacity = int(input())

racks = 0

rack_sum = 0

while stack:
    a = int(stack.pop())
    if rack_sum + a < capacity:
        rack_sum += a
    elif rack_sum + a == capacity:
        racks += 1
        rack_sum = 0
    elif rack_sum + a > capacity:
        racks += 1
        rack_sum = a
    if len(stack) == 0 and rack_sum > 0:
        racks += 1

print(racks)
