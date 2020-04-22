size = int(input())

matrix = [list(input()) for _ in range(size)]

counter = 0

for row in range(size):
    max_hits = 0
    for element in range(size):
        if matrix[row][element] == 'K':
            if row + 2 < size and element + 1 < size:
                if matrix[row + 2][element + 1] == 'K':
                    matrix[row + 2][element + 1] = '0'
                    counter += 1
            if row + 2 < size and element - 1 > 0:
                if matrix[row + 2][element - 1] == 'K':
                    matrix[row + 2][element - 1] = '0'
                    counter += 1
            if row - 2 > 0 and element + 1 < size:
                if matrix[row - 2][element + 1] == 'K':
                    matrix[row - 2][element + 1] = '0'
                    counter += 1
            if row - 2 > 0 and element - 1 > 0:
                if matrix[row - 2][element - 1] == 'K':
                    matrix[row - 2][element - 1] = '0'
                    counter += 1
            if element + 2 < size and row + 1 < size:
                if matrix[row + 1][element + 2] == 'K':
                    matrix[row + 1][element + 2] = '0'
                    counter += 1
            if element + 2 < size and row - 1 > 0:
                if matrix[row - 1][element + 2] == 'K':
                    matrix[row - 1][element + 2] = '0'
                    counter += 1
            if element - 2 > 0 and row - 1 > 0:
                if matrix[row - 1][element - 2] == 'K':
                    matrix[row - 1][element - 2] = '0'
                    counter += 1
            if element - 2 > 0 and row + 1 < size:
                if matrix[row + 1][element - 2] == 'K':
                    matrix[row + 1][element - 2] = '0'
                    counter += 1

print(counter)
