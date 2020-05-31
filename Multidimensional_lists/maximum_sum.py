import sys

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

sum_submatrix = -sys.maxsize
best_start = None

for row in range(len(matrix) - 2):
    for col in range(len(matrix[row]) - 2):

        fist_row = matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]
        second_row = matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]
        third_row = matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]
        current_sum = sum(fist_row)+sum(second_row)+sum(third_row)

        if current_sum > sum_submatrix:
            sum_submatrix = current_sum
            best_start = (row, col)

best_matrix = []

rows, cols = best_start[0], best_start[1]

for i in range(3):
    best_matrix.append([])
    current_column = cols
    current_row = rows+i
    for j in range(3):
        best_matrix[i].append(matrix[current_row][current_column])
        current_column += 1

print(f'Sum = {sum_submatrix}')

for i in best_matrix:
    print(' '.join([str(j) for j in i]))
