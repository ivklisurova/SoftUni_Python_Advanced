rows, col = map(int, input().split(', '))

matrix = [list(map(int, input().split(', '))) for i in range(rows)]

max_submatrix = []
max_result_submatrix = 0

for row in range(len(matrix) - 1):
    for element in range(len(matrix[row]) - 1):
        sumbmatrx = matrix[row][element], matrix[row][element + 1], matrix[row + 1][element], matrix[row + 1][
            element + 1]
        result = sum(sumbmatrx)
        if result > max_result_submatrix:
            max_result_submatrix = result
            max_submatrix = sumbmatrx

print(f'{max_submatrix[0]} {max_submatrix[1]}\n{max_submatrix[2]} {max_submatrix[3]}')
print(max_result_submatrix)
