def build_the_matrix(start, row, col):
    string = ''
    string += chr(start_ch + i)
    string += chr((start_ch + i + j))
    string += chr(start_ch + i)
    submatrix.append(string)
    return string


r, c = map(int, input().split(' '))

start_ch = ord('a')

matrix = []

for i in range(r):
    submatrix = []
    for j in range(c):
        build_the_matrix(start_ch, i, j)
    matrix.append(submatrix)

[print(' '.join(x)) for x in matrix]
