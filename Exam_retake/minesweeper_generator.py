def calculate(matrix, position, dir):
    val = 0
    for i in dir:
        new_row = position[0] + dir[i][0]
        new_col = position[1] + dir[i][1]
        if not validate(matrix, new_row, new_col):
            continue
        if matrix[new_row][new_col]=='*':
            val += 1
    matrix[position[0]][position[1]] = val
    return matrix


def validate(matrix, new_pos_r, new_pos_c):
    is_valid = True
    if new_pos_r < 0 or new_pos_r >= len(matrix):
        is_valid = False
    elif new_pos_c < 0 or new_pos_c >= len(matrix[new_pos_r]):
        is_valid = False
    return is_valid


size = int(input())
n = int(input())

field = [['None' for _ in range(size)] for _ in range(size)]

positions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
    'up left': (-1, -1),
    'up right': (-1, 1),
    'down left': (1, -1),
    'down right': (1, 1)
}

for i in range(n):
    position = input()
    position = tuple(int(num) for num in position.replace('(', '').replace(')', '').replace('...', '').split(', '))
    row = position[0]
    col = position[1]
    field[row][col] = '*'

for r in range(len(field)):
    for c in range(len(field[r])):
        if field[r][c]=='None':
            current_position = [r, c]
            calculate(field, current_position, positions)

for x in field:
    print(' '.join([str(i) for i in x]))