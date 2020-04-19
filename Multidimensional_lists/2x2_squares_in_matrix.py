rows, cols = map(int, input().split(' '))

matrix = [input().split(' ') for i in range(rows)]

equals = 0

if rows >= 2 and cols >= 2:
    for row in range(len(matrix) - 1):
        for element in range(len(matrix[row]) - 1):
            submatrx = matrix[row][element], matrix[row][element + 1], matrix[row + 1][element], matrix[row + 1][
                element + 1]
            if matrix[row][element] == matrix[row][element + 1] == matrix[row + 1][element] == matrix[row + 1][
                element + 1]:
                equals += 1

    print(equals)

