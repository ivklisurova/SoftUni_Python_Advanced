n = int(input())

matrix = [list(map(int, input().split(' '))) for _ in range(n)]

next_idx = 0

total_sum = 0

for i in matrix:
    total_sum += i[next_idx]
    next_idx += 1

print(total_sum)