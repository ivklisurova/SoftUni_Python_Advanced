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
    global is_win
    steps = dirrs[case]
    new_r = location[0] + steps[0]
    new_c = location[1] + steps[1]
    if matrix[new_r][new_c] == '-':
        move_player(location, new_r, new_c, matrix)
    elif matrix[new_r][new_c] == 'B':
        move_player(location, new_r, new_c, matrix)
        a = player_location(matrix)
        move_player(location, new_r, new_c, matrix)
        pass
    elif matrix[new_r][new_c] == 'T':
        pass
    elif matrix[new_r][new_c] == 'F':

        matrix[new_r][new_c] = 'f'
        matrix[location[0]][location[1]] = '-'
        is_win = True
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

is_win = False

for _ in range(commands_count):
    command = input()
    current_location = player_location(field)
    get_the_case(current_location, field, command, directions)