from collections import deque

n = int(input())

pump_map = deque()

for _ in range(n):
    args = input().split(' ')
    fuel = int(args[0])
    distance = int(args[1])
    diff = fuel - distance
    pump_map.append(diff)

for i in range(n):
    pump = pump_map.popleft()
    if pump > 0:
        left_fuel = pump
        for j in range(len(pump_map)):
            left_fuel += pump_map[j]
            if left_fuel < 0:
                pump_map.append(pump)
                break
        if left_fuel >= 0:
            print(i)
            break
    else:
        pump_map.append(pump)
