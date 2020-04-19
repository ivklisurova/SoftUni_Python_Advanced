n = int(input())

matrix = [list(map(int, input().split(' '))) for i in range(n)]

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

start_idx = 0

for i in matrix:
    primary_diagonal_sum += i[start_idx]
    start_idx += 1

start_idx = 0

for j in matrix[::-1]:
    secondary_diagonal_sum += j[start_idx]
    start_idx += 1

diff = abs(primary_diagonal_sum-secondary_diagonal_sum)
print(diff)

