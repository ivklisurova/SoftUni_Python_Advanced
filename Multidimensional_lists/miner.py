def is_valid_cell(n, new_row, new_col):
    is_valid = True
    if new_row >= n or new_row < 0:
        is_valid = False
    elif new_col >= n or new_col < 0:
        is_valid = False
    return is_valid


def collect(matrix, new_col, new_row):
    global coal_count
    global interrupted
    if matrix[new_row][new_col] == 'c':
        coal_count -= 1
        if coal_count == 0:
            print(f'You collected all coals! ({new_row}, {new_col})')
            interrupted = True
            return 1
        else:
            return 0
    elif matrix[new_row][new_col] == 'e':
        print(f'Game over! ({new_row}, {new_col})')
        interrupted = True
        return 2
    else:
        return 0


def move_the_miner(matrix, new_row, new_col):
    global start_row
    global start_col
    matrix[start_row][start_col] = '*'
    matrix[new_row][new_col] = 's'
    start_row = new_row
    start_col = new_col
    return matrix


n = int(input())

commands = input().split(' ')

matrix = [input().split(' ') for i in range(n)]

interrupted = False

# coals in field
coal_count = sum(x.count('c') for x in matrix)

# locate the miner
start_row = None
start_col = None

for row in range(len(matrix)):
    for i in range(len(matrix[row])):
        if matrix[row][i] == 's':
            start_row = row
            start_col = i

for command in commands:
    if command == 'up':
        new_row = start_row - 1
        new_col = start_col
        # -is end of the field?
        if is_valid_cell(n, new_row, new_col):
            # -what character is in the given cell
            if collect(matrix, new_col, new_row) > 0:
                break
            # -move the miner to the new position
            move_the_miner(matrix, new_row, new_col)
    elif command == 'down':
        new_row = start_row + 1
        new_col = start_col
        if is_valid_cell(n, new_row, new_col):
            if collect(matrix, new_col, new_row) > 0:
                break
            move_the_miner(matrix, new_row, new_col)
    elif command == 'left':
        new_row = start_row
        new_col = start_col - 1
        if is_valid_cell(n, new_row, new_col):
            if collect(matrix, new_col, new_row) > 0:
                break
            move_the_miner(matrix, new_row, new_col)
    elif command == 'right':
        new_row = start_row
        new_col = start_col + 1
        if is_valid_cell(n, new_row, new_col):
            if collect(matrix, new_col, new_row) > 0:
                break
            move_the_miner(matrix, new_row, new_col)

if not interrupted:
    print(f'{coal_count} coals left. ({start_row}, {start_col})')
