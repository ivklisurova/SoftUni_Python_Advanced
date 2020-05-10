def get_position(sequence):
    position = None
    for i in range(len(sequence)):
        for j in sequence[i]:
            if j == 'P':
                position = (i, sequence[i].index('P'))
    return position


def get_new_position(old_pos, string):
    position = None
    if string == 'up':
        position = (old_pos[0] - 1, old_pos[1])
    elif string == 'down':
        position = (old_pos[0] + 1, old_pos[1])
    elif string == 'left':
        position = (old_pos[0], old_pos[1] - 1)
    elif string == 'right':
        position = (old_pos[0], old_pos[1] + 1)
    return position


def solve(sequence, position, text):
    global str_to_return
    locate_in_sequence = sequence[position[0]][position[1]]
    if locate_in_sequence != '-':
        str_to_return += locate_in_sequence
    sequence[position[0]][position[1]] = 'P'
    return str_to_return


def clear_old_position(sequence, position):
    sequence[position[0]][position[1]] = '-'
    return sequence


text = input()
n = int(input())
str_to_return = text

matrix = [[i for i in input()] for x in range(n)]

m = int(input())

for _ in range(m):
    command = input()
    player_curr_position = get_position(matrix)
    player_new_position = get_new_position(player_curr_position, command)
    if 0 <= player_new_position[0] < n and 0 <= player_new_position[1] < n:
        solve(matrix, player_new_position, str_to_return)
        clear_old_position(matrix, player_curr_position)
    else:
        if len(str_to_return) > 0:
            str_to_return = str_to_return[:len(str_to_return) - 1]

print(str_to_return)
[print(''.join(i)) for i in matrix]
