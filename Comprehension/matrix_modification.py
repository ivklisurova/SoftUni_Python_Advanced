n = int(input())

matrix = [list(map(int, input().split(' '))) for x in range(n)]

while True:
    args = input().split()
    command = args[0]
    if command == 'END':
        break
    row = int(args[1])
    col = int(args[2])
    value = int(args[3])
    if command == 'Add':
        if 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix[row]):
            matrix[row][col] += value
        else:
            print('Invalid coordinates')
    elif command == 'Subtract':
        if 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix[row]):
            matrix[row][col] -= value
        else:
            print('Invalid coordinates')


[print(' '.join(map(str, i))) for i in matrix]
