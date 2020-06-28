def get_snake_position(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'S':
                location = (r, c)
                return location


def get_burrow_location(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'B':
                location = (r, c)
                return location


def move_the_snake(matrix, case, current_pos, log_positions):
    global food_qty
    global out
    change = log_positions[case]
    new_r = current_pos[0] + change[0]
    new_c = current_pos[1] + change[1]
    if new_r < 0 or new_r > len(matrix) - 1:
        matrix[current_pos[0]][current_pos[1]] = '.'
        out = True
        return
    if new_c < 0 or new_c > len(matrix[new_r]) - 1:
        matrix[current_pos[0]][current_pos[1]] = '.'
        out = True
        return
    if matrix[new_r][new_c] == '*':
        food_qty += 1
        matrix[new_r][new_c] = 'S'
        matrix[current_pos[0]][current_pos[1]] = '.'
    elif matrix[new_r][new_c] == 'B':
        matrix[new_r][new_c] = '.'
        matrix[current_pos[0]][current_pos[1]] = '.'
        snake_new_pos = get_burrow_location(matrix)
        matrix[snake_new_pos[0]][snake_new_pos[1]] = 'S'
    else:
        matrix[new_r][new_c] = 'S'
        matrix[current_pos[0]][current_pos[1]] = '.'

    return matrix


n = int(input())

territory = [[x for x in input()] for i in range(n)]

commands = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

food_qty = 0
out = False
win = False

while True:
    command = input()
    current_location = get_snake_position(territory)
    move_the_snake(territory, command, current_location, commands)
    if out:
        break
    if food_qty == 10:
        win = True
        break

if win:
    print('You won! You fed the snake.')
else:
    print('Game over!')

print(f'Food eaten: {food_qty}')

[print(''.join(x)) for x in territory]