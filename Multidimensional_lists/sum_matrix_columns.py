rows, col = map(int, input().split(', '))

matrix = [(list(map(int, input().split(' ')))) for i in range(rows)]

for i in range(col):
    sum_columns = 0
    for j in range(rows):
        sum_columns += matrix[j][i]

    print(sum_columns)

