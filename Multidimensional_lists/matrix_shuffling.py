rows, columns = map(int, input().split(' '))

matrix = [list(input().split(' ')) for i in range(rows)]

is_valid = True

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
            len_len = len(matrix)
            for x in range(len(matrix)):
                if row1 > len(matrix[x]) or col1 > (len(matrix)) or row2 > len(matrix[x]) or col2 > len(matrix):
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
