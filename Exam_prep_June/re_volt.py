def player_location(matrix):
    for r in range(len(matrix)):
        if 'f' in matrix[r]:
            location = (r, matrix[r].index('f'))
            return location


def move_player(location, new_r, new_c, matrix):
    matrix[new_r][new_c] = 'f'
    matrix[location[0]][location[1]] = '-'
    return matrix


def get_the_case(location, matrix, case, dirrs):
    global is_winning
    steps = dirrs[case]
    new_r = location[0] + steps[0]
    new_c = location[1] + steps[1]
    if new_r < 0:
        new_r = -1
    if new_c < 0:
        new_c = -1
    if new_r >= len(matrix):
        new_r = 0
    if new_c >= len(matrix[new_r]):
        new_c = 0
    if matrix[new_r][new_c] == '-':
        move_player(location, new_r, new_c, matrix)
    elif matrix[new_r][new_c] == 'B':
        move_player(location, new_r, new_c, matrix)
        new_loc = player_location(matrix)
        r = new_loc[0] + steps[0]
        c = new_loc[1] + steps[1]
        if r < 0:
            r = -1
        if c < 0:
            c = -1
        if r >= len(matrix):
            r = 0
        if c >= len(matrix[r]):
            c = 0
        if matrix[r][c] == 'F':
            is_winning = True
        move_player(new_loc, r, c, matrix)
        matrix[new_loc[0]][new_loc[1]] = 'B'
    elif matrix[new_r][new_c] == 'T':
        pass
    elif matrix[new_r][new_c] == 'F':
        move_player(location, new_r, new_c, matrix)
        is_winning = True
    return matrix


n = int(input())
commands_count = int(input())

field = [[i for i in input()] for x in range(n)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

is_winning = False

for _ in range(commands_count):
    if not is_winning:
        command = input()
        current_location = player_location(field)
        get_the_case(current_location, field, command, directions)
    else:
        break

if is_winning:
    print('Player won!')
else:
    print('Player lost!')

[print(''.join(x)) for x in field]
