rows, columns = map(int, input().split(' '))

matrix = [list(input().split(' ')) for i in range(rows)]

while True:
    args = input()
    if args == 'END':
        break
    if args.startswith('swap'):
        args = args.split(' ')
        if len(args) == 5:
            row1 = int(args[1])
            col1 = int(args[2])
            row2 = int(args[3])
            col2 = int(args[4])

            for x in range(len(matrix)):
                if row1 >= len(matrix) or col1 >= (len(matrix[x])) or row2 >= len(matrix) or col2 >= len(matrix[x]) \
                        or row1 < 0 or col1 < 0 or row2 < 0 or col2 < 0:
                    print('Invalid input!')
                    break
            else:
                first_args = matrix[row1][col1]
                second_args = matrix[row2][col2]
                matrix[row1][col1] = second_args
                matrix[row2][col2] = first_args

                for i in matrix:
                    print(' '.join(i))
        else:
            print('Invalid input!')

    else:
        print('Invalid input!')
