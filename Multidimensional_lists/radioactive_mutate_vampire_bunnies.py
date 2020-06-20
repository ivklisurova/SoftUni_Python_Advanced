def get_position(matrix):
    start_position = None
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'P':
                start_position = (r, c)
    return start_position


def get_the_case(start_position, case):
    new_position = None
    if case == 'U':
        new_position = (start_position[0] - 1, start_position[1])
    elif case == 'D':
        new_position = (start_position[0] + 1, start_position[1])
    elif case == 'L':
        new_position = (start_position[0], start_position[1] - 1)
    elif case == 'R':
        new_position = (start_position[0], start_position[1] + 1)
    return new_position


def validate_is_out(position, matrix):
    global is_out
    if position[0] < 0 or position[0] > len(matrix) - 1:
        is_out = True
    elif position[1] < 0 or position[1] > len(matrix[position[0]]) - 1:
        is_out = True


def validate_player_hit_bunny(matrix, position):
    global is_dead
    if matrix[position[0]][position[1]] == 'B':
        is_dead = True


def move_player(start_position, new_position, matrix):
    matrix[new_position[0]][new_position[1]] = 'P'
    matrix[start_position[0]][start_position[1]] = '.'
    return matrix


def remove_player(matrix, last_position):
    matrix[last_position[0]][last_position[1]] = 'B'
    return matrix


def locate_bunnies(matrix):
    bunnies_position = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'B':
                bunnies_position.append((i, j))
    return bunnies_position


def reproduce_bunnies(matrix):
    global is_dead
    for bunny_position in locate_bunnies(matrix):
        r = bunny_position[0]
        c = bunny_position[1]
        if r - 1 >= 0:
            if matrix[r - 1][c] == 'P':
                is_dead = True
            matrix[r - 1][c] = 'B'
        if r + 1 < len(matrix):
            if matrix[r + 1][c] == 'P':
                is_dead = True
            matrix[r + 1][c] = 'B'
        if c - 1 >= 0:
            if matrix[r][c - 1] == 'P':
                is_dead = True
            matrix[r][c - 1] = 'B'
        if c + 1 < len(matrix[r]):
            if matrix[r][c + 1] == 'P':
                is_dead = True
            matrix[r][c + 1] = 'B'
    return matrix


coordinates = list(map(int, input().split(' ')))

matrix = [[i for i in input()] for x in range(coordinates[0])]

directions = [x for x in input()]

is_dead = False
is_out = False
last_position = None

for case in directions:
    start = get_position(matrix)
    new_position = get_the_case(start, case)
    last_position = new_position
    move_player(start, new_position, matrix)
    reproduce_bunnies(matrix)

    validate_player_hit_bunny(matrix, new_position)
    validate_is_out(new_position, matrix)

    if is_out:
        remove_player(matrix, last_position)
        last_position = start
        break

    if is_dead:
        remove_player(matrix, last_position)
        break

for row in matrix:
    print(''.join(row))

if is_out:
    print(f'won: {last_position[0]} {last_position[1]}')
elif is_dead:
    print(f'dead: {last_position[0]} {last_position[1]}')
