def get_the_targets(matrix):
    located_targets = 0
    for r in matrix:
        for i in r:
            if i == 't':
                located_targets += 1
    return located_targets


def get_plane_location(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'p':
                location = (r, c)
                return location


def get_new_location(current_location, direction, steps):
    current_row = current_location[0]
    current_col = current_location[1]
    new_location = None
    if direction == 'right':
        new_location = (current_row, current_col + steps)
    elif direction == 'left':
        new_location = (current_row, current_col - steps)
    elif direction == 'down':
        new_location = (current_row + steps, current_col)
    elif direction == 'up':
        new_location = (current_row - steps, current_col)
    return new_location


def validate_new_location(new_location, matrix):
    is_valid = True
    new_row = new_location[0]
    new_col = new_location[1]
    if new_row < 0 or new_row >= len(matrix):
        is_valid = False
    elif new_col < 0 or new_col >= len(matrix[new_row]):
        is_valid = False
    return is_valid


def solve(case, current_location, new_location, matrix):
    global counter_targets
    if case == 'move':
        if matrix[new_location[0]][new_location[1]] == '.':
            matrix[current_location[0]][current_location[1]] = '.'
            matrix[new_location[0]][new_location[1]] = 'p'
    if case == 'shoot':
        if matrix[new_location[0]][new_location[1]] == 't':
            counter_targets -= 1
        matrix[new_location[0]][new_location[1]] = 'x'


n = int(input())

battlefield = [input().split(' ') for _ in range(n)]

m = int(input())

targets = get_the_targets(battlefield)
counter_targets = targets

for _ in range(m):
    if counter_targets == 0:
        break
    args = input().split(' ')
    command = args[0]
    direction = args[1]
    steps = int(args[2])
    plane_location = get_plane_location(battlefield)
    next_location = get_new_location(plane_location, direction, steps)
    if validate_new_location(next_location, battlefield):
        solve(command, plane_location, next_location, battlefield)

if counter_targets:
    print(f'Mission failed! {counter_targets} targets left.')
else:
    print(f'Mission accomplished! All {targets} targets destroyed.')

for r in battlefield:
    print(' '.join(r))
