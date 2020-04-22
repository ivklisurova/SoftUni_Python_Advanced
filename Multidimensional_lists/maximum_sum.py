n, m = map(int, input().split(' '))

matrix = [list(map(int, input().split(' '))) for _ in range(n)]

max_submatrix = []
sum_submatrix = 0


for row in range(n - 2):
    for col in range(m - 2):
        fist_row = matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]
        second_row = matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]
        third_row = matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]
        current_sum = sum(fist_row) + sum(second_row) + sum(third_row)
        if current_sum > sum_submatrix:
            max_submatrix.clear()
            max_submatrix.append(list(fist_row))
            max_submatrix.append(list(second_row))
            max_submatrix.append(list(third_row))
            sum_submatrix = current_sum

print(f'Sum = {sum_submatrix}')

for i in max_submatrix:
    print(*i, sep=' ')
