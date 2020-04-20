rows, cols = map(int, input().split(' '))

matrix = [input().split(' ') for _ in range(rows)]

equals = 0


for row in range(rows-1):
    for element in range(cols-1):
        submatrx = matrix[row][element], matrix[row][element + 1], matrix[row + 1][element], matrix[row + 1][
            element + 1]
        if matrix[row][element] == matrix[row][element + 1] == matrix[row + 1][element] == matrix[row + 1][
            element + 1]:
            equals += 1

print(equals)

