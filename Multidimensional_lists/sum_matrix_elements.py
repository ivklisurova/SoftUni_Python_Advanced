row, col = map(int, input().split(', '))

matrix = []

[matrix.append(list(map(int, input().split(', ')))) for i in range(row)]

total_sum = 0

for i in matrix:
    total_sum += sum(i)

print(total_sum)
print(matrix)

